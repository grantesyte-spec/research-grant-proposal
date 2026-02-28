# PubMed Research Script

Purpose: research English literature on PubMed and generate `pubmed_results.md`.

## File Output Location
**IMPORTANT:** Write results to `workspace/research-projects/[课题名]/pubmed_results.md`
- See SKILL.md "File Storage Convention" section for directory structure
- Do NOT write to skill directory

## Prerequisite

**Step 0 must be completed first:**
- Ensure `issue_keywords.md` exists (generated from SKILL.md Step 0)
- Read the keyword matrix from `issue_keywords.md`

## Browser Rules (OpenClaw CLI)

> **⚠️ 重要原则：控制信息量，避免上下文膨胀**
> 
> 浏览器快照返回整个页面DOM，信息量巨大会稀释注意力。遵循以下规则：

1. Use a **single tab only** throughout the entire research process.
   - Do NOT open new tabs; use navigate to stay in the same tab.
   - If a new tab accidentally opens, close it immediately and focus back to the original tab.
2. Wait 10-15 seconds before taking snapshot after navigation.
   - This allows the page to fully load and stabilizes element refs.
   - Dynamic pages (like PubMed search results) need time to render.
3. Check `openclaw browser tabs` first if unsure about current tab state.
4. If visual overlays appear, continue if search controls remain operable.
5. Judge operability by snapshot refs.
6. If uncertain about current page state, run `openclaw browser snapshot` first, then decide the next action.
7. **精确提取，避免全量快照**：
   - 使用 `snapshot --compact` 获取简化版本（推荐首选）
   - 使用 `grep` 过滤关键内容：`snapshot --compact | grep -E "Abstract|PMID|202"`
   - 使用 `head -50` 限制行数，避免信息过载
8. **分步处理策略**：
   - 第一步：获取文章列表（简化版snapshot）
   - 第二步：选择目标文章后，逐个打开详情页
   - 不要试图从一次快照中提取所有信息
9. **提取摘要时的最佳实践**：
   ```bash
   # 先看简化版
   openclaw browser snapshot --compact | head -80
   
   # 精确定位摘要区域
   openclaw browser snapshot --compact | grep -A 10 "Abstract"
   ```
7. Prefer `openclaw browser type ... --submit` over a separate click on search when available.
8. For article detail pages, prefer `openclaw browser navigate` using the article URL instead of clicking title links that may open a new tab.
9. If a new tab appears, close it immediately with `openclaw browser tab close <id>` and continue with the original `targetId`.

## Step 0: 读取检索矩阵 (前置步骤)

**必须先执行此步骤：**

1. 读取 `issue_keywords.md` 文件
2. 提取 PubMed 检索用的关键词矩阵（英文）
3. 按优先级排序确定检索顺序

### 关键词来源

从 issue_keywords.md 中提取并翻译为英文：
- 理论基础英文关键词
- 护理理论英文关键词
- 研究对象英文关键词
- 交叉组合英文关键词

### 检索轮次设计

按照 issue_keywords.md 中的矩阵执行检索：

**第1轮 - 理论基础检索**
**第2轮 - 护理理论检索**
**第3轮 - 单一疾病检索**
**第4轮 - 疾病交叉检索**
**第5轮 - 综合检索**

---

### 1) Open PubMed

Use OpenClaw CLI to navigate:
```bash
openclaw browser navigate https://pubmed.ncbi.nlm.nih.gov/
```

### 2) Run Queries

**使用 issue_keywords.md 中的关键词矩阵，按优先级顺序检索：**

从 issue_keywords.md 中提取并翻译的关键词示例：
- `transtheoretical model nursing`
- `stages of change nursing`
- `health belief model nursing`
- `Orem self-care model nursing`
- `Orem self-care theory diabetes`
- `Orem self-care hip fracture`
- `femoral neck fracture diabetes nursing`
- `hip fracture diabetes rehabilitation`
- `elderly fracture diabetes nursing`

For each query, use OpenClaw CLI:
```bash
# Type query and submit
openclaw browser type <search_field_ref> "[关键词]" --submit

# Apply date filter (use RELATIVE time filter, e.g., "5 years" - do NOT hardcode specific years)
openclaw browser snapshot --compact
# Look for date filter options: typically a timeline slider or dropdown with "1 year", "5 years", "10 years"
# Select "5 years" filter - PubMed will calculate the relative date range automatically

# View results
openclaw browser snapshot --format aria
```

### 3) Select and Verify Papers

**⚠️ 关键要求：每篇文献必须打开详情页阅读摘要，不能仅凭标题判断！**

Select 5-7 papers and verify:
- Topic relevance
- Authors
- **Year (must be within last 5 years from current execution year - use RELATIVE check)**
- Abstract relevance (must read abstract text, not title-only)
- PMID and URL validity

For each selected paper, **must execute the following steps**:

1. **Open article detail page** (cannot skip):
   ```bash
   openclaw browser navigate https://pubmed.ncbi.nlm.nih.gov/<PMID>/
   openclaw browser snapshot --format aria
   ```

2. **Read abstract content**: Find "Abstract" section in the page snapshot

3. **Extract abstract key points** (1-3 bullets): From the actual abstract, not inferred from title

4. **Write relevance sentence**: Based on abstract content, not title guess

**Verification checklist (for each paper):**
- [ ] Opened detail page
- [ ] Found abstract content
- [ ] Abstract key points from原文 (not guessed)
- [ ] Year within last 5 years confirmed
- [ ] PMID/URL valid

If abstract is unavailable/inaccessible, mark `NOT VERIFIED` and replace with another paper.
If year requirement is not met, mark `NOT VERIFIED` and replace with another paper.

> **Important lesson (2026-02-28)**: Having output ≠ correctly completed. Writing pubmed_results.md doesn't mean verification is done — ensure every paper's abstract key points come from actual detail page content.

### 4) Create `pubmed_results.md`

After PubMed is complete, continue to Wanfang. Do not draft proposal at this stage.

Required structure:

```markdown
# PubMed Research Results

## Topic
[课题名称]

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
