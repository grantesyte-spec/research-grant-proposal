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

### Do NOT Use web_fetch
- ❌ Never use `web_fetch` tool for fetching external content
- ✅ Use browser tools (`browser` with `action=open`, `action=snapshot`) instead
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

**Primary Search Tools:**
```bash
# Google Scholar (recommended for English)
open "https://scholar.google.com/scholar?q=keywords"

# ScienceDirect
open "https://www.sciencedirect.com"

# CNKI (中国知网) - requires institutional login
open "https://kns.cnki.net/kns8s/search?classid=WD0FTY92"
```

**Search Keywords Strategy:**
- English: "collaborative care nursing diabetes hip fracture"
- Chinese: "协同护理 糖尿病 髋部骨折 前瞻性护理"

### Step 2: Verify Each Reference

For each candidate reference, verify:

**2.1 Check Authenticity:**
```bash
# Google Scholar
# 1. Click on the article title
# 2. Verify author names match
# 3. Check publication year
# 4. Confirm journal/publisher exists
# 5. Look for "Cited by" count (legitimate papers have citations)
```

**2.2 Verify with DOI:**
- Look for DOI in article metadata
- Visit: https://doi.org/[DOI]
- Confirm article loads correctly

**2.3 Check Citation Count:**
- Google Scholar shows citation count
- Papers with 0 citations may be questionable
- Highly cited papers (>10) are reliable

**2.4 Cross-Reference Check:**
- Search for the article title in quotes
- Check if same article appears on publisher site
- Verify authors and publication details match

### Step 3: Document Verification Results

For each verified reference, record:
```
[编号] Author(s). Title[J]. Journal, Year, Vol(Issue): Pages. DOI. 【验证: 数据库】被引用X次. 验证链接: https://...
```

**Verification URL Options:**
| Source | Verification URL Format |
|--------|------------------------|
| Google Scholar | `https://scholar.google.com/scholar?q=Title+Author+Year` |
| ScienceDirect | `https://www.sciencedirect.com/science/article/pii/XXX` |
| PubMed | `https://pubmed.ncbi.nlm.nih.gov/PMID/` |
| DOI | `https://doi.org/[DOI]` |
| CNKI | `https://kns.cnki.net/kns8s/search?classid=WD0FTY92&q=Title` |

### Step 4: Common Issues and Solutions

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
- Use institutional credentials
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

### 1. **Do NOT Use web_fetch**
- ❌ web_fetch is not allowed for this skill
- ✅ Use browser tools instead (browser action=open, action=snapshot)

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

## Reference Format (Chinese Academic Standard)

```
[序号] 作者. 题名[J]. 刊名, 年, 卷(期): 起止页码. DOI. 验证链接: https://...
```

**Examples:**

**English Journal Article:**
```
[1] Tseng MY, Liang J, Wang JS, et al. Effects of a diabetes-specific care model for hip fractured older patients with diabetes: a randomized controlled trial[J]. Experimental Gerontology, 2019, 118: 31-38. DOI: 10.1016/j.exger.2019.01.006. 验证链接: https://doi.org/10.1016/j.exger.2019.01.006
```

**Chinese Journal Article:**
```
[5] 王青, 李明华. 多学科协作护理模式在糖尿病合并髋部骨折患者中的应用研究[J]. 中华护理杂志, 2020, 55(3): 321-326. 验证链接: https://scholar.google.com/scholar?q=王青+多学科协作+2020
```

**Thesis/Dissertation:**
```
[8] Zhang J. The integrated care model for the management of older patients with hip fracture in China[D]. University of New South Wales, 2023. 验证链接: https://scholar.google.com/scholar?q=Zhang+2023+hip+fracture
```

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

- [ ] No use of web_fetch tool
- [ ] All write() calls include complete parameters (path/file_path + content)
- [ ] All numerical data verified (no typos like "4型糖尿病" → "4亿人")
- [ ] All references verified through Google Scholar/ScienceDirect/DOI
- [ ] All references include verification URLs
- [ ] In-text citations [1], [2], [3]... match reference list
- [ ] Reference titles are complete and properly formatted
- [ ] Document structure follows Chinese academic standards

## Related Skills

- [summarize](../summarize/SKILL.md) - Summarize research papers for reference
- [github](../github/SKILL.md) - Manage proposal repository on GitHub
