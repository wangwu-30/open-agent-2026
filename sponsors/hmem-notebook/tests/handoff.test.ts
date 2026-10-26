import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import test, { type TestContext } from "node:test";

const root = fileURLToPath(new URL("../", import.meta.url));
const question = "当前仍生效的部署决策";

function cli(state: string, ...args: string[]): string {
  // Each call is a new process: no in-memory HMEM instance can carry over.
  const result = spawnSync(process.execPath, ["--import", "tsx", path.join(root, "notebook.ts"), ...args], {
    cwd: root,
    env: { ...process.env, HMEM_NOTEBOOK_DIR: state },
    encoding: "utf8",
    timeout: 30_000,
  });
  assert.equal(result.status, 0, result.error?.message ?? result.stderr);
  return result.stdout;
}

function temporaryState(t: TestContext): string {
  const state = fs.mkdtempSync(path.join(os.tmpdir(), "hubcrew-hmem-"));
  t.after(() => fs.rmSync(state, { recursive: true, force: true }));
  return state;
}

test("handoff survives process exit with real retrieval, provenance and ledger", (t) => {
  const state = temporaryState(t);
  const empty = cli(state, "ask", question);
  assert.match(empty, /Nothing in memory/);
  assert.doesNotMatch(empty, /provenance mem-/);

  // Consume an ID before seeding; neither retrieval nor audit may assume mem-3.
  cli(state, "remember", "We prefer tea during the evening.");
  const seed = cli(state, "seed");
  for (const kind of ["unfinished_work", "failed_path", "live_decision"]) {
    assert.match(seed, new RegExp(`handoff:${kind}`));
  }
  const liveId = seed.match(/remembered (mem-\d+) via Mining -> Store[^\n]*\n\s+\[live_decision\]/)?.[1];
  assert.ok(liveId, seed);
  assert.notEqual(liveId, "mem-3");

  const recalled = cli(state, "ask", question);
  assert.match(recalled, /engine source: vendor\/hmem/);
  assert.match(recalled, /retrieval query: current live deployment decision deploy \(explicit demo alias/);
  assert.match(recalled, /mode: retrieval-only/);
  assert.match(recalled, new RegExp(`- \\[${liveId}\\] \\[live_decision\\].*Mac mini`));
  assert.equal(recalled.match(/^- \[(mem-\d+)\]/m)?.[1], liveId, recalled);
  const provenanceLine = recalled.split("\n").find((line) => line.startsWith(`provenance ${liveId}: `));
  assert.ok(provenanceLine, recalled);
  const provenance = JSON.parse(provenanceLine.slice(`provenance ${liveId}: `.length));
  assert.equal(provenance.source, "interaction:chat_message");
  assert.equal(provenance.origin, "chat_message");
  assert.equal(provenance.label, "HubCrew demo seed: live_decision");
  assert.deepEqual(provenance.refs, ["seed/handoff-session.txt"]);
  assert.equal(typeof provenance.learnedAt, "number");

  const audit = cli(state, "audit", liveId);
  for (const action of ["create", "update", "read"]) {
    assert.ok(audit.includes(`${liveId} ${action} by hubcrew:notebook`), audit);
  }
  assert.match(audit, /"query":"current live deployment decision deploy"/);
  assert.ok(cli(state, "ask", "current live deployment decision deploy").includes(`[${liveId}] [live_decision]`));

  const secondSeed = cli(state, "seed");
  assert.equal((secondSeed.match(/already remembered /g) ?? []).length, 3);
  const before = ["state.json", "ledger.jsonl"].map((name) => fs.readFileSync(path.join(state, name), "utf8"));
  assert.match(cli(state, "sleep", "--preview"), /nothing applied/);
  assert.deepEqual(["state.json", "ledger.jsonl"].map((name) => fs.readFileSync(path.join(state, name), "utf8")), before);
});

test("ask can retrieve a different user-written decision without seeding", (t) => {
  const state = temporaryState(t);
  const fact = "[live_decision] We decided the current live deployment decision: deploy to a blue canary after a human signoff.";
  const saved = cli(state, "remember", fact);
  const id = saved.match(/remembered (mem-\d+)/)?.[1];
  assert.ok(id, saved);
  const recalled = cli(state, "ask", question);
  assert.ok(recalled.includes(`[${id}] ${fact}`), recalled);
  assert.doesNotMatch(recalled, /Mac mini|HubCrew demo seed|handoff-session/);
  assert.match(recalled, /"label":"mined from chat_message"/);
  assert.match(cli(state, "audit", id), /read by hubcrew:notebook/);
});
