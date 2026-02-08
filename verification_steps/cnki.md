# CNKI Research & Verification Guide

## Scope
- China National Knowledge Infrastructure (CNKI)
- Primary source for Chinese nursing literature
- No VPN required

---

## PART A: RESEARCH PHASE (Required First)

### A1: Define Search Keywords

**CRITICAL LESSON**: Start with SIMPLE keywords, not complex combinations.

**WRONG** (failed in practice):
```
"Orem 自理模式 股骨颈骨折 糖尿病"
→ Result: "抱歉，暂无数据，请稍后重试"
```

**RIGHT** (success in practice):
```
"Orem 自理模式"
→ Result: 759 articles found
```

**Strategy:**
1. Start with core concept: `Orem 自理模式`
2. If too many results, add ONE modifier
3. If no results, simplify, simplify, simplify!

**Example Keywords:**
```
# Simple first (recommended)
Orem 自理模式
Orem 自理 护理
动机行为 转化 理论

# Add ONE modifier if needed
Orem 自理模式 糖尿病
Orem 自理模式 骨折
```

### A2: Open CNKI
```bash
openclaw browser --browser-profile chrome open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92&rlang=CHINESE"
```

### A3: Search and Explore

**IMPORTANT LESSON**: After EVERY page change, you MUST re-run snapshot!

```bash
# Step 1: Open CNKI
openclaw browser --browser-profile chrome open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92&rlang=CHINESE"

# Step 2: CRITICAL - Get page snapshot FIRST
openclaw browser --browser-profile chrome snapshot --compact

# Step 3: Find the search box ref (typically e18)
# Look for "textbox" or input field

# Step 4: Type and submit
openclaw browser --browser-profile chrome type e18 "Orem 自理模式" --submit

# Step 5: CRITICAL - Wait for page to load
openclaw browser --browser-profile chrome wait --load networkidle

# Step 6: CRITICAL - Re-run snapshot after page change!
openclaw browser --browser-profile chrome snapshot --compact
```

**Why Re-run Snapshot?**
- "Refs are not stable across navigations"
- Element refs change after each page load
- Without new snapshot, you'll get: `Error: Element "e18" not found`

### A4: Record Initial Findings

**Create research_notes.md and record:**
- Keywords used
- Total results found
- Relevant article titles
- Journal names and years

**Example entry:**
```
## CNKI Search #1
Keywords: Orem 自理模式
Results: 759 articles found

Relevant titles:
1. 以Orem自理模式为指导的延续性护理对2型糖尿病... (2024)
2. Orem自理模式理论对急诊创伤骨折患者... (2024)
3. 奥伦自理模式在糖尿病肾病患者护理中的应用... (2024)
```

---

## PART B: SELECTION PHASE

### B1: Click on Promising Articles

```bash
# Click article link (typically opens in same tab)
openclaw browser --browser-profile chrome click [article-ref]

# CRITICAL - Wait for load
openclaw browser --browser-profile chrome wait --load networkidle

# CRITICAL - Re-run snapshot!
openclaw browser --browser-profile chrome snapshot --compact
```

### B2: Extract Full Citation Information

From article detail page, extract:
- ✅ Full title
- ✅ Authors (first 2-3)
- ✅ Journal name
- ✅ Publication year
- ✅ Volume, Issue, Pages
- ✅ Abstract
- ✅ Verification URL (copy from browser)

### B3: Add to Selected References

```markdown
## Selected CNKI References

### #1 - High Relevance
**Title**: [Full Title]
**Authors**: [First 2-3 authors], et al.
**Journal**: [Journal Name], [Year], [Vol]([Issue]): [Pages]
**URL**: https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&...
**Relevance**: HIGH - Addresses Orem model in [population]
```

---

## PART C: VERIFICATION PHASE (After Research Complete)

**BEFORE verification:**
- ✅ Research completed (searched and explored)
- ✅ 10-15 references selected
- ✅ All saved in research_notes.md

### C1: Verify 5 Elements

```bash
# Open the verification URL you saved
openclaw browser --browser-profile chrome open "[verification-url]"

# Wait for load
openclaw browser --browser-profile chrome wait --load networkidle

# Re-run snapshot
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
✓ TOPIC: YES - Matches research topic
✓ AUTHORS: YES - Wang Y, Zhang X confirmed
✓ YEAR: YES - 2024 matches
✓ ABSTRACT: YES - Relevant to proposal
✓ URL: YES - Accessible

**Full Citation**:
[1] Authors. Title[J]. Journal, Year, Vol(Issue): Pages. 
    Verification URL: https://kns.cnki.net/kcms/detail/detail.aspx?...
```

---

## COMPLETE WORKFLOW

```
STEP 1: Research
  ├── A1: Start with SIMPLE keywords
  ├── A2: Open CNKI
  ├── A3: snapshot → type --submit → wait → snapshot
  └── A4: Record findings

STEP 2: Selection
  ├── B1: Click article → wait → snapshot
  ├── B2: Extract citations
  └── B3: Add to selected

STEP 3: Verification (Only AFTER selection complete)
  ├── C1: Verify 5 elements
  └── C2: Record results
```

---

## LESSONS LEARNED (Updated from Practice)

### Lesson 1: Start with Simple Keywords
```
❌ WRONG: "Orem 自理模式 股骨颈骨折 糖尿病"
→ No results, timeout, or error

✅ RIGHT: "Orem 自理模式" 
→ 759 results found!
```

### Lesson 2: Re-run Snapshot After Every Page Change
```bash
# ❌ WRONG - Using old ref
type e18 "keywords"
→ Error: Element "e18" not found

# ✅ RIGHT - Get new snapshot
snapshot  # Get new refs
type e18 "keywords"  # Use new ref
```

### Lesson 3: Wait for Network Idle
```bash
# ❌ WRONG - No wait
type "keywords" --submit
snapshot immediately

# ✅ RIGHT - Wait for load
type "keywords" --submit
wait --load networkidle
snapshot
```

### Lesson 4: If No Results, Simplify
```
# Strategy:
# 1. Remove modifiers (糖尿病, 骨折)
# 2. Use core concept only
# 3. Try alternative terms
```

---

## TROUBLESHOOTING

### Problem 1: No Results
```
Message: "抱歉，暂无数据，请稍后重试"
Solution: 
1. Simplify keywords
2. Remove modifiers
3. Try: "Orem 自理模式" first
```

### Problem 2: Element Ref Invalid
```
Error: Element "e18" not found
Solution:
1. Re-run: openclaw browser --browser-profile chrome snapshot --compact
2. Use new ref from snapshot
3. NEVER use old refs after page navigation
```

### Problem 3: Can't Find Search Box
```
Solution:
1. Run snapshot again
2. Look for "textbox" in output
3. Try different refs (e18, e17, e16...)
```

### Problem 4: Page Didn't Load
```
Solution:
1. Check wait --load networkidle
2. Increase wait time
3. Refresh page
```

---

## GOLDEN RULES

```
1. Start SIMPLE → Add complexity later
2. snapshot → type → wait → snapshot (after EVERY change)
3. Research FIRST → Select → THEN Verify
4. Record EVERYTHING in research_notes.md
5. Never verify what you haven't found
```

---

## EXAMPLE: Complete CNKI Session (from Practice)

```bash
# 1. Start with simple keywords
open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92"
snapshot
→ Found ref e18 for search box

# 2. Search with simple term
type e18 "Orem 自理模式" --submit
wait --load networkidle
snapshot
→ Found 759 results!

# 3. Record findings
→ Added to research_notes.md

# 4. Select promising article
click [article-ref]
wait --load networkidle
snapshot
→ Extract citation

# 5. Verify (after selection complete)
open "[verification-url]"
wait --load networkidle
snapshot
→ Verify 5 elements
→ Record as VERIFIED
```

---

## COMMON REF PATTERNS

| Element | Typical Ref |
|---------|------------|
| Search box | e18, e17, e16 |
| Search button | e9, e33 |
| Article title | varies |

**Remember**: Refs CHANGE after navigation. Always re-snapshot!
