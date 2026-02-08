# PubMed Reference Verification Steps

## Scope
- PubMed (NCBI - National Center for Biotechnology Information)
- English biomedical and nursing literature verification
- Use `openclaw browser` for verification

---

## CRITICAL: Research-First Workflow

**BEFORE verification, you MUST do research:**

```
1. Search PubMed for relevant English literature  
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
- ✅ **PMID**: PubMed unique identifier

---

## 4-Step Verification Process

### Step 1: Open PubMed
```bash
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/"
```

### Step 2: Get Page Snapshot
```bash
openclaw browser --browser-profile chrome snapshot --compact
```
Note: Search box ref is typically `e14`, Search button ref is `e15`

### Step 3: Enter Search Keywords

**Recommended: Use type --submit**
```bash
openclaw browser --browser-profile chrome type e14 "Orem self-care model diabetes hip fracture" --submit
```

**Alternative: Use PMID directly**
```bash
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/[PMID]/"
```

### Step 4: Get Article Details

```bash
openclaw browser --browser-profile chrome wait --load networkidle
openclaw browser --browser-profile chrome snapshot --compact
```

---

## 8-Step Detailed Process

### Step 1: Open PubMed Homepage
```bash
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/"
```

### Step 2: Get Homepage Snapshot
```bash
openclaw browser --browser-profile chrome snapshot --compact
```

### Step 3: Enter Search Keywords
```bash
openclaw browser --browser-profile chrome type e14 "keywords"
```

### Step 4: Submit Search
```bash
openclaw browser --browser-profile chrome type e14 "keywords" --submit
```

### Step 5: Wait for Page Load
```bash
openclaw browser --browser-profile chrome wait --load networkidle
```

### Step 6: Get Search Results
```bash
openclaw browser --browser-profile chrome snapshot --compact
```

### Step 7: Click Article Title
```bash
openclaw browser --browser-profile chrome click [article-ref]
```

### Step 8: Verify Details
```bash
openclaw browser --browser-profile chrome snapshot --compact
```

---

## Record Research Findings

After search, create `research_notes.md`:

```markdown
## PubMed Search Results
**Keywords**: [Search terms]
**Total Results**: [Number]

### Relevant Articles
| # | Title | PMID | Authors | Journal | Year | Relevance |
|---|-------|------|---------|---------|------|-----------|
| 1 | [Title] | [PMID] | [Authors] | [Journal] | [Year] | High |

### Selected for Proposal
- [1] Full citation with PMID URL
```

---

## Example Verification

```bash
# Search
openclaw browser --browser-profile chrome type e14 "Orem self-care model nursing" --submit

# Verify
[1] Younas A, et al. Usefulness of nursing theory-guided practice[J]. 
    Scand J Caring Sci, 2019, 33(3): 540-555.
    PMID: 30866078
    Verification URL: https://pubmed.ncbi.nlm.nih.gov/30866078/
    
    Status: VERIFIED ✓✓✓✓✓
```

---

## Troubleshooting

### Issue 1: Tab Disappears
**Solution**: Use PMID URL directly

### Issue 2: No Results
**Solution**: Simplify keywords

### Issue 3: Abstract NOT Relevant
**Solution**: Mark FAILED → Search for replacement

### Issue 4: DOI Not Available
**Solution**: Use PMID as primary identifier (still verifiable)

---

## Golden Rule

```bash
type --submit "keywords" → wait --load → snapshot → verify
```

---

## Important Notes

1. **Research FIRST**: Always do research before verification
2. **Document Everything**: Save findings to research_notes.md  
3. **PMID Reliable**: Every PubMed article has unique PMID
4. **Sequential**: Complete CNKI before PubMed
5. **Bot Detection**: PubMed may close tabs, use PMID URLs
