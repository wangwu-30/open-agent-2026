# DEMO-SCRIPT — 1–4 分钟（冲 Demo 15）

官方要求：demo video **1–4 minutes**，展示主流程、如何解挑战、关键特性、**Zetaris & Meterless 如何接入**。

建议总长：**3:00–3:30**（留余量，勿超 4:00）。

## 分镜

| 时码 | 画面 | 口述（中/英可混，评委偏英 → 建议英主中辅） | 卡点 |
|---:|---|---|---|
| 0:00–0:20 | 标题卡：HubCrew · Track 03 · wangwu.ai | “One person, many named agents. Handoffs used to lose context. HubCrew turns memory and constitution into reliable action.” | 片头勿超过 20s |
| 0:20–0:45 | HubCards 打开 → 点名一个 agent（或等价会话 UI） | “Human entry is HubCards. Alerts default here; urgent also hits Telegram until push exists.” | 若真机不稳：切预先录好的 HubCards 片段，口播声明 live+recorded |
| 0:45–1:20 | 交接包可视化：未完成 / 失败路径 / 仍生效决策 | “Constitution G1: when I address a named agent, it inherits prior decision preferences. Handoff carries unfinished work, failed paths, and live decisions.” | **必须出现三块字段**，勿只口头 |
| 1:20–2:00 | Meterless：`remember` 一条决策 → `ask` 召回并显示 memory id / provenance → 可选 `audit` | “Memory spine is Meterless H-MEM—not a fake vector paste. Judges can see mining, retrieval, and ledger.” | 终端字体够大；startup 行显示 engine source |
| 2:00–2:35 | Zetaris：SQL Editor 或脚本 `SELECT … LIMIT 5` → agent 用结果决定优先级/是否告警 | “Data plane is Zetaris. The agent queries governed facts before it acts.” | 至少一条真实查询结果入镜 |
| 2:35–3:05 | 行动：告警卡片进 HubCards（或 IM 流式回复 via imwire） | “Decision becomes an action on the same human surface—no lost ping.” | 成功回执入镜 |
| 3:05–3:25 | 架构一页（mermaid 导出图）+ GitHub URL | “Single agent = entry + own scheduler; collaboration sits above. Repo: github.com/wangwu-30/open-agent-2026.” | URL 停留 ≥3s |
| 3:25–3:40 | 结束卡：Track 03 · pre-existing declared · sponsors named | “Pre-existing HubCards/crew declared. Meterless + Zetaris integrated as shown.” | **勿声称未拍到的能力** |

## 录制清单

- [ ] 麦克风清晰；分辨率 ≥ 1080p
- [ ] 脱敏：无真实密钥、私人聊天全文
- [ ] Meterless 与 Zetaris **各至少 10 秒实机**
- [ ] 片尾贴：repo、wangwu.ai、作者 GitHub @wangwu-30
- [ ] 上传：YouTube 未列出 / Loom / Drive；链接写入提交表

## 备用（若 HubCards 当日崩）

B-roll 顺序：架构图 → H-MEM CLI 全流程 → Zetaris SQL → imwire echo/assistant → 口头说明 HubCards 为默认告警面（配静态截图）。仍需声明 pre-existing + 何为今晚 delta。

## 幻灯提纲（§06 另要 slide deck；可另做 6–8 页）

1. Problem & user  
2. Solution one-liner  
3. Architecture diagram  
4. Agent workflow (handoff → reason → act)  
5. Stack (HubCards, 班组, imwire, H-MEM, Zetaris)  
6. Meterless usage (commands → services)  
7. Zetaris usage (query → decision)  
8. What’s unique + future (Nightshift optional, push, open-source HubCards)
