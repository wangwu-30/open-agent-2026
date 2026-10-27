# DECISION — Open Agent Hackathon 2026

**已采用方案 / Archived：Track 03 HubCrew 已 Submitted。** 当前状态见 [demo/SUBMISSION-STATUS.md](./demo/SUBMISSION-STATUS.md)；以下保留原选型依据，原冲刺安排已结束。

**原决策记录日期**: 2026-10-26（原文采用 America/Los_Angeles）；提交核验为北京时间 2026-10-27 01:38。
**交稿死线**: UTC 2026-10-27 23:45 = 北京时间 2026-10-28 07:45  
**原参赛目标**: 冠军（不弃 Sponsor tech 10）

## 选定

| 项 | 决定 |
|---|---|
| Track | **03 Reasoning Architecture** |
| 项目叙事 | **HubCards + 家用班组（home multi-agent）** |
| 已采用公开仓路径 | **(C)** `wangwu-30/open-agent-2026`（架构文档 + demo 脚本 + Meterless/Zetaris 桥接 + 链到现有公开仓）已交付 |
| 赞助商 | **Meterless + Zetaris** 本地桥与查询证据已交付，范围见 [SPONSOR-PLAN.md](./SPONSOR-PLAN.md) |
| 不走 | Wildcard（奖池更小，且「只评新工作」，会打折扣已有 HubCards/班组存量） |

## 为何 Track 03（重评结论）

1. **赛题对齐**：Track 03 =「把 data / knowledge / memory / reasoning 变成可靠决策与行动」。家用班组的核心正是：命名 agent 交接（未完成工作 / 失败路径 / 仍生效决策）+ 宪法 G1 偏好接管 + 单入口任务调度 → 可靠行动；HubCards 是人侧入口。
2. **奖池**：Track 03 现金池 $3,600（1/2/3 = $1,500 / $1,200 / $900）> Wildcard $2,000。
3. **Wildcard 不利**：强制双赞助且 **只评新工作**；佳恒存量（HubCards/班组/imwire/teamrecall）无法吃满 Impact/Technical。规则 §05 已要求**所有轨**接 Zetaris+Meterless，走 Wildcard 没有「免接赞助」优势，只多了「存量打折」。
4. **无硬证据**表明 Wildcard 更易夺冠 → **已选择 Track 03 + 双赞助方案**。

## 为何 HubCards + 家用班组（可组合个人项目）

- **用户**：佳恒本人（一人运营多个命名 agent），入口要稳、告警要到人。
- **HubCards**：定制 iOS 家用班组入口；agent 告警默认走 HubCards；尚无 push 时紧急另走 Telegram。
- **班组**：一个 agent = 单一入口 + 自己的任务调度；多 agent 协作在上层独立层。
- **宪法 G1**：点名命名 agent 时接管上轮决策偏好；交接含未完成 / 试过失败 / 仍生效决策；各 agent 自有宪法与 skill；验收用离线对比。
- **可引用的公开锚点**（已核实 public）：
  - https://github.com/wangwu-30/imwire — agent↔IM 入口层（Telegram/飞书等）
  - https://github.com/wangwu-30/teamrecall — git-native 团队记忆（可作为 knowledge 旁路）
  - HubCards / 班组运行时：**本次提交未公开完整主运行时**；采用路径 C 材料仓，实际演示范围见 [提交 Description](./demo/submission-description.txt)。

## 原评分策略（100，历史方案）

以下为原规划，不代表全部链路已在 demo 中实现；实际展示的是 H-MEM 跨进程检索与 Zetaris SQL，自动派工和告警送达仍为架构方向。

| 维度 | 分 | 打法 |
|---|---:|---|
| Impact | 30 | 真实一人多 agent 家用场景；交接失败=上下文丢失，本方案直接打 |
| Technical | 20 | 分层：入口→调度→记忆(H-MEM)→数据(Zetaris)→行动；公开桥接代码可审 |
| Demo | 15 | 1–4 分钟硬流程：点名交接 → 记忆召回带 provenance → 行动/告警到 HubCards |
| Innovation | 15 | 「单 agent 调度 vs 上层协作」分层 + 宪法/失败路径进记忆 |
| UX | 10 | HubCards 一人入口；demo 里只露一个清晰表面 |
| Sponsor tech | 10 | **不可弃**：Meterless H-MEM（agentathon-starter）+ Zetaris SQL 数据层；见 `SPONSOR-PLAN.md` |

## 提交要求与完成记录

- 官方 §05：**Every submission must integrate Zetaris and Meterless.**
- §06 所需 demo 视频、slide deck、GitHub+README、赞助商用法说明已提交，实际材料链接见提交状态记录。
- 预存产品代码已在表单 **declare**（HubCards/班组/imwire/teamrecall/benefit）。
- 双赞助本地桥、查询证据及实现边界已写入材料，见 [SPONSOR-PLAN.md](./SPONSOR-PLAN.md)。

## 一句话

**Track 03 + HubCards/班组推理架构 + 路径 C 公开仓 + Meterless H-MEM 与 Zetaris 本地演示，已完成提交。**
