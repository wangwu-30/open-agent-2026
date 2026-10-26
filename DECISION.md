# DECISION — Open Agent Hackathon 2026

**日期（America/Los_Angeles）**: 2026-10-26  
**交稿死线**: UTC 2026-10-27 23:45 = 北京时间 2026-10-28 07:45  
**目标**: 冠军（不弃 Sponsor tech 10）

## 选定

| 项 | 决定 |
|---|---|
| Track | **03 Reasoning Architecture** |
| 项目叙事 | **HubCards + 家用班组（home multi-agent）** |
| 公开仓默认路径 | **(C)** 新建 `wangwu-30/open-agent-2026`（架构文档 + demo 脚本 + Meterless/Zetaris 桥接 + 链到现有公开仓） |
| 赞助商 | **必须诚实接入 Meterless + Zetaris**（官方规则 §05：Every submission must integrate…；非仅 Wildcard） |
| 不走 | Wildcard（奖池更小，且「只评新工作」，会打折扣已有 HubCards/班组存量） |

## 为何 Track 03（重评结论）

1. **赛题对齐**：Track 03 =「把 data / knowledge / memory / reasoning 变成可靠决策与行动」。家用班组的核心正是：命名 agent 交接（未完成工作 / 失败路径 / 仍生效决策）+ 宪法 G1 偏好接管 + 单入口任务调度 → 可靠行动；HubCards 是人侧入口。
2. **奖池**：Track 03 现金池 $3,600（1/2/3 = $1,500 / $1,200 / $900）> Wildcard $2,000。
3. **Wildcard 不利**：强制双赞助且 **只评新工作**；佳恒存量（HubCards/班组/imwire/teamrecall）无法吃满 Impact/Technical。规则 §05 已要求**所有轨**接 Zetaris+Meterless，走 Wildcard 没有「免接赞助」优势，只多了「存量打折」。
4. **无硬证据**表明 Wildcard 更易夺冠 → **默认 Track 03 + 双赞助加分**。

## 为何 HubCards + 家用班组（可组合个人项目）

- **用户**：佳恒本人（一人运营多个命名 agent），入口要稳、告警要到人。
- **HubCards**：定制 iOS 家用班组入口；agent 告警默认走 HubCards；尚无 push 时紧急另走 Telegram。
- **班组**：一个 agent = 单一入口 + 自己的任务调度；多 agent 协作在上层独立层。
- **宪法 G1**：点名命名 agent 时接管上轮决策偏好；交接含未完成 / 试过失败 / 仍生效决策；各 agent 自有宪法与 skill；验收用离线对比。
- **可引用的公开锚点**（已核实 public）：
  - https://github.com/wangwu-30/imwire — agent↔IM 入口层（Telegram/飞书等）
  - https://github.com/wangwu-30/teamrecall — git-native 团队记忆（可作为 knowledge 旁路）
  - HubCards / 班组运行时：**目前无 public repo** → 用 demo 录屏 + 路径 C 文档仓承载提交。

## 冲冠军的分数地图（100）

| 维度 | 分 | 打法 |
|---|---:|---|
| Impact | 30 | 真实一人多 agent 家用场景；交接失败=上下文丢失，本方案直接打 |
| Technical | 20 | 分层：入口→调度→记忆(H-MEM)→数据(Zetaris)→行动；公开桥接代码可审 |
| Demo | 15 | 1–4 分钟硬流程：点名交接 → 记忆召回带 provenance → 行动/告警到 HubCards |
| Innovation | 15 | 「单 agent 调度 vs 上层协作」分层 + 宪法/失败路径进记忆 |
| UX | 10 | HubCards 一人入口；demo 里只露一个清晰表面 |
| Sponsor tech | 10 | **不可弃**：Meterless H-MEM（agentathon-starter）+ Zetaris SQL 数据层；见 `SPONSOR-PLAN.md` |

## 合规要点（写进提交表，勿伪造）

- 官方 §05：**Every submission must integrate Zetaris and Meterless.**
- §06 必交：1–4 min demo 视频、slide deck、GitHub+README、赞助商用法说明。
- 预存产品代码须在表单 **declare**（HubCards/班组/imwire/teamrecall）。
- Sponsor tech：未接则 0 分且可能违反 §05 → 今晚优先落地最小双接入（见 SPONSOR-PLAN）。

## 一句话

**Track 03 + HubCards/班组推理架构 + 路径 C 公开仓 + 今晚 Meterless H-MEM 与 Zetaris 最小桥接，冲冠军。**
