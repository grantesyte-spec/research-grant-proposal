# CNKI Research & Verification Guide

## Scope
- China National Knowledge Infrastructure (CNKI)
- Primary source for Chinese nursing literature
- No VPN required

---

## PART A: RESEARCH PHASE (Required First)

### A1: Define Search Keywords

Based on the research topic, identify:
- **Core concepts**: Orem self-care model, nursing intervention
- **Population**: Hip fracture, diabetes, elderly
- **Outcome measures**: Self-care ability, glycemic control, recovery

**Example Keywords:**
```
Orem 自理模式 护理
股骨颈骨折 护理
糖尿病 护理
Orem 自理模式 糖尿病
动机行为转化理论 护理
```

### A2: Open CNKI
```bash
openclaw browser --browser-profile chrome open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92&rlang=CHINESE"
```

### A3: Search and Explore

```bash
# Get page snapshot to find refs
openclaw browser --browser-profile chrome snapshot --compact

# Try different keywords
openclaw browser --browser-profile chrome type e18 "Orem 自理模式 护理" --submit
openclaw browser --browser-profile chrome wait --load networkidle
openclaw browser --browser-profile chrome snapshot --compact
```

### A4: Record Initial Findings

**Create research_notes.md and record:**
- Keywords used
- Total results found
- Relevant article titles (don't cite yet - just explore)
- Journal names and years

**Example entry:**
```
## CNKI Search #1
Keywords: Orem 自理模式 护理
Results: 994 articles found

Relevant titles found:
1. 以奥瑞姆自理模式为基础的护理模式对急诊创伤骨折患者... (2025)
2. 基于循证支持的Orem自理模式干预对糖尿病合并精神分裂症... (2025)
...
```

---

##ION PHASE

 PART B: SELECT### B1: Click on Promising Articles

For each potentially relevant article:
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
- ✅ Publication date (Year)
- ✅ Volume, Issue (if available)
- ✅ Pages (if available)
- ✅ Abstract
- ✅ Verification URL

### B3: Add to Selected References

Update research_notes.md:
```markdown
## Selected CNKI References

### #1 - High Relevance
**Title**: [Full Title]
**Authors**: [First 2-3 authors], et al.
**Journal**: [Journal Name], [Year], [Vol]([Issue]): [Pages]
**URL**: https://kns.cnki.net/kcms/detail/detail.aspx?...
**Abstract**: [Paste abstract]
**Relevance**: HIGH - Directly addresses Orem model in [population]
```

---

## PART C: VERIFICATION PHASE (After Research Complete)

**BEFORE verification:**
- ✅ Research completed
- ✅ 10-15 references selected
- ✅ All saved in research_notes.md

### C1: Verify 5 Elements

For EACH selected reference:

```bash
# Open verification URL
openclaw browser --browser-profile chrome open "[verification-url]"
openclaw browser --browser-profile chrome snapshot --compact
```

**Check:**
```
✓ TOPIC: Does title match? YES/NO
✓ AUTHORS: Do first 2-3 authors match? YES/NO
✓ YEAR: Does year match? YES/NO
✓ ABSTRACT: Is abstract relevant to proposal? YES/NO
✓ URL: Can you access the article? YES/NO
```

### C2: Record Verification Result

```markdown
## CNKI Verification Results

### #1 - VERIFIED ✓

**Title**: [Title]
**Authors**: [Authors]
**Journal**: [Journal], [Year]

VERIFICATION RESULTS:
✓ TOPIC: YES - Matches hip fracture nursing
✓ AUTHORS: YES - Wang Y, Zhang X confirmed
✓ YEAR: YES - 2022 matches
✓ ABSTRACT: YES - Relevant to proposal
✓ URL: YES - Accessible

**Full Citation**:
[1] Wang Y, Zhang X, Liu J. Effects of nursing intervention on hip fracture[J]. 
    Chinese Journal of Nursing, 2022, 57(8): 1021-1026. 
    Verification URL: https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&...
```

---

## COMPLETE WORKFLOW

```
STEP 1: Research
  ├── A1: Define keywords
  ├── A2: Open CNKI
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

## 8-STEP QUICK REFERENCE

### Research Steps (1-4)
1. `open CNKI` - Open advanced search
2. `snapshot` - Get page refs
3. `type "keywords" --submit` - Search
4. `wait --load` - Wait for results
5. `snapshot` - Review results

### Selection Steps (5-6)
5. `click [article-ref]` - Open article
6. `wait --load → snapshot` - Get details

### Verification Steps (7-8)
7. `open [URL]` - Open verification URL
8. `verify 5 elements` - Confirm accuracy

---

## TROUBLESHOOTING

### No Results
- Simplify keywords
- Try broader terms
- Check spelling

### Can't Access Article
- Try different database (PubMed)
- Mark as unavailable

### Irrelevant Abstract
- Mark FAILED
- Continue searching

---

## GOLDEN RULE

```
Research FIRST → Select → THEN Verify
Never verify what you haven't found through research
```

---

## EXAMPLE: Complete CNKI Session

```bash
# Session 1: Initial Research
open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92"
type e18 "Orem 自理模式 护理" --submit
wait --load
snapshot
→ Record findings in research_notes.md

# Session 2: Select Articles  
click [article-ref-2]  # Click "Orem自理模式对急诊创伤骨折患者"
wait --load
snapshot
→ Extract citation, add to selected references

# Session 3: Verify
open "https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&filename=..."
snapshot
→ Verify 5 elements
→ Record as VERIFIED
```
