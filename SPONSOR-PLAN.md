# SPONSOR-PLAN — 双赞助交付记录 / Archived

**Track 03 / HubCrew 已 Submitted，提交阶段已完成。** 核验时间为 **2026-10-27 01:38 北京时间**；状态和实际声明见 [demo/SUBMISSION-STATUS.md](./demo/SUBMISSION-STATUS.md) 与 [提交 Description](./demo/submission-description.txt)。原冲刺计划和派工指令已归档，本页记录实际交付范围。

原方案按活动规则 §05 的 Zetaris / Meterless 双赞助要求准备；两者用法已写入提交材料。完整架构方向与本次实际演示的边界如下。

<!-- 保留桥接文档现有的 Task A / Task B 链接。 -->
<a id="task-a--meterless-h-mem默认选这条最快可演示"></a>

## Task A — Meterless H-MEM：本地桥已交付

- [sponsors/hmem-notebook/](./sponsors/hmem-notebook/README.md) 已提供 TypeScript CLI，调用官方参考引擎的 `remember`、`ask`、`audit`、`sleep` 服务；安装、复现步骤及命令到 service 的映射均在该 README。
- Demo 展示真实写入后在新进程检索，包含 memory id、相关度与 provenance；[原始输出与执行记录](./demo/evidence/README.md) 已保存。
- 演示使用 `retrieval-only` 模式与参考实现的确定性哈希向量。本地桥尚未自动连接 HubCards、G1 或 Zetaris。

<a id="task-b--zetaris规则必接可能成-blocker"></a>

## Task B — Zetaris：本机 SQL 与证据已交付

- Mac mini 本机 Docker Compose 实例已实跑，`./verify.sh` **9/9 PASS**，见 [LIVE.md](./sponsors/zetaris/LIVE.md)。原“实例未安装”的阻塞已解除。
- 已核验 `SELECT 1`、`NY_TAXI.taxi_zones LIMIT 5`、`TPCDS_DB.reason ORDER BY r_reason_sk LIMIT 5`；[查询记录](./sponsors/zetaris/query_home_ops.md#3-已实跑样本结果与-hubcrew-演示决策2026-10-26) 保存结果摘要与 P0–P2 交接优先级映射。
- Demo 使用实际 Zetaris 浏览器查询录屏；[视频核验记录](./demo/evidence/video-qc.md) 已保存。
- 查询对象是 supplied samples，优先级为人工演示映射；未声明生产家用数据或自动端到端派工、告警送达。
- [SETUP.md](./sponsors/zetaris/SETUP.md) 保留接入准备阶段的安装与客户端参考；其中旧阻塞文字以 LIVE 记录为准。

## Task C — 公开仓与提交材料：已完成

- 已采用路径 C：[wangwu-30/open-agent-2026](https://github.com/wangwu-30/open-agent-2026) 保存架构文档、赞助桥、查询证据、[demo](./demo/hubcrew-demo.mp4) 与 [幻灯](./HubCrew-Open-Agent-2026.pptx)。
- 相关公开代码：[imwire](https://github.com/wangwu-30/imwire)、[teamrecall](https://github.com/wangwu-30/teamrecall)。
- HubCards、家用班组、imwire、teamrecall、benefit 已声明为预存代码；主运行时未全部开源的边界已保留。

## 已归档的备选方案

原路径 A（HubCards / 班组公开镜像）、路径 B（仅 imwire + 录屏）、Nightshift / Nemotron 和 HubCards 原生 SDK 深接均为旧备选或扩展设想，已退出本次提交待办，不声明为已实现。提交完成情况与平台回执统一见 [SUBMISSION-STATUS.md](./demo/SUBMISSION-STATUS.md)。
