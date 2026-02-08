---
name: research-grant-proposal
description: Generate academic research grant proposals in Chinese with validated references and Word export.
---

# Research Grant Proposal Generator (研究课题申请书生成器)

Generate professional academic research grant proposals in Chinese with proper formatting, validated references with URLs, and Word document export.

## Quick Start

1. Provide research topic and requirements
2. Skill generates proposal with in-text citations [1], [2], etc.
3. All references include verification URLs for manual check
4. Export as Word (.docx) to `~/Desktop/`

## Output Structure

Generated proposal includes:
- Research title and objectives
- Background and significance (立题依据)
- Research content and expected outcomes
- Methodology and technical approach
- References section with [1]-[10] and verification URLs

## Citation Format

### In-Text Citations
Use brackets: `[1]`, `[2]`, `[1][2]`, `[1]-[3]`

### Reference List
```
[序号] 作者. 文章题目[J]. 期刊名称, 年, 卷(期): 起止页码. DOI. 验证链接: https://...
```

**Examples:**
```
[1] Wang Y, Li X. Effects of nursing intervention on hip fracture[J]. J Clin Nurs, 2022, 31(15): 2156-2165. DOI: 10.1111/jocn.16235. 验证链接: https://doi.org/10.1111/jocn.16235

[2] 李明华, 王建国. Orem自理模式在老年髋部骨折患者护理中的应用[J]. 中华护理杂志, 2020, 55(8): 1121-1126. DOI: 10.3761/j.issn.0254-1769.2020.08.001. 验证链接: https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&filename=ZHHL202008001
```

## Reference Verification Workflow

**Critical: All references must be verified. AI must iterate until all references are authentic.**

### AI Self-Correction Loop

```
┌─────────────────────────────────────────────────────────────┐
│                    VERIFICATION LOOP                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────┐                                       │
│  │ Generate Proposal │ ←── Initial input                      │
│  └────────┬─────────┘                                       │
│           ↓                                                 │
│  ┌──────────────────┐    ┌──────────────────┐            │
│  │ Verify All       │──NO→│ Find Replacement │            │
│  │ References Auth? │     │ Reference        │            │
│  └────────┬─────────┘     └────────┬─────────┘            │
│           ↓ YES                     ↓                       │
│  ┌──────────────────┐     ┌──────────────────┐            │
│  │ Export Word      │     │ Update Proposal  │            │
│  │ Document         │     │ with New Ref     │            │
│  └──────────────────┘     └────────┬─────────┘            │
│                                    │                       │
│                                    └───────────────────────┘
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Step 1: Generate Initial Proposal

Generate proposal with references (may include unverifiable ones).

### Step 2: Verify Each Reference

**For each reference, check:**

1. **Database Access**
   ```bash
   # Try to access verification URL
   openclaw browser --profile chrome open "[verification-url]"
   
   # If URL fails or returns 404:
   # → Mark as FAILED
   # → Find replacement reference
   ```

2. **Authenticity Criteria**
   ```
   ✓ Article exists at verification URL
   ✓ Authors match the citation
   ✓ Publication year is correct
   ✓ Journal is real and peer-reviewed
   ✓ DOI resolves correctly (if available)
   ✓ Content is accessible
   ```

3. **Quality Assessment**
   ```
   ✓ Published in reputable journal
   ✓ Relevant to research topic
   ✓ Within last 10 years
   ✓ Has citations/impact
   ```

### Step 3: Handle Failed References

**If a reference fails verification:**

1. **Search for Replacement**
   ```bash
   # Use search keywords from failed reference
   openclaw browser --profile chrome open "https://scholar.google.com/scholar?q=topic+keywords"
   # OR CNKI
   open "https://kns.cnki.net/kns8s/search?classid=WD0FTY92&q=topic+keywords"
   # OR 万方数据库
   open "https://www.wanfangdata.com.cn/"
   ```

2. **Select Valid Replacement**
   - Choose article from verified database
   - Ensure similar topic/coverage
   - Note: "Replacement for ref #[X]"

3. **Update Proposal**
   - Replace failed reference with new one
   - Update all in-text citations
   - Restart verification loop

### Step 4: Continue Until Complete

**Loop criteria:**
- ALL references must be verifiable
- ALL in-text citations must match reference list
- NO broken links or missing DOIs

**Only when loop completes:**
→ Export Word document

### Reference Verification Template

AI must record for each reference:

```
[1] AUTHOR. TITLE[J]. JOURNAL, YEAR.
    Status: VERIFIED/FAILED
    Database: CNKI/Google Scholar/ScienceDirect/DOI
    Verification URL: https://...
    If FAILED → Replacement: [NEW-REF]
```

## Browser Tool Usage

**⚠️ Important: Use CLI mode, not JSON API**

```bash
# Open URL
openclaw browser --profile chrome open "https://kns.cnki.net/kns8s/search"

# Get page structure
openclaw browser --profile chrome snapshot --compact

# Type/Click (use ref from snapshot)
openclaw browser --profile chrome type e8 "关键词" --target-id <tab-id>
openclaw browser --profile chrome click e10 --target-id <tab-id>
```

**Do NOT use:** `web_fetch` tool

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| JSON API errors | Use CLI mode: `openclaw browser --profile chrome <command>` |
| Missing path in write | Always include: `write(content="text", path="/file.txt") |
| Typo in numbers | Verify: 亿/万, %, decimals |

## Output Location

```
~/Desktop/[课题名称]课题申请书.docx
```

## Best Practices Checklist

Before submitting:
- [ ] No web_fetch tool used
- [ ] All write() calls include complete parameters
- [ ] Numerical data verified (no typos like "4型糖尿病" → "4亿人")
- [ ] **ALL references verified through verification loop**
- [ ] **NO failed/unverifiable references remain**
- [ ] All in-text citations match reference list
- [ ] Document follows Chinese academic standards

## Reference Quality Sources

### English Journals
- Journal of Clinical Nursing
- International Journal of Nursing Studies
- Osteoporosis International
- Geriatric Nursing

### Chinese Core Journals
- 中华护理杂志
- 中国护理管理
- 护理学杂志
- 中华糖尿病杂志
- 中国实用护理杂志
