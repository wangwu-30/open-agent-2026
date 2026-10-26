# HubCrew · Meterless H-MEM bridge

供 Track 03 HubCrew 终端演示使用：把班组交接示例写入 Meterless H-MEM，再跨进程召回部署决策，展示 memory id、provenance 与审计历史。实现范围对应根目录 [SPONSOR-PLAN.md 的 Task A](../../SPONSOR-PLAN.md#task-a--meterless-h-mem默认选这条最快可演示)。

## 从零启动

需要 Node.js 22 或更新版本、npm、Git，以及安装时的网络连接。从本仓根目录执行：

```bash
cd sponsors/hmem-notebook
npm install
npm run setup
```

`setup` 将官方 H-MEM 参考实现放入 `vendor/hmem/`，固定上游提交为 `1742dec56a66e58eef9dda2d2b865823758ca8cd`。`vendor/` 不入库，因此每份新克隆都必须运行这一步。CLI 启动时应显示 `engine source: vendor/hmem`；若缺少引擎或 setup 失败，先修复安装，再继续演示。

依赖和引擎安装后，以下命令使用离线 `retrieval-only` 模式，无需 API key。记忆与账本保存在本子目录的 `.notebook/`，由 H-MEM 负责持久化和恢复。

## 录屏流程与冷启动验收

以下命令均在 `sponsors/hmem-notebook/` 执行：

```bash
# 写入三个交接示例：unfinished_work / failed_path / live_decision
npx tsx notebook.ts seed

# seed 已退出；新的 CLI 进程从磁盘恢复记忆并执行真实检索
npx tsx notebook.ts ask "当前仍生效的部署决策"

# 将下面的占位符替换为上一步实际返回的 memory id
npx tsx notebook.ts audit '<memory-id>'

# 可选：展示整理计划，不执行整理
npx tsx notebook.ts sleep --preview
```

`seed` 按原文跳过已存在的示例，可以重复执行。`ask` 应显示召回的部署决策、memory id、相关度与 provenance；`audit` 应显示同一 id 的写入和读取账本记录。也可关闭终端，再进入同一目录执行相同 `ask`，确认无需重新 seed 即可召回。冷启动指重启进程并保留 `.notebook/`；删除它会删除本地演示记忆。

自动验收使用独立进程和隔离的数据目录，验证写入后退出、重新启动检索和审计：

```bash
npm test
```

新增自己的交接事实可运行：

```bash
npx tsx notebook.ts remember "We always deploy HubCrew only after green CI and a rollback check."
```

若 `ask` 没有返回目标记忆，保留实际结果，检查 seed 输出、engine source 和状态目录；不要用预写答案代替召回结果。审计时始终使用本次输出中的 id。

## 命令如何使用 H-MEM

入口是 [notebook.ts](./notebook.ts)，引擎装载见 [src/engine.ts](./src/engine.ts)。调用进入官方参考实现中的以下服务：

| 命令 | H-MEM service | 实际作用 |
|---|---|---|
| `remember "…"` / `seed` | `MemoryMiningService` + `MemoryStoreService` | 挖掘输入并写入记忆；未命中挖掘规则的输入通过 Store 原文捕获 |
| `ask "…"` | `MemoryRetrievalService` | 混合评分、排序、返回记忆及上下文；输出实际召回 id 与 provenance |
| `audit <memory-id>` | `TrustLedgerService` | 读取该记忆的追加式账本历史，包括写入与检索读取 |
| `sleep --preview` | `SleepCycleService` | 展示巩固（`short_term` → `long_term`）、归档和综合候选，不应用计划 |

## 引擎来源与演示边界

模板来自 [Meterless agentathon-starter](https://github.com/Meterless/Meterless/tree/1742dec56a66e58eef9dda2d2b865823758ca8cd/templates/agentathon-starter)；engine source 是其 [H-MEM reference](https://github.com/Meterless/Meterless/tree/1742dec56a66e58eef9dda2d2b865823758ca8cd/engines/hmem/reference)，安装后位于 `vendor/hmem/src/`。模板与参考引擎使用 Apache-2.0 许可证；引擎合同见上游 [engines/hmem/AGENTS.md](https://github.com/Meterless/Meterless/blob/1742dec56a66e58eef9dda2d2b865823758ca8cd/engines/hmem/AGENTS.md)。

此桥接调用真实 H-MEM 服务。参考实现使用 64 维确定性哈希向量、ASCII tokenizer 和 JSON/JSONL 持久化，适合说明记忆生命周期，不具备生产语义向量模型的检索能力。JSON/JSONL 是引擎的存储格式；检索、评分与账本操作由 H-MEM 完成。

为支持指定录屏问句，CLI 将精确问句 `当前仍生效的部署决策` 显式映射为英文检索词 `current live deployment decision deploy`，同时打印原问句与实际查询。其他问句原样传入引擎，目前不提供通用中文语义检索。此适配仅改变查询文本，不替换引擎结果，也不按 id 选取预定答案。检索沿用模板的 `threshold: 0.1`。

`unfinished_work`、`failed_path` 和 `live_decision` 是交接示例的输入分类；`live_decision` 不表示引擎保证过滤全部旧决策。请结合返回内容、provenance 和审计历史判断结果。当前交付是本地 CLI 记忆桥与示例，未自动连接 HubCards、G1 或 Zetaris；Zetaris 仍属于 [Task B](../../SPONSOR-PLAN.md#task-b--zetaris规则必接可能成-blocker)。

`.notebook/`、`vendor/`、`node_modules/` 和本地密钥文件由 `.gitignore` 排除，不应提交。复现通过安装步骤与示例输入完成。
