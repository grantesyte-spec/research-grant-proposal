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

## Verification Checklist

- `cnki_results.md` exists with 5+ verified papers
- `pubmed_results.md` exists with 5+ verified papers
- `wanfang_results.md` exists with 5+ verified papers
- `research_notes.md` merges all sources
- Final references count is 15+

## Output

- Markdown draft in current session
- Optional DOCX export via `scripts/generate_proposal.py`
