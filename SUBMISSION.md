# SUBMISSION — 字段草稿归档 / Submitted

**Track 03 / HubCrew 已正式提交，核验时间为 2026-10-27 01:38 北京时间。** 当前状态以 [demo/SUBMISSION-STATUS.md](./demo/SUBMISSION-STATUS.md) 为准，最终英文文本见 [demo/submission-description.txt](./demo/submission-description.txt)。以下是原字段草稿与中文对照，已补齐实际材料入口，作为历史参考。

硬截止：**2026-10-28 07:45 北京时间**（UTC 2026-10-27 23:45）。

---

## English (archived field draft)

The architecture below includes intended end-to-end behavior. The submitted demo shows two working local sponsor bridges; automatic HubCards/H-MEM/Zetaris dispatch and alert delivery are not claimed as demonstrated. See the final Description linked above.

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
  - Submission repo: https://github.com/wangwu-30/open-agent-2026 (docs + sponsor bridges + demo script)
  - IM adapter layer: https://github.com/wangwu-30/imwire (public, MIT)
  - Team knowledge memory: https://github.com/wangwu-30/teamrecall (public, MIT)
- HubCards / home crew runtime: **declared as pre-existing product code**; the full runtime is not open-sourced in this submission. Demonstrated scope is recorded in the final Description.
- Dev: Cursor / Codex on Mac mini for bridges; no fake sponsor screenshots.

### Demo link
Submitted via direct platform upload: https://iframe.mediadelivery.net/embed/778121/17cbf265-3373-4da8-a126-0daaaebf0eca (3:10 / 1080p). Public backup and upload record: [demo/DEMO-URL.md](./demo/DEMO-URL.md).

### Slide deck link
https://github.com/wangwu-30/open-agent-2026/blob/main/HubCrew-Open-Agent-2026.pptx

### GitHub repository
https://github.com/wangwu-30/open-agent-2026
Related (declared in submission): https://github.com/wangwu-30/imwire · https://github.com/wangwu-30/teamrecall

### Sponsor tech — Zetaris
**Live (2026-10-26):** Docker Compose on Mac mini (`~/zetaris/zetaris-platform`); `./verify.sh` 9/9 PASS; UI http://localhost:3000. Read-only Lightning SQL via UI→API→driver verified (`SELECT 1`, `NY_TAXI.taxi_zones`, `TPCDS_DB.reason` → HubCrew P0–P2 handoff mapping). Evidence: `sponsors/zetaris/LIVE.md`, `sponsors/zetaris/query_home_ops.md` §3. Setup: https://zetaris.github.io/getting-started/

### Sponsor tech — Meterless
**Live:** Meterless **H-MEM** via `agentathon-starter` (`remember`/`ask`/`audit`/`sleep`) as handoff+constitution memory spine — `sponsors/hmem-notebook/` (fed9a1d). Starter: https://github.com/Meterless/Meterless/tree/main/templates/agentathon-starter
Nightshift: archived stretch idea; not claimed as implemented in this submission.

### Cursor / NVIDIA (archived notes)
- Cursor/Codex: used to implement sponsor bridges and docs on Mac mini (`taskq` jobs).
- NVIDIA/Nemotron: **no execution claimed** in the submitted Description.

### Pre-existing product code (declared)
HubCards (iOS entry), home multi-agent crew (班组), imwire, teamrecall, related home deployment (benefit). Hackathon delta: reasoning-architecture documentation, public submission repo, Meterless H-MEM bridge, Zetaris query path, demo + slides.

### Website
https://www.wangwu.ai

---

## 中文对照（归档参考）

**标题**：HubCrew：一人家用班组的命名 Agent 推理架构  
**一句话**：HubCards 单入口 + 命名 agent 交接（未完成/失败路径/仍生效决策）+ 宪法偏好，把记忆变成可靠行动。  
**赛道**：Track 03 Reasoning Architecture  
**问题**：一人多 agent 时交接丢上下文、偏好与失败路径丢失、告警分散。  
**方案**：单 agent=入口+自调度；协作在上层；G1 宪法；Meterless H-MEM 做记忆脊梁；Zetaris 做可查询数据层；HubCards/Telegram 送达。  
**Demo / 仓 / 幻灯**：已提交，实际链接见上文与提交状态记录。
**赞助商**：本地 H-MEM 桥与 Zetaris SQL 演示已交付，见 [SPONSOR-PLAN.md](./SPONSOR-PLAN.md)；样本优先级为人工映射，自动端到端送达仍为架构方向。
**预存代码**：已在提交表如实 declare。
