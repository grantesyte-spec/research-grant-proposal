# PubMed Research & Verification Guide

## Scope
- PubMed (NCBI - National Center for Biotechnology Information)
- Primary source for English biomedical and nursing literature
- Use `openclaw browser` for verification

---

## PART A: RESEARCH PHASE (Required First)

### A1: Define Search Keywords

Based on the research topic, identify:
- **Core concepts**: Orem self-care model, transtheoretical model, nursing intervention
- **Population**: Hip fracture, diabetes, elderly, older adults
- **Outcomes**: Self-care, rehabilitation, glycemic control, functional recovery

**Example Keywords:**
```
Orem self-care model nursing
Transtheoretical model nursing intervention
Hip fracture elderly rehabilitation
Diabetes elderly self-management
Self-care agency nursing
```

### A2: Open PubMed
```bash
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/"
```

### A3: Search and Explore

```bash
# Get page snapshot
openclaw browser --browser-profile chrome snapshot --compact

# Try different keywords (search box is typically e14)
openclaw browser --browser-profile chrome type e14 "Orem self-care model nursing" --submit
openclaw browser --browser-profile chrome wait --load networkidle
openclaw browser --browser-profile chrome snapshot --compact
```

### A4: Record Initial Findings

**Create research_notes.md and record:**
- Keywords used
- Total results found
- Relevant article titles (PMIDs)
- Journal names and years

**Example entry:**
```
## PubMed Search #1
Keywords: Orem self-care model nursing
Results: 712 articles found

Relevant articles:
1. Effects of nursing theory-guided practice (PMID: 30866078, 2019)
2. Self-care in older adults (PMID: 35012345, 2022)
...
```

---

## PART B: SELECTION PHASE

### B1: Click on Promising Articles

```bash
openclaw browser --browser-profile chrome click [article-ref]
openclaw browser --browser-profile chrome wait --load networkidle
openclaw browser --browser-profile chrome snapshot --compact
```

### B2: Extract Full Citation Information

From article detail page, extract:
- ✅ Full title
- ✅ All authors
- ✅ Journal name
- ✅ Publication date (Year, Month)
- ✅ Volume, Issue, Pages
- ✅ DOI (if available)
- ✅ PMID
- ✅ Abstract
- ✅ Verification URL

### B3: Add to Selected References

Update research_notes.md:
```markdown
## Selected PubMed References

### #1 - High Relevance
**Title**: [Full Title]
**PMID**: [PMID Number]
**Authors**: [First 2-3 authors], et al.
**Journal**: [Journal Name], [Year] [Month]; [Vol]([Issue]): [Pages]
**DOI**: [DOI if available]
**URL**: https://pubmed.ncbi.nlm.nih.gov/[PMID]/
**Abstract**: [Paste abstract]
**Relevance**: HIGH - Addresses [specific aspect]
```

---

## PART C: VERIFICATION PHASE (After Research Complete)

**BEFORE verification:**
- ✅ Research completed
- ✅ 10-15 references selected
- ✅ All saved in research_notes.md

### C1: Verify 5 Elements

```bash
# Use PMID URL directly (most reliable)
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/[PMID]/"
openclaw browser --browser-profile chrome snapshot --compact
```

**Check:**
```
✓ TOPIC: Does title match? YES/NO
✓ AUTHORS: Do first 2-3 authors match? YES/NO
✓ YEAR: Does year match? YES/NO
✓ ABSTRACT: Is abstract relevant? YES/NO
✓ PMID: Is PMID correct? YES/NO
```

### C2: Record Verification Result

```markdown
## PubMed Verification Results

### #1 - VERIFIED ✓

**Title**: [Title]
**PMID**: [PMID]
**Authors**: [Authors]
**Journal**: [Journal], [Year]

VERIFICATION RESULTS:
✓ TOPIC: YES - Matches research topic
✓ AUTHORS: YES - Wang Y, Zhang X confirmed
✓ YEAR: YES - 2022 matches
✓ ABSTRACT: YES - Relevant to proposal
✓ PMID: YES - 35012345 correct

**Full Citation**:
[1] Wang Y, Zhang X, Liu J. Effects of nursing intervention on hip fracture[J]. 
    J Clin Nurs, 2022, 31(15): 2156-2165. 
    PMID: 35012345. 
    Verification URL: https://pubmed.ncbi.nlm.nih.gov/35012345/
```

---

## COMPLETE WORKFLOW

```
STEP 1: Research
  ├── A1: Define keywords
  ├── A2: Open PubMed
  ├── A3: Search and explore (multiple times)
  └── A4: Record initial findings

STEP 2: Selection
  ├── B1: Click promising articles
  ├── B2: Extract full citations
  └── B3: Add selected references

STEP 3: Verification (Only AFTER selection)
  ├── C1: Verify 5 elements for each
  └── C2: Record results
```

---

## 4-STEP QUICK REFERENCE

### Research Steps (1-2)
1. `open PubMed` - Open homepage
2. `type "keywords" --submit` - Search

### Selection Steps (3)
3. `click article` → `wait --load` → `snapshot` - Get details

### Verification Steps (4)
4. `open PMID URL` → `verify 5 elements` - Confirm accuracy

---

## ALTERNATIVE: Direct PMID Search

For known PMIDs:
```bash
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/[PMID]/"
openclaw browser --browser-profile chrome snapshot --compact
→ Extract and verify
```

---

## TROUBLESHOOTING

### Tab Disappears
- Solution: Use PMID URL directly
- Open new tab and continue

### No Results
- Solution: Simplify keywords
- Try broader terms
- Check spelling

### Can't Find Article
- Solution: Use PMID to search directly
- Try alternative keywords

### Abstract Not Relevant
- Solution: Mark FAILED
- Continue searching

---

## GOLDEN RULE

```
Research FIRST → Select → THEN Verify
Never verify what you haven't found through research
```

---

## EXAMPLE: Complete PubMed Session

```bash
# Session 1: Initial Research
open "https://pubmed.ncbi.nlm.nih.gov/"
type e14 "Orem self-care model nursing" --submit
wait --load
snapshot
→ Record findings in research_notes.md

# Session 2: Select Articles
click [article-ref]  # Click promising article
wait --load
snapshot
→ Extract citation, add to selected references

# Session 3: Verify
open "https://pubmed.ncbi.nlm.nih.gov/35012345/"
snapshot
→ Verify 5 elements
→ Record as VERIFIED
```
