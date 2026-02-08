# Wanfang Research & Verification Guide

## Scope
- Wanfang Data (万方数据)
- Supplementary source for Chinese science & technology literature
- Use when CNKI results are insufficient

---

## IMPORTANT: Search Order

1. **CNKI** - Primary source for Chinese literature
2. **PubMed** - Primary source for English literature  
3. **Wanfang** - Supplementary (use only if needed)

---

## PART A: RESEARCH PHASE (Required First)

### A1: Define Search Keywords

Same keywords as CNKI search:
- Orem 自理模式 护理
- 股骨颈骨折 护理
- 糖尿病 护理
- 动机行为转化理论 护理

### A2: Open Wanfang
```bash
openclaw browser --browser-profile chrome open "https://www.wanfangdata.com.cn/"
```

### A3: Search and Explore

```bash
# Get page snapshot to find refs
openclaw browser --browser-profile chrome snapshot --compact

# Search (find search box ref)
openclaw browser --browser-profile chrome type [search-ref] "Orem 自理模式 护理" --submit
openclaw browser --browser-profile chrome wait --load networkidle
openclaw browser --browser-profile chrome snapshot --compact
```

### A4: Record Initial Findings

**Create research_notes.md:**
```
## Wanfang Search #1 (Supplementary)
Keywords: Orem 自理模式 护理
Results: [Number] articles found

Relevant titles:
1. [Title] ([Journal], [Year])
2. [Title] ([Journal], [Year])
...
```

---

## PART B: SELECTION PHASE

### B1: Click on Promising Articles

**CRITICAL: Opens in NEW TAB!**
```bash
openclaw browser --browser-profile chrome click [article-ref]
```

### B2: SWITCH TO NEW TAB (Required!)
```bash
# List all tabs
openclaw browser --browser-profile chrome tabs

# Output:
# 1. Google  https://...  id: FB0A51FD...
# 2. Wanfang  https://...  id: 5C56321A...
# 3. (untitled)  https://...article-detail/...  id: ABC12345...

# Focus on article tab
openclaw browser --browser-profile chrome focus [article-tab-id]
```

### B3: Get Article Details
```bash
openclaw browser --browser-profile chrome wait --load networkidle
openclaw browser --browser-profile chrome snapshot --compact
```

### B4: Extract Full Citation

Extract:
- ✅ Full title
- ✅ Authors
- ✅ Journal name
- ✅ Publication date
- ✅ Volume, Issue, Pages
- ✅ Abstract
- ✅ Verification URL

### B5: Add to Selected References

```markdown
## Selected Wanfang References (Supplementary)

### #1 - Medium Relevance
**Title**: [Full Title]
**Authors**: [First 2-3], et al.
**Journal**: [Journal Name], [Year], [Vol]([Issue]): [Pages]
**URL**: https://www.wanfangdata.com.cn/details/article-detail/...
**Abstract**: [Paste abstract]
**Relevance**: MEDIUM - Addresses [aspect]
**Note**: Supplementary to CNKI results
```

---

## PART C: VERIFICATION PHASE (After Research Complete)

**BEFORE verification:**
- ✅ CNKI search completed
- ✅ PubMed search completed  
- ✅ Wanfang search completed (supplementary)
- ✅ 10-15 references selected

### C1: Verify 5 Elements

```bash
# Find the verification URL in your research_notes.md
openclaw browser --browser-profile chrome open "[verification-url]"

# If article is in new tab
tabs
focus [article-tab-id]
wait --load
snapshot
```

**Check:**
```
✓ TOPIC: Does title match? YES/NO
✓ AUTHORS: Do first 2-3 authors match? YES/NO
✓ YEAR: Does year match? YES/NO
✓ ABSTRACT: Is abstract relevant? YES/NO
✓ URL: Can you access? YES/NO
```

### C2: Record Verification

```markdown
## Wanfang Verification Results

### #1 - VERIFIED ✓

**Title**: [Title]
**Authors**: [Authors]
**Journal**: [Journal], [Year]

VERIFICATION RESULTS:
✓ TOPIC: YES
✓ AUTHORS: YES
✓ YEAR: YES
✓ ABSTRACT: YES
✓ URL: YES

**Full Citation**:
[1] Authors. Title[J]. Journal Name, Year, Vol(Issue): Pages. 
    Verification URL: https://www.wanfangdata.com.cn/details/article-detail/...
```

---

## TAB MANAGEMENT

### List All Tabs
```bash
openclaw browser --browser-profile chrome tabs
```

### Switch Tabs
```bash
openclaw browser --browser-profile chrome focus [tab-id]
```

### Close Tabs
```bash
openclaw browser --browser-profile chrome close [tab-id]
```

### Keep Track
```
Tab 1: Search page
Tab 2: Article #1
Tab 3: Article #2
```

---

## COMPLETE WORKFLOW

```
STEP 1: Research (CNKI & PubMed FIRST)
  ├── CNKI: Search, explore, record
  ├── PubMed: Search, explore, record
  └── Wanfang: Only if needed

STEP 2: Selection
  ├── Click promising articles
  ├── SWITCH TO NEW TAB
  ├── Extract citations
  └── Add to selected references

STEP 3: Verification (After ALL selection complete)
  ├── Verify each reference
  └── Record results
```

---

## 8-STEP QUICK REFERENCE

### Research Steps (1-4)
1. `open Wanfang` - Open homepage
2. `snapshot` - Get refs
3. `type --submit` - Search
4. `wait --load → snapshot` - Review results

### Selection Steps (5-6)
5. `click article` → opens NEW TAB
6. `tabs → focus [new-tab-id] → wait → snapshot` - Get details

### Verification Steps (7-8)
7. `open [URL]` or `tabs → focus → snapshot`
8. `verify 5 elements` - Confirm accuracy

---

## TROUBLESHOOTING

### Can't Find Article
- Cause: Still on search tab, not article tab
- Fix: `tabs` → `focus [article-tab-id]`

### Multiple Tabs Open
- Solution: Clean up unused tabs
- `tabs` → `close [unwanted-tab-id]`

### No Results
- Solution: Simplify keywords
- Use CNKI instead

### Abstract Not Relevant
- Solution: Mark FAILED
- This is supplementary source anyway

---

## GOLDEN RULE

```
CNKI FIRST → PubMed SECOND → Wanfang LAST (if needed)
NEVER verify what you haven't found through research
NEW TAB behavior - ALWAYS switch tabs after clicking!
```

---

## EXAMPLE: Complete Wanfang Session

```bash
# After CNKI and PubMed searches are done...

# Session 1: Wanfang Research (Supplementary)
open "https://www.wanfangdata.com.cn/"
type [ref] "Orem 自理模式 护理" --submit
wait --load
snapshot
→ Record findings (supplementary only)

# Session 2: Selection
click [article-ref]  # Opens NEW TAB!
tabs
focus [ABC12345]  # Switch to article tab
wait --load
snapshot
→ Extract citation, add to selected

# Session 3: Verification
tabs
focus [article-tab-id]  # Go back to article
snapshot
→ Verify 5 elements
→ Record as VERIFIED
```

---

## COMPARISON TABLE

| Aspect | CNKI | Wanfang | PubMed |
|--------|------|---------|--------|
| **Priority** | 1st (Chinese) | 3rd (Supplementary) | 2nd (English) |
| **Tab Behavior** | Same tab | **NEW TAB** ⚠️ | Same tab |
| **Tab Management** | Not needed | Required | Not needed |
| **Coverage** | Chinese journals | Chinese journals | English journals |
| **Use When** | First choice | CNKI insufficient | For English lit |

---

## KEY DIFFERENCES FROM CNKI

1. **NEW TAB behavior** - Must switch tabs after clicking
2. **Supplementary only** - Use CNKI first
3. **Less familiar** - May need more exploration
4. **Tab cleanup** - More important here
