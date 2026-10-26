// Offline answer rendering. Every line comes from MemoryRetrievalService;
// no model, credentials, network calls, or fabricated answer fallback.
import type { RetrievedMemory } from "../vendor/hmem/src/types.ts";

export function answer(question: string, memories: RetrievedMemory[]): string {
  if (memories.length === 0) {
    return `Nothing in memory answers "${question}" yet. Teach me: notebook remember "<fact>"`;
  }
  return [
    `Retrieved context for "${question}":`,
    ...memories.map(({ memory, relevance }) =>
      `- [${memory.id}] ${memory.content} (relevance ${relevance.toFixed(4)})`),
  ].join("\n");
}
