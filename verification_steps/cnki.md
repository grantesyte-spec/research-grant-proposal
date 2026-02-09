# CNKI Research Script

Purpose: research Chinese literature on CNKI and generate `cnki_results.md`.

## Browser Rules

1. Use a single tab only.
2. Use `navigate` to change pages, do not open extra tabs.
3. Keep one `targetId` for all actions.
4. If visual captcha text appears, check if core controls are still operable before stopping.
5. Trust actionable refs from snapshot (for example: topic field + search button), not page warnings.

## Steps

### 1) Open CNKI Advanced Search

- URL: `https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92&rlang=CHINESE`
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
- Abstract relevance
- Verifiable URL

### 4) Create `cnki_results.md`

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
Status: TOPIC✓ AUTHORS✓ YEAR✓ ABSTRACT✓ URL✓
```
