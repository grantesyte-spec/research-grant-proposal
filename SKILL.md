---
name: research-grant-proposal
description: Generate academic research grant proposals in Chinese with validated references and Word export. Includes detailed reference verification workflow using Google, PubMed, Scholar, ScienceDirect CNKI, and other academic databases. All references include citation numbers and verification URLs.
---

# Research Grant Proposal Generator (研究课题申请书生成器)

Generate professional academic research grant proposals in Chinese with proper formatting, validated references with URLs, and Word document export.

## Quick Start

1. **Provide research topic and requirements**
2. **Skill generates proposal with in-text citations [1], [2], etc.**
3. **All references include verification URLs for manual check**
4. **Export as Word (.docx) to desktop**

## Important: Tools Usage Guidelines

**Critical: Follow these rules when using tools:**

### Browser Tool: Use CLI Mode Instead of JSON API

**⚠️ Important Discovery: The browser JSON API in OpenClaw may have compatibility issues. Always use CLI mode instead.**

**❌ Avoid (JSON API - may fail):**
```json
browser({
  "action": "act",
  "kind": "type",
  "ref": "e8",
  "text": "hello"
})
// Error: "request required"
```

**✅ Use CLI mode (recommended):**
```bash
openclaw browser --profile chrome type e8 "搜索关键词" --target-id <tab-id>
```

**Common CLI Commands:**
```bash
# Open a URL
openclaw browser --profile chrome open "https://kns.cnki.net/kns8s/search"

# Get page snapshot
openclaw browser --profile chrome snapshot --compact --target-id <tab-id>

# Type text into input field
openclaw browser --profile chrome type e8 "搜索关键词" --target-id <tab-id>

# Click a button/link
openclaw browser --profile chrome click e10 --target-id <tab-id>

# List tabs
openclaw browser --profile chrome tabs

# Check browser status
openclaw browser --profile chrome status
```

**Workflow for CNKI Verification:**
```bash
# 1. Open CNKI search page
openclaw browser --profile chrome open "https://kns.cnki.net/kns8s/search?classid=WD0FTY92"

# 2. Get the tab ID from output (e.g., "targetId": "F32587B995D467451EA8F11DA12BFB52")

# 3. Take snapshot to find element refs
openclaw browser --profile chrome snapshot --compact --target-id F32587B995D467451EA8F11DA12BFB52

# 4. Type search keywords into search box (ref=e8)
openclaw browser --profile chrome type e8 "Orem 自理模式 糖尿病 骨折 护理" --target-id F32587B995D467451EA8F11DA12BFB52

# 5. Click search button (ref=e10)
openclaw browser --profile chrome click e10 --target-id F32587B995D467451EA8F11DA12BFB52
```

### Do NOT Use web_fetch
- ❌ Never use `web_fetch` tool for fetching external content
- ✅ Use browser CLI tools (`openclaw browser --profile chrome`) instead
- ⚠️ This is a strict user requirement - always check if user has given explicit instructions about tool usage

### Verify All Parameters Before Tool Calls
- ✅ Always include ALL required parameters for tool calls
- ✅ Double-check `path` or `file_path` parameters for write operations
- ✅ For write tool: provide `content`, `path` (or `file_path`) together
- ❌ Avoid calling write without complete parameters

**Example - Correct:**
```python
write(content="text", path="/file.txt")
```

**Example - Incorrect:**
```python
write(content="text")  # Missing path parameter!
```

## Document Structure

The generated proposal includes:
- Research title and objectives
- Background and significance (立题依据) with in-text citations [1]-[20]
- Research content and expected outcomes
- Research methodology and technical approach
- Timeline and milestones
- References section with numbered citations [1], [2], [3]... and verification URLs

## In-Text Citations

**Format:** Cite using superscript numbers in brackets [1]

**Examples in text:**
- "协同护理模式可显著改善患者预后[1][2]"
- "多学科协作已被证明是有效的干预方法[3][4][5]"
- "参考Tseng等[6]的研究设计..."

**Rules:**
- Cite when referencing specific research findings
- Cite when describing established methods
- Cite when stating statistics or data
- Group related references together [1][2][3]
- Use [1]-[5] for consecutive references

## Reference List with Verification URLs

**Each reference includes:**
1. Numbered citation [1]
2. Full bibliographic information (APA/Chinese format)
3. DOI (if available)
4. **Verification URL** for manual check

**Format:**
```
[1] Author(s). Title[J]. Journal, Year, Vol(Issue): Pages. DOI. 验证链接: https://...
[2] Author(s). Title[J]. Journal, Year, Vol(Issue): Pages. 验证链接: https://...
```

## Reference Verification Workflow

**Critical: All references must be verified before including in proposals.**

### Step 1: Search for References

**Primary Search Tools (CLI Mode):**

```bash
# CNKI (中国知网) - requires institutional login
# Step 1: Open CNKI search page
openclaw browser --profile chrome open "https://kns.cnki.net/kns8s/search?classid=WD0FTY92"

# Step 2: Type search keywords (search box ref=e8)
openclaw browser --profile chrome type e8 "协同护理 糖尿病 髋部骨折" --target-id <tab-id>

# Step 3: Click search button (button ref=e10)
openclaw browser --profile chrome click e10 --target-id <tab-id>

# CNKI Advanced Search
openclaw browser --profile chrome open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92&rlang=CHINESE"
# Then use snapshot to find element refs, type in ref=e18 (topic field), click ref=e33 (search)

# Google Scholar (recommended for English)
open "https://scholar.google.com/scholar?q=keywords"

# ScienceDirect
open "https://www.sciencedirect.com"
```

**Search Keywords Strategy:**
- English: "collaborative care nursing diabetes hip fracture"
- Chinese: "协同护理 糖尿病 髋部骨折 前瞻性护理"

### Step 2: Verify Each Reference

**Using Browser CLI for Verification:**

For each candidate reference, verify:

**2.1 Open Article on CNKI:**
```bash
# Click on article title from search results (note the ref from snapshot)
openclaw browser --profile chrome click e48 --target-id <tab-id>  # e48 is article title link
```

**2.2 Check Authenticity:**
```bash
# On article page, verify:
# 1. Author names match
# 2. Publication year is correct
# 3. Journal name is visible
# 4. Volume, issue, pages are present
# 5. DOI is available (look for "DOI" link)

# Take snapshot to verify details
openclaw browser --profile chrome snapshot --compact --target-id <tab-id>
```

**2.3 Verify with DOI:**
- Look for DOI in article metadata
- Click DOI link or visit: https://doi.org/[DOI]
- Confirm article loads correctly

**2.4 Check Citation Count:**
- CNKI shows "被引" (citation count)
- Papers with 0 citations may be questionable
- Highly cited papers (>5) are reliable

**2.5 Cross-Reference Check:**
- Search for the article title in Google Scholar
- Check if same article appears on publisher site
- Verify authors and publication details match

### Step 3: Document Verification Results

For each verified reference, record:
```
[编号] Author(s). Title[J]. Journal, Year, Vol(Issue): Pages. DOI. 【验证: 数据库】被引用X次. 验证链接: https://...
```

**Verification URL Options:**
| Source | Verification URL Format | CLI Access |
|--------|------------------------|-----------|
| CNKI | `https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&...` | `openclaw browser --profile chrome open "URL"` |
| Google Scholar | `https://scholar.google.com/scholar?q=Title+Author+Year` | `open "URL"` |
| ScienceDirect | `https://www.sciencedirect.com/science/article/pii/XXX` | `open "URL"` |
| PubMed | `https://pubmed.ncbi.nlm.nih.gov/PMID/` | `open "URL"` |
| DOI | `https://doi.org/[DOI]` | `open "URL"` |

**For CNKI URLs, always capture the full URL from browser navigation after clicking article link.**

### Step 4: Common Issues and Solutions

**Issue: Browser JSON API returns "request required" error**
- ✅ **Solution:** Use CLI mode instead: `openclaw browser --profile chrome type e8 "text" --target-id <tab-id>`

**Issue: CNKI shows "暂无数据" (no results)**
- Try alternative keywords (simplified vs traditional Chinese)
- Use fewer keywords or broader search terms
- Check if search field ref has changed (take new snapshot)

**Issue: Article not found in database**
- Try alternative search (title in quotes, author name)
- Check for spelling variations
- Verify the journal exists

**Issue: Citation count is 0 for recent paper**
- Acceptable if published within 1-2 years
- Check if it's from a reputable journal

**Issue: Author name mismatch**
- Check author profiles on Google Scholar
- Look for "Author profile" links
- Verify institutional affiliation

**Issue: CNKI access requires login**
- User is logged in with institutional account (CNKI_3XLBNUJH)
- If login expires, ask user to re-login on browser
- Alternative: Use Google Scholar for Chinese journals
- Record as "requires institutional login"

### Step 5: Reference Quality Criteria

Include only references that meet ALL:
- [ ] Published in peer-reviewed journal
- [ ] Authors can be verified
- [ ] Journal has impact factor or is reputable
- [ ] DOI or stable URL available
- [ ] Content directly relevant to research topic
- [ ] Published within last 10 years (except seminal papers)

**Exclude:**
- Predatory journals (check Beall's List)
- Non-peer-reviewed sources
- Duplicate publications
- Non-accessible sources

## Common Pitfalls to Avoid

### 1. **Use CLI Mode for Browser Operations**
- ❌ Avoid using browser JSON API (may return "request required" errors)
- ✅ Use CLI mode: `openclaw browser --profile chrome <command> <args>`
- ✅ Example: `openclaw browser --profile chrome type e8 "hello" --target-id <tab-id>`

### 2. **Verify All Parameters**
- ❌ Never call write without complete parameters
- ✅ Always include `path` or `file_path` with `content`
- ✅ Example: `write(content="text", path="/file.txt")`

### 3. **Check for Typos**
- ❌ Avoid errors like "4型糖尿病" when meaning "4亿人"
- ✅ Proofread all numerical data and statistics
- ✅ Verify unit accuracy (e.g., "亿" vs "万", "%")

### 4. **Verify Reference Titles**
- ❌ Avoid incomplete or poorly formatted titles
- ✅ Use full journal titles in standard format
- ✅ Double-check author names and initials

### 5. **Do NOT Use web_fetch**
- ❌ web_fetch is not allowed for this skill
- ✅ Use browser CLI tools instead

## Reference Format (Chinese Academic Standard)

### English References
```
[序号] Author(s). Title[J]. Journal, Year, Vol(Issue): Pages. DOI. 验证链接: https://...
```

### Chinese References
```
[序号] 作者1, 作者2, 作者3. 文章题目[J]. 期刊名称, 年, 卷(期): 起止页码. DOI. 验证链接: https://...
```

**Examples:**

**English Journal Article:**
```
[1] Tseng MY, Liang J, Wang JS, et al. Effects of a diabetes-specific care model for hip fractured older patients with diabetes: a randomized controlled trial[J]. Experimental Gerontology, 2019, 118(1): 31-38. DOI: 10.1016/j.exger.2019.01.006. 验证链接: https://doi.org/10.1016/j.exger.2019.01.006
```

**Chinese Journal Article:**
```
[2] 王青, 李明华, 陈晓红. 多学科协作护理模式在2型糖尿病合并髋部骨折患者中的应用研究[J]. 中华护理杂志, 2020, 55(3): 321-326. DOI: 10.3761/j.issn.0254-1769.2020.03.001. 验证链接: https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLAST2021&filename=ZHHL202003001
```

**Chinese Thesis/Dissertation:**
```
[5] 张三. 老年2型糖尿病患者骨质疏松性骨折的护理干预研究[D]. 北京协和医学院, 2023. 验证链接: https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CMFD&dbname=CMFD202402&filename=102278021.nh
```

**Chinese Conference Paper:**
```
[8] 李四, 王五. 协同护理模式在骨科患者中的应用[C]. 2022中国护理管理大会论文集, 2022: 156-160. 验证链接: https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CPFD&dbname=CPFD2023&filename=2022HL0415R014
```

## 中文参考文献支持

### 搜索中文文献

**CNKI（中国知网）- 需要机构登录**
```
https://kns.cnki.net/kns8s/search?classid=WD0FTY92
```

**万方数据库**
```
https://www.wanfangdata.com.cn/index/index.do
```

**维普期刊**
```
http://www.cqvip.com/
```

**Google Scholar（中文文献）**
```
https://scholar.google.com/scholar?q=site:cnki.net+关键词
# 或
https://scholar.google.com/scholar?q=中文标题+作者+年份
```

### 中文参考文献格式

**核心期刊格式（符合中科院/CSCD标准）：**
```
[序号] 作者. 文章题目[J]. 期刊名称, 年, 卷(期): 起止页码. DOI.
```

**学位论文格式：**
```
[序号] 作者. 论文题目[D]. 城市: 学校名称, 年.
```

**会议论文格式：**
```
[序号] 作者. 文章题目[C]. 会议名称, 年: 起止页码.
```

**著作格式：**
```
[序号] 作者. 书名[M]. 版次. 出版地: 出版社, 年.
```

### 中文参考文献验证方法

**方法1：CNKI验证（推荐，需要机构登录）**

**⚠️ 重要：使用命令行模式访问浏览器**

由于 OpenClaw 的 browser JSON API 在某些场景下可能不稳定，建议使用命令行模式：

```bash
# 1. 打开 CNKI 搜索页面
openclaw browser --profile chrome open "https://kns.cnki.net/kns8s/search?classid=WD0FTY92"

# 2. 获取页面快照（查看搜索框 ref）
openclaw browser --profile chrome snapshot --target-id <tab-id> --compact

# 3. 在搜索框输入关键词（假设搜索框 ref=e8）
openclaw browser --profile chrome type e8 "协同护理 糖尿病 髋部骨折" --target-id <tab-id>

# 4. 执行搜索
openclaw browser --profile chrome click e10 --target-id <tab-id>  # 点击搜索按钮
```

**详细步骤：**

1. 打开 CNKI 高级搜索页面：
   ```bash
   openclaw browser --profile chrome open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92&rlang=CHINESE"
   ```

2. 获取页面结构：
   ```bash
   openclaw browser --profile chrome snapshot --compact
   ```
   记录搜索框的 ref ID（如 `e18` 为主题搜索框）

3. 输入搜索词：
   ```bash
   openclaw browser --profile chrome type e18 "Orem 自理模式 糖尿病 骨折 护理" --target-id <tab-id>
   ```

4. 点击搜索按钮（通常 ref=`e33`）：
   ```bash
   openclaw browser --profile chrome click e33 --target-id <tab-id>
   ```

5. 浏览搜索结果并记录验证链接

**验证链接格式：**
```
https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLAST2021&filename=ZHHL202003001
```

**方法2：Google Scholar验证（无需登录）**
1. 访问：https://scholar.google.com/scholar?q=中文标题+作者+年份
2. 点击"引用"查看完整信息
3. 验证链接格式：
   ```
   https://scholar.google.com/scholar?q=王青+多学科协作+2020
   ```

**方法3：万方/维普验证**
1. 访问相应数据库
2. 搜索文章标题
3. 记录DOI或永久链接

### 中文文献质量评估标准

**核心期刊（满足任一即可）：**
- [ ] 北大核心期刊目录来源
- [ ] CSCD（中国科学引文数据库）来源
- [ ] 科技核心期刊（统计源期刊）
- [ ] 中文核心期刊要目总览

**常见中文护理期刊：**
- 中华护理杂志
- 中国护理管理
- 护理学杂志
- 护理研究
- 解放军护理杂志
- 中华现代护理杂志
- 护士进修杂志
- 护理管理杂志

### 中英文参考文献混合使用建议

1. **引用国外研究时**：优先使用英文原文
2. **引用国内特色研究时**：使用中文文献
3. **引用国内政策/指南时**：使用中文文献
4. **引用方法学内容时**：中英文均可
5. **数量建议**：中文文献占30-50%为佳

## Common Topics

This skill is optimized for nursing and medical research topics:
- Collaborative care models (协同护理模式)
- Prospective nursing management (前瞻性护理管理)
- Chronic disease management (糖尿病、高血压、骨质疏松)
- Orthopedic nursing (骨科护理、髋部骨折)
- Quality of life and clinical outcomes

## Usage Examples

**Basic:**
- "Generate a research grant proposal about collaborative nursing care with verified references"
- "Create a proposal for diabetes nursing management research"

**Advanced:**
- "Create a grant proposal titled 'Collaborative Care Combined with Prospective Nursing Management in Type 2 Diabetes Patients with Osteoporotic Intertrochanteric Femoral Fractures' with [1]-[20] citations and verification URLs for each reference"

## Output Location

Generated Word documents are saved to:
```
~/Desktop/[proposal-title].docx
```

## Output Example

**In-text citations:**
```
协同护理模式已被证明可显著改善患者预后[1][2]，多学科协作团队
的建立是实施该模式的关键[3][4]。
```

**References section:**
```
五、近五年核心期刊参考文献

[1] Moran WP, Chen GJ, Watters C, et al. Using a collaborative approach 
    to reduce postoperative complications for hip-fracture patients: a 
    three-year follow-up[J]. The Joint Commission Journal on Quality 
    and Patient Safety, 2006, 32(11): 573-584. 
    验证链接: https://scholar.google.com/scholar?q=Moran+2006+hip+fracture

[2] Tseng MY, Liang J, Wang JS, et al. Effects of a diabetes-specific 
    care model for hip fractured older patients with diabetes: a 
    randomized controlled trial[J]. Experimental Gerontology, 2019, 
    118: 31-38. DOI: 10.1016/j.exger.2019.01.006. 
    验证链接: https://doi.org/10.1016/j.exger.2019.01.006
```

## Best Practices Checklist

Before submitting any generated proposal:

- [ ] Browser operations use CLI mode (`openclaw browser --profile chrome`) not JSON API
- [ ] No use of web_fetch tool
- [ ] All write() calls include complete parameters (path/file_path + content)
- [ ] All numerical data verified (no typos like "4型糖尿病" → "4亿人")
- [ ] All references verified through CNKI CLI / Google Scholar / ScienceDirect / DOI
- [ ] All references include verification URLs
- [ ] In-text citations [1], [2], [3]... match reference list
- [ ] Reference titles are complete and properly formatted
- [ ] Document structure follows Chinese academic standards

## Related Skills

- [summarize](../summarize/SKILL.md) - Summarize research papers for reference
- [github](../github/SKILL.md) - Manage proposal repository on GitHub
