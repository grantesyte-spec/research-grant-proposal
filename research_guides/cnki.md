# CNKI Research Script

Purpose: research Chinese core-journal literature on CNKI and generate `cnki_results.md`.

## File Output Location
**IMPORTANT:** Write results to `workspace/research-projects/[课题名]/cnki_results.md`
- See SKILL.md "File Storage Convention" section for directory structure
- Do NOT write to skill directory

## Prerequisite

**Step 0 must be completed first:**
- Ensure `issue_keywords.md` exists (generated from SKILL.md Step 0)
- Read the keyword matrix from `issue_keywords.md`

## Browser Rules (OpenClaw CLI)

1. Use a **single tab only** throughout the entire research process.
   - Do NOT open new tabs; use navigate to stay in the same tab.
   - If a new tab accidentally opens, close it immediately and focus back to the original tab.
2. Wait 10-15 seconds before taking snapshot after navigation.
   - This allows the page to fully load and stabilizes element refs.
   - Dynamic pages (like CNKI search results) need time to render.
3. Check `openclaw browser tabs` first if unsure about current tab state.
4. If visual overlays appear (e.g., captcha, slider puzzle), continue if search controls remain operable.
   - CNKI may show verification UI but still allow searches for logged-in users.
   - If search results appear despite the verification prompt, the function is working.
   - Don't assume the page is broken just because a verification box is visible.
5. Judge operability by snapshot refs.
6. If uncertain about current page state, run `openclaw browser snapshot` first, then decide the next action.
7. Prefer `openclaw browser type ... --submit` over a separate click on search when available.
8. **For article detail pages: MUST use `openclaw browser navigate <article_url>` instead of clicking title links.**
   - Clicking title links often fails with timeout errors
   - Get the article URL from snapshot: look for `/url: https://kns.cnki.net/kcms2/article/abstract?...` in the title link element
9. If a new tab appears, close it immediately with `openclaw browser tab close <id>` and continue with the original `targetId`.
10. **Getting search box ref:** Use `openclaw browser snapshot --labels | grep textbox` to find the textbox ref (usually e8 or similar)
11. **Getting article URLs from search results:** Each title in search results has a URL. Extract URLs from snapshot looking for links with `/url: https://kns.cnki.net/kcms2/article/abstract?...`

## Step 0: 读取检索矩阵

1. 读取 `issue_keywords.md` 文件
2. 提取 CNKI 检索用的关键词矩阵
3. 按优先级排序确定检索顺序

---

### 1) Open CNKI

```bash
openclaw browser navigate https://kns.cnki.net/kns8s/search
```

### 2) Click "中文" Filter

搜索页面加载后，需要点击"中文"筛选中文文献：

```bash
# 先获取页面快照确认元素
openclaw browser snapshot --compact
# 找到"中文"选项（通常在页面左侧），点击选中
# 例如：checkbox "中文" 或 link "中文"
```

### 3) Run Queries (Chinese only)

使用 issue_keywords.md 中的关键词矩阵，按优先级顺序检索：

```bash
# 输入关键词并搜索
openclaw browser type <search_field_ref> "[关键词]" --submit

# 等待搜索结果加载
sleep 5
openclaw browser snapshot --compact
```

### 3) Select and Verify Papers (基于摘要验证)

选择5-7篇相关文献并验证：
- 主题相关性
- 作者
- **年份（必须在近5年内）**
- **摘要相关性（必须阅读摘要，而非仅标题）**
- URL有效性
- 中文语言
- 核心期刊标签（WJCI/北大核心/科技核心/CSCD/CSSCI）

对于每篇选中的文献，记录：
- `摘要要点`（1-3条）
- `与课题的相关性`（一句话）
- `核心期刊标签`

**导航到文献详情页：**
```bash
openclaw browser navigate <article_url>
openclaw browser snapshot --format aria
```

### 4) Create `cnki_results.md`

Required structure:

```markdown
# CNKI Research Results

## Topic
[课题名称]

## Search Keywords & Results
| Keyword | Results |
|---|---|

## Verified References
### #1 - VERIFIED ✓
Title: ...
Authors: ...
Journal: ...
Year: ...
URL: ...
Core journal label: ...
摘要要点:
- ...
- ...
与课题的相关性: ...
Status: TOPIC✓ AUTHORS✓ YEAR✓ ABSTRACT✓ URL✓ CHINESE✓ CORE✓
```
