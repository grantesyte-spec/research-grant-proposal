# PubMed Research & Verification Guide

## Scope
- PubMed (NCBI - National Center for Biotechnology Information)
- Primary source for English biomedical and nursing literature

---

## QUICK REFERENCE

```
STEP 0: Break down topic into keywords
STEP 1: Research - Search and explore  
STEP 2: Selection - Click and extract
STEP 3: Verification - Confirm 5 elements (use PMID)
```

---

## STEP 0: Break Down Topic

**Original Topic:**
```
Application of Orem Self-Care Model based on Transtheoretical Model in Nursing Care of Hip Fracture Patients with Diabetes
```

**Break Down:**
| # | Concept | Keywords |
|---|---------|----------|
| 1 | Theory | transtheoretical model, TTM |
| 2 | Theory | orem self-care model |
| 3 | Population | hip fracture, elderly |
| 4 | Comorbidity | diabetes, glycemic control |
| 5 | Intervention | nursing, rehabilitation |

**Search each concept:**
```bash
"oren self-care model nursing"      # 77,273 results
"transtheoretical model nursing"    # [results]
"hip fracture elderly rehabilitation" # [results]
```

---

## STEP 1: Research Phase

### 1.1 Open PubMed
```bash
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/"
```

### 1.2 Search
```bash
# Get refs FIRST
snapshot

# Search (typically ref=e14)
type e14 "oren self-care model nursing" --submit

# Wait and snapshot
wait --load networkidle
snapshot
```

### 1.3 Record Findings
```
## PubMed Search
Keywords: oren self-care model nursing
Results: 77,273 articles

Relevant:
1. [Title] (PMID: [PMID], [Year])
2. [Title] (PMID: [PMID], [Year])
```

---

## STEP 2: Selection Phase

### 2.1 Click Article
```bash
click [article-ref]
wait --load networkidle
snapshot
```

### 2.2 Extract Citation
```
**Title**: [Full Title]
**PMID**: [PMID Number]
**Authors**: [First 2-3], et al.
**Journal**: [Journal], [Year]
**URL**: https://pubmed.ncbi.nlm.nih.gov/[PMID]/
```

---

## STEP 3: Verification Phase

### 3.1 Verify 5 Elements (use PMID - most reliable!)
```bash
# Best: Use PMID directly
open "https://pubmed.ncbi.nlm.nih.gov/[PMID]/"

# Wait and snapshot
wait --load networkidle
snapshot
```

**Check:**
```
✓ TOPIC: Title matches? YES/NO
✓ AUTHORS: First 2-3 match? YES/NO
✓ YEAR: Year matches? YES/NO
✓ ABSTRACT: Relevant? YES/NO
✓ PMID: Correct? YES/NO
```

### 3.2 Record
```
## [1] VERIFIED ✓
Title: [Title]
PMID: [PMID]
Citation: Authors. Journal, Year.
Status: ✓✓✓✓✓
```

---

## RECORDING TEMPLATE

```markdown
# Literature Research Notes

## Topic
[Your topic]

## PubMed Search
Keywords: [keywords]
Results: [number]

### Selected References
| # | Title | PMID | Authors | Journal | Year |
|---|-------|------|---------|---------|------|
| 1 | [Title] | [PMID] | [Authors] | [Journal] | [Year] |

### #1 - VERIFIED ✓
**Title**: [Title]
**PMID**: [PMID]
**Authors**: [Authors]
**Journal**: [Journal], [Year]
Status: ✓✓✓✓✓
```

---

## PUBMED ADVANTAGES

| Feature | PubMed | CNKI |
|---------|--------|------|
| Results Count | More (77K+) | Fewer (759+) |
| Identifier | PMID (reliable) | No standard ID |
| English Coverage | ✅ Excellent | Limited |
| Chinese Coverage | Limited | ✅ Excellent |

**Strategy**: Use BOTH databases!

---

## TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| Tab disappears | Use PMID URL directly |
| No results | Simplify keywords |
| Element ref not found | Re-run snapshot |
| Can't find article | Search by PMID |

---

## GOLDEN RULES

1. Break down topic first → then search
2. snapshot → type → wait → snapshot (after EVERY change)
3. Use PMID for verification (most reliable)
4. Research → Select → THEN Verify
5. Record everything in research_notes.md

---

## EXAMPLE SESSION

```bash
# 1. Break down topic
# Keywords: oren self-care model nursing

# 2. Search
open "https://pubmed.ncbi.nlm.nih.gov/"
snapshot
type e14 "oren self-care model nursing" --submit
wait --load networkidle
snapshot
→ Found 77,273 results!

# 3. Found relevant article
# "Usefulness of nursing theory-guided practice" (PMID: 30866078)

# 4. Verify by PMID (most reliable)
open "https://pubmed.ncbi.nlm.nih.gov/30866078/"
wait --load networkidle
snapshot
→ Verify 5 elements
→ Record as VERIFIED
```
