# CNKI Reference Verification Steps

## Scope
- China National Knowledge Infrastructure (CNKI)
- Chinese nursing research literature verification
- No VPN required

## Verification Goals

For EACH reference, verify these 5 elements:
- ✅ **TOPIC**: Article matches research topic (title matches proposal theme)
- ✅ **AUTHORS**: At least first 2-3 authors correct
- ✅ **YEAR**: Publication year correct
- ✅ **ABSTRACT**: Article abstract is relevant to proposal
- ⚠️ DOI: Some articles may not have DOI
- ⚠️ Volume/Issue/Pages: Obtain from detail page

## 5-Element Verification Checklist

```
✓ TOPIC: Title matches research topic
✓ AUTHORS: First 2-3 authors match citation
✓ YEAR: Publication year matches
✓ ABSTRACT: Content is relevant to proposal
   - Does the abstract discuss the same population?
   - Does the abstract address the same intervention?
   - Does the abstract measure similar outcomes?
   - If NOT relevant → Mark FAILED → Search again
```

## If Abstract is NOT Relevant → FAILED

When abstract does NOT match proposal:
1. Mark reference as **FAILED**
2. Document why:
   ```
   FAILED REASON: Abstract discusses [X] but proposal needs [Y]
   ```
3. Search for replacement article
4. Re-verify ALL references from beginning

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
- ✅ **Abstract** (for relevance verification)
- ⚠️ Volume/Issue (e.g., "28(6)")
- ⚠️ Pages (e.g., "45-52")
- ⚠️ DOI (if available)

### Step 8: Verify 5 Elements

**Template**:
```
[1] Authors. Title[J]. Journal, Year.
    
    VERIFICATION RESULTS:
    ✓ TOPIC: YES/NO (Title matches research topic)
    ✓ AUTHORS: YES/NO (First 2-3 authors match)
    ✓ YEAR: YES/NO (Year matches)
    ✓ ABSTRACT: YES/NO (Content relevant to proposal)
    
    If ANY is NO → FAILED → Search again
```

## Verification Result Format

```markdown
## [Number] [VERIFIED/FAILED]

**Title**: [Full Title]
- **Authors**: [First 3 authors, et al.]
- **Journal**: [Journal Name]
- **Publication Date**: [YYYY-MM-DD]
- **Abstract**: [First 2-3 sentences...]
- **Relevance Check**:
  - Population matches: YES/NO
  - Intervention matches: YES/NO
  - Outcomes match: YES/NO
- **Status**: [TOPIC✓ AUTHORS✓ YEAR✓ ABSTRACT✓] or [FAILED]
- **If FAILED**: [Reason and replacement search needed]

**Failed Example**:
[3] Authors. Title[J]. Journal, 2019.
    FAILED: Abstract discusses elderly hypertension, 
    but proposal focuses on hip fracture with diabetes.
    → REPLACEMENT SEARCH NEEDED
```

## Troubleshooting

### Issue 1: Abstract NOT Relevant
**Symptom**: Article discusses different population/intervention
**Solution**:
1. Mark as FAILED
2. Document why not relevant
3. Search for replacement
4. Re-verify ALL references

### Issue 2: No Search Results
**Symptom**: "抱歉，暂无数据，请稍后重试。"
**Solution**:
1. Simplify keywords
2. Remove some terms
3. Try: `Orem 自理模式` → `Orem 糖尿病`

### Issue 3: Element Ref Invalid
**Symptom**: `Element "e18" not found`
**Solution**:
```bash
openclaw browser --browser-profile chrome snapshot --compact
# Use new ref value
```

### Issue 4: Refs Change After Navigation
**Cause**: "Refs are not stable across navigations"
**Solution**: Must re-run `snapshot` after any page change

## Verification Checklist

After verification, confirm:

- [ ] Article accessible normally
- [ ] **TOPIC**: Title matches proposal theme
- [ ] **AUTHORS**: First 3 author names correct
- [ ] **YEAR**: Publication year correct
- [ ] **ABSTRACT**: Content relevant to proposal
  - [ ] Same population
  - [ ] Same/similar intervention
  - [ ] Similar outcomes measured
- [ ] Volume/Issue obtained (if available)
- [ ] Page range obtained (if available)
- [ ] DOI obtained (if available)

## Important Notes

1. **5 Elements Required**: TOPIC, AUTHORS, YEAR, ABSTRACT, DOI/URL
2. **Abstract Critical**: Must check relevance to proposal
3. **If Not Relevant → FAILED**: Don't include irrelevant references
4. **Wait Time**: Must `wait --load networkidle` after page navigation
5. **Ref Changes**: Must re-snapshot after navigation

## Golden Rule

```bash
snapshot → type --submit "keywords" → wait --load → snapshot → click → wait → snapshot → verify 5 elements
```

## Comparison: CNKI vs PubMed vs Wanfang

| Aspect | CNKI | PubMed | Wanfang |
|--------|------|---------|---------|
| **5-Element Verify** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Search Method** | type --submit | type --submit | type --submit |
| **Abstract Check** | ✅ Required | ✅ Required | ✅ Required |
| **Tab Behavior** | Same tab | Same tab | **NEW TAB** |
| **Chinese Coverage** | ✅ Strong | Limited | ✅ Strong |
| **English Coverage** | Limited | ✅ Strong | Limited |
