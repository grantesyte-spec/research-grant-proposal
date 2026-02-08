# PubMed Research & Verification Guide

## Scope
- PubMed (NCBI - National Center for Biotechnology Information)
- Primary source for English biomedical and nursing literature
- Use `openclaw browser` for verification

---

## PART A: RESEARCH PHASE (Required First)

### A1: Define Search Keywords

**Strategy**: Similar to CNKI, start with core concepts.

**Example Keywords:**
```
# Simple first (recommended)
Orem self-care model nursing
Transtheoretical model nursing
Self-care elderly

# Add modifiers if needed
Orem self-care model fracture
Transtheoretical model elderly rehabilitation
```

**Note**: PubMed usually returns more results than CNKI.

### A2: Open PubMed
```bash
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/"
```

### A3: Search and Explore

**IMPORTANT LESSON**: Same as CNKI - Re-run snapshot after EVERY change!

```bash
# Step 1: Open PubMed
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/"

# Step 2: CRITICAL - Get page snapshot FIRST
openclaw browser --browser-profile chrome snapshot --compact

# Step 3: Find search box ref (typically e14)
# Look for "combobox" or input field

# Step 4: Type and submit
openclaw browser --browser-profile chrome type e14 "Orem self-care model nursing" --submit

# Step 5: CRITICAL - Wait for load
openclaw browser --browser-profile chrome wait --load networkidle

# Step 6: CRITICAL - Re-run snapshot!
openclaw browser --browser-profile chrome snapshot --compact
```

### A4: Record Initial Findings

**Create research_notes.md:**
```
## PubMed Search #1
Keywords: Orem self-care model nursing
Results: 77,273 articles found

Relevant:
1. Usefulness of nursing theory-guided practice (PMID: 30866078, 2019)
2. Effect of Early Rehabilitation Nursing Based on Orem's Self-Care Theory (PMID: 36120688, 2022)
```

---

## PART B: SELECTION PHASE

### B1: Click on Promising Articles

```bash
# Click article
openclaw browser --browser-profile chrome click [article-ref]

# Wait for load
openclaw browser --browser-profile chrome wait --load networkidle

# CRITICAL - Re-run snapshot!
openclaw browser --browser-profile chrome snapshot --compact
```

### B2: Extract Full Citation

From detail page, extract:
- ✅ Full title
- ✅ PMID (unique identifier!)
- ✅ Authors
- ✅ Journal name
- ✅ Year, Volume, Issue, Pages
- ✅ DOI (if available)
- ✅ Abstract

### B3: Add to Selected References

```markdown
## Selected PubMed References

### #1 - Very High Relevance
**Title**: [Full Title]
**PMID**: [PMID Number]
**Authors**: [First 2-3], et al.
**Journal**: [Journal Name], [Year] [Month]; [Vol]([Issue]): [Pages]
**DOI**: [DOI if available]
**URL**: https://pubmed.ncbi.nlm.nih.gov/[PMID]/
**Relevance**: VERY HIGH - Addresses Orem model + [population]
```

---

## PART C: VERIFICATION PHASE (After Research Complete)

**BEFORE verification:**
- ✅ Research completed
- ✅ 10-15 references selected
- ✅ All saved in research_notes.md

### C1: Verify 5 Elements (with PMID)

```bash
# Method 1: Use PMID URL (most reliable)
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/[PMID]/"

# Method 2: Use DOI
openclaw browser --browser-profile chrome open "https://doi.org/[DOI]"

# Wait and snapshot
openclaw browser --browser-profile chrome wait --load networkidle
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

### C2: Record Verification

```markdown
## PubMed Verification Results

### #1 - VERIFIED ✓

**Title**: [Title]
**PMID**: [PMID]
**Authors**: [Authors]
**Journal**: [Journal], [Year]

VERIFICATION RESULTS:
✓ TOPIC: YES - Matches research topic
✓ AUTHORS: YES - Younas A confirmed
✓ YEAR: YES - 2019 matches
✓ ABSTRACT: YES - Relevant to proposal
✓ PMID: YES - 30866078 correct

**Full Citation**:
[1] Authors. Title[J]. Journal, Year, Vol(Issue): Pages. 
    PMID: [PMID]. 
    Verification URL: https://pubmed.ncbi.nlm.nih.gov/[PMID]/
```

---

## COMPLETE WORKFLOW

```
STEP 1: Research
  ├── A1: Define keywords
  ├── A2: Open PubMed
  ├── A3: snapshot → type --submit → wait → snapshot
  └── A4: Record findings

STEP 2: Selection
  ├── B1: Click article → wait → snapshot
  ├── B2: Extract citations
  └── B3: Add to selected

STEP 3: Verification (After selection complete)
  ├── C1: Verify 5 elements (use PMID)
  └── C2: Record results
```

---

## LESSONS LEARNED (Updated from Practice)

### Lesson 1: PMID is Reliable Identifier
```bash
# ✅ BEST - Use PMID directly
open "https://pubmed.ncbi.nlm.nih.gov/30866078/"
→ Always works

# ✅ GOOD - Use DOI
open "https://doi.org/10.1111/scs.12670"
→ Works if DOI is valid
```

### Lesson 2: PubMed Returns More Results
```
CNKI: 759 results for "Orem 自理模式"
PubMed: 77,273 results for "Orem self-care model nursing"
→ PubMed has more English literature
→ CNKI has more Chinese literature
```

### Lesson 3: Same Snapshot Rule Applies
```bash
# ❌ WRONG - Skip snapshot
type e14 "keywords" --submit
→ Error: Element "e14" not found

# ✅ RIGHT - Snapshot first
snapshot
type e14 "keywords" --submit
wait --load
snapshot
```

### Lesson 4: Transtheoretical Model Keywords
```
# Working searches:
"Orem self-care model nursing" → 77,273 results
"transtheoretical model elderly rehabilitation" → 171 results
"nursing theory-guided practice" → Many results
```

---

## TROUBLESHOOTING

### Problem 1: Tab Disappears
```
Cause: PubMed detects automation
Solution:
1. Use PMID URL directly (most reliable)
2. Open new tab manually
3. Continue verification
```

### Problem 2: No Results
```
Solution:
1. Simplify keywords
2. Check spelling
3. Try alternative terms
```

### Problem 3: Can't Find Article
```
Solution:
1. Use PMID to search directly
2. Try different keywords
3. Check filters (abstract, free full text)
```

### Problem 4: Dynamic Content
```
Solution:
1. wait --load networkidle
2. Re-run snapshot
3. Wait for abstract to appear
```

---

## GOLDEN RULES

```
1. Start SIMPLE → Add complexity
2. snapshot → type → wait → snapshot (always!)
3. Use PMID for verification (most reliable)
4. Research FIRST → Select → THEN Verify
5. Record EVERYTHING in research_notes.md
```

---

## EXAMPLE: Complete PubMed Session (from Practice)

```bash
# 1. Search with simple keywords
open "https://pubmed.ncbi.nlm.nih.gov/"
snapshot
→ Found ref e14 for search box

# 2. Search
type e14 "Orem self-care model nursing" --submit
wait --load networkidle
snapshot
→ Found 77,273 results!

# 3. Found highly relevant article
# "Usefulness of nursing theory-guided practice" (PMID: 30866078)

# 4. Verify using PMID (most reliable)
open "https://pubmed.ncbi.nlm.nih.gov/30866078/"
wait --load networkidle
snapshot
→ Verified 5 elements
→ Recorded as VERIFIED

# 5. Search for TTM literature
type e14 "transtheoretical model elderly rehabilitation" --submit
wait --load networkidle
snapshot
→ Found 171 results
→ Found: "Influence of health education based on TTM in elderly patients" (PMID: 38975135)
```

---

## ADVANTAGE: PubMed vs CNKI

| Feature | PubMed | CNKI |
|---------|--------|------|
| **Results Count** | More (77K+) | Fewer (759+) |
| **Identifier** | PMID (reliable) | No standard ID |
| **English Coverage** | ✅ Excellent | Limited |
| **Chinese Coverage** | Limited | ✅ Excellent |
| **Access** | Free | May require login |
| **Tab Stability** | May close tabs | More stable |

**Strategy**: Use BOTH databases for comprehensive coverage!
