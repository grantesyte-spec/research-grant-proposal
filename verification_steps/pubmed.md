# PubMed Reference Verification Steps

## Scope
- PubMed (NCBI - National Center for Biotechnology Information)
- English biomedical and nursing literature verification
- Requires web_fetch tool (browser automation has limitations)

## Verification Goals
- ✅ TOPIC: Article matches research topic
- ✅ AUTHORS: At least first 2-3 authors correct
- ✅ YEAR: Publication year correct
- ✅ PMID: PubMed unique identifier
- ✅ DOI: Most articles have DOI
- ✅ JOURNAL: Official journal name

## Important Discovery

**Key Finding**: 
- `openclaw browser` returns HTTP 404 for PubMed
- **`web_fetch` tool works successfully** for PubMed verification

**Recommendation**: Use `web_fetch` for PubMed verification, not browser automation.

## 4-Step Verification Process

### Step 1: Search PubMed via web_fetch
```bash
web_fetch(url="https://pubmed.ncbi.nlm.nih.gov/?term=keywords")
```

**Example**:
```bash
web_fetch(url="https://pubmed.ncbi.nlm.nih.gov/?term=Orem+self-care+model+nursing")
```

### Step 2: Extract Search Results
From web_fetch response, extract:
- ✅ Total results count
- ✅ Article titles
- ✅ Authors (first 3)
- ✅ Journals
- ✅ Publication dates
- ✅ PMIDs
- ✅ DOIs

### Step 3: Get Article Details (Optional)
For specific article verification:
```bash
web_fetch(url="https://pubmed.ncbi.nlm.nih.gov/[PMID]/")
```

**Example**:
```bash
web_fetch(url="https://pubmed.ncbi.nlm.nih.gov/32050090/")
```

### Step 4: Record Verification Result
Extract from details page:
- ✅ Full title
- ✅ All authors
- ✅ Journal name with volume/issue/pages
- ✅ Publication date
- ✅ DOI
- ✅ PMID
- ✅ Abstract (for TOPIC verification)

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

### Web Fetch Response (Simplified)
```json
{
  "url": "https://pubmed.ncbi.nlm.nih.gov/?term=Orem+self-care+model+nursing",
  "status": 200,
  "text": "77,272 results\n\n[1] Younas A, et al. Scand J Caring Sci. 2019 Sep;33(3):540-555. DOI: 10.1111/scs.12670. PMID: 30866078",
  "tookMs": 1068
}
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

### Issue 1: Browser Returns 404
**Symptom**: `openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/"` returns HTTP 404
**Solution**: Use `web_fetch` instead

### Issue 2: web_fetch Returns Incomplete Data
**Symptom**: Text truncated or missing details
**Solution**: 
- Check `truncated: false` in response
- If truncated, try specific PMID URL
- Use `extractMode: "text"` for raw text

### Issue 3: No Results for Search Term
**Symptom**: "0 results" or very few results
**Solution**:
1. Simplify search terms
2. Try alternative keywords
3. Check spelling

### Issue 4: DOI Not Available
**Cause**: Some older articles lack DOI
**Solution**: Use PMID as primary identifier

### Issue 5: Article Retracted/Withdrawn
**Symptom**: Response shows "Retracted"
**Solution**: Find replacement article, do not use retracted references

## Important Notes

1. **Use web_fetch**: Browser automation doesn't work for PubMed
2. **PMID is Reliable**: Every PubMed article has unique PMID
3. **DOI is Preferred**: Use DOI for verification when available
4. **Check Retractions**: Look for "Retracted"标记
5. **Search First**: Use broad search to find relevant articles
6. **Verify Specifics**: Get details for each candidate reference

## Search Strategy Examples

### Broad Search (Find Relevant Articles)
```bash
web_fetch(url="https://pubmed.ncbi.nlm.nih.gov/?term=Orem+self-care+model+nursing")
```

### Specific Search (Hip Fracture + Nursing)
```bash
web_fetch(url="https://pubmed.ncbi.nlm.nih.gov/?term=hip+fracture+nursing+Orem")
```

### Get Specific Article
```bash
web_fetch(url="https://pubmed.ncbi.nlm.nih.gov/30866078/")
```

## PubMed URL Patterns

| Purpose | URL Pattern |
|---------|------------|
| Search | `https://pubmed.ncbi.nlm.nih.gov/?term=keywords` |
| Article Details | `https://pubmed.ncbi.nlm.nih.gov/[PMID]/` |
| DOI Resolution | `https://doi.org/[DOI]` |

## Verification Checklist

- [ ] Search returned relevant results
- [ ] Article accessible via PMID URL
- [ ] Title matches research topic
- [ ] First 3 author names correct
- [ ] Journal name correct
- [ ] Publication year correct
- [ ] DOI available and resolvable
- [ ] Article not retracted
- [ ] Reference formatted correctly

## Comparison: CNKI vs PubMed

| Aspect | CNKI | PubMed |
|--------|------|--------|
| **Access Method** | openclaw browser | web_fetch |
| **Primary ID** | None | PMID |
| **DOI Availability** | Sometimes missing | Usually available |
| **Language** | Chinese | English |
| **Nursing Coverage** | Strong | Very Strong |
| **Verification Speed** | Moderate | Fast |
