# PubMed Research Script

Purpose: research English literature on PubMed and generate `pubmed_results.md`.

## Browser Rules (OpenClaw CLI)

1. Use a single tab only.
2. Keep one `targetId` across all actions.
3. Use `openclaw browser navigate` for URL transitions.
4. If visual overlays appear, continue if search controls remain operable.
5. Judge operability by snapshot refs.
6. If uncertain about current page state, run `openclaw browser snapshot` first, then decide the next action.
7. Prefer `openclaw browser type ... --submit` over a separate click on search when available.
8. For article detail pages, prefer `openclaw browser navigate` using the article URL instead of clicking title links that may open a new tab.
9. If a new tab appears, close it immediately with `openclaw browser tab close <id>` and continue with the original `targetId`.

## Steps

### 1) Open PubMed

Use OpenClaw CLI to navigate:
```bash
openclaw browser navigate https://pubmed.ncbi.nlm.nih.gov/
```

### 2) Run Queries

Suggested queries:
- `transtheoretical model nursing diabetes`
- `Orem self-care nursing`
- `hip fracture diabetes rehabilitation`
- `femoral neck fracture diabetes nursing`

For each query, use OpenClaw CLI:
```bash
# Type query and submit
openclaw browser type <search_field_ref> "Orem self-care nursing" --submit

# View results
openclaw browser snapshot --format aria
```

### 3) Select and Verify Papers

Select 5-7 papers and verify:
- Topic relevance
- Authors
- Year
- Abstract relevance (must read abstract text, not title-only)
- PMID and URL validity

For each selected paper, record mandatory fields:
- `Abstract key points` (1-3 bullets)
- `Relevance to topic` (one sentence)

**Navigate to article detail pages using OpenClaw CLI:**
```bash
# Use article URL format
openclaw browser navigate https://pubmed.ncbi.nlm.nih.gov/<PMID>/

# Read abstract
openclaw browser snapshot --format aria
```

If abstract is unavailable/inaccessible, mark `NOT VERIFIED` and replace with another paper.

### 4) Create `pubmed_results.md`

After PubMed is complete, continue to Wanfang. Do not draft proposal at this stage.

Required structure:

```markdown
# PubMed Research Results

## Topic
...

## Search Keywords & Results
| Keyword | Results |
|---|---|

## Selected References
| # | Title | PMID | Authors | Journal | Year | Relevance |

## Verified References
### #1 - VERIFIED ✓
Title: ...
PMID: ...
Authors: ...
Journal: ...
Year: ...
URL: ...
Abstract key points:
- ...
- ...
Relevance to topic: ...
Status: TOPIC✓ AUTHORS✓ YEAR✓ ABSTRACT✓ PMID✓
```
