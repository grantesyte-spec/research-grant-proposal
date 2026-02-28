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

> **⚠️ 重要原则：控制信息量，避免上下文膨胀**
> 
> 浏览器快照返回整个页面DOM，信息量巨大会稀释注意力。遵循以下规则：

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
7. **精确提取，避免全量快照**：
   - 使用 `snapshot --compact` 获取简化版本（推荐首选）
   - 使用 `grep` 过滤关键内容：`snapshot --compact | grep -E "摘要：|核心|北大"`
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
   openclaw browser snapshot --compact | grep -A 5 "摘要"
   ```
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

### 2) Click "中文" Filter (重要步骤)

搜索页面加载后，**必须先点击"中文"筛选**，否则默认显示中英文混合结果：

```bash
# 方法1：使用JavaScript点击中文筛选按钮（推荐）
openclaw browser act --kind evaluate --fn "document.querySelector('.switch-ChEn .ch').click()"

# 方法2：尝试通过URL参数切换
openclaw browser navigate "https://kns.cnki.net/kns8s/search?param0=Chinese"
```

**为什么必须点击中文：**
- 默认"总库"包含中英文文献
- 核心期刊筛选选项只在选中"中文"后才出现
- 不点击中文会漏掉大量中文核心期刊

**验证是否成功切换到中文：**
```bash
openclaw browser snapshot --compact | grep -E "来源类别|北大|CSCD|WJCI|核心"
```
如果看到"来源类别"下有"北大核心"、"CSCD"、"WJCI"等选项，说明切换成功。

### 3) Select Core Journal Filter (核心期刊筛选)

点击"中文"后，在搜索结果页面左侧会出现"来源类别"筛选选项：

```bash
# 查看来源类别筛选选项
openclaw browser snapshot --compact | grep -E "来源类别|北大|CSCD|WJCI|核心" -A 5

# 常见核心期刊选项：
# - 北大核心 (checkbox "北大核心")
# - CSCD (checkbox "CSCD")  
# - WJCI (checkbox "WJCI")
# - 科技核心
```

**勾选核心期刊：**
```bash
# 点击北大核心复选框（通常是 checkbox "北大核心"）
openclaw browser click <checkbox_ref>

# 示例：点击编号为e46的复选框
openclaw browser click e46

# 等待结果更新
sleep 5
openclaw browser snapshot --compact
```

### 4) Run Queries (Chinese only)

使用 issue_keywords.md 中的关键词矩阵，按优先级顺序检索：

```bash
# 输入关键词并搜索
openclaw browser type <search_field_ref> "[关键词]" --submit

# 等待搜索结果加载
sleep 5
openclaw browser snapshot --compact
```

### 5) Select and Verify Papers (基于摘要验证)

**⚠️ 关键要求：每篇文献必须打开详情页阅读摘要，不能仅凭标题判断！**

选择5-7篇相关文献并验证：
- 主题相关性
- 作者
- **年份（必须在近5年内）**
- **摘要相关性（必须阅读摘要，而非仅标题）**
- URL有效性
- 中文语言
- 核心期刊标签（WJCI/北大核心/科技核心/CSCD/CSSCI）

对于每篇选中的文献，**必须执行以下步骤**：

1. **打开详情页**（不能跳过）：
   ```bash
   openclaw browser navigate <article_url>
   openclaw browser snapshot --format aria
   ```

2. **读取摘要内容**：从页面快照中找到"摘要："部分，记录实际内容

3. **提取摘要要点**（1-3条）：从摘要中提炼，不是从标题推断

4. **撰写相关性一句**：基于摘要内容撰写，不是基于标题猜测

**验证检查清单（每篇文献）：**
- [ ] 打开了详情页
- [ ] 找到了摘要内容
- [ ] 摘要要点来自原文（不是猜的）
- [ ] 核心期刊标签已确认
- [ ] 年份在近5年内

> **重要教训（2026-02-28）**：有输出 ≠ 正确完成。写出了cnki_results.md不代表验证做好了——必须确保每篇文献的摘要要点都来自详情页的真实内容。

### 6) Create `cnki_results.md`

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
