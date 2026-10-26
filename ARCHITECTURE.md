# ARCHITECTURE — HubCrew × Track 03

对齐 Track 03：**data → knowledge → memory → reasoning → reliable decisions & actions**。

## 分层主张（佳恒口径，勿改）

1. **一个 agent** = **单一入口** + **自己的任务调度**（决定进哪个 session：排队或新开）。
2. **多 agent 协作** = 上层独立层（点名、交接、路由），不要和单 agent 核混在一起。
3. **HubCards** = 家用班组人侧入口；告警默认 HubCards；无 push 时紧急 Telegram。
4. **宪法 G1** = 点名命名 agent → 接管上轮决策偏好；交接包 = 未完成 + 试过失败 + 仍生效决策；各 agent 自有宪法/skill；验收离线对比。

## 系统图（mermaid）

```mermaid
flowchart TB
  subgraph Human["人侧"]
    U[佳恒 / 一人运营]
    HC[HubCards iOS 入口]
    TG[Telegram 紧急兜底]
  end

  subgraph Entry["入口层 Entry"]
    IM[imwire L1–L2<br/>多 IM 适配 + person/session]
    HCAPI[HubCards 会话 / 告警通道]
  end

  subgraph AgentCore["单 Agent 核 = 入口 + 自调度"]
    SCH[Task Scheduler<br/>queue vs new session]
    CONST[Agent Constitution + Skills]
    REASON[Reasoning Loop<br/>decide / act / report]
  end

  subgraph Collab["上层协作层 Collaboration"]
    NAME[Named routing 点名]
    HO[Handoff package<br/>unfinished / failed / live decisions]
    G1[Constitution G1<br/>偏好接管]
  end

  subgraph Memory["Memory · Meterless H-MEM"]
    REM[remember · mining+store]
    ASK[ask · retrieval+provenance]
    AUD[audit · trust ledger]
    SLP[sleep · consolidation]
  end

  subgraph Data["Data · Zetaris"]
    ZQ[Lightning SQL / REST|JDBC]
    SAMP[Samples + home-ops facts]
  end

  subgraph Knowledge["Knowledge 旁路"]
    TR[teamrecall git-native lessons]
  end

  subgraph Action["行动 / 送达"]
    ACT[Tools: 写回 / 派工 / 告警]
    OUT[HubCards card / IM reply]
  end

  U --> HC
  U --> TG
  HC --> HCAPI
  TG --> IM
  HCAPI --> NAME
  IM --> NAME
  NAME --> G1 --> HO
  HO --> SCH
  SCH --> REASON
  CONST --> REASON
  REASON <--> ASK
  REASON --> REM
  REASON --> AUD
  REASON --> SLP
  REASON <--> ZQ
  ZQ --> SAMP
  REASON -.-> TR
  REASON --> ACT --> OUT
  OUT --> HC
  OUT --> IM
```

## 与 Track 03 对齐点（评委一眼能指）

| Track 03 要素 | 本方案落点 |
|---|---|
| Data | Zetaris 查询家用/样本事实，再决策优先级与是否告警 |
| Knowledge | 宪法/skill + teamrecall 旁路（团队已审教训） |
| Memory | Meterless H-MEM：交接与决策写入、带 provenance 召回、sleep 巩固 |
| Reasoning | 单 agent 调度循环 + G1 偏好 + 失败路径忌避 |
| Reliable decisions & actions | 交接包结构化 → 行动/告警到 HubCards；离线对比验收 |

## 运行时拓扑（家用）

- **Phone**: HubCards（人）
- **Mac mini**: 班组 agent 进程、Codex/taskq、Meterless bridge、可选 Zetaris client
- **Public GitHub**: `open-agent-2026`（文档+桥）· `imwire` · `teamrecall`
- **Private**: HubCards 源码 / 班组完整运行时（demo 录屏证明，提交表 declare）

## 非目标（今晚）

- 不把公司飞书班组与家用部署打成一套 demo。
- 不伪造 Nightshift/Nemotron，除非 Mac mini 真跑通。
- Bot **不写产品代码**；桥接由 Mac mini Codex/taskq 按 `SPONSOR-PLAN.md` 落地。
