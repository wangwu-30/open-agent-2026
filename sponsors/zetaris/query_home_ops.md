# Zetaris → HubCrew 只读查询与决策草稿

**状态：尚无 Zetaris 实例；下列 SQL 均未执行，没有查询结果，也没有完成 HubCrew 接入。** 本文供后续拿到本机或 AWS 实例、只读账号后实跑和录屏。先按 [SETUP.md](./SETUP.md) 完成所选连接通道的 preflight；实例未装、连接检查失败或样本不可见时，保留 blocker，不填成功结果。

目标来自 [SPONSOR-PLAN.md Task B](../../SPONSOR-PLAN.md#task-b--zetaris规则必接可能成-blocker)：在推理前读取 Zetaris 数据，并说明结果如何影响告警优先级或交接顺序。本稿只准备查询与演示规则；不会创建数据源、写表、修改权限或连接生产家用库。

## 1. 按顺序执行只读 SQL

在 Zetaris SQL Editor 或 [SETUP.md](./SETUP.md) 对应的客户端中，**每次只提交一个 SQL 块**。以下不带结尾分号，便于直接传给 JDBC / REST 单语句客户端。任何一步失败，先记录错误；不要用猜测结果继续决策。

使用官方脚本时，从本项目根目录进入 `sponsors/zetaris/getting-started`，先预览语句；`--dry-run` 不联网，只检查脚本如何解析输入，不能证明服务器接受 SQL：

```sh
python3 scripts/run_sql.py --channel jdbc --dry-run -e 'SELECT 1'
```

只有实例就绪且所选通道通过 preflight 后，才移除 `--dry-run` 执行，并逐条替换 `-e` 后的 SQL；选择直接 REST 时把 `--channel jdbc` 改为 `--channel rest`。本次只验证预览命令，不执行连接查询。

检查执行通道：

```sql
SELECT 1
```

验收条件是实际收到值 `1`；这只是预期，不是已观测结果。

发现当前账号可见的 Lightning 数据库：

```sql
SHOW LIGHTNING DATABASES
```

检查是否存在 `NY_TAXI` 或 `TPCDS_DB`。干净实例返回空列表是有效结果，但意味着下面的样本演示仍受阻；此时应取得样本访问条件，不在本任务中创建或导入数据。`SHOW DATASOURCES` 不用于判断文件样本是否存在。

仅对已发现的数据库执行相应查询：

```sql
SHOW LIGHTNING TABLES NY_TAXI
```

```sql
SHOW LIGHTNING TABLES TPCDS_DB
```

确认表和列后再取样；两套样本互为备选，至少完成一套才有样本读路径证据。

```sql
DESCRIBE DATASOURCE TABLE NY_TAXI.taxi_zones
```

```sql
SELECT * FROM NY_TAXI.taxi_zones LIMIT 5
```

```sql
DESCRIBE DATASOURCE TABLE TPCDS_DB.reason
```

```sql
SELECT * FROM TPCDS_DB.reason LIMIT 5
```

如果采用 TPCDS 演示，可用下面的稳定排序版本选取输入；字段名取自官方入门示例，仍须以当前实例 `DESCRIBE` 结果核对：

```sql
SELECT r_reason_sk, r_reason_desc
FROM TPCDS_DB.reason
ORDER BY r_reason_sk
LIMIT 5
```

每条取样查询最多返回 5 行；无 `ORDER BY` 的取样不保证顺序。返回 5 行不能证明整表只有 5 行，也不能据此计算真实积压或错误率。REST 返回值可能是字符串，数值比较前需转换并检查格式。

## 2. 【待实跑替换】样本结果如何影响 HubCrew 决策

`NY_TAXI` 和 `TPCDS_DB` 是 supplied samples，不是家庭运维遥测。以下规则是**人工定义的演示映射**，用于展示“查询 → 推理 → 交接”的顺序；阈值不是现行产品策略，样本行也不代表真实故障。当前没有任何实际输入、优先级判断或告警发送结果。

计划选取一套成功读取的样本，把每条有效样本行映射为一个临时演示待办；将本次实际取到的行数记为 `sample_row_count`，范围为 0–5。它只表示本次演示输入规模，不是数据库总行数或家用班组真实积压。采用 TPCDS 时，用 `r_reason_sk` 标识演示待办，保留 `r_reason_desc` 作为样本描述；不把描述解释为真实故障原因。

| 【待实跑替换】真实输入条件 | 人工定义的演示决策 | HubCrew 交接顺序示例 |
|---|---|---|
| 所选样本查询成功且 `sample_row_count` 为 3–5 | 演示优先级设为“高” | 将“处理本轮演示待办”排在例行汇总之前，并在交接包记录所用查询和行数 |
| 所选样本查询成功且 `sample_row_count` 为 1–2 | 演示优先级设为“常规” | 保持例行交接顺序，附上样本来源与待办标识 |
| 查询成功但 `sample_row_count` 为 0 | 无样本可展示；不产生业务优先级判断 | 先交接“补齐演示数据”这项未完成工作，不能写成“家庭系统无告警” |
| 查询失败、无权限或未发现样本 | 数据读取 blocker；不产生业务优先级判断 | 先交接连接或权限问题及已试失败路径，不能填默认成功或静默降低告警优先级 |

实跑时应记录实际命中的一行规则，再由后续接入工作把判断交给 HubCrew；本稿没有实现自动调度、H-MEM 写入或消息发送。告警出口沿用 [ARCHITECTURE.md](../../ARCHITECTURE.md) 的既定约定：默认 HubCards，无 push 时紧急 Telegram；本演示映射本身不触发真实紧急告警。

交接包继续使用项目已有的三类信息：

- **未完成工作**：本轮演示待办及依据；没有实例时明确写“Zetaris 实例未安装，查询未执行”。
- **试过失败**：只记录实际尝试、脱敏错误和影响，不预填网络或权限故障。
- **仍生效决策**：明确样本用途、人工演示阈值和实际采用的优先级；不能声称已获得生产事实。

若后续改用真实 home-ops 的错误率或积压作输入，需要先确认授权的数据源、字段和时间窗口，并另写只读 SQL。本文未创建这些表，也不推定它们已存在。

## 3. 后续实跑记录模板

保留本节的未执行状态，直到有实际证据；仅填脱敏摘要，不粘贴账号、完整连接凭证或原始敏感数据。

```text
【待实跑替换】
状态：未执行
运行时间（含时区）：待填
实例类型 / 版本：待填（local / AWS；版本以实际信息为准）
所用通道：待填（JDBC / direct REST / UI proxy）
Preflight：当前预备检查 NOT READY，见 SETUP.md；实例就绪后的检查待执行（JDBC、REST 分列）
SELECT 1：未执行
SHOW LIGHTNING DATABASES：未执行
所选数据库、表及 DESCRIBE 摘要：待填
实际执行 SQL：待填
结果摘要：待填（实际行数、必要的脱敏样本标识；无虚构返回）
数据范围：supplied sample；不是生产家用库
采用的演示映射及优先级：待填
交接顺序及原因：待填（关联本次 SQL 和实际结果）
HubCrew / H-MEM / 告警出口实际接入状态：未接入
证据位置：待填（脱敏输出或录屏时间点）
剩余 blocker / 下一步：实例未安装
```

完成查询记录只证明只读路径与演示输入。要满足 [DEMO-SCRIPT.md](../../DEMO-SCRIPT.md) 的 Zetaris 段，还需展示真实查询结果，以及实际结果影响决策的过程；不能把本草稿或规则表当作接入证明。

## 核验来源

SQL、样本表名和协议注意事项核对自上游提交 `6a2fbaa47c32c9ac33f6584c64b43b146c621bed`：

- [官方首次 SQL 指南](./getting-started/docs/connections/lightning-recipe-reference.md)
- [官方客户端配置](./getting-started/docs/connections/client-setup.md)
- [项目架构与告警出口](../../ARCHITECTURE.md)
- [赞助商 Task B](../../SPONSOR-PLAN.md#task-b--zetaris规则必接可能成-blocker)

本次核验仅涉及文档与 SQL 文本，未连接 Zetaris、未执行查询。
