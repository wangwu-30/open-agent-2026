// HubCrew handoff notebook, adapted from Meterless agentathon-starter.
// Commands call the official H-MEM reference; state belongs to the engine.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { loadHMEM } from "./src/engine.ts";
import { answer } from "./src/llm.ts";
import type { HMEM, MemoryRecord } from "./vendor/hmem/src/index.ts";

const here = path.dirname(fileURLToPath(import.meta.url));
const HANDOFF_QUESTION = "当前仍生效的部署决策";
// The reference tokenizer is ASCII-only. This is one disclosed demo alias,
// not a translation model. All other questions go to the engine unchanged.
const DEPLOY_QUERY = "current live deployment decision deploy";
const THRESHOLD = 0.1; // The upstream notebook's demo threshold (engine default: 0.35).

async function remember(hmem: HMEM, text: string, seedRef?: string): Promise<MemoryRecord[]> {
  const mined = await hmem.mine("chat_message", text);
  const records = mined.length ? mined : [hmem.add({
    content: text, type: "general", source: "notebook:manual",
  })];
  for (const record of records) {
    const kind = record.content.match(/^\[(unfinished_work|failed_path|live_decision)\]/)?.[1];
    if (kind || seedRef) {
      // Handoff categories are application tags, not invented H-MEM types.
      // Metadata updates go through Store and are recorded by TrustLedger.
      hmem.store.update(record.id, {
        tags: [...record.tags, ...(kind ? [`handoff:${kind}`] : []), ...(seedRef ? ["demo:hubcrew"] : [])],
        provenance: seedRef ? {
          ...record.provenance,
          label: `HubCrew demo seed: ${kind ?? "general"}`,
          refs: [seedRef],
        } : record.provenance,
      });
    }
    console.log(`remembered ${record.id} via ${mined.length ? "Mining -> Store" : "Store (direct capture)"} [${record.layer}]`);
    console.log(`  ${record.content}`);
    console.log(`  tags: ${record.tags.join(", ")}`);
  }
  return records;
}

async function main(): Promise<void> {
  const [command, ...rest] = process.argv.slice(2);
  const arg = rest.filter((a) => !a.startsWith("--")).join(" ").trim();
  if (!command || command === "--help" || command === "help") return usage();
  const { HMEM, source } = await loadHMEM();
  const persistDir = path.resolve(process.env.HMEM_NOTEBOOK_DIR ?? path.join(here, ".notebook"));
  console.log(`engine source: ${source} | state: ${persistDir}`);
  const hmem = new HMEM({ persistDir, actor: "hubcrew:notebook" });

  switch (command) {
    case "remember": {
      if (!arg) throw new Error('Usage: notebook remember "<fact>"');
      await remember(hmem, arg);
      break;
    }
    case "ask": {
      if (!arg) throw new Error('Usage: notebook ask "<question>"');
      const query = arg === HANDOFF_QUESTION ? DEPLOY_QUERY : arg;
      console.log(`question: ${arg}`);
      console.log(`retrieval query: ${query}${query !== arg ? " (explicit demo alias; ASCII tokenizer)" : ""}`);
      const result = hmem.query(query, { threshold: THRESHOLD });
      hmem.store.persist(); // Persist the engine's access counters as well as its read ledger.
      console.log(`mode: retrieval-only | threshold: ${THRESHOLD} | strategy: ${result.trace.strategy}`);
      console.log(`trace: ${result.trace.retrievalReason}`);
      console.log(answer(arg, result.memories));
      for (const { memory } of result.memories) {
        // These are fields on the actual retrieved record, not seed lookups.
        console.log(`provenance ${memory.id}: ${JSON.stringify({
          source: memory.source,
          ...memory.provenance,
          tags: memory.tags,
          supersedes: memory.supersedes,
          supersededBy: memory.supersededBy,
          derivedFrom: memory.derivedFrom,
        })}`);
      }
      if (result.memories.length) {
        console.log(`audit a returned id: npx tsx notebook.ts audit ${result.memories[0].memory.id}`);
      }
      break;
    }
    case "audit": {
      if (!arg) throw new Error("Usage: notebook audit <memory-id>");
      const history = hmem.ledger.history(arg);
      if (history.length === 0) throw new Error(`No ledger entries for ${arg}`);
      console.log(`TrustLedger history: ${arg}`);
      for (const entry of history) {
        console.log(`- ${entry.memoryId} ${entry.action} by ${entry.actor} at ${new Date(entry.timestamp).toISOString()}`);
        if (entry.newState?.provenance) {
          console.log(`  source: ${entry.newState.source} | provenance: ${JSON.stringify(entry.newState.provenance)}`);
        }
        if (entry.details) console.log(`  details: ${JSON.stringify(entry.details)}`);
      }
      break;
    }
    case "sleep": {
      const preview = hmem.sleep.preview();
      console.log("sleep plan (nothing applied):");
      console.log(`  consolidate: ${preview.toConsolidate.length} | archive: ${preview.toArchive.length} | synthesize: ${preview.toSynthesize.length} groups`);
      if (!rest.includes("--preview")) {
        const report = hmem.sleep.execute(preview);
        console.log(`executed with in-process backup ${report.backupId} (not retained after CLI exit)`);
      }
      break;
    }
    case "seed": {
      const seedRef = "seed/handoff-session.txt";
      const lines = fs.readFileSync(path.join(here, seedRef), "utf-8").split("\n").map((l) => l.trim()).filter(Boolean);
      console.log("HubCrew demo handoff (illustrative facts, not production events):");
      for (const line of lines) {
        const existing = hmem.store.all().find((m) => m.content === line);
        if (existing) console.log(`already remembered ${existing.id}: ${existing.content}`);
        else await remember(hmem, line, seedRef);
      }
      console.log(`\nSeed process can exit now. Cold recall: npx tsx notebook.ts ask "${HANDOFF_QUESTION}"`);
      break;
    }
    default:
      throw new Error(`Unknown command: ${command}. Run notebook --help.`);
  }
}

function usage(): void {
  console.log(`HubCrew handoff notebook (official Meterless H-MEM reference)

  npx tsx notebook.ts seed                     remember three demo handoff categories
  npx tsx notebook.ts remember "<fact>"        mine a fact (or direct capture) into memory
  npx tsx notebook.ts ask "<question>"         retrieve context with memory IDs + provenance
  npx tsx notebook.ts audit <memory-id>        inspect append-only ledger history
  npx tsx notebook.ts sleep --preview         preview consolidation without applying it

State: .notebook/ next to notebook.ts; override with HMEM_NOTEBOOK_DIR.
Demo question: ${HANDOFF_QUESTION}`);
}

main().catch((err) => {
  console.error((err as Error).message);
  process.exitCode = 1;
});
