# Wanfang Research Script

Purpose: research Chinese literature on Wanfang and generate `wanfang_results.md`.

## Browser Rules

1. Use a single tab only.
2. Keep one `targetId` across all actions.
3. Prefer `navigate` over opening new pages in new tabs.
4. If visual overlays appear, continue when search controls remain operable.
5. Judge page state by actionable refs from snapshot.
6. If uncertain about current page state, run `snapshot` first, then decide the next action.
7. Prefer `type ... --submit` over a separate click on search when available.

## Steps

### 1) Open Wanfang

- `https://www.wanfangdata.com.cn/`

### 2) Run Queries

Suggested queries:
- `Orem self-care nursing`
- `transtheoretical model nursing`
- `femoral neck fracture diabetes nursing`
- `hip fracture diabetes rehabilitation nursing`

For each query:
- enter query
- submit
- snapshot results

### 3) Select and Verify Papers

Select 5-7 papers and verify:
- Topic relevance
- Authors
- Year
- Abstract relevance (must read abstract text, not title-only)
- URL accessibility

For each selected paper, record mandatory fields:
- `Abstract key points` (1-3 bullets)
- `Relevance to topic` (one sentence)

If abstract is unavailable/inaccessible, mark `NOT VERIFIED` and replace with another paper.

### 4) Create `wanfang_results.md`

After Wanfang is complete, aggregate all three result files first. Do not draft proposal before aggregation.

Required structure:

```markdown
# Wanfang Research Results

## Topic
...

## Search Keywords & Results
| Keyword | Results |
|---|---|

## Selected References
| # | Title | Authors | Journal | Year | Relevance |

## Verified References
### #1 - VERIFIED ✓
Title: ...
Authors: ...
Journal: ...
Year: ...
URL: ...
Abstract key points:
- ...
- ...
Relevance to topic: ...
Status: TOPIC✓ AUTHORS✓ YEAR✓ ABSTRACT✓ URL✓
```
