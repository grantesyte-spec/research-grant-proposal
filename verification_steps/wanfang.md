# Wanfang Research Script

Purpose: research **Chinese core-journal literature** on Wanfang and generate `wanfang_results.md`.

## Browser Rules (OpenClaw CLI)

1. Use a single tab only.
2. Keep one `targetId` across all actions.
3. Prefer `openclaw browser navigate` over opening new pages in new tabs.
4. If visual overlays appear, continue when search controls remain operable.
5. Judge page state by actionable refs from snapshot.
6. If uncertain about current page state, run `openclaw browser snapshot` first, then decide the next action.
7. Prefer `openclaw browser type ... --submit` over a separate click on search when available.
8. **Wanfang website is SLOW and has UNSTABLE page state.**
   - **After each action, ALWAYS run `snapshot` to check current page state before proceeding.**
   - **If you encounter "Element not found" errors, IMMEDIATELY refresh the page with `navigate` and re-obtain element references.**
   - **Increase wait time (sleep) appropriately, as Wanfang uses AJAX loading.**
9. **For Wanfang, analyze abstracts directly from the search results page to select relevant papers.**
   - Search results on Wanfang typically display abstract content in the snippet.
   - **NO need to click into individual article pages to read full abstracts.**
   - Use the visible abstract summary from search results for verification.
   - This avoids page navigation issues and speeds up the verification process.
10. For article detail pages, prefer `openclaw browser navigate` using the article URL instead of clicking title links that may open a new tab.
11. If a new tab appears, close it immediately with `openclaw browser tab close <id>` and continue with the original `targetId`.

## Steps

### 1) Open Wanfang

Use OpenClaw CLI to navigate:
```bash
openclaw browser navigate https://www.wanfangdata.com.cn/
```

### 2) Run Queries (Chinese only)

Suggested queries:
- `Orem 自理模式 护理`
- `动机行为转化 理论 护理`
- `股骨颈骨折 合并 糖尿病 护理`
- `股骨颈骨折 糖尿病 围手术期 护理`

For each query, use OpenClaw CLI:
```bash
# Type query and submit
openclaw browser type <search_field_ref> "Orem 自理模式 护理" --submit

# Apply filters (use RELATIVE time filter, e.g., "近5年" - do NOT hardcode specific years)
openclaw browser snapshot --format aria
# Look for filter options: 语种=中文, 文献类型=期刊, 期刊级别=北大核心/CSCD/CSSCI, 发表时间=近5年
# Wanfang typically has a date filter dropdown - select "近5年" (last 5 years)

# Check results
openclaw browser snapshot --compact
```

### 3) Select and Verify Papers

Select 5-7 papers and verify:
- Topic relevance
- Authors
- **Year (must be within last 5 years from current execution year - use RELATIVE check)**
- **Abstract relevance (read from search results page directly, NO need to click into article pages)**
  - Wanfang search results typically show the abstract in the snippet/摘要 section
  - Extract key points directly from the visible abstract summary
- URL accessibility
- Chinese-language check
- Core-journal label check (capture visible label text)

For each selected paper, record mandatory fields:
- `Abstract key points` (1-3 bullets - extract from search results snippet)
- `Relevance to topic` (one sentence)
- `Core journal label` (for example: 北大核心 / 科技核心 / CSCD / CSSCI)

**Example of extracting from search results:**
```bash
# After search, use --compact snapshot to view results with abstracts
openclaw browser snapshot --compact | grep -E "摘要：|CSTPCD|北大核心"

# Identify papers with visible abstracts and core journal labels
# Select the most relevant ones based on visible information
```

**Why analyze from search results:**
- Wanfang search results display 摘要 (abstract) directly in the snippet
- Avoids page navigation and element reference issues
- Significantly faster verification process
- Reduces the risk of "element not found" errors

If the visible abstract from search results is insufficient to determine relevance, then navigate to the article page:
```bash
openclaw browser navigate https://www.wanfangdata.com.cn/details/detail.aspx?dbcode=CAPJ&dbname=CAPJLAST&filename=...

# Read abstract only if necessary
openclaw browser snapshot --compact
```

If abstract is unavailable/inaccessible, mark `NOT VERIFIED` and replace with another paper.
If Chinese-language, core-journal, or year requirements are not met, mark `NOT VERIFIED` and replace with another paper.

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
