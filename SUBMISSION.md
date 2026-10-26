# SUBMISSION — 可粘贴字段草稿

> 入口：https://hackathon.genai.works/event/open-agent-hackathon-2026  
> 死线：UTC 2026-10-27 23:45（北京 10-28 07:45）  
> 占位符用 `[[...]]` — 佳恒提交前替换。

---

## English (paste into form)

### Project title
**HubCrew: Named-Agent Reasoning Architecture for One-Person Home Ops**

### One-liner / tagline
A single human entry (HubCards) plus named agents that hand off unfinished work, failed paths, and live decisions—turning memory and constitution into reliable actions.

### Track
Track 03 — Reasoning Architecture

### Problem / target users
Solo operators who run many specialized agents at home hit the same failure mode: context dies at handoff. Preferences, half-finished tasks, and “we already tried X” leak between agents. Alerts scatter across IMs. The user is one person; the system behaves like many forgetful interns.

**Primary user:** a single builder/operator (wangwu / 佳恒) coordinating a home multi-agent crew from one phone surface.

### Solution
**HubCrew** layers:
1. **Human entry** — HubCards (custom iOS): default surface for agent alerts; urgent fallback Telegram until push ships.
2. **Per-agent reasoning unit** — one agent = one entry + its own task scheduler (queue vs new session).
3. **Upper collaboration layer** — naming/handoff, not mixed into the single-agent core.
4. **Constitution G1** — when a named agent is addressed, it inherits prior decision preferences; handoff package = unfinished work + failed attempts + still-valid decisions; each agent has its own constitution & skills; acceptance via offline comparison.
5. **Memory spine (Meterless H-MEM)** — `remember` / `ask` / `audit` / `sleep` so decisions and failures are mined, retrieved with provenance, and consolidated.
6. **Data plane (Zetaris)** — governed SQL over sample/home ops facts the agent must reason on before acting.

### Technical approach
- Architecture: Entry → Session/Scheduler → Memory (H-MEM) → Tools/Data (Zetaris + IM adapters) → Action/Alert.
- Public code anchors:
  - Submission repo: `[[https://github.com/wangwu-30/open-agent-2026]]` (docs + sponsor bridges + demo script)
  - IM adapter layer: https://github.com/wangwu-30/imwire (public, MIT)
  - Team knowledge memory: https://github.com/wangwu-30/teamrecall (public, MIT)
- HubCards / home crew runtime: demonstrated on device / Mac mini; **declared as pre-existing product code** (not all open-sourced tonight).
- Dev: Cursor / Codex on Mac mini for bridges; no fake sponsor screenshots.

### Demo link
`[[YouTube / Loom / drive URL — 1–4 min, see DEMO-SCRIPT.md]]`

### Slide deck link
`[[Google Slides / PDF URL — see slide outline in CHECKLIST]]`

### GitHub repository
`[[https://github.com/wangwu-30/open-agent-2026]]`  
Related (declare in form): https://github.com/wangwu-30/imwire · https://github.com/wangwu-30/teamrecall

### Sponsor tech — Zetaris
`[[Describe after SPONSOR-PLAN tasks land]]`  
Planned: Zetaris instance (local or AWS) + read-only Lightning SQL over sample/home-ops tables; agent queries before deciding handoff priority / alert urgency. Setup refs: https://zetaris.github.io/getting-started/

### Sponsor tech — Meterless
`[[Describe after SPONSOR-PLAN tasks land]]`  
Planned: Meterless **H-MEM** via `agentathon-starter` (`remember`/`ask`/`audit`/`sleep`) as the handoff+constitution memory spine. Starter: https://github.com/Meterless/Meterless/tree/main/templates/agentathon-starter  
Nightshift: optional stretch if Mac mini GPU path ready—not required for minimal score.

### Cursor / NVIDIA (if asked)
- Cursor/Codex: used to implement sponsor bridges and docs on Mac mini (`taskq` jobs).
- NVIDIA/Nemotron: **not claimed unless Nightshift path actually runs**; optional stretch only.

### Pre-existing product code (declare)
HubCards (iOS entry), home multi-agent crew (班组), imwire, teamrecall, related home deployment (benefit). Hackathon delta: reasoning-architecture documentation, public submission repo, Meterless H-MEM bridge, Zetaris query path, demo + slides.

### Website
https://www.wangwu.ai

---

## 中文对照（给佳恒审，不必整段贴英文表）

**标题**：HubCrew：一人家用班组的命名 Agent 推理架构  
**一句话**：HubCards 单入口 + 命名 agent 交接（未完成/失败路径/仍生效决策）+ 宪法偏好，把记忆变成可靠行动。  
**赛道**：Track 03 Reasoning Architecture  
**问题**：一人多 agent 时交接丢上下文、偏好与失败路径丢失、告警分散。  
**方案**：单 agent=入口+自调度；协作在上层；G1 宪法；Meterless H-MEM 做记忆脊梁；Zetaris 做可查询数据层；HubCards/Telegram 送达。  
**Demo / 仓 / 幻灯**：见占位符；仓默认 `open-agent-2026`。  
**赞助商**：今晚按 `SPONSOR-PLAN.md` 最小双接入；**禁止空口声称已集成**。  
**预存代码**：提交表如实 declare。
