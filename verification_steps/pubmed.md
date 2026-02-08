# PubMed Reference Verification Steps

## Scope
- PubMed (NCBI - National Center for Biotechnology Information)
- English biomedical and nursing literature verification
- Use `openclaw browser` for verification

## Verification Goals
- ✅ TOPIC: Article matches research topic
- ✅ AUTHORS: At least first 2-3 authors correct
- ✅ YEAR: Publication year correct
- ✅ PMID: PubMed unique identifier
- ✅ DOI: Most articles have DOI
- ✅ JOURNAL: Official journal name

## 4-Step Verification Process

### Step 1: Open PubMed Homepage
```bash
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/"
```

### Step 2: Get Page Snapshot
```bash
openclaw browser --browser-profile chrome snapshot --compact
```
Note: Search box ref is typically `e14`, Search button ref is `e15`

### Step 3: Enter Search Keywords

**Option A: Use type + click separately**
```bash
openclaw browser --browser-profile chrome type e14 "Orem self-care model diabetes hip fracture"
openclaw browser --browser-profile chrome click e15
```

**Option B: Use type --submit (Recommended)**
```bash
openclaw browser --browser-profile chrome type e14 "Orem self-care model diabetes hip fracture" --submit
```
**Advantage**: Single command to input and submit search

**Option C: Use URL with search term**
```bash
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/?term=Orem+self-care+model"
```

### Step 4: Get Article Details

**After search results load:**
```bash
openclaw browser --browser-profile chrome click [article-ref]
openclaw browser --browser-profile chrome snapshot --compact
```

**Or use PMID URL directly:**
```bash
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/[PMID]/"
openclaw browser --browser-profile chrome snapshot --compact
```

## 8-Step Detailed Process (Full)

### Step 1: Open PubMed Homepage
```bash
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/"
```

### Step 2: Get Homepage Snapshot
```bash
openclaw browser --browser-profile chrome snapshot --compact
```
Note: Search box ref is typically `e14`, Search button ref is `e15`

### Step 3: Enter Search Keywords
```bash
openclaw browser --browser-profile chrome type e14 "Orem self-care model diabetes hip fracture nursing"
```

### Step 4: Submit Search

**Option A: Click search button**
```bash
openclaw browser --browser-profile chrome click e15
```

**Option B: Press Enter**
```bash
openclaw browser --browser-profile chrome press Enter
```

**Option C: Use --submit**
```bash
openclaw browser --browser-profile chrome type e14 "Orem self-care model" --submit
```

### Step 5: Wait for Page Load
```bash
openclaw browser --browser-profile chrome wait --load networkidle
```

### Step 6: Get Search Results Snapshot
```bash
openclaw browser --browser-profile chrome snapshot --compact
```
Look for:
- Total results count
- Article titles with PMIDs
- Authors and journals

### Step 7: Click Article Title
```bash
openclaw browser --browser-profile chrome click [article-ref]
```

### Step 8: Get Article Details
```bash
openclaw browser --browser-profile chrome snapshot --compact
```
Extract:
- Full title
- All authors
- Journal with volume/issue/pages
- Publication date
- DOI
- PMID
- Abstract

## Verification Result Format

```markdown
## [Number] [Pending/Verified]

**Title**: [Full Title]
- **Authors**: [First 3 authors, et al.]
- **Journal**: [Journal Name], [Year], [Vol]([Issue]): [Pages]
- **Publication Date**: [YYYY MM DD]
- **PMID**: [PMID Number]
- **DOI**: [DOI Number]
- **Verification Link**: https://pubmed.ncbi.nlm.nih.gov/[PMID]/
- **Status**: [TOPIC✓ AUTHORS✓ YEAR✓ PMID✓ DOI✓]

**Reference Format**:
[Authors]. [Title][J]. [Journal], [Year], [Vol]([Issue]): [Pages]. DOI: [DOI]. PMID: [PMID].
```

## Example Verification

### Search with --submit
```bash
openclaw browser --browser-profile chrome type e14 "Orem self-care model nursing" --submit
```

### Snapshot Response (Simplified)
```
[1] Younas A, et al. Scand J Caring Sci. 2019 Sep;33(3):540-555. DOI: 10.1111/scs.12670. PMID: 30866078
```

### Article Details Snapshot
```
## Usefulness of nursing theory-guided practice: an integrative review

Younas A, et al.
Scand J Caring Sci.
2019 Sep;33(3):540-555.
DOI: 10.1111/scs.12670
PMID: 30866078

Abstract: Nursing theory-guided practice helps improve the quality of nursing care...
```

### Recorded Verification
```markdown
## [1] VERIFIED

**Title**: Usefulness of nursing theory-guided practice: an integrative review
- **Authors**: Younas A, et al.
- **Journal**: Scand J Caring Sci, 2019 Sep;33(3):540-555
- **PMID**: 30866078
- **DOI**: 10.1111/scs.12670
- **Verification Link**: https://pubmed.ncbi.nlm.nih.gov/30866078/
- **Status**: TOPIC✓ AUTHORS✓ YEAR✓ PMID✓ DOI✓

**Reference**:
Younas A, et al. Usefulness of nursing theory-guided practice: an integrative review[J]. Scand J Caring Sci, 2019, 33(3): 540-555. DOI: 10.1111/scs.12670. PMID: 30866078.
```

## Troubleshooting

### Issue 1: Tab Disappears During Automation
**Symptom**: `Error: tab not found`
**Cause**: PubMed detects automation and closes tab
**Solution**:
1. Use different tab strategy
2. Increase wait time
3. If persistent, search for article using PMID URL directly

### Issue 2: No Search Results Displayed
**Symptom**: Search page shows no results
**Solution**:
1. Simplify search terms
2. Try: `Orem self-care model` first, then add more terms
3. Use URL with search term: `https://pubmed.ncbi.nlm.nih.gov/?term=Orem+self-care`

### Issue 3: Cannot Find Article in Results
**Symptom**: Article not visible in snapshot
**Solution**:
1. Scroll down or check next pages
2. Use PMID to search directly
3. Try alternative keywords

### Issue 4: DOI Not Available
**Cause**: Some older articles lack DOI
**Solution**: Use PMID as primary identifier

### Issue 5: Article Retracted/Withdrawn
**Symptom**: Response shows "Retracted"
**Solution**: Find replacement article, do not use retracted references

## Important Notes

1. **Golden Rule**: snapshot → type --submit → wait → snapshot
2. **PMID is Reliable**: Every PubMed article has unique PMID
3. **DOI Preferred**: Use DOI for verification when available
4. **Check Retractions**: Look for "Retracted"标记
5. **Navigation**: Refs change after navigation, always re-snapshot
6. **Bot Detection**: PubMed may close tabs, try alternative approaches
7. **--submit Option**: Use `type [ref] "keywords" --submit` for efficient single-step search

## PubMed URL Patterns

| Purpose | URL Pattern |
|---------|------------|
| Homepage | `https://pubmed.ncbi.nlm.nih.gov/` |
| Search | `https://pubmed.ncbi.nlm.nih.gov/?term=keywords` |
| Article | `https://pubmed.ncbi.nlm.nih.gov/[PMID]/` |
| DOI | `https://doi.org/[DOI]` |

## Verification Checklist

- [ ] Article accessible via browser
- [ ] Search returned relevant results
- [ ] Article visible in snapshot
- [ ] Title matches research topic
- [ ] First 3 author names correct
- [ ] Journal name correct
- [ ] Publication year correct
- [ ] DOI available and visible
- [ ] PMID confirmed
- [ ] Article not retracted
- [ ] Reference formatted correctly

## Comparison: CNKI vs PubMed

| Aspect | CNKI | PubMed |
|--------|------|--------|
| **Search Method** | `type --submit` or `type` + `click` | Similar approach |
| **Browser Stability** | ✅ Stable | ⚠️ Less stable (tabs close) |
| **Primary ID** | None | PMID |
| **DOI Availability** | Sometimes missing | Usually available |
| **Language** | Chinese | English |
| **Nursing Coverage** | Strong | Very Strong |
| **Bot Detection** | Low | Medium |
