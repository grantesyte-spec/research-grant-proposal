---
name: research-grant-proposal
description: Generate academic research grant proposals in Chinese with validated references and Word export. Includes detailed reference verification workflow using Google Scholar, ScienceDirect, PubMed, CNKI, and other academic databases.
---

# Research Grant Proposal Generator (研究课题申请书生成器)

Generate professional academic research grant proposals in Chinese with proper formatting, validated references, and Word document export.

## Quick Start

1. **Provide research topic and requirements**
2. **Skill generates proposal with verified references**
3. **Export as Word (.docx) to desktop**

## Document Structure

The generated proposal includes:
- Research title and objectives
- Background and significance (立题依据)
- Research content and expected outcomes
- Research methodology and technical approach
- Timeline and milestones
- References (validated from academic databases)

## Word Document Format

- Chinese fonts (宋体)
- Proper headings (16pt title, 14pt section, 12pt body)
- Tables for metrics and team members
- Professional academic formatting
- Saved to Desktop as `.docx`

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
[编号] Author(s). Title[J]. Journal, Year, Vol(Issue): Pages. DOI. 【验证: Google Scholar/数据库】被引用X次
```

**Verification Status:**
- ✅ **Google Scholar** - Verified authentic
- ✅ **ScienceDirect** - Verified authentic
- ✅ **PubMed** - Verified authentic
- ✅ **CNKI** - Verified authentic (requires login)
- ⚠️ **Requires Manual Verification** - Could not verify automatically

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
- "Create a grant proposal titled 'Collaborative Care Combined with Prospective Nursing Management in Type 2 Diabetes Patients with Osteoporotic Intertrochanteric Femoral Fractures' and verify all 15 references through Google Scholar"

## Output Location

Generated Word documents are saved to:
```
~/Desktop/[proposal-title].docx
```

## Reference Format (Chinese Academic Standard)

```
[序号] 作者. 题名[J]. 刊名, 年, 卷(期): 起止页码. DOI/URL. 【验证: 数据库】被引用X次
```

Example:
```
[3] Tseng MY, Liang J, Wang JS, et al. Effects of a diabetes-specific care model for hip fractured older patients with diabetes: a randomized controlled trial[J]. Experimental Gerontology, 2019, 118: 31-38. 【验证: Google Scholar】被引用15次
```

## Related Skills

- [summarize](../summarize/SKILL.md) - Summarize research papers for reference
- [github](../github/SKILL.md) - Manage proposal repository on GitHub
