# Open Agent Hackathon 2026 — 交稿材料包

给王五的助手 / 佳恒。赛道：**Track 03** · 项目：**HubCards + 家用班组** · 目标：**冠军**。

| 文件 | 用途 |
|---|---|
| [DECISION.md](./DECISION.md) | 为何 Track03、路径 C、双赞助 |
| [SUBMISSION.md](./SUBMISSION.md) | 提交表英文字段 + 中文对照 |
| [ARCHITECTURE.md](./ARCHITECTURE.md) | 推理架构 mermaid |
| [DEMO-SCRIPT.md](./DEMO-SCRIPT.md) | 1–4 分钟分镜 + 幻灯提纲 |
| [SPONSOR-PLAN.md](./SPONSOR-PLAN.md) | Meterless/Zetaris 今晚任务（交 Codex/taskq） |
| [CHECKLIST.md](./CHECKLIST.md) | 佳恒要点步骤 + blockers |

代码接入：**不要让云端 bot 改产品仓**；按 SPONSOR-PLAN 派 Mac mini。

## Sponsors

- [Meterless H-MEM bridge](./sponsors/hmem-notebook/README.md)：Track 03 HubCrew 的本地交接记忆演示，包含三类 seed、跨进程检索、provenance 与审计；安装和录屏步骤见子目录 README。
- [Zetaris 接入预备](./sponsors/zetaris/SETUP.md)：[官方入门](https://zetaris.github.io/getting-started/)与本机 / AWS Free Tier 路线、客户端配置和 preflight；[只读 SQL 与 HubCrew 告警优先级草稿](./sponsors/zetaris/query_home_ops.md)说明 Track 03 数据层计划。**实例未装则 blocker**：当前尚无实例、无真实查询结果，预备文档不代表已完成 [Task B](./SPONSOR-PLAN.md#task-b--zetaris规则必接可能成-blocker) 接入。官方仓库以子模块固定版本，首次使用先执行 `git submodule update --init sponsors/zetaris/getting-started`。
