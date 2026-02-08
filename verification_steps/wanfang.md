# Wanfang Reference Verification Steps

## Scope
- Wanfang Data (万方数据)
- Chinese science and technology literature
- Complementary to CNKI

---

## CRITICAL: Research-First Workflow

**BEFORE verification, you MUST do research:**

```
1. Search CNKI first (primary Chinese source)
2. Search PubMed for English literature
3. THEN search Wanfang for supplementary Chinese sources
4. Record findings in research_notes.md
5. Select 10-15 quality references
6. THEN verify references
```

**NEVER verify references without doing research first.**

---

## Important: New Tab Behavior

**Key Difference**:
- Clicking search results **opens in NEW tab** (not same tab)
- You must **switch to the new tab** to continue verification

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

### Step 1: Open Wanfang Homepage
```bash
openclaw browser --browser-profile chrome open "https://www.wanfangdata.com.cn/"
```

### Step 2: Get Page Snapshot
```bash
openclaw browser --browser-profile chrome snapshot --compact
```

### Step 3: Enter Search Keywords
```bash
openclaw browser --browser-profile chrome type [search-box-ref] "keywords" --submit
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

### Step 8: Get Article Details
```bash
openclaw browser --browser-profile chrome wait --load networkidle
openclaw browser --browser-profile chrome snapshot --compact
```

---

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

---

## Record Research Findings

After search, create `research_notes.md`:

```markdown
## Wanfang Search Results (Supplementary)
**Keywords**: [Search terms]
**Total Results**: [Number]

### Relevant Articles
| # | Title | Authors | Journal | Year | Relevance |
|---|-------|---------|---------|------|-----------|
| 1 | [Title] | [Authors] | [Journal] | [Year] | Medium |

### Selected for Proposal
- [1] Full citation with URL
```

---

## Example Workflow

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

# 5. Switch to new tab
focus [new-tab-id]

# 6. Get article details
wait --load networkidle
snapshot

# 7. Verify
[1] Authors. Title[J]. Journal, 2021.
    Status: VERIFIED ✓✓✓✓✓
```

---

## Troubleshooting

### Issue 1: Tab Disappears After Click
**Cause**: Article opened in new tab, but you stayed on old tab
**Solution**:
```bash
tabs
focus [new-tab-id]
```

### Issue 2: Cannot Find Article in Snapshot
**Cause**: Still on search page, not article page
**Solution**:
1. Run `tabs` to check current tabs
2. Switch to the article tab
3. Re-run `snapshot`

### Issue 3: Multiple Tabs Open
**Solution**:
```bash
tabs
close [unwanted-tab-id]
focus [correct-tab-id]
```

### Issue 4: Search Returns No Results
**Solution**: Simplify keywords, or use CNKI instead

### Issue 5: Abstract NOT Relevant
**Solution**: Mark FAILED → Search for replacement

---

## Golden Rule for Wanfang

```bash
# Search phase
snapshot → type --submit "keywords" → wait → snapshot

# Article phase (new tab!)
click article → tabs → focus [new-tab-id] → wait → snapshot → verify
```

---

## Important Notes

1. **Research FIRST**: Always do research before verification
2. **Document Everything**: Save findings to research_notes.md
3. **New Tab Behavior**: Clicking articles opens new tab - MUST switch tabs!
4. **Tab Management**: Use `tabs` and `focus [tab-id]` commands
5. **Sequential**: CNKI → PubMed → Wanfang (in that order)
6. **Wait After Switch**: Always `wait --load networkidle` after switching tabs

---

## Comparison: CNKI vs Wanfang vs PubMed

| Aspect | CNKI | Wanfang | PubMed |
|--------|------|---------|--------|
| **Search Order** | 1st | 3rd | 2nd |
| **Tab Behavior** | Same tab | **NEW TAB** ⚠️ | Same tab |
| **Tab Management** | Not needed | Required | Not needed |
| **Chinese Coverage** | ✅ Strong | ✅ Strong | Limited |
| **English Coverage** | Limited | Limited | ✅ Strong |
