# CNKI Research Script

Purpose: research **Chinese core-journal literature** on CNKI and generate `cnki_results.md`.

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

### 2) Run Queries (Chinese only)

Suggested queries:
- `Orem 自理模式 护理`
- `动机行为转化 理论 护理`
- `股骨颈骨折 合并 糖尿病 护理`
- `股骨颈骨折 糖尿病 围手术期 护理`

For each query:
- input query
- click search
- apply filters when available:
  - 语种：中文
  - 来源类别/期刊级别：北大核心、科技核心、CSCD、CSSCI（或平台显示的等效核心标签）
- snapshot results
- record result count if visible

### 3) Select and Verify Papers

Select 5-7 relevant papers and verify each item:
- Topic relevance
- Authors
- Year
- **Downloaded document relevance** (must read document text, not title-only)
- Verifiable URL
- Chinese-language check
- Core-journal label check (capture visible label text)

For each selected paper, record mandatory fields:
- `Document key points` (1-3 bullets)
- `Relevance to topic` (one sentence)
- `Core journal label` (for example: 北大核心 / 科技核心 / CSCD / CSSCI)

Operational requirement:
- CNKI entries may jump to `a12.papermao` download gateway.
- Trigger download and wait **10-15 seconds** before concluding success/failure.
- If the first link fails, try provided alternate download links on the same page.

If document text is unavailable/inaccessible, mark `NOT VERIFIED` and replace with another paper.
If Chinese-language or core-journal requirements are not met, mark `NOT VERIFIED` and replace with another paper.

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
Core journal label: ...
Document key points:
- ...
- ...
Relevance to topic: ...
Status: TOPIC✓ AUTHORS✓ YEAR✓ DOC✓ URL✓ CHINESE✓ CORE✓
```
