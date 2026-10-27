# Open Agent Hackathon 2026 — HubCrew 已提交材料包

**Submitted：Track 03 — Reasoning Architecture / HubCrew 已正式提交。** 北京时间 **2026-10-27 01:38** 已核验 `Submitted 1/1`；硬截止为 **2026-10-28 07:45 北京时间**。

提交状态、平台回执和实际材料以 [demo/SUBMISSION-STATUS.md](./demo/SUBMISSION-STATUS.md) 为准。本仓保存 **HubCards + 家用班组** 的提交材料、赞助桥与演示证据；冲刺待办已归档。

| 文件 | 用途 |
|---|---|
| [demo/SUBMISSION-STATUS.md](./demo/SUBMISSION-STATUS.md) | 当前提交状态、确认截图与平台链接 |
| [demo/submission-description.txt](./demo/submission-description.txt) | 实际提交的英文 Description |
| [demo/DEMO-URL.md](./demo/DEMO-URL.md) · [视频文件](./demo/hubcrew-demo.mp4) | 已提交的 3:10 / 1080p demo、托管链接与公开备用 |
| [HubCrew-Open-Agent-2026.pptx](./HubCrew-Open-Agent-2026.pptx) | 已提交幻灯 |
| [demo/evidence/](./demo/evidence/) · [demo/FINISH.md](./demo/FINISH.md) | 演示证据、视频核验与收尾记录 |
| [DECISION.md](./DECISION.md) | 已采用的 Track 03、路径 C、双赞助决策记录 |
| [SUBMISSION.md](./SUBMISSION.md) | 归档字段草稿与中文对照；最终文本见实际 Description |
| [ARCHITECTURE.md](./ARCHITECTURE.md) | 推理架构 Mermaid 与提交范围 |
| [DEMO-SCRIPT.md](./DEMO-SCRIPT.md) | 已归档的原分镜与幻灯提纲，附实际产物入口 |
| [SPONSOR-PLAN.md](./SPONSOR-PLAN.md) | Meterless / Zetaris 已交付范围、证据与旧计划归档 |
| [CHECKLIST.md](./CHECKLIST.md) | 提交已完成摘要与旧清单归档说明 |

预存代码（HubCards、家用班组、imwire、teamrecall、benefit）已在提交中声明；本次增量为公开仓、架构文档、赞助桥/查询证据、demo 与幻灯。

## Sponsors

- [Meterless H-MEM bridge](./sponsors/hmem-notebook/README.md)：Track 03 HubCrew 的本地交接记忆演示，包含三类 seed、跨进程检索、provenance 与审计；安装和录屏步骤见子目录 README。
- **Zetaris 本机只读样本查询已实跑**（2026-10-26，北京时间）：Mac mini 实例 `./verify.sh` 9/9 PASS，`SELECT 1`、`NY_TAXI.taxi_zones LIMIT 5`、`TPCDS_DB.reason ORDER BY r_reason_sk LIMIT 5` 均通过，见 [LIVE.md](./sponsors/zetaris/LIVE.md)。[查询与演示决策记录](./sponsors/zetaris/query_home_ops.md#3-已实跑样本结果与-hubcrew-演示决策2026-10-26)展示 5 条 reason 样本到交接优先级的人工映射；样本不代表真实家用故障，尚未自动接通 HubCrew、H-MEM 或告警出口。[接入预备文档](./sponsors/zetaris/SETUP.md)保留历史安装与客户端参考，其中旧阻塞状态已由 LIVE 记录更新。官方仓库以子模块固定版本，首次使用先执行 `git submodule update --init sponsors/zetaris/getting-started`。
