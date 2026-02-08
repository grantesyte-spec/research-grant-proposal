# CNKI Reference Verification Steps

## Scope
- China National Knowledge Infrastructure (CNKI)
- Chinese nursing research literature verification
- No VPN required

## Verification Goals
- ✅ TOPIC: Article matches research topic
- ✅ AUTHORS: At least first 2-3 authors correct
- ✅ YEAR: Publication year correct
- ⚠️ DOI: Some articles may not have DOI
- ⚠️ Volume/Issue/Pages: Obtain from detail page

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

**Option A: Use type + click separately**
```bash
openclaw browser --browser-profile chrome type [search-box-ref] "Orem 自理模式 糖尿病"
openclaw browser --browser-profile chrome click [search-button-ref]
```

**Option B: Use type --submit (Recommended)**
```bash
openclaw browser --browser-profile chrome type [search-box-ref] "Orem 自理模式 糖尿病" --submit
```
**Advantage**: Single command to input and submit search

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
# Click article title link
openclaw browser --browser-profile chrome click [article-ref]

# Wait for load
openclaw browser --browser-profile chrome wait --load networkidle

# Get detail page snapshot
openclaw browser --browser-profile chrome snapshot --compact
```

### Step 7: Extract Complete Article Information
From detail page, extract:
- ✅ Full title
- ✅ All authors (check "显示全部作者" link)
- ✅ Journal name
- ✅ Publication date (YYYY-MM-DD)
- ⚠️ Volume/Issue (e.g., "28(6)")
- ⚠️ Pages (e.g., "45-52")
- ⚠️ DOI (if available)

## Verification Result Format

```markdown
## [Number] [Pending/Verified]

**Title**: [Full Title]
- **Authors**: [First 3 authors, et al.]
- **Journal**: [Journal Name]
- **Publication Date**: [YYYY-MM-DD]
- **Citations**: [Number]
- **Verification Link**: [CNKI URL]
- **Status**: [TOPIC✓ AUTHORS✓ YEAR✓ VOL✓ PAGES✓ DOI✓]

**Manual Verification Links**:
- CNKI: https://kns.cnki.net/kcms2/article/abstract?[article_id]
- Google Scholar: https://scholar.google.com/scholar?q="Full Title"
```

## Troubleshooting

### Issue 1: No Search Results
**Symptom**: "抱歉，暂无数据，请稍后重试。"
**Solution**:
1. Simplify keywords (remove some terms)
2. Try: `Orem 自理模式` → `Orem 糖尿病` → `自理模式 糖尿病`
3. Check if captcha verification required

### Issue 2: Element Ref Invalid
**Symptom**: `Element "e18" not found`
**Solution**:
```bash
# Re-get page snapshot
openclaw browser --browser-profile chrome snapshot --compact
# Use new ref value
```

### Issue 3: Refs Change After Navigation
**Cause**: "Refs are not stable across navigations"
**Solution**: Must re-run `snapshot` after any page change

### Issue 4: Partial Author Information
**Cause**: Long author lists are collapsed by default
**Solution**: Click "显示全部作者" (Show All Authors) link

### Issue 5: Missing Volume/Pages/DOI
**Cause**: Some journal articles lack complete metadata
**Solution**:
1. Check HTML reading version
2. Use Google Scholar to supplement
3. Mark as `[Partially Verified]`

## Verification Checklist

After verification, confirm:

- [ ] Article accessible normally
- [ ] Title matches citation
- [ ] First 3 author names correct
- [ ] Journal name correct
- [ ] Publication year correct
- [ ] Volume/Issue obtained (if available)
- [ ] Page range obtained (if available)
- [ ] DOI obtained (if available)
- [ ] Verification URL accessible

## Important Notes

1. **Simplification Strategy**: Complex search queries may return no results
2. **Wait Time**: Must `wait --load networkidle` after page navigation
3. **Ref Changes**: Refs become invalid after navigation, must re-snapshot
4. **Captcha**: If captcha appears, may require manual handling
5. **Information Completeness**: Not all articles have complete DOI and page info
6. **--submit Option**: Use `type [ref] "keywords" --submit` for single-step input and search

## Golden Rule

```bash
snapshot → type --submit "keywords" → wait --load → snapshot
```

## Comparison: CNKI vs PubMed

| Aspect | CNKI | PubMed |
|--------|------|--------|
| **Search Method** | `type --submit` or `type` + `click` | Similar approach |
| **Primary ID** | None | PMID |
| **DOI Availability** | Sometimes missing | Usually available |
| **Language** | Chinese | English |
| **Nursing Coverage** | Strong | Very Strong |
| **Bot Detection** | Low | Medium |
