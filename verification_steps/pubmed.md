# PubMed Research & Verification Guide

## Scope
- PubMed (NCBI - National Center for Biotechnology Information)
- Primary source for English biomedical and nursing literature
- Use `openclaw browser` for verification

---

## PART A: RESEARCH PHASE (Required First)

### A1: Break Down Research Topic into Keywords

**CRITICAL LESSON**: Before searching, BREAK DOWN the topic into keywords!

**Original Topic:**
```
Application of Orem Self-Care Model based on Transtheoretical Model in Nursing Care of Hip Fracture Patients with Diabetes
```

**BREAK DOWN into Concepts:**
| Concept | English | Alternative Keywords |
|---------|---------|---------------------|
| Theory 1 | Transtheoretical Model | stages of change, TTM, behavior change |
| Theory 2 | Orem Self-Care Model | Orem theory, self-care, self-management |
| Population | Hip fracture | hip fracture, femoral neck fracture, elderly |
| Comorbidity | Diabetes | diabetes, diabetic, glycemic control |
| Intervention | Nursing | nursing, nursing intervention, rehabilitation |

**Strategy - Search Each Concept Separately:**
```
# Search each concept separately
1. transtheoretical model nursing
2. orem self-care model nursing
3. hip fracture elderly rehabilitation
4. diabetes elderly nursing
5. nursing intervention elderly fracture
```

**Why Break Down?**
- Long complex queries → No results
- Individual concepts → More results
- Different combinations → Comprehensive coverage

### A2: Define Search Keywords

**LESSON FROM PRACTICE**: Start with simple concepts, then combine.

**Example Keywords (from topic breakdown):**
```
# From topic breakdown - search each concept
transtheoretical model nursing
orem self-care model nursing
hip fracture elderly rehabilitation
diabetes elderly nursing

# Simple first (recommended)
oren self-care model nursing
transtheoretical model
self-care elderly

# Add modifiers if needed
oren self-care model diabetes
transtheoretical model elderly rehabilitation
```

### A3: Open PubMed
```bash
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/"
```

### A4: Search and Explore

**IMPORTANT LESSON**: Same as CNKI - Re-run snapshot after EVERY change!

```bash
# Step 1: Open PubMed
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/"

# Step 2: CRITICAL - Get page snapshot FIRST
openclaw browser --browser-profile chrome snapshot --compact

# Step 3: Find search box ref (typically e14)
# Look for "combobox" or input field

# Step 4: Type and submit
openclaw browser --browser-profile chrome type e14 "oren self-care model nursing" --submit

# Step 5: CRITICAL - Wait for load
openclaw browser --browser-profile chrome wait --load networkidle

# Step 6: CRITICAL - Re-run snapshot!
openclaw browser --browser-profile chrome snapshot --compact
```

### A5: Record Initial Findings

**Create research_notes.md:**
```
## PubMed Search - Topic Breakdown

### Concept 1: transtheoretical model nursing
Keywords: transtheoretical model nursing
Results: ~171 articles found

### Concept 2: orem self-care model nursing
Keywords: orem self-care model nursing
Results: 77,273 articles found

### Concept 3: hip fracture elderly rehabilitation
Keywords: hip fracture elderly rehabilitation
Results: [results]

### Concept 4: diabetes elderly nursing
Keywords: diabetes elderly nursing
Results: [results]

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

# CRITICAL - Wait and snapshot
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
STEP 0: BREAK DOWN TOPIC (NEW!)
  ├── Identify concepts in topic
  ├── Create keyword variations
  └── Search each concept separately

STEP 1: Research
  ├── A1: Break down topic
  ├── A2: Define keywords
  ├── A3: Open PubMed
  ├── A4: snapshot → type --submit → wait → snapshot
  └── A5: Record findings

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

### Lesson 1: Break Down Topic First
```
❌ WRONG: Search whole topic
"Application of Orem Self-Care Model based on Transtheoretical Model in Nursing Care of Hip Fracture Patients with Diabetes"

✅ RIGHT: Break down and search each concept
1. "oren self-care model nursing" → 77,273 results ✓
2. "transtheoretical model nursing" → [results]
3. "hip fracture elderly rehabilitation" → [results]
```

### Lesson 2: PMID is Reliable Identifier
```
✅ BEST - Use PMID directly
open "https://pubmed.ncbi.nlm.nih.gov/30866078/"
→ Always works

✅ GOOD - Use DOI
open "https://doi.org/10.1111/scs.12670"
→ Works if DOI is valid
```

### Lesson 3: PubMed Returns More Results
```
CNKI: 759 results for "Orem 自理模式"
PubMed: 77,273 results for "oren self-care model nursing"
→ PubMed has more English literature
→ CNKI has more Chinese literature
→ Use BOTH databases!
```

### Lesson 4: Same Snapshot Rule Applies
```
❌ WRONG - Skip snapshot
type e14 "keywords" --submit
→ Error: Element "e14" not found

✅ RIGHT - Snapshot first
snapshot
type e14 "keywords" --submit
wait --load
snapshot
```

### Lesson 5: Transtheoretical Model Keywords
```
# Working searches:
"oren self-care model nursing" → 77,273 results
"transtheoretical model nursing" → [results]
"nursing theory-guided practice" → Many results
"behavior change elderly rehabilitation" → [results]
```

---

## TOPIC BREAKDOWN TEMPLATE

**Original Topic:**
```
[Your research topic here]
```

**Break Down:**
| # | Concept | English | Keywords |
|---|---------|---------|----------|
| 1 | Theory 1 | [Concept 1] | keyword1, keyword2 |
| 2 | Theory 2 | [Concept 2] | keyword3, keyword4 |
| 3 | Population | [Target population] | keyword5, keyword6 |
| 4 | Comorbidity | [Complications] | keyword7, keyword8 |
| 5 | Intervention | [Intervention type] | keyword9, keyword10 |

**Search Combinations:**
```bash
# Search each concept
1. keyword1 keyword3
2. keyword1 keyword5
3. keyword3 keyword5
4. keyword3 keyword7
...
```

---

## GOLDEN RULES

```
1. BREAK DOWN TOPIC first - then search
2. Start SIMPLE → Add complexity
3. snapshot → type → wait → snapshot (always!)
4. Use PMID for verification (most reliable)
5. Research FIRST → Select → THEN Verify
6. Record EVERYTHING in research_notes.md
7. Use BOTH CNKI and PubMed for comprehensive coverage
```

---

## EXAMPLE: Topic Breakdown

**Original Topic:**
```
Application of Orem Self-Care Model based on Transtheoretical Model in Nursing Care of Hip Fracture Patients with Diabetes
```

**Break Down:**
| # | Concept | Keywords |
|---|---------|----------|
| 1 | Transtheoretical Model | transtheoretical model, TTM, stages of change |
| 2 | Orem Self-Care Model | orem self-care model, self-management |
| 3 | Hip Fracture | hip fracture, femoral neck fracture, elderly |
| 4 | Diabetes | diabetes, diabetic, glycemic control |
| 5 | Nursing | nursing, rehabilitation nursing |

**Search Combinations:**
```bash
1. "oren self-care model nursing" → 77,273 results ✓
2. "transtheoretical model nursing" → [results]
3. "hip fracture elderly rehabilitation" → [results]
4. "diabetes elderly nursing" → [results]
5. "transtheoretical model oren self-care" → [results]
```

---

## EXAMPLE: Complete PubMed Session (from Practice)

```bash
# 1. BREAK DOWN TOPIC
# Topic: Application of Orem Self-Care Model based on Transtheoretical Model in Nursing Care of Hip Fracture Patients with Diabetes
# Keywords:
# - orem self-care model nursing
# - transtheoretical model nursing
# - hip fracture elderly rehabilitation
# - diabetes elderly nursing

# 2. Search with simple keywords
open "https://pubmed.ncbi.nlm.nih.gov/"
snapshot
→ Found ref e14 for search box

# 3. Search each concept
type e14 "oren self-care model nursing" --submit
wait --load networkidle
snapshot
→ Found 77,273 results!

# 4. Found highly relevant article
# "Usefulness of nursing theory-guided practice" (PMID: 30866078)

# 5. Verify using PMID (most reliable)
open "https://pubmed.ncbi.nlm.nih.gov/30866078/"
wait --load networkidle
snapshot
→ Verified 5 elements
→ Recorded as VERIFIED

# 6. Search for TTM literature
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
1. Break down topic first
2. Simplify keywords
3. Check spelling
4. Try alternative terms
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

## COMMON REF PATTERNS

| Element | Typical Ref |
|---------|------------|
| Search box | e14, e13 |
| Search button | e15, e16 |
| Article link | varies |

**Remember**: Refs CHANGE after navigation. Always re-snapshot!
