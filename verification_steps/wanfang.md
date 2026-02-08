## CRITICAL: Sequential Verification Required

**IMPORTANT**: Do NOT perform concurrent verifications.

When verifying references:
1. Complete ALL CNKI verifications FIRST
2. Then complete ALL PubMed verifications
3. Finally complete Wanfang verifications (supplementary)
4. Do NOT switch between databases mid-verification

**Why Sequential?**
- Browser tabs may conflict between databases
- Tab management becomes complex with multiple databases
- Easier to track progress and errors
- Cleaner verification records

**Verification Order:**
1. CNKI (Chinese references) - First priority
2. PubMed (English references) - Second priority
3. Wanfang (supplementary Chinese) - Third priority

**For Each Database:**
```bash
# Complete all verifications for this database first
# Then move to the next database
# Do NOT interleave verifications
```

**Wanfang Note:**
- Articles open in NEW TAB - remember to switch tabs
- Clean up unused tabs between verifications
- Complete all Wanfang references last

---

# Wanfang Reference Verification Steps

## Scope
- Wanfang Data (万方数据)
- Chinese science and technology literature
- Complementary to CNKI

## Important: New Tab Behavior

**Key Difference**:
- Clicking search results **opens in NEW tab** (not same tab)
- You must **switch to the new tab** to continue verification

## Verification Goals

For EACH reference, verify these 5 elements:
- ✅ **TOPIC**: Article matches research topic (title matches proposal theme)
- ✅ **AUTHORS**: At least first 2-3 authors correct
- ✅ **YEAR**: Publication year correct
- ✅ **ABSTRACT**: Article abstract is relevant to proposal
- ⚠️ DOI: Some articles may not have DOI

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

### Step 1: Open Wanfang Homepage
```bash
openclaw browser --browser-profile chrome open "https://www.wanfangdata.com.cn/"
```

### Step 2: Get Page Snapshot
```bash
openclaw browser --browser-profile chrome snapshot --compact
```

### Step 3: Enter Search Keywords

**Option A: Use type --submit (Recommended)**
```bash
openclaw browser --browser-profile chrome type [search-box-ref] "Orem 自理模式 糖尿病" --submit
```

**Option B: Use type + click**
```bash
openclaw browser --browser-profile chrome type [search-box-ref] "Orem 自理模式 糖尿病"
openclaw browser --browser-profile chrome click [search-button-ref]
```

### Step 4: Wait for Page Load
```bash
openclaw browser --browser-profile chrome wait --load networkidle
```

### Step 5: Get Search Results Snapshot
```bash
openclaw browser --browser-profile chrome snapshot --compact
```

### Step 6: Click Article (Opens in NEW Tab!)

**Important**: Article opens in NEW tab
```bash
openclaw browser --browser-profile chrome click [article-ref]
```

### Step 7: SWITCH TO NEW TAB (Critical!)
```bash
# List all tabs
openclaw browser --browser-profile chrome tabs

# Output shows tabs with IDs:
# 1. Google  https://...  id: FB0A51FD...
# 2. Wanfang  https://...  id: 5C56321A...
# 3. (untitled)  https://...article-detail/...  id: ABC12345...

# Focus on the new tab (article page)
openclaw browser --browser-profile chrome focus [new-tab-id]
```

### Step 8: Get Article Details and Verify 5 Elements
```bash
# Wait for new tab to load
openclaw browser --browser-profile chrome wait --load networkidle

# Get snapshot of article page
openclaw browser --browser-profile chrome snapshot --compact

# Verify 5 elements:
# 1. TOPIC: Does title match proposal theme?
# 2. AUTHORS: Do first 2-3 authors match?
# 3. YEAR: Does year match?
# 4. ABSTRACT: Is abstract relevant to proposal?
# 5. DOI: Is DOI available?
```

## Tab Management Commands

### List all tabs:
```bash
openclaw browser --browser-profile chrome tabs
```

### Switch to specific tab:
```bash
openclaw browser --browser-profile chrome focus [tab-id]
```

### Close a tab:
```bash
openclaw browser --browser-profile chrome close [tab-id]
```

## Verification Result Format

```markdown
## [Number] [VERIFIED/FAILED]

**Title**: [Full Title]
- **Authors**: [First 3 authors, et al.]
- **Journal**: [Journal Name], [Year], [Vol]([Issue]): [Pages]
- **Abstract**: [First 2-3 sentences...]
- **Relevance Check**:
  - Population matches: YES/NO
  - Intervention matches: YES/NO
  - Outcomes match: YES/NO
- **Status**: [TOPIC✓ AUTHORS✓ YEAR✓ ABSTRACT✓ DOI✓] or [FAILED]

**Failed Example**:
[3] Authors. Title[J]. Journal, 2020.
    FAILED: Abstract discusses hospital nursing management,
    but proposal focuses on patient self-care at home.
    → REPLACEMENT SEARCH NEEDED
```

## Example Workflow with New Tabs

```bash
# 1. Search on homepage
openclaw browser --browser-profile chrome type e5 "Orem 自理模式 护理" --submit
wait --load networkidle

# 2. Get search results
snapshot

# 3. Click article (opens NEW tab)
click [article-ref]

# 4. List tabs to find new one
tabs
# Output: 3 tabs - original + new article tab

# 5. Switch to new tab
focus [new-tab-id]

# 6. Get article details
wait --load networkidle
snapshot

# 7. Verify 5 elements
# [1] Authors. Title[J]. Journal, 2021.
#     Status: ALL VERIFIED ✓✓✓✓✓
```

## Troubleshooting

### Issue 1: Tab Disappears After Click
**Cause**: Article opened in new tab, but you stayed on old tab
**Solution**:
```bash
# List all tabs
openclaw browser --browser-profile chrome tabs

# Focus on the new tab
openclaw browser --browser-profile chrome focus [new-tab-id]
```

### Issue 2: Abstract NOT Relevant
**Symptom**: Article discusses different population/intervention
**Solution**:
1. Mark as FAILED
2. Document why not relevant
3. Search for replacement
4. Re-verify ALL references

### Issue 3: Cannot Find Article in Snapshot
**Cause**: Still on search page, not article page
**Solution**:
1. Run `tabs` to check current tabs
2. Switch to the article tab
3. Re-run `snapshot`

### Issue 4: Multiple Tabs Open
**Cause**: Clicked multiple articles
**Solution**:
```bash
# List all tabs
tabs

# Close unnecessary tabs
close [unwanted-tab-id]

# Focus on correct tab
focus [correct-tab-id]
```

### Issue 5: Search Returns No Results
**Cause**: Keywords too specific
**Solution**:
1. Simplify keywords
2. Use CNKI instead if needed

## Verification Checklist

- [ ] Search returned relevant results
- [ ] Clicked article (new tab opened)
- [ ] Switched to new tab successfully
- [ ] Article page loaded completely
- [ ] **TOPIC**: Title matches proposal theme
- [ ] **AUTHORS**: First 3 author names correct
- [ ] **YEAR**: Publication year correct
- [ ] **ABSTRACT**: Content relevant to proposal
  - [ ] Same population
  - [ ] Same/similar intervention
  - [ ] Similar outcomes measured
- [ ] Volume/Issue/Pages obtained
- [ ] DOI obtained (if available)

## Important Notes

1. **5 Elements Required**: TOPIC, AUTHORS, YEAR, ABSTRACT, DOI/URL
2. **Abstract Critical**: Must check relevance to proposal
3. **If Not Relevant → FAILED**: Don't include irrelevant references
4. **New Tab Behavior**: Clicking articles opens new tab - MUST switch tabs!
5. **Tab Management**: Use `tabs` and `focus [tab-id]` commands
6. **Wait After Switch**: Always `wait --load networkidle` after switching tabs

## Golden Rule for Wanfang

```bash
# Search phase
snapshot → type --submit "keywords" → wait → snapshot

# Article phase (new tab!)
click article → tabs → focus [new-tab-id] → wait → snapshot → verify 5 elements
```

## Comparison: CNKI vs Wanfang vs PubMed

| Aspect | CNKI | Wanfang | PubMed |
|--------|------|---------|---------|
| **5-Element Verify** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Search Method** | type --submit | type --submit | type --submit |
| **Abstract Check** | ✅ Required | ✅ Required | ✅ Required |
| **Tab Behavior** | Same tab | **NEW TAB** ⚠️ | Same tab |
| **Tab Management** | Not needed | Required | Not needed |
| **Chinese Coverage** | ✅ Strong | ✅ Strong | Limited |
| **English Coverage** | Limited | Limited | ✅ Strong |
| **DOI Availability** | Sometimes missing | Sometimes missing | ✅ Usually available |
