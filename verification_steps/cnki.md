# CNKI Research & Verification Guide

## Scope
- China National Knowledge Infrastructure (CNKI)
- Primary source for Chinese nursing literature
- No VPN required

---

## PART A: RESEARCH PHASE (Required First)

### A1: Break Down Research Topic into Keywords

**CRITICAL LESSON**: Before searching, BREAK DOWN the topic into keywords!

**Original Topic:**
```
基于动机行为转化理论的Orem自理模式支持在股骨颈骨折合并糖尿病患者护理中的应用
```

**BREAK DOWN into Concepts:**
| Concept | Chinese | Alternative Keywords |
|---------|---------|---------------------|
| Theory 1 | 动机行为转化理论 | 行为改变理论、阶段变化理论 |
| Theory 2 | Orem自理模式 | Orem理论、自理理论、自护理论 |
| Population | 股骨颈骨折 | 髋部骨折、髋关节骨折、骨折 |
| Comorbidity | 糖尿病 | 血糖、高血糖、糖代谢 |
| Intervention | 护理 | 护理干预、康复护理、护理模式 |

**Strategy - Search Each Concept Separately:**
```
# Search each concept separately
1. 动机行为转化理论 护理
2. Orem 自理模式 护理
3. 股骨颈骨折 护理
4. 糖尿病 护理
5. 骨折 糖尿病
```

**Why Break Down?**
- Long complex queries → No results
- Individual concepts → More results
- Different combinations → Comprehensive coverage

### A2: Define Search Keywords

**LESSON FROM PRACTICE**: Start with SIMPLE keywords, not complex combinations.

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
1. Break down topic first (see A1)
2. Start with core concept: `Orem 自理模式`
3. If too many results, add ONE modifier
4. If no results, simplify, simplify, simplify!

**Example Keywords:**
```
# From topic breakdown - search each concept
动机行为转化理论 护理
Orem 自理模式 护理
股骨颈骨折 护理
糖尿病 护理

# Simple first (recommended)
Orem 自理模式
Orem 自理 护理
动机行为 转化 理论

# Add ONE modifier if needed
Orem 自理模式 糖尿病
Orem 自理模式 骨折
```

### A3: Open CNKI
```bash
openclaw browser --browser-profile chrome open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92&rlang=CHINESE"
```

### A4: Search and Explore

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

### A5: Record Initial Findings

**Create research_notes.md and record:**
- Keywords used (from topic breakdown)
- Total results found
- Relevant article titles
- Journal names and years

**Example entry:**
```
## CNKI Search - Topic Breakdown

### Concept 1: 动机行为转化理论 护理
Keywords: 动机行为转化理论 护理
Results: ~26 articles found

### Concept 2: Orem 自理模式 护理
Keywords: Orem 自理模式 护理
Results: 759 articles found

Relevant:
1. 以Orem自理模式为指导的延续性护理对2型糖尿病... (2024)
2. Orem自理模式理论对急诊创伤骨折患者... (2024)

### Concept 3: 股骨颈骨折 护理
Keywords: 股骨颈骨折 护理
Results: [results]

### Concept 4: 糖尿病 护理
Keywords: 糖尿病 护理
Results: [results]
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

# CRITICAL - Re-run snapshot!
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
STEP 0: BREAK DOWN TOPIC (NEW!)
  ├── Identify concepts in topic
  ├── Create keyword variations
  └── Search each concept separately

STEP 1: Research
  ├── A1: Break down topic
  ├── A2: Define keywords
  ├── A3: Open CNKI
  ├── A4: snapshot → type --submit → wait → snapshot
  └── A5: Record findings

STEP 2: Selection
  ├── B1: Click article → wait → snapshot
  ├── B2: Extract citations
  └── B3: Add to selected

STEP 3: Verification (After selection complete)
  ├── C1: Verify 5 elements
  └── C2: Record results
```

---

## LESSONS LEARNED (Updated from Practice)

### Lesson 1: Break Down Topic First
```
❌ WRONG: Search whole topic
"基于动机行为转化理论的Orem自理模式支持在股骨颈骨折合并糖尿病患者护理中的应用"

✅ RIGHT: Break down and search each concept
1. 动机行为转化理论 护理 → ~26 results
2. Orem 自理模式 护理 → 759 results
3. 股骨颈骨折 护理 → [results]
4. 糖尿病 护理 → [results]
```

### Lesson 2: Start with Simple Keywords
```
❌ WRONG: Complex keyword combination
"Orem 自理模式 股骨颈骨折 糖尿病"
→ No results, timeout, or error

✅ RIGHT: Start simple, add complexity
"Orem 自理模式" → 759 results!
```

### Lesson 3: Re-run Snapshot After Every Page Change
```bash
# ❌ WRONG - Using old ref
type e18 "keywords"
→ Error: Element "e18" not found

# ✅ RIGHT - Get new snapshot
snapshot  # Get new refs
type e18 "keywords"  # Use new ref
```

### Lesson 4: Wait for Network Idle
```bash
# ❌ WRONG - No wait
type "keywords" --submit
snapshot immediately

# ✅ RIGHT - Wait for load
type "keywords" --submit
wait --load networkidle
snapshot
```

### Lesson 5: If No Results, Simplify
```
# Strategy:
# 1. Remove modifiers (糖尿病, 骨折)
# 2. Use core concept only
# 3. Try alternative terms
```

---

## TOPIC BREAKDOWN TEMPLATE

**Original Topic:**
```
[Your research topic here]
```

**Break Down:**
| # | Concept | Chinese | Keywords |
|---|---------|---------|----------|
| 1 | Theory 1 | [Concept 1] | keyword1, keyword2 |
| 2 | Theory 2 | [Concept 2] | keyword3, keyword4 |
| 3 | Population | [Target population] | keyword5, keyword6 |
| 4 | Comorbidity | [Complications] | keyword7, keyword8 |
| 5 | Intervention | [Intervention type] | keyword9, keyword10 |

**Search Each:**
```bash
# Search each concept
1. keyword1  keyword3
2. keyword1  keyword5
3. keyword3  keyword5
4. keyword3  keyword7
...
```

---

## GOLDEN RULES

```
1. BREAK DOWN TOPIC first - then search
2. Start SIMPLE → Add complexity later
3. snapshot → type → wait → snapshot (after EVERY change)
4. Research FIRST → Select → THEN Verify
5. Record EVERYTHING in research_notes.md
6. Never verify what you haven't found
```

---

## EXAMPLE: Topic Breakdown

**Original Topic:**
```
基于动机行为转化理论的Orem自理模式支持在股骨颈骨折合并糖尿病患者护理中的应用
```

**Break Down:**
| # | Concept | Keywords |
|---|---------|----------|
| 1 | 动机行为转化理论 | 动机行为转化理论、行为改变理论 |
| 2 | Orem自理模式 | Orem自理模式、Orem理论、自理理论 |
| 3 | 股骨颈骨折 | 股骨颈骨折、髋部骨折、骨折 |
| 4 | 糖尿病 | 糖尿病、高血糖、糖代谢 |
| 5 | 护理干预 | 护理、康复护理、护理模式 |

**Search Combinations:**
```bash
1. "Orem 自理模式 护理" → 759 results ✓
2. "动机行为转化理论 护理" → 26 results ✓
3. "股骨颈骨折 护理" → [results]
4. "糖尿病 护理" → [results]
5. "骨折 糖尿病 护理" → [results]
```

---

## TROUBLESHOOTING

### Problem 1: No Results
```
Message: "抱歉，暂无数据，请稍后重试"
Solution: 
1. Break down topic first
2. Simplify keywords
3. Remove modifiers
4. Try: "Orem 自理模式" first
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

## EXAMPLE: Complete CNKI Session (from Practice)

```bash
# 1. BREAK DOWN TOPIC
# Topic: 基于动机行为转化理论的Orem自理模式支持在股骨颈骨折合并糖尿病患者护理中的应用
# Keywords:
# - 动机行为转化理论 护理
# - Orem 自理模式 护理
# - 股骨颈骨折 护理
# - 糖尿病 护理

# 2. Start with simple keyword
open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92"
snapshot
→ Found ref e18 for search box

# 3. Search each concept
type e18 "Orem 自理模式" --submit
wait --load networkidle
snapshot
→ Found 759 results!

# 4. Record findings
→ Added to research_notes.md

# 5. Search another concept
type e18 "动机行为转化理论 护理" --submit
wait --load networkidle
snapshot
→ Found 26 results

# 6. Select promising article
click [article-ref]
wait --load networkidle
snapshot
→ Extract citation

# 7. Verify (after selection complete)
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
