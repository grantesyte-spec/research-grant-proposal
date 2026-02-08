# CNKI Reference Verification Steps

## Scope
- China National Knowledge Infrastructure (CNKI)
- Chinese nursing research literature verification
- No VPN required

---

## CRITICAL: Research-First Workflow

**BEFORE verification, you MUST do research:**

```
1. Search CNKI for relevant literature
2. Record findings in research_notes.md
3. Select 10-15 quality references
4. THEN verify references
```

**NEVER verify references without doing research first.**

---

## Verification Goals

For EACH reference found during research, verify these 5 elements:
- ✅ **TOPIC**: Article matches research topic
- ✅ **AUTHORS**: At least first 2-3 authors correct
- ✅ **YEAR**: Publication year correct
- ✅ **ABSTRACT**: Abstract relevant to proposal
- ✅ **URL**: Verification URL accessible

---

## 8-Step Verification Process

### Step 1: Open CNKI Advanced Search
```bash
openclaw browser --browser-profile chrome open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92&rlang=CHINESE"
```

### Step 2: Get Page Snapshot (Find Element Refs)
```bash
openclaw browser --browser-profile chrome snapshot --compact
```
**Note**: Search box is typically `ref=e18`, Search button is `ref=e33`

### Step 3: Enter Search Keywords

**Recommended: Use type --submit**
```bash
openclaw browser --browser-profile chrome type [search-box-ref] "Orem 自理模式 糖尿病" --submit
```

### Step 4: Wait for Page Load (Critical!)
```bash
openclaw browser --browser-profile chrome wait --load networkidle
```

### Step 5: Get Search Results Snapshot
```bash
openclaw browser --browser-profile chrome snapshot --compact
```

**Success Indicators**:
- Result count visible (e.g., "共找到 75 条结果")
- Article list visible (title, authors, journal, date)

### Step 6: View Article Details
```bash
openclaw browser --browser-profile chrome click [article-ref]
openclaw browser --browser-profile chrome wait --load networkidle
openclaw browser --browser-profile chrome snapshot --compact
```

### Step 7: Extract Complete Information
From detail page, extract:
- ✅ Full title
- ✅ All authors (check "显示全部作者" link)
- ✅ Journal name
- ✅ Publication date
- ✅ Abstract (for relevance)
- ⚠️ Volume/Issue (if available)
- ⚠️ Pages (if available)
- Verification URL

### Step 8: Verify 5 Elements

```
[1] Authors. Title[J]. Journal, Year.

    VERIFICATION RESULTS:
    ✓ TOPIC: YES/NO (Title matches)
    ✓ AUTHORS: YES/NO (First 2-3 match)
    ✓ YEAR: YES/NO (Year matches)
    ✓ ABSTRACT: YES/NO (Relevant)
    ✓ URL: YES/NO (Accessible)
    
    Status: [VERIFIED] or [FAILED]
```

---

## Record Research Findings

After search, create `research_notes.md`:

```markdown
## CNKI Search Results
**Keywords**: [Search terms]
**Total Results**: [Number]

### Relevant Articles
| # | Title | Authors | Journal | Year | Relevance |
|---|-------|---------|---------|------|-----------|
| 1 | [Title] | [Authors] | [Journal] | [Year] | High |

### Selected for Proposal
- [1] Full citation with URL
```

---

## Troubleshooting

### Issue 1: No Search Results
**Solution**: Simplify keywords

### Issue 2: Element Ref Invalid  
**Solution**: Re-run `snapshot` to get new refs

### Issue 3: Refs Change After Navigation
**Cause**: "Refs are not stable across navigations"
**Solution**: Must re-run `snapshot` after any page change

### Issue 4: Abstract NOT Relevant
**Solution**: Mark FAILED → Search for replacement

---

## Golden Rule

```bash
snapshot → type --submit "keywords" → wait --load → snapshot → click → wait → snapshot → verify
```

---

## Important Notes

1. **Research FIRST**: Always do research before verification
2. **Document Everything**: Save findings to research_notes.md
3. **Wait Time**: Must `wait --load networkidle` after navigation
4. **Ref Changes**: Must re-snapshot after navigation
5. **Sequential**: Complete CNKI before PubMed/Wanfang
