# CHECKLIST — 佳恒本人要点的（冲冠军）

时区：America/Los_Angeles；死线 **UTC 2026-10-27 23:45 = 北京 2026-10-28 07:45**。  
活动页：https://hackathon.genai.works/event/open-agent-hackathon-2026

## 今晚优先级（从上到下）

### P0 — 挡提交 / 挡冠军

| # | 动作 | 谁 | 状态 |
|---|---|---|---|
| 1 | 注册/登录 GenAI.Works，确认有 **Team**（个人也要 team 账号），选 **Track 03** | 佳恒 | ☐ |
| 2 | 确认黑客松平台 **Submission** 表单字段；对照 `SUBMISSION.md` 粘贴 | 佳恒 | ☐ |
| 3 | 建 public 仓 **`wangwu-30/open-agent-2026`**（路径 C）并推送 README | 佳恒点头 → Mac mini Codex | ☐ |
| 4 | **Meterless H-MEM** 按 `SPONSOR-PLAN` Task A 跑通并可录屏 | Mac mini Codex/taskq | ☐ |
| 5 | **Zetaris** 实例就绪 + 只读 SQL + 决策链说明（Task B） | 佳恒装实例 + Codex | ☐ |
| 6 | 录 **1–4 min** demo（`DEMO-SCRIPT.md`），上传得链 | 佳恒 | ☐ |
| 7 | 做 **slide deck**（提纲在 DEMO-SCRIPT），上传得链 | 佳恒 / 可派助手出初稿 | ☐ |
| 8 | 提交表填写赞助商说明；**declare 预存代码**；检查无密钥 | 佳恒 | ☐ |
| 9 | 在死线前点 Submit；保留确认页截图 | 佳恒 | ☐ |

### P1 — 抬分

| # | 动作 | 状态 |
|---|---|---|
| 10 | Demo 中 HubCards 真机告警成功回执 | ☐ |
| 11 | README 含 H-MEM 命令→service 映射表 | ☐ |
| 12 | 架构图导出 PNG 进幻灯 | ☐ |
| 13 | imwire / teamrecall 在提交说明中作为 related public code | ☐ |

### P2 — 有余力

| # | 动作 | 状态 |
|---|---|---|
| 14 | Nightshift 最小试跑（勿因此挤掉 P0） | ☐ |
| 15 | 路径 A：HubCards 脱敏 public 镜像 | ☐ |
| 16 | 中英双语幻灯 | ☐ |

---

## 官方 §06 对照（已从活动页规则 JSON 抽出）

必须有：
1. **Demo video 1–4 min**（主流程 + 如何解挑战 + 关键特性 + **Zetaris & Meterless 集成**）
2. **Slide deck**（问题与用户、方案、工作流/架构、技术栈、赞助商用法与 uniqueness、产品视觉、未来）
3. **GitHub**（源码 + README：setup/usage/deps；Colab 则给链接）
4. **文字说明**：Zetaris、Meterless、Cursor（若用）、NVIDIA（若用）如何贡献、有何独特

§05：Every submission **must** integrate Zetaris and Meterless；预存产品代码必须 declare。

---

## 公开仓实况（2026-10-26 核实）

**已确认 public（节选，与叙事相关）**：
- https://github.com/wangwu-30/imwire — IM 适配 / session（推荐作为入口层锚点）
- https://github.com/wangwu-30/teamrecall — git-native 知识记忆
- 另有 public：`3am`, `neo-market`, `agent-collab-goals`, `daily-skill`, `ai-digest-registry`, …（共 22 个 public；完整列表以 GitHub API 为准）

**未发现 public**：
- HubCards
- 家用班组完整运行时

→ **默认路径 C**：`wangwu-30/open-agent-2026`；用录屏证明 HubCards。  
→ 不要在材料里假装已有 HubCards public URL。

---

## Blockers（按可能性）

1. **Zetaris 实例未装 / 无 AWS Free Tier / 本机规格不够** → 冠军级合规风险。动作：今晚先走 getting-started「Run locally」或 AWS 清单；卡住就写进提交诚实说明并仍尽量出 sample 查询录屏。
2. **公开仓未建** → 用路径 C，30–60 分钟可解。
3. **HubCards 无法录屏** → 用 DEMO-SCRIPT 备用 B-roll + 静态 UI。
4. **Meterless `npm run setup` 失败** → 查 vendor/；按官方 README，setup 不可跳。
5. **把赞助商写成「后续可选」** → **冲冠军不允许**；规则要求必须集成。只能写「已集成最小路径」或「进行中+证据」，不能空口。

---

## 提交前 5 分钟自检

- [ ] Track = 03（不是 Wildcard）  
- [ ] 双赞助在 demo **和** slides **和** 文字说明里都出现  
- [ ] Repo 匿名可开  
- [ ] 预存代码已 declare  
- [ ] 无密钥、无私人聊天  
- [ ] 视频 ≤ 4:00  
- [ ] 死线时区没搞错（UTC 23:45）
