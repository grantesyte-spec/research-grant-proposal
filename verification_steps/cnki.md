# CNKI Research & Verification Guide

## Scope
- China National Knowledge Infrastructure (CNKI)
- Primary source for Chinese nursing literature
- No VPN required

---

## QUICK REFERENCE

```
STEP 0: Break down topic into keywords
STEP 1: Research - Search and explore
STEP 2: Selection - Click and extract
STEP 3: Verification - Confirm 5 elements
```

---

## STEP 0: Break Down Topic

**Original Topic:**
```
基于动机行为转化理论的Orem自理模式支持在股骨颈骨折合并糖尿病患者护理中的应用
```

**Break Down:**
| # | Concept | Keywords |
|---|---------|----------|
| 1 | Theory | 动机行为转化理论 |
| 2 | Theory | Orem 自理模式 |
| 3 | Population | 股骨颈骨折、糖尿病 |
| 4 | Intervention | 护理、康复 |

**Search each concept:**
```bash
"Orem 自理模式 护理"     # 759 results
"动机行为转化理论 护理"   # 26 results
"股骨颈骨折 护理"        # [results]
"糖尿病 护理"           # [results]
```

---

## STEP 1: Research Phase

### 1.1 Open CNKI
```bash
openclaw browser --browser-profile chrome open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92&rlang=CHINESE"
```

### 1.2 Search
```bash
# Get refs FIRST
snapshot

# Search (typically ref=e18)
type e18 "Orem 自理模式" --submit

# Wait and snapshot
wait --load networkidle
snapshot
```

### 1.3 Record Findings
```
## CNKI Search Results
Keywords: Orem 自理模式 护理
Results: 759 articles found

Relevant:
1. [Title] ([Journal], [Year])
2. [Title] ([Journal], [Year])
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
**Authors**: [First 2-3], et al.
**Journal**: [Journal], [Year]
**URL**: https://kns.cnki.net/kcms/detail/detail.aspx?...
```

---

## STEP 3: Verification Phase

### 3.1 Verify 5 Elements
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

### 3.2 Record
```
## [1] VERIFIED ✓
Title: [Title]
Citation: Authors. Journal, Year.
Status: TOPIC✓ AUTHORS✓ YEAR✓ ABSTRACT✓ URL✓
```

---

## RECORDING TEMPLATE

```markdown
# Literature Research Notes

## Topic
[Your topic]

## CNKI Search
Keywords: [keywords]
Results: [number]

### Selected References
| # | Title | Authors | Journal | Year | Relevance |
|---|-------|---------|---------|------|-----------|
| 1 | [Title] | [Authors] | [Journal] | [Year] | High |

### #1 - VERIFIED ✓
**Title**: [Title]
**Authors**: [Authors]
**Journal**: [Journal], [Year]
Status: ✓✓✓✓✓
```

---

## TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| No results | Simplify keywords |
| Element ref not found | Re-run snapshot |
| Can't access article | Try different database |
| Irrelevant abstract | Mark FAILED, search again |

---

## GOLDEN RULES

1. Break down topic first → then search
2. snapshot → type → wait → snapshot (after EVERY change)
3. Research → Select → THEN Verify
4. Record everything in research_notes.md
5. Never verify what you haven't found

---

## EXAMPLE SESSION

```bash
# 1. Break down topic
# Keywords: Orem 自理模式 护理

# 2. Search
open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92"
snapshot
type e18 "Orem 自理模式" --submit
wait --load networkidle
snapshot
→ Found 759 results!

# 3. Select
click [article-ref]
wait --load networkidle
snapshot
→ Extract citation

# 4. Verify
open "[URL]"
wait --load networkidle
snapshot
→ Verify 5 elements
→ Record as VERIFIED
```
