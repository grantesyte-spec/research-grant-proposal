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
2. Wait 5 seconds before taking snapshot after navigation.
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
10. Prefer `openclaw browser type ... --submit` over a separate click on search when available.
11. **For article detail pages: MUST use `openclaw browser navigate <article_url>` instead of clicking title links.**
   - Clicking title links often fails with timeout errors
   - Get the article URL from snapshot: look for `/url: https://kns.cnki.net/kcms2/article/abstract?...` in the title link element
12. If a new tab appears, close it immediately with `openclaw browser tab close <id>` and continue with the original `targetId`.
13. **Getting search box ref:** Use `openclaw browser snapshot --labels | grep textbox` to find the textbox ref (usually e8 or similar)
14. **Getting article URLs from search results:** Each title in search results has a URL. Extract URLs from snapshot looking for links with `/url: https://kns.cnki.net/kcms2/article/abstract?...`

## Step 0: 读取检索矩阵

1. 读取 `issue_keywords.md` 文件
2. 提取 CNKI 检索用的关键词矩阵
3. 按优先级排序确定检索顺序

---

### 1) Open CNKI

```bash
openclaw browser navigate https://kns.cnki.net/kns8s/search
```

### 2) Run Queries - 先获取搜索框ref

**重要：每轮检索前先获取搜索框ref，确保ref有效**

```bash
# 获取搜索框ref
openclaw browser snapshot --compact | grep -E "textbox.*中文" | head -3
# 通常返回 ref=e8
```

使用 issue_keywords.md 中的关键词矩阵，按优先级顺序检索：

```bash
# 输入关键词并搜索
openclaw browser type <search_field_ref> "[关键词]" --submit
```

**核心流程循环：**
```
搜索 → 点击中文 → 检查来源类别
    ↓
有核心期刊选项 → 勾选并选文献
    ↓
暂无分组结果 → 立即换下一组关键词（不要纠结）
```

### 3) Click "中文" Filter + 检查结果 (重要步骤)

搜索页面加载后，**必须先点击"中文"筛选**，然后立即检查结果：

```bash
# 点击中文筛选
openclaw browser evaluate --fn "(el) => { const items = document.querySelectorAll('.ch'); for(let item of items) { if(item.textContent.includes('中')) { item.click(); break; } } }"
```

**为什么必须点击中文：**
- 默认"总库"包含中英文文献
- 核心期刊筛选选项只在选中"中文"后才出现
- 不点击中文会漏掉大量中文核心期刊

**立即检查来源类别状态：**
```bash
openclaw browser snapshot --compact | grep -E "来源类别" -A 3
```

**判断结果（二选一）：**
1. **如果有核心期刊选项**（如"北大核心"、"CSCD"、"WJCI"）→ 继续Step 4勾选核心期刊
2. **如果显示"暂无分组结果"** → 立即换下一组关键词，不要继续尝试

**验证是否成功切换到中文：**
只要看到"来源类别"这个筛选项（term: 来源类别），就说明切换成功。

### 4) Select Core Journal Filter (核心期刊筛选)

**⚠️ 必须使用精确提取，避免全量快照：**

```bash
# 精确提取来源类别筛选选项（推荐）
openclaw browser snapshot --compact | grep -E "来源类别" -A 3
```

**常见核心期刊选项：**
- 北大核心 (checkbox "北大核心")
- CSCD (checkbox "CSCD")
- WJCI (checkbox "WJCI")
- 科技核心 (checkbox "科技核心")
- CA (checkbox "CA")
- AJ (checkbox "AJ")
- ISR (checkbox "ISR")

**⚠️ 重要规则：当有多个核心期刊选项时，必须全部勾选！**

当搜索结果页面左侧"来源类别"显示多个核心期刊选项时（如同时显示"北大核心"、"CSCD"、"WJCI"），**必须勾选所有核心期刊选项**，以获取最全面的核心期刊文献。

**处理流程：**
1. 先提取**所有**来源类别复选框（不管是什么核心期刊，全部勾选）：
   ```bash
   # 提取来源类别下所有checkbox的ref
   openclaw browser snapshot --compact | grep -E "term: 来源类别" -A 10 | grep "checkbox"
   ```

2. **依次点击勾选每个checkbox**：
   ```bash
   # 假设找到 e46, e47, e48, e49...
   openclaw browser click e46
   sleep 2
   openclaw browser click e47
   sleep 2
   openclaw browser click e48
   # 继续勾选所有找到的checkbox...
   ```

3. **验证全部勾选成功**：
   ```bash
   sleep 5
   openclaw browser snapshot --compact | grep -E "row \"[0-9]" | head -15
   ```

### 5) Select and Verify Papers (基于摘要验证 - 必须打开详情页)

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
