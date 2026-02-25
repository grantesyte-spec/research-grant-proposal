# CNKI Research Script

Purpose: research **Chinese core-journal literature** on CNKI and generate `cnki_results.md`.

## Browser Rules (OpenClaw CLI)

1. Use a single tab only.
2. Use OpenClaw **browser CLI commands** (`openclaw browser ...`) for all browser actions.
3. Use `openclaw browser navigate` to change pages, do not open extra tabs.
4. If visual captcha text appears, check if core controls are still operable before stopping.
5. Trust actionable refs from snapshot (for example: topic field + search button), not page warnings.
6. If uncertain about current page state, run `openclaw browser snapshot` first, then decide the next action.
7. Prefer `openclaw browser type ... --submit` over a separate click on search when available.
8. For article detail pages, prefer `openclaw browser navigate` using the article URL instead of clicking title links that may open a new tab.
9. If a new tab appears, close it immediately with `openclaw browser tab close <id>` and continue in the original tab.
10. Always treat this CNKI URL as the canonical page to return to when redirected:
    `http://118.25.64.223:8081/kns8s/defaultresult/index`

## Steps

### 1) Open CNKI Advanced Search

Use OpenClaw CLI to navigate:
```bash
openclaw browser navigate http://118.25.64.223:8081/kns8s/defaultresult/index
```

Take snapshot and identify:
```bash
openclaw browser snapshot --format aria
```
- Find topic field ref (search input)
- Find search button ref

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

# Save current result-list URL for later return after download redirects
# (copy from browser address bar output/context)

# Apply filters (use RELATIVE time filter, e.g., "近5年" - do NOT hardcode specific years)
openclaw browser snapshot --format aria
# Look for filter options: 语种=中文, 来源类别=北大核心/CSCD/CSSCI, 发表时间=近5年
# CNKI typically has a date filter dropdown - select "近5年" (last 5 years)

# Check results count
openclaw browser snapshot --compact
```

### 3) Select and Verify Papers

**Important Workflow - Download & Analyze One by One:**

1. **Extract Links (DO NOT CLICK)** — From search results, extract each paper's download URL
   - Find the download URL in the result row (look for `id=` parameter)
   - **CRITICAL**: Must include both `id=` AND `&ddata=` parameters — the full URL must contain `&ddata=` at the end
   - Example: `http://a12.papermao.net/cdown?id=XXX&ddata=YYY|CJFQ|...`
   - Save these complete URLs to a file for later use

2. **Download One Paper** — Use the saved URL to download one paper at a time

3. **Analyze Before Next** — After download completes, extract and analyze the document content
   - Only then proceed to download the next paper

**Repeat**: Extract → Save URL → Download → Analyze → Next Paper

---

**Select 5-7 relevant papers and verify each item:**
- Topic relevance
- Authors
- **Year (must be within last 5 years from current execution year - use RELATIVE check)**
- **Downloaded document relevance** (must read document text, not title-only)
- Verifiable URL (complete URL with `&ddata=` parameter)
- Chinese-language check
- Core-journal label check (capture visible label text)

For each selected paper, record mandatory fields:
- `Document key points` (1-3 bullets)
- `Relevance to topic` (one sentence)
- `Core journal label` (for example: 北大核心 / 科技核心 / CSCD / CSSCI)

**Download and verify documents using saved URLs:**
```bash
# Navigate directly to the saved download URL (includes &ddata= parameter)
openclaw browser navigate <SAVED_DOWNLOAD_URL>

# Wait for download to complete in browser
# Check local Downloads folder for new files
ls -la ~/Downloads/

# Extract document content using pdfplumber or similar tool
# Analyze and record key points

# Return to CNKI search results for next paper
openclaw browser navigate http://118.25.64.223:8081/kns8s/defaultresult/index
```

**Key Point**: The download URL MUST contain `&ddata=` parameter. Without it, the download will fail.

Do NOT use `https://navi.cnki.net/` as a generic return page for this workflow.

If document text is unavailable/inaccessible, mark `NOT VERIFIED` and replace with another paper.
If Chinese-language, core-journal, or year requirements are not met, mark `NOT VERIFIED` and replace with another paper.

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
