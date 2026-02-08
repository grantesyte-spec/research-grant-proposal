---
name: research-grant-proposal
description: Generate academic research grant proposals in Chinese based on REAL literature research and validated references.
---

# Research Grant Proposal Generator

**IMPORTANT**: This skill follows a RESEARCH-FIRST workflow.

## WORKFLOW

```
STEP 0: Break down topic into keywords
STEP 1: Research - Search CNKI → PubMed → Wanfang
STEP 2: Select - Choose 10-15 relevant references
STEP 3: Verify - Confirm 5 elements for each
STEP 4: Generate - Write proposal with real citations
```

---

## STEP 0: Break Down Topic

**Example Topic:**
```
基于动机行为转化理论的Orem自理模式支持在股骨颈骨折合并糖尿病患者护理中的应用
```

**Break Down:**
| # | Concept | Keywords |
|---|---------|----------|
| 1 | Theory | 动机行为转化理论, Orem 自理模式 |
| 2 | Population | 股骨颈骨折, 糖尿病 |
| 3 | Intervention | 护理, 康复 |

**Search each concept in each database.**

---

## STEP 1: Research

### CNKI (Chinese Literature)
```bash
openclaw browser --browser-profile chrome open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92&rlang=CHINESE"
snapshot
type e18 "[keywords]" --submit
wait --load networkidle
snapshot
```

### PubMed (English Literature)
```bash
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/"
snapshot
type e14 "[keywords]" --submit
wait --load networkidle
snapshot
```

### Wanfang (Supplementary Chinese)
```bash
openclaw browser --browser-profile chrome open "https://www.wanfangdata.com.cn/"
snapshot
type [ref] "[keywords]" --submit
wait --load networkidle
snapshot

# NOTE: Articles open in NEW TAB!
tabs
focus [article-tab-id]
```

---

## STEP 2: Select References

Choose 10-15 high-quality references from your searches.

**Record in research_notes.md:**
```markdown
## Selected References

### CNKI
1. Authors. Title[J]. Journal, Year. URL

### PubMed  
1. Authors. Title[J]. Journal, Year. PMID: [PMID]. URL
```

---

## STEP 3: Verify 5 Elements

For EACH selected reference:

```bash
open "[verification-url]"
wait --load networkidle
snapshot
```

**Check:**
```
✓ TOPIC: Title matches? YES/NO
✓ AUTHORS: First 2-3 match? YES/NO
✓ YEAR: Year matches? YES/NO
✓ ABSTRACT: Relevant? YES/NO
✓ URL: Accessible? YES/NO
```

**Record:**
```
## [1] VERIFIED ✓
Status: TOPIC✓ AUTHORS✓ YEAR✓ ABSTRACT✓ URL✓
```

---

## STEP 4: Generate Proposal

**Output Structure:**
1. Background & Significance
2. Objectives & Content
3. Methods & Technical Approach
4. Expected Outcomes & Innovation
5. References (ONLY verified real citations)

**Citation Format:**
```
[number] Authors. Title[J]. Journal, Year, Vol(Issue): Pages. Verification URL.
```

---

## RECORDING TEMPLATE

Create `research_notes.md`:

```markdown
# Literature Research Notes

## Topic
[Research topic]

## CNKI Search
Keywords: [keywords]
Results: [number]

### Selected References
| # | Title | Authors | Journal | Year | Relevance |
|---|-------|---------|---------|------|-----------|
| 1 | [Title] | [Authors] | [Journal] | [Year] | High |

### #1 - VERIFIED ✓
[Full citation]
Status: ✓✓✓✓✓
```

---

## GOLDEN RULES

1. **Break down topic first** → then search
2. **snapshot → type → wait → snapshot** (after EVERY change)
3. **NEW TAB** (Wanfang) - Always switch tabs!
4. **Research → Select → THEN Verify → Generate**
5. **Record everything** in research_notes.md
6. **Never fabricate** - only cite what you found
7. **Use PMID** (PubMed) - most reliable identifier

---

## TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| No results | Simplify keywords |
| Ref not found | Re-run snapshot |
| Tab issues | Use `tabs` → `focus [id]` |
| Can't access | Try different database |

---

## OUTPUT LOCATION

```
~/Desktop/[Topic Name]课题申请书.docx
```

---

## FILES

- **SKILL.md**: This file (high-level workflow)
- **verification_steps/cnki.md**: Detailed CNKI guide
- **verification_steps/pubmed.md**: Detailed PubMed guide
- **verification_steps/wanfang.md**: Detailed Wanfang guide
