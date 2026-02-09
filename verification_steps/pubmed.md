# PubMed Research Script

Purpose: research English literature on PubMed and generate `pubmed_results.md`.

## Browser Rules

1. Use a single tab only.
2. Keep one `targetId` across all actions.
3. Use `navigate` for URL transitions.
4. If visual overlays appear, continue if search controls remain operable.
5. Judge operability by snapshot refs.
6. If uncertain about current page state, run `snapshot` first, then decide the next action.
7. Prefer `type ... --submit` over a separate click on search when available.

## Steps

### 1) Open PubMed

Start from:
- `https://pubmed.ncbi.nlm.nih.gov/`

### 2) Run Queries

Suggested queries:
- `transtheoretical model nursing diabetes`
- `Orem self-care nursing`
- `hip fracture diabetes rehabilitation`
- `femoral neck fracture diabetes nursing`

For each query:
- type into search box
- submit
- snapshot results

### 3) Select and Verify Papers

Select 5-7 papers and verify:
- Topic relevance
- Authors
- Year
- Abstract relevance
- PMID and URL validity

Use article URL format:
- `https://pubmed.ncbi.nlm.nih.gov/<PMID>/`

### 4) Create `pubmed_results.md`

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
Status: TOPIC✓ AUTHORS✓ YEAR✓ ABSTRACT✓ PMID✓
```
