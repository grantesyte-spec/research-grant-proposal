# CNKI Research Script

Purpose: research Chinese literature on CNKI and generate `cnki_results.md`.

## Browser Rules

1. Use a single tab only.
2. Use `navigate` to change pages, do not open extra tabs.
3. Keep one `targetId` for all actions.
4. If visual captcha text appears, check if core controls are still operable before stopping.
5. Trust actionable refs from snapshot (for example: topic field + search button), not page warnings.
6. If uncertain about current page state, run `snapshot` first, then decide the next action.
7. Prefer `type ... --submit` over a separate click on search when available.
8. For article detail pages, prefer `navigate` using the article URL instead of clicking title links that may open a new tab.
9. If a new tab appears, close it immediately and continue with the original `targetId`.

## Steps

### 1) Open CNKI Advanced Search

- URL: `http://118.25.64.223:8081/kns8s/defaultresult/index`
- Take snapshot and identify:
  - topic field ref
  - search button ref

### 2) Run Queries

Suggested queries:
- `Orem self-care nursing`
- `transtheoretical model nursing`
- `femoral neck fracture diabetes nursing`
- `hip fracture diabetes rehabilitation nursing`

For each query:
- input query
- click search
- snapshot results
- record result count if visible

### 3) Select and Verify Papers

Select 5-7 relevant papers and verify each item:
- Topic relevance
- Authors
- Year
- Abstract relevance (must read abstract text, not title-only)
- Verifiable URL

For each selected paper, record mandatory fields:
- `Abstract key points` (1-3 bullets)
- `Relevance to topic` (one sentence)

If abstract is unavailable/inaccessible, mark `NOT VERIFIED` and replace with another paper.

### 4) Create `cnki_results.md`

After CNKI is complete, continue to PubMed. Do not draft proposal at this stage.

Required structure:

```markdown
# CNKI Research Results

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
