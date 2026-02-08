# Wanfang Reference Verification Steps

## Scope
- Wanfang Data (万方数据)
- Chinese science and technology literature
- Complementary to CNKI

## Important: New Tab Behavior

**Key Difference from CNKI**:
- Clicking search results **opens in NEW tab** (not same tab)
- You must **switch to the new tab** to continue verification

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

### Step 5: Get Search Results
```bash
openclaw browser --browser-profile chrome snapshot --compact
```

### Step 6: Click Article (Opens in NEW Tab!)

**Important**: Article opens in NEW tab
```bash
openclaw browser --browser-profile chrome click [article-ref]
```

### Step 7: SWITCH TO NEW TAB
```bash
# Get list of tabs
openclaw browser --browser-profile chrome tabs

# Output shows tabs with IDs
# 1. Google  https://www.google.com.hk/  id: FB0A51FD...
# 2. Wanfang  https://www.wanfangdata.com.cn/...  id: 5C56321A...
# 3. (untitled)  https://www.wanfangdata.com.cn/article-detail/...  id: ABC12345...

# Focus on the new tab (article page)
openclaw browser --browser-profile chrome focus [new-tab-id]
```

### Step 8: Get Article Details
```bash
# Wait for new tab to load
openclaw browser --browser-profile chrome wait --load networkidle

# Get snapshot of article page
openclaw browser --browser-profile chrome snapshot --compact
```

## Handling New Tabs

### Tab Management Commands

**List all tabs:**
```bash
openclaw browser --browser-profile chrome tabs
```

**Switch to specific tab:**
```bash
openclaw browser --browser-profile chrome focus [tab-id]
```

**Close a tab:**
```bash
openclaw browser --browser-profile chrome close [tab-id]
```

### Example Workflow with New Tabs

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
```

## Verification Result Format

```markdown
## [Number] [Pending/Verified]

**Title**: [Full Title]
- **Authors**: [First 3 authors, et al.]
- **Journal**: [Journal Name], [Year], [Vol]([Issue]): [Pages]
- **Publication Date**: [YYYY-MM-DD]
- **Verification Link**: [Wanfang URL]
- **Status**: [TOPIC✓ AUTHORS✓ YEAR✓]

**Reference Format**:
[Authors]. [Title][J]. [Journal], [Year], [Vol]([Issue]): [Pages]. 验证链接: [URL].
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

### Issue 2: Cannot Find Article in Snapshot
**Cause**: Still on search page, not article page
**Solution**:
1. Run `tabs` to check current tabs
2. Switch to the article tab
3. Re-run `snapshot`

### Issue 3: Multiple Tabs Open
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

### Issue 4: Search Returns No Results
**Cause**: Keywords too specific or system busy
**Solution**:
1. Simplify keywords: `Orem 自理模式` → `Orem 护理`
2. Use advanced search
3. Try CNKI instead

### Issue 5: Page Content Not Fully Loaded
**Cause**: Dynamic content needs time
**Solution**:
```bash
# Wait longer
wait --load networkidle

# Or use evaluate to check content
evaluate --fn '() => document.readyState'
```

## Important Notes

1. **New Tab Behavior**: Clicking articles opens new tab - MUST switch tabs!
2. **Tab Management**: Use `tabs` and `focus [tab-id]` commands
3. **Wait After Switch**: Always `wait --load networkidle` after switching tabs
4. **Multiple Tabs**: Clean up unused tabs to avoid confusion
5. **CNKI Alternative**: If Wanfang has issues, use CNKI instead

## Golden Rule for Wanfang

```bash
# Search phase
snapshot → type --submit "keywords" → wait → snapshot

# Article phase (new tab!)
click article → tabs → focus [new-tab-id] → wait → snapshot
```

## Comparison: CNKI vs Wanfang vs PubMed

| Aspect | CNKI | Wanfang | PubMed |
|--------|------|---------|--------|
| **Article Opens** | Same tab | **NEW TAB** | Same tab |
| **Tab Management** | Not needed | Required | Not needed |
| **Browser Stability** | ✅ Stable | ⚠️ Medium | ⚠️ Medium |
| **Chinese Coverage** | ✅ Strong | ✅ Strong | Limited |
| **Nursing Journals** | ✅ Good | ✅ Good | ✅ Excellent |
| **Search Simplicity** | ✅ Easy | ⚠️ Medium | ✅ Easy |

## Verification Checklist

- [ ] Search returned relevant results
- [ ] Clicked article (new tab opened)
- [ ] Switched to new tab successfully
- [ ] Article page loaded completely
- [ ] Title matches research topic
- [ ] First 3 author names correct
- [ ] Journal name correct
- [ ] Publication year correct
- [ ] Volume/Issue/Pages obtained
- [ ] Reference formatted correctly
