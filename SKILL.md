---
name: research-grant-proposal
description: Generate Chinese-language academic nursing grant proposals based on verified literature from CNKI, PubMed, and Wanfang. Use when the user asks for proposal writing, literature-backed sections, technical routes, or reference lists.
---

# Research Grant Proposal Generator

## Hard Rules (MUST FOLLOW)

1. Run databases in sequence only: **CNKI → PubMed → Wanfang**.
2. Keep **one browser tab only** during the full run.
3. Do not run database research in parallel.
4. Keep the same `targetId` across browser actions to prevent context drift.
5. Treat page operability by actionable refs, not by visual overlays.
6. Do not open article links via normal click if they may spawn a new tab; prefer `navigate` with the extracted URL in the same tab.
7. If a new tab opens accidentally, immediately close it and continue in the original `targetId`.

## Minimum Literature Requirements

- CNKI: 5-7 verified papers
- PubMed: 5-7 verified papers
- Wanfang: 5-7 verified papers
- Total: 15-21 verified references

## Workflow

### Step 1: Database Research (MANDATORY ORDER)

Read and execute each file in order:

1. `verification_steps/cnki.md` → produce `cnki_results.md`
2. `verification_steps/pubmed.md` → produce `pubmed_results.md`
3. `verification_steps/wanfang.md` → produce `wanfang_results.md`

**Abstract-level verification is mandatory for every selected paper.**
- For each selected paper, capture:
  - `Abstract key points` (1-3 bullets)
  - `Relevance to topic` (one sentence)
- If no abstract is accessible, mark as `NOT VERIFIED` and replace it.

### Step 2: Aggregate (MANDATORY GATE)

Read all three result files and produce `research_notes.md` using `research_notes_template.md`.

**Do not draft the proposal before all three result files exist and pass minimum counts.**

### Step 3: Draft Proposal (ONLY AFTER GATE PASSES)

Generate final proposal sections using only verified references:

1. Main research content and objectives
2. Rationale (purpose, significance, domestic/international landscape, trend)
3. R&D content and expected outputs
4. Methods and technical route (with process diagram)
5. Core references in the last 5 years

**In-text citation mapping is mandatory in proposal body.**
- Key claims must include bracket citations like `[1]`, `[3,7]`.
- Reference list numbering must map one-to-one with in-text citations.

## Verification Checklist

- `cnki_results.md` exists with 5+ verified papers
- `pubmed_results.md` exists with 5+ verified papers
- `wanfang_results.md` exists with 5+ verified papers
- Each database has 5+ papers with `ABSTRACT✓` and written abstract key points
- `research_notes.md` merges all sources and includes evidence-to-claim mapping
- Final references count is 15+
- Proposal body includes in-text bracket citations mapped to final reference list

## Output

- Markdown draft in current session
- Optional DOCX export via `scripts/generate_proposal.py`
