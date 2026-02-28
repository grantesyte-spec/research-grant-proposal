# Wanfang Research Script

Purpose: research **Chinese core-journal literature** on Wanfang and generate `wanfang_results.md`.

## File Output Location
**IMPORTANT:** Write results to `workspace/research-projects/[课题名]/wanfang_results.md`
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

1. Use a single tab only.
2. Keep one `targetId` across all actions.
3. Prefer `openclaw browser navigate` over opening new pages in new tabs.
4. If visual overlays appear, continue when search controls remain operable.
5. Judge page state by actionable refs from snapshot.
6. If uncertain about current page state, run `openclaw browser snapshot` first, then decide the next action.
7. **精确提取，避免全量快照**：
   - 使用 `snapshot --compact` 获取简化版本（推荐首选）
   - 使用 `grep` 过滤关键内容：`snapshot --compact | grep -E "摘要：|核心|Wanfang"`
   - 使用 `head -50` 限制行数，避免信息过载
8. **分步处理策略**：
   - 第一步：获取文章列表（简化版snapshot）
   - 第二步：选择目标文章后，逐个打开详情页
   - 不要试图从一次快照中提取所有信息
9. **Wanfang网站特殊注意事项**：
   - Wanfang网站加载慢，页面状态不稳定
   - 每次操作后都要运行snapshot检查当前页面状态
   - 遇到"Element not found"错误时，立即刷新页面并重新获取元素引用
   - 适当增加等待时间，因为Wanfang使用AJAX加载
10. Prefer `openclaw browser type ... --submit` over a separate click on search when available.
11. **For Wanfang, analyze abstracts directly from the search results page to select relevant papers.**
    - Search results on Wanfang typically display abstract content in the snippet.
    - **NO need to click into individual article pages to read full abstracts.**
    - Use the visible abstract summary from search results for verification.
    - This avoids page navigation issues and speeds up the verification process.
12. For article detail pages, prefer `openclaw browser navigate` using the article URL instead of clicking title links that may open a new tab.
13. If a new tab appears, close it immediately with `openclaw browser tab close <id>` and continue with the original `targetId`.
14. **提取摘要时的最佳实践**：
    ```bash
    # 先看简化版
    openclaw browser snapshot --compact | head -80
    
    # 精确定位摘要区域
    openclaw browser snapshot --compact | grep -A 5 "摘要"
    ```

## Step 0: 读取检索矩阵 (前置步骤)

**必须先执行此步骤：**

1. 读取 `issue_keywords.md` 文件
2. 提取 Wanfang 检索用的关键词矩阵（中文）
3. 按优先级排序确定检索顺序

### 关键词来源

从 issue_keywords.md 中提取中文关键词：
- 理论基础关键词
- 护理理论关键词
- 研究对象关键词
- 交叉组合关键词

### 检索轮次设计

按照 issue_keywords.md 中的矩阵执行检索：

**第1轮 - 理论基础检索（如TTM、健康信念模式等）**
**第2轮 - 护理理论检索（如Orem自理模式）**
**第3轮 - 单一疾病检索（如骨折、糖尿病）**
**第4轮 - 疾病交叉检索（如骨折+糖尿病）**
**第5轮 - 综合检索（如Orem+糖尿病+护理）**

---

### 1) Open Wanfang

Use OpenClaw CLI to navigate:
```bash
openclaw browser navigate https://www.wanfangdata.com.cn/
```

### 2) Run Queries (Chinese only)

**使用 issue_keywords.md 中的关键词矩阵，按优先级顺序检索：**

从 issue_keywords.md 中提取的关键词示例：
- `动机行为转化理论 护理`
- `跨理论模型 护理`
- `Orem 自理模式 护理`
- `Orem 糖尿病 护理`
- `Orem 骨折 护理`
- `股骨颈骨折 糖尿病 护理`
- `髋部骨折 糖尿病 护理`
- `老年骨折 糖尿病 护理`

For each query, use OpenClaw CLI:
```bash
# Type query and submit
openclaw browser type <search_field_ref> "[关键词]" --submit

# Apply filters (use RELATIVE time filter, e.g., "近5年" - do NOT hardcode specific years)
openclaw browser snapshot --format aria
# Look for filter options: 语种=中文, 文献类型=期刊, 期刊级别=WJCI/北大核心/CSCD/CSSCI, 发表时间=近5年
# Wanfang typically has a date filter dropdown - select "近5年" (last 5 years)

# Check results
openclaw browser snapshot --compact
```

### 3) Select and Verify Papers

**⚠️ 关键要求：必须从搜索结果页面读取摘要内容，不能仅凭标题判断！**

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

For each selected paper, **must execute the following steps**:

1. **Read abstract from search results** (cannot skip):
   - Use `--compact` snapshot to view results with abstracts
   - Find "摘要：" section in the snapshot
   - Extract abstract key points from visible content

2. **Extract abstract key points** (1-3 bullets): From visible abstract, not inferred from title

3. **Confirm core journal label**: Must see label text (WJCI/北大核心/科技核心/CSCD/CSSCI)

4. **Write relevance sentence**: Based on abstract content, not title guess

**Verification checklist (for each paper):**
- [ ] Found abstract content in search results
- [ ] Abstract key points from visible content (not guessed)
- [ ] Core journal label confirmed
- [ ] Year within last 5 years confirmed
- [ ] Chinese language confirmed

If the visible abstract from search results is insufficient to determine relevance, then navigate to the article page:
```bash
openclaw browser navigate https://www.wanfangdata.com.cn/details/detail.aspx?dbcode=CAPJ&dbname=CAPJLAST&filename=...

# Read abstract only if necessary
openclaw browser snapshot --compact
```

If abstract is unavailable/inaccessible, mark `NOT VERIFIED` and replace with another paper.
If Chinese-language, core-journal, or year requirements are not met, mark `NOT VERIFIED` and replace with another paper.

> **Important lesson (2026-02-28)**: Having output ≠ correctly completed. Writing wanfang_results.md doesn't mean verification is done — ensure every paper's abstract key points come from visible search results content.

### 4) Create `wanfang_results.md`

After Wanfang is complete, aggregate all three result files first. Do not draft proposal before aggregation.

Required structure:

```markdown
# Wanfang Research Results

## Topic
[课题名称]

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
