# Wanfang Research & Verification Guide

## Scope
- Wanfang Data (万方数据)
- Supplementary source for Chinese literature

---

## QUICK REFERENCE

```
STEP 0: Break down topic into keywords
STEP 1: Research - Search and explore
STEP 2: Selection - Click → NEW TAB → Extract
STEP 3: Verification - Confirm 5 elements
```

---

## IMPORTANT: Search Order

1. **CNKI** - Primary source for Chinese
2. **PubMed** - Primary source for English
3. **Wanfang** - Supplementary (use only if needed)

---

## STEP 0: Break Down Topic

Same keywords as CNKI:
```bash
"Orem 自理模式 护理"
"动机行为转化理论 护理"
"股骨颈骨折 护理"
"糖尿病 护理"
```

---

## STEP 1: Research Phase

### 1.1 Open Wanfang
```bash
openclaw browser --browser-profile chrome open "https://www.wanfangdata.com.cn/"
```

### 1.2 Search
```bash
# Get refs FIRST
snapshot

# Search (find ref from snapshot)
type [search-ref] "Orem 自理模式" --submit

# Wait and snapshot
wait --load networkidle
snapshot
```

### 1.3 Record Findings
```
## Wanfang Search (Supplementary)
Keywords: Orem 自理模式 护理
Results: [number]

Relevant:
1. [Title] ([Journal], [Year])
```

---

## STEP 2: Selection Phase (NEW TAB!)

### 2.1 Click Article (Opens NEW TAB!)
```bash
click [article-ref]
```

### 2.2 SWITCH TO NEW TAB (Required!)
```bash
# List all tabs
tabs

# Focus on article tab
focus [article-tab-id]
```

### 2.3 Get Details
```bash
wait --load networkidle
snapshot
```

### 2.4 Extract Citation
```
**Title**: [Full Title]
**Authors**: [First 2-3], et al.
**Journal**: [Journal], [Year]
**URL**: https://www.wanfangdata.com.cn/details/...
```

---

## STEP 3: Verification Phase

### 3.1 Verify 5 Elements
```bash
# Find article tab
tabs
focus [article-tab-id]
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
Status: ✓✓✓✓✓
```

---

## TAB MANAGEMENT

| Command | Purpose |
|---------|----------|
| `tabs` | List all open tabs |
| `focus [tab-id]` | Switch to specific tab |
| `close [tab-id]` | Close a tab |

**Example:**
```bash
# List tabs
tabs
→ Tab 1: Search page
→ Tab 2: Article #1 (id: ABC123)

# Switch to article
focus ABC123

# Continue...
```

---

## RECORDING TEMPLATE

```markdown
# Literature Research Notes

## Topic
[Your topic]

## Wanfang Search (Supplementary)
Keywords: [keywords]
Results: [number]

### Selected References
| # | Title | Authors | Journal | Year |
|---|-------|---------|---------|------|
| 1 | [Title] | [Authors] | [Journal] | [Year] |

### #1 - VERIFIED ✓
**Title**: [Title]
**URL**: [wanfang-url]
Status: ✓✓✓✓✓
```

---

## TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| Can't find article | Check NEW TAB! |
| Multiple tabs open | Use `tabs` → `focus [id]` |
| No results | Simplify keywords or use CNKI |
| Abstract irrelevant | Mark FAILED, search again |

---

## GOLDEN RULES

1. Break down topic first → then search
2. snapshot → type → wait → snapshot (after EVERY change)
3. NEW TAB behavior - ALWAYS switch tabs after clicking!
4. Research → Select → THEN Verify
5. Record everything in research_notes.md
6. CNKI FIRST → PubMed SECOND → Wanfang LAST

---

## EXAMPLE SESSION

```bash
# 1. Search
open "https://www.wanfangdata.com.cn/"
snapshot
type [ref] "Orem 自理模式 护理" --submit
wait --load networkidle
snapshot
→ Found results!

# 2. Select - NEW TAB!
click [article-ref]
→ Opens NEW TAB!

# 3. Switch tabs
tabs
focus [ABC123]  # Article tab

# 4. Get details
wait --load networkidle
snapshot
→ Extract citation

# 5. Verify
wait --load networkidle
snapshot
→ Verify 5 elements
→ Record as VERIFIED
```
