# Wanfang Research Script

Purpose: research **Chinese core-journal literature** on Wanfang and generate `wanfang_results.md`.

## Browser Rules

1. Use a single tab only.
2. Keep one `targetId` across all actions.
3. Prefer `navigate` over opening new pages in new tabs.
4. If visual overlays appear, continue when search controls remain operable.
5. Judge page state by actionable refs from snapshot.
6. If uncertain about current page state, run `snapshot` first, then decide the next action.
7. Prefer `type ... --submit` over a separate click on search when available.
8. For article detail pages, prefer `navigate` using the article URL instead of clicking title links that may open a new tab.
9. If a new tab appears, close it immediately and continue with the original `targetId`.

## Steps

### 1) Open Wanfang

- `https://www.wanfangdata.com.cn/`

### 2) Run Queries (Chinese only)

Suggested queries:
- `Orem 自理模式 护理`
- `动机行为转化 理论 护理`
- `股骨颈骨折 合并 糖尿病 护理`
- `股骨颈骨折 糖尿病 围手术期 护理`

For each query:
- enter query
- submit
- apply filters when available:
  - 语种：中文
  - 文献类型：期刊
  - 期刊级别/来源类别：北大核心、科技核心、CSCD、CSSCI（或平台显示的等效核心标签）
- snapshot results

### 3) Select and Verify Papers

Select 5-7 papers and verify:
- Topic relevance
- Authors
- Year
- Abstract relevance (must read abstract text, not title-only)
- URL accessibility
- Chinese-language check
- Core-journal label check (capture visible label text)

For each selected paper, record mandatory fields:
- `Abstract key points` (1-3 bullets)
- `Relevance to topic` (one sentence)
- `Core journal label` (for example: 北大核心 / 科技核心 / CSCD / CSSCI)

If abstract is unavailable/inaccessible, mark `NOT VERIFIED` and replace with another paper.
If Chinese-language or core-journal requirements are not met, mark `NOT VERIFIED` and replace with another paper.

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
Core journal label: ...
Abstract key points:
- ...
- ...
Relevance to topic: ...
Status: TOPIC✓ AUTHORS✓ YEAR✓ ABSTRACT✓ URL✓ CHINESE✓ CORE✓
```
