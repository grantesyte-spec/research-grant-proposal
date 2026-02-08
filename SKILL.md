---
name: research-grant-proposal
description: Generate academic research grant proposals in Chinese based on REAL literature research and validated references.
---

# Research Grant Proposal Generator

**IMPORTANT**: This skill follows a RESEARCH-FIRST workflow. You MUST search for real literature BEFORE generating any proposal.

## CRITICAL WORKFLOW

```
STEP 1: Research (MANDATORY)     ← DO THIS FIRST
  ├── Search CNKI for Chinese literature
  ├── Search PubMed for English literature  
  ├── Search Wanfang for supplementary Chinese literature
  └── Record ALL findings in research_notes.md

STEP 2: Analyze & Select          ← AFTER RESEARCH
  ├── Review search results
  ├── Select 10-15 high-quality references
  └── Verify references are REAL (not fabricated)

STEP 3: Generate Proposal          ← BASED ON REAL LITERATURE
  ├── Write proposal based on research findings
  ├── Cite ONLY the verified real references
  └── Export to Word document

STEP 4: Final Verification         ← OPTIONAL
  └── Double-check all references are correctly cited
```

## ⚠️ GOLDEN RULES

1. **NEVER generate a proposal without doing research first**
2. **NEVER fabricate references** - all citations must come from actual search results
3. **Research MUST be completed before any writing begins**
4. **Document everything** - save research findings to file

---

## STEP 1: LITERATURE RESEARCH (REQUIRED)

When user provides a research topic, you MUST:

### 1.1 Search CNKI (Chinese Literature)
```bash
# Open CNKI advanced search
openclaw browser --browser-profile chrome open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92&rlang=CHINESE"

# Get page snapshot to find element refs
openclaw browser --browser-profile chrome snapshot --compact

# Search with keywords (typically ref=e18)
openclaw browser --browser-profile chrome type e18 "Orem 自理模式 护理" --submit

# Wait for results
openclaw browser --browser-profile chrome wait --load networkidle

# Get search results
openclaw browser --browser-profile chrome snapshot --compact
```

### 1.2 Search PubMed (English Literature)
```bash
# Open PubMed
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/"

# Get page snapshot
openclaw browser --browser-profile chrome snapshot --compact

# Search (typically ref=e14 for search box)
openclaw browser --browser-profile chrome type e14 "Orem self-care model nursing" --submit

# Wait for results
openclaw browser --browser-profile chrome wait --load networkidle

# Get search results
openclaw browser --browser-profile chrome snapshot --compact
```

### 1.3 Search Wanfang (Supplementary Chinese)
```bash
# Open Wanfang
openclaw browser --browser-profile chrome open "https://www.wanfangdata.com.cn/"

# Get page snapshot
openclaw browser --browser-profile chrome snapshot --compact

# Search
openclaw browser --browser-profile chrome type [search-ref] "Orem 自理模式 护理" --submit

# Wait for results
openclaw browser --browser-profile chrome wait --load networkidle

# NOTE: Articles open in NEW TAB!
openclaw browser --browser-profile chrome tabs
openclaw browser --browser-profile chrome focus [new-tab-id]
```

---

## STEP 2: RECORD RESEARCH FINDINGS

### Create research_notes.md

After each search session, CREATE a file called `research_notes.md`:

```markdown
# Literature Research Notes

## Topic
[Research topic provided by user]

## Search Date
[Date]

## CNKI Search Results
**Keywords**: [Search terms used]
**Total Results**: [Number]

### Relevant Articles Found
| # | Title | Authors | Journal | Year | Relevance |
|---|-------|---------|---------|------|-----------|
| 1 | [Article Title] | [Authors] | [Journal] | [Year] | High/Medium/Low |

### Full Citation (if accessed)
[Complete reference with URL]

## PubMed Search Results  
**Keywords**: [Search terms used]
**Total Results**: [Number]

### Relevant Articles Found
| # | Title | PMID | Authors | Journal | Year | Relevance |
|---|-------|------|---------|---------|------|-----------|
| 1 | [Article Title] | [PMID] | [Authors] | [Journal] | [Year] | High/Medium/Low |

## Wanfang Search Results
[Similar format]

## Selected References for Proposal
[List of 10-15 selected references with justification]

## Research Gaps
[What literature is missing? What needs to be addressed?]
```

### Key Information to Extract

For EACH relevant article found:
- ✅ Full title
- ✅ Authors (first 2-3)
- ✅ Journal name
- ✅ Publication year
- ✅ Volume, issue, pages (if available)
- ✅ Abstract (for relevance check)
- ✅ Verification URL (CNKI/PubMed/Wanfang link)
- ✅ Relevance to the topic (High/Medium/Low)

---

## STEP 3: GENERATE PROPOSAL (AFTER RESEARCH)

**CRITICAL**: Only generate proposal AFTER completing Step 1 & 2.

### Output Structure

Generated proposal includes:
- 1. Background & Significance (立题依据)
- 2. Objectives & Content (研究目标与内容)
- 3. Methods & Technical Approach (研究方法与技术路线)
- 4. Expected Outcomes & Innovation (预期成果与创新点)
- 5. References (参考文献) - MUST be from research findings

### Citation Format

**In-Text Citations:**
Use brackets: `[1]`, `[2]`, `[1][2]`, `[1]-[3]`

**Reference List:**
```
[number] Authors. Article title[J]. Journal Name, Year, Volume(Issue): Pages. Verification URL: https://...
```

**Examples:**
```
[1] Wang Y, Zhang X, Liu J. Effects of nursing intervention on hip fracture[J]. J Clin Nurs, 2022, 31(15): 2156-2165. Verification URL: https://pubmed.ncbi.nlm.nih.gov/35012345/

[2] Li M, Wang J. Orem self-care model in elderly hip fracture patients[J]. Chinese Journal of Nursing, 2021, 56(8): 1121-1126. Verification URL: https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&filename=ZHHL202108001
```

**NOTE**: All references MUST come from your research findings. Do NOT cite anything you haven't found.

---

## STEP 4: VERIFICATION (FINAL CHECK)

Even though you found real references during research, do a final verification:

### For Each Reference in Proposal:

1. **Verify Reference Exists**
   ```bash
   openclaw browser --browser-profile chrome open "[verification-url]"
   openclaw browser --browser-profile chrome snapshot --compact
   ```

2. **Verify 5 Elements**
   ```
   ✓ TOPIC: Does title match? YES/NO
   ✓ AUTHORS: Do first 2-3 authors match? YES/NO  
   ✓ YEAR: Does year match? YES/NO
   ✓ ABSTRACT: Is abstract relevant to proposal? YES/NO
   ✓ URL: Can you access the article? YES/NO
   ```

3. **Record Verification**
   ```markdown
   ## [1] VERIFIED
   
   **Title**: [Title]
   - **Authors**: [Authors]  
   - **Journal**: [Journal], [Year]
   - **Status**: TOPIC✓ AUTHORS✓ YEAR✓ ABSTRACT✓ URL✓
   ```

---

## COMMON PITFALLS

| Pitfall | Solution |
|---------|----------|
| Skipping research | ALWAYS do research first - it's mandatory |
| Fabricating references | NEVER cite anything you haven't found |
| Using old/outdated references | Prioritize last 5 years |
| Irrelevant abstracts | Verify abstract relevance to topic |
| Broken URLs | Test all verification URLs |
| Forgetting to save research | Create research_notes.md file |
| Mixing up references | Track which DB each came from |

---

## OUTPUT LOCATION

```
~/Desktop/[Topic Name]课题申请书.docx
```

---

## RESEARCH WORKFLOW CHECKLIST

Before generating ANY proposal, confirm:

- [ ] CNKI search completed and recorded
- [ ] PubMed search completed and recorded
- [ ] Wanfang search completed (if needed)
- [ ] research_notes.md created with findings
- [ ] 10-15 relevant references selected
- [ ] All references verified as REAL
- [ ] References are relevant to topic
- [ ] Only THEN generate proposal

---

## REFERENCE VERIFICATION STEPS

### CNKI (Chinese)
- **File**: `verification_steps/cnki.md`
- **Features**: openclaw browser automation, 8-step process, --submit option, 5-element verification

### PubMed (English)
- **File**: `verification_steps/pubmed.md`  
- **Features**: PMID-based verification, 4/8-step options, --submit option

### Wanfang (Chinese)
- **File**: `verification_steps/wanfang.md`
- **Features**: NEW TAB behavior, tab management (tabs, focus)

---

## SUMMARY: THE CORRECT ORDER

```
1. User provides topic
2. YOU DO RESEARCH (CNKI + PubMed + Wanfang)
3. YOU RECORD findings in research_notes.md
4. YOU SELECT 10-15 real references
5. YOU VERIFY references are real
6. ONLY THEN generate proposal citing real references
7. Export to Word
```

**REMEMBER**: Research FIRST, Writing SECOND. Never skip Step 1.
