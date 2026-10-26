# Zetaris 接入预备：尚无实例

适用于 [SPONSOR-PLAN Task B](../../SPONSOR-PLAN.md#task-b--zetaris规则必接可能成-blocker)。目标是取得本机或 AWS 实例后，用只读 SQL 为 HubCrew 的告警优先级 / 交接顺序提供事实。**当前实例未安装，接入仍是 blocker；没有 SQL 查询结果，也没有接通 HubCrew 告警。** 演示拟用 `NY_TAXI.taxi_zones` / `TPCDS_DB.reason` 样本，不能称为生产家用数据。

核对日期：2026-10-26。依据：[官方入口](https://zetaris.github.io/getting-started/)、[client-setup.md](./getting-started/docs/connections/client-setup.md) 与官方仓库提交 [`6a2fbaa47c32c9ac33f6584c64b43b146c621bed`](https://github.com/zetaris/getting-started/tree/6a2fbaa47c32c9ac33f6584c64b43b146c621bed)。以下安装步骤是后续操作指南，本次未安装平台、客户端依赖或创建云资源。

## 1. 取得固定版本的官方脚本

官方仓库已经 clone 到 `sponsors/zetaris/getting-started`，并以 Git 子模块记录来源和版本。从本项目根目录执行：

```sh
git submodule update --init sponsors/zetaris/getting-started
git -C sponsors/zetaris/getting-started rev-parse HEAD
cd sponsors/zetaris/getting-started
```

后文客户端命令均在该子目录执行。子模块内先读 [AGENTS.md](./getting-started/AGENTS.md) 和 [Codex 连接指南](./getting-started/docs/connections/codex-connection.md)。普通复现使用上面的固定版本，通常会处于 detached HEAD。重新评估新版文档时，才在干净的子模块工作区先 `git switch main`，再 `git pull --ff-only`，核对差异后由外层仓库提交新的版本指针。

## 2. 路线 A：本机 Docker Compose

依据：[选择安装路线](./getting-started/docs/install/choose-install.md)、[本机安装指南](./getting-started/docs/install/updated_zetaris_installation_guide.md)。

1. 在 [Zetaris Cloud Run locally](https://cloud.enterprise.zetaris.com/dashboard/download) 注册 / 登录，取得 `zetaris-platform.zip`、与之配套的 `.env`、镜像仓库凭证及适用的许可 / 评估资格。`getting-started` 只有指南、脚本和数据配方，不含平台镜像或安装分发包。**没有这些材料就停在此处。** 当前未确认官方提供无需交互账号的免费静默安装包，因此本次只做预备文档。
2. 准备 Docker Desktop（macOS / Windows；Windows 通过 WSL2 执行）或 Docker Engine + Compose（Linux）。官方推荐 Engine 25+、给 Docker 分配 8 GB 内存和 4 CPU，安装检查在内存低于 6 GB 时失败；至少 15 GB 空闲磁盘并为数据和日志留余量。镜像为 amd64，Apple Silicon 需要仿真；还要检查 Docker 虚拟磁盘空间和镜像仓库网络。
3. 将安装包放在本项目仓库之外，解压并在 `zetaris-platform` 目录按下载页指引登录镜像仓库，再运行 `./preflight.sh`。凭证在交互提示中输入，不写进命令、文档或录屏。
4. 在编辑器中配置平台包自带的 `.env`，保留配套镜像设置。设置初始管理员邮箱、密码、组织；核对本机参数 `ZSPARK_DRIVER_MEM=2g`、`ZSPARK_DRIVER_CORES=2`、`ZSPARK_MASTER_URL=local[2]`、`ZETARIS_API_MAX_HEAP=1g`、`UI_PORT=3000`、`ALLOWED_ORIGINS=http://localhost:3000`、`GUI_URL=http://localhost:3000`，`COMPOSE_PROFILES` 留空，样本配置 `ZETARIS_SEED_TPCH=true`。账户和密码要求见安装指南。**平台 `.env` 与下文客户端 `.env.local` 是两份不同配置**；平台文件始终留在仓库外。
5. 材料齐全且平台 preflight 通过后，才在平台目录执行：

   ```sh
   chmod 600 .env
   docker compose config --quiet
   docker compose pull
   docker compose up -d
   docker compose ps --all
   ./verify.sh
   ```

   `--quiet` 避免打印解析后的凭证。以服务状态和 `verify.sh` 九项检查通过为准，`init` / `bootstrap` 正常状态为 `Exited (0)`。然后打开 `http://localhost:3000` 登录，继续客户端配置和查询验证。

完成演示后可在平台目录运行 `docker compose stop` 暂停并保留数据。`docker compose down` 保留命名卷；`down -v` 会删除数据和密钥，不作为默认清理步骤。

## 3. 路线 B：AWS Free Tier（仅记录，未创建资源）

依据：[Zetaris AWS Free Tier 清单](./getting-started/docs/install/aws-free-tier-checklist.md)、[Managed AWS 集群指南](./getting-started/docs/install/managed-aws-cluster-guide.md)。

1. 需要本人交互登录 Zetaris Cloud 与 AWS，确认 AWS 账户资格、计划、余额、到期日和 CloudFormation / IAM 权限。以 [AWS 计划说明](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html) 与 [Free Tier 条款](https://aws.amazon.com/free/terms/) 为准：新客户可获 $100 起始额度及最高 $100 活动额度；Free plan 在六个月或额度耗尽时结束。已有账户不能假定获得新客户额度，也不能通过重复开账户领取。
2. **本任务禁止创建需要付费的云资源。** 未确认有效 Free plan、资源适用范围和额度覆盖时，停在创建资源之前；出现 Paid plan、要求升级、资格不符或费用不明就停止。仅有 credits 或预算告警不能当作免费保证。不要为了领取活动额度自动启动 EC2 / RDS 等服务，也不要进行会自动转成付费计划的操作（例如加入 AWS Organizations）。
3. 条件满足后，可按官方指南手动走 **Compute → Credentials → Add AWS Account → Quickstart**，核对区域（指南推荐 `us-west-1`）、成本提示和 IAM 权限，再创建 CloudFormation stack；待 `CREATE_COMPLETE` 后回到 Zetaris 验证账户。
4. 在 **Compute → Clusters** 选择已验证账户和 **Mini**，核对配置与费用后创建；等全部初始化阶段完成、状态为 **Active**。这一系列动作本次均未执行。
5. 从集群 Overview 的 **Access** 获取实际 Sign-in URL、主机及 JDBC endpoint；用该实例的组织账户登录，并为只读客户端准备适当权限。使用实例提供的 REST 地址，不能沿用 `localhost` 或本机 Docker 账号。继续下文 preflight 和样本查询。

后续清理按官方指南先删除集群，确认 **Deleted**，再删除对应 CloudFormation stack，确认 `DELETE_COMPLETE` 后标记 credential 删除。暂停集群不等于清理完成；EFS / S3 可能保留并继续消耗额度或产生费用，应核对保留资源与账单，删除数据前确认内容可丢弃。

## 4. 客户端 `.env.local` 和驱动 JAR

**文件位置：`sponsors/zetaris/getting-started/.env.local`**。脚本默认按官方仓库根寻找该文件；不要假定会加载外层 `open-agent-2026/.env.local`。以下命令只创建空文件且不覆盖已有值，实例与凭证到位后再在本地编辑器中填写：

```sh
umask 077
touch .env.local
chmod 600 .env.local
git check-ignore -v .env.local
```

参考上游 [`.env.example`](./getting-started/.env.example)，只填所选协议需要的键；不要复制其中的示例联系人。脚本不会替换进程中已有的同名环境变量，切换实例时留意旧的导出值。

| 键 | 需要的场景 / 值 |
|---|---|
| `ZETARIS_JDBC_URL` | JDBC：本机为 `jdbc:zetaris:lightning@localhost:10000`；AWS 用实例提供的地址 |
| `ZETARIS_JDBC_JAR` | JDBC：匹配实例版本的 Zetaris 驱动 JAR **绝对路径** |
| `ZETARIS_USERNAME`、`ZETARIS_PASSWORD` | JDBC 必填；拉取 OpenAPI spec 的 Basic auth、可选 UI proxy 登录也使用；选能完成查询的非管理员账户 |
| `ZETARIS_REST_URL` | 直接 REST：本机为 `http://localhost:8888/api/v1.0`；远程用提供的 API base，保留 `/api/v1.0` |
| `ZETARIS_API_KEY` | 直接 REST 必填；由用户在实例 UI 的 **Management → API Tokens** 创建并直接保存到本地文件；不发给 agent、不贴日志 |
| `ZETARIS_ORG_ID` | REST / UI proxy：**Management → Organisation** 中的数字 ID，不能用组织名、URL slug 或猜测默认值 |
| `ZETARIS_BASE_URL` | 仅 UI proxy helpers：本机为 `http://localhost:3000`，远程用 UI origin，不附路径；不是直接 REST 地址 |
| `ZETARIS_QUERY_LIMIT` | 仅 UI proxy helper：可设为 `5`，上游默认 `1000`；本任务 SQL 仍显式 `LIMIT 5` |
| `ZETARIS_ENGINE_ID` | UI proxy helper 可选 compute engine ID |
| `ZETARIS_USER_AGENT` | 仅调用外部 API 的创建脚本需要 `app_name user@domain.tld`；本任务只读样本查询无需此键 |

本任务不需要 `PG*` 直连 PostgreSQL 参数，也不需要把镜像仓库或 AWS 密钥写进客户端文件。REST 的 `X-Request-ID` 由上游脚本生成 UUID，无需新增环境键。OpenAPI spec 用用户名 / 密码的 Basic auth，不能用 bearer key；仅做本次样本查询无需额外下载 spec。

JDBC 还需要 JDK 11+，驱动类为 `com.zetaris.lightning.jdbc.LightningDriver`。向提供实例 / 驱动的一方取得匹配 JAR 的实际位置，设置 `ZETARIS_JDBC_JAR`；本次未提供该路径，不搜索或猜测文件。JAR 保存在仓库外，不随提交分发。

macOS 的 `/usr/bin/java` 可能只是占位程序。可用 `/usr/libexec/java_home -V` 检查；若使用 Homebrew OpenJDK 17，`JAVA_HOME` 通常为 `/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home`（仅在该安装存在时设置），再运行 `"$JAVA_HOME/bin/java" -version` 确认版本。缺 JDK 时可使用官方建议的免费依赖 `brew install openjdk@17`，但这只准备客户端，不能安装或解锁 Zetaris 平台；本次未执行。

官方 Python JDBC runner 还需 `.venv` / `jaydebeapi`，之后准备客户端时可执行：

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements.txt
```

直接 Java JDBC 不需要这两个 Python 组件；直接 REST runner 使用 Python 标准库，不需要 JDK / JAR。详情见 [脚本指南](./getting-started/scripts/HOWTO.md)。

## 5. Preflight：分别报告 JDBC 与 REST

在 `sponsors/zetaris/getting-started` 中运行。preflight 只读，但配置齐全时会连接实例并发送检查查询，不只是本地检查：

```sh
# JDBC + REST：JAR 路径从 .env.local 读取。
python3 scripts/preflight.py --jdbc --env-file .env.local

# 只检查 REST（仍会提示 JDBC / spec 的用户名和密码是否缺失）。
python3 scripts/preflight.py --env-file .env.local
```

判断规则：

- `--jdbc` 仍检查 REST；缺 REST key 会使总退出码为 1，即使 JDBC 成功。应分开记录 JDBC、直接 REST、可选 UI proxy 的状态，不能用总退出码替代每条路线的结论。
- JDBC 要确认 Java 版本、JAR、所选 runner 的依赖、实际端点和认证查询。当前版本仅检测 Java 路径，不检查版本；TCP 检查硬编码 `localhost:10000`，而真正 JDBC 查询读取 `ZETARIS_JDBC_URL`。AWS 应另外对实例提供的主机 / 端口运行 `nc -zv HOST PORT`（替换为真实值），再以实际 JDBC 查询验证，不能因本机端口关闭误判 AWS 失败。
- 当前脚本会把端口检查的任何 `OSError` 显示为 `closed`。若独立网络检查报 `Operation not permitted`，先按网络权限问题排查，不能当作实例未启动。
- REST 成功应包括 `GET /datasource/datasources` 返回 HTTP 200 和 `SELECT 1` 验证。缺 key 时根本不会发起 REST 请求；401 需查认证，400 需核对组织 ID / 请求 ID。直接 REST 成功不代表 UI proxy 成功。不调用本机端口 `8889`。
- `SHOW LIGHTNING DATABASES`、USL 元数据检查在脚本中仅记为 INFO。后续必须亲自核对目标库 / 表是否存在；干净实例可能为空，不为填样本而自动执行创建脚本。所选查询路线缺前提或认证失败时停止实跑。

### 本次实际检查记录（2026-10-26）

已运行 `python3 scripts/preflight.py --jdbc`，退出码 **1**，输出 **`NOT READY: 10 check(s) failed`**。未创建 `.env.local` 或填写任何凭证。

| 项目 | 实际结果 |
|---|---|
| 主机 / Docker | macOS arm64、16 GiB 主机内存；Docker server 29.4.0、Compose 5.6.0，daemon 可用，10 CPU / 约 7.8 GiB 内存；主机约 23 GiB 可用磁盘，平台包及 Docker 虚拟磁盘仍待检查 |
| JDBC | `.env.local`、用户名 / 密码、可用 JDK、`.venv`、`jaydebeapi` 和 JAR 路径均缺；`localhost:10000` 独立 TCP 检查为 `ConnectionRefusedError`（errno 61）；未发送 JDBC SQL |
| 直接 REST | 缺 `ZETARIS_API_KEY`，脚本在发请求前失败；未验证 HTTP 服务 / 认证，未发送 REST SQL |
| 样本 / HubCrew | 未查询，未验证样本存在，未改变告警优先级或发送告警 |

这些是前提缺失的真实检查结果，不能作为连接成功证据。获得实例、端点、只读账号及所选协议的凭证 / 驱动后，重新执行本节检查。

另已用官方 `run_sql.py --dry-run` 预览查询草稿中的 9 个 SQL 块；均只打印语句，没有发送到 Zetaris。这只验证客户端预览流程，不证明服务端接受这些查询。

## 6. 后续只读验收

按 [query_home_ops.md](./query_home_ops.md) 逐条预览和执行 `SELECT 1`、`SHOW LIGHTNING DATABASES`、元数据查询及 `LIMIT 5`。记录真实执行时间、实例类型、协议、SQL、实际行数 / 脱敏摘要，再替换文中的【待实跑替换】；演示策略与真实家用告警分开说明。

Task B 完成还需要真实查询结果影响至少一次推理前的优先级 / 交接顺序，并留下可复核的决策前后证据。当前提交只完成可推送的预备工作。

## Install status (2026-10-26 北京时间 ≈01:00)
- Hobby / Run locally on **Mac mini** (`~/zetaris/zetaris-platform`)
- Registry login OK; `./preflight.sh` PASS (WARN: arm64 emulation, ~7GB Docker RAM)
- `docker compose pull` + `up -d` OK; `./verify.sh` **9/9 PASS**
- UI http://localhost:3000 — admin email from compose `.env` / `~/zetaris/registry.env` (chmod 600, not in git)
- JDBC jar: `jdbc/ndp-jdbc-driver-2.4.3.1-7eff043-driver.jar` (Java runtime not yet installed on mini; REST/UI path verified)
- Sample SQL: TPCDS_DB.reason and NY_TAXI.taxi_zones readable — see query_home_ops.md §3
