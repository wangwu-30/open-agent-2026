# Open Agent Hackathon 2026 — 交稿材料包

给王五的助手 / 佳恒。赛道：**Track 03** · 项目：**HubCards + 家用班组** · 目标：**冠军**。

| 文件 | 用途 |
|---|---|
| [DECISION.md](./DECISION.md) | 为何 Track03、路径 C、双赞助 |
| [SUBMISSION.md](./SUBMISSION.md) | 提交表英文字段 + 中文对照 |
| [ARCHITECTURE.md](./ARCHITECTURE.md) | 推理架构 mermaid |
| [DEMO-SCRIPT.md](./DEMO-SCRIPT.md) | 1–4 分钟分镜 + 幻灯提纲 |
| [SPONSOR-PLAN.md](./SPONSOR-PLAN.md) | Meterless/Zetaris (live on Mac mini — see sponsors/zetaris/LIVE.md) 今晚任务（交 Codex/taskq） |
| [CHECKLIST.md](./CHECKLIST.md) | 佳恒要点步骤 + blockers |

代码接入：**不要让云端 bot 改产品仓**；按 SPONSOR-PLAN 派 Mac mini。

## Sponsors

- [Meterless H-MEM bridge](./sponsors/hmem-notebook/README.md)：Track 03 HubCrew 的本地交接记忆演示，包含三类 seed、跨进程检索、provenance 与审计；安装和录屏步骤见子目录 README。
- **Zetaris 本机只读样本查询已实跑**（2026-10-26，北京时间）：Mac mini 实例 `./verify.sh` 9/9 PASS，`SELECT 1`、`NY_TAXI.taxi_zones LIMIT 5`、`TPCDS_DB.reason ORDER BY r_reason_sk LIMIT 5` 均通过，见 [LIVE.md](./sponsors/zetaris/LIVE.md)。[查询与演示决策记录](./sponsors/zetaris/query_home_ops.md#3-已实跑样本结果与-hubcrew-演示决策2026-10-26)展示 5 条 reason 样本到交接优先级的人工映射；样本不代表真实家用故障，尚未自动接通 HubCrew、H-MEM 或告警出口。[接入预备文档](./sponsors/zetaris/SETUP.md)保留安装与客户端参考。官方仓库以子模块固定版本，首次使用先执行 `git submodule update --init sponsors/zetaris/getting-started`。
