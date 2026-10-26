# SPONSOR-PLAN — 今晚最小双接入（冲 Sponsor tech 10）

规则硬约束（活动页 §05）：**Every submission must integrate Zetaris and Meterless.**  
§06 demo/slides/说明都要讲清二者如何用。  
**本 bot 不写产品代码**；下列全部交给 **Mac mini Codex / taskq**。

## 优先级

| P | 项 | 估时 | 冠军必要？ |
|---|---|---|---|
| P0 | Meterless H-MEM via agentathon-starter，接到「交接/决策」记忆脊梁 | 1–2h | **是** |
| P0 | 公开仓 `wangwu-30/open-agent-2026` 放桥接+README+本目录文档 | 0.5h | **是** |
| P1 | Zetaris 实例 + 只读 SQL + agent 决策前查询 1 次 | 2–4h（含装机/账号） | **是（规则）** |
| P2 | Nightshift / Nemotron | 不排今晚 | 否（加分项） |
| P2 | 深接 HubCards 原生 SDK | 不排今晚 | 否（录屏证明即可） |

---

## Task A — Meterless H-MEM（默认选这条，最快可演示）

**目标**：班组交接包与关键决策写入 H-MEM；点名后 `ask` 带 provenance 召回；demo 能跑 `remember/ask/audit`。

**官方起点**：
```bash
npx degit meterless/meterless/templates/agentathon-starter hubcrew-hmem
cd hubcrew-hmem
npm install
npm run setup   # 必做：vendor H-MEM
npx tsx notebook.ts seed
npx tsx notebook.ts ask "what did we decide about storage"
```
模板：https://github.com/Meterless/Meterless/tree/main/templates/agentathon-starter  
引擎说明：`engines/hmem/AGENTS.md`

### 交给 Mac mini Codex/taskq 的任务说明（可原样粘贴）

```
【taskq】Open Agent 2026 · Meterless H-MEM bridge（勿改 HubCards / 班组主仓大范围重构）

目标：在 ~/src/open-agent-2026（或佳恒指定目录）落地可演示的 H-MEM 记忆脊梁，服务 Track03 HubCrew 叙事。

步骤：
1) degit meterless/meterless/templates/agentathon-starter 到仓库子目录 sponsors/hmem-notebook
2) npm install && npm run setup（确保 vendor/ 存在；README 写明 engine source）
3) 增加 scripts/handoff_seed.ts（或扩展 notebook.ts）：
   - remember 至少 3 条结构化记忆：unfinished_work / failed_path / live_decision（可用中英短句）
   - ask 查询「当前仍生效的部署决策」并打印 memory id + provenance
   - audit 一条 id
   - sleep --preview（可选，入镜加分）
4) README 用表格映射：命令 → H-MEM service（Mining/Store/Retrieval/TrustLedger/Sleep）——评委找这个
5) 不要提交 .notebook/、vendor/、密钥；setup 步骤写进 README
6) 验收：冷启动后仍能 ask 到 seed 记忆；终端输出可录屏

禁止：伪造 retrieval；把普通 JSON 文件说成 H-MEM；改 imwire/teamrecall 主线 API 除非必要。
```

**验收**：录屏段 1:20–2:00 可直接用。

---

## Task B — Zetaris（规则必接；可能成 blocker）

**目标**：任意 Zetaris 实例（本机或 AWS）上跑通只读 SQL；在推理前用查询结果影响「告警优先级 / 交接顺序」之一。

**官方起点**：https://zetaris.github.io/getting-started/  
辅助仓：https://github.com/zetaris/getting-started  
凭证只放 `.env.local`。

### 交给 Mac mini Codex/taskq 的任务说明

```
【taskq】Open Agent 2026 · Zetaris read-path（最小）

前提：佳恒已在 Zetaris Cloud 选好 Local 或 Managed AWS，并完成登录。若尚未装实例——先停，列出安装 blocker，不要瞎编连接成功。

步骤：
1) clone zetaris/getting-started；按 docs/connections/client-setup.md 配 .env.local
2) python3 scripts/preflight.py --jdbc（或文档推荐检查）；分开报告 JDBC / REST
3) 只读：SELECT 1；SHOW LIGHTNING DATABASES；对 NY_TAXI 或 TPCDS_DB 做 SELECT … LIMIT 5
4) 在 open-agent-2026/sponsors/zetaris/ 写 query_home_ops.md：记录所用 SQL、结果摘要、如何影响 HubCrew 决策（例：错误率/积压阈值 → 提高告警优先级）
5) 可选：一个 30 行 Python/TS 包装，把查询 JSON 打成 agent 可读 brief（无密钥入库）
6) README 写清：实例类型（local/AWS）、演示用表、与 Track03 data 平面的关系

禁止：提交密码/API key；宣称「联邦了生产家用库」若只用 sample；跳过 preflight 假装成功。
```

**若今晚装实例来不及**：仍须在提交说明写 **诚实状态** + 剩余步骤；同时 **优先抢出 Meterless**，并尽量用 Zetaris sample 的最短路径（文档称可用 supplied samples 做项目）。**空提交双赞助 = 违规风险 + Sponsor 0。**

---

## Task C — 公开仓路径（默认 C，最快可交）

```
【taskq】创建并推送 public 仓 wangwu-30/open-agent-2026

内容：
- README.md：项目一句话、Track03、架构图链接、demo 链接占位、赞助商用法、预存代码 declare
- docs/ 放入本目录已写的 DECISION/ARCHITECTURE/DEMO-SCRIPT/SUBMISSION 精简版
- sponsors/hmem-notebook（Task A）
- sponsors/zetaris/（Task B 产物）
- 链到 https://github.com/wangwu-30/imwire 与 teamrecall
LICENSE: MIT

验收：匿名浏览器可打开；README 从零到跑通 H-MEM ≤ 5 分钟。
```

### 路径对比（已评估）

| 路径 | 内容 | 速度 | 风险 |
|---|---|---|---|
| **C（默认）** | 新建 `open-agent-2026` 文档+桥 | 最快 | 需声明主运行时未全开源 |
| A | HubCards/班组仓改 public 或镜像 | 中 | 私货/密钥清理成本 |
| B | 只交 imwire + 录屏 | 快 | 叙事偏 IM，Track03 记忆/数据层弱 |

**推荐：C + 链 imwire/teamrecall + 录屏证 HubCards。**

---

## 非目标

- 本 bot / 云端 agent **不**直接改佳恒产品仓。
- 不接 Wildcard 专轨（见 DECISION）。
- Nightshift：仅当 Task A/B/C 完成后有余力再开。
