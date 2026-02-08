# PubMed Reference Verification Steps

## Scope
- PubMed (NCBI - National Center for Biotechnology Information)
- English biomedical and nursing literature verification
- Use `openclaw browser` for verification

## Verification Goals

For EACH reference, verify these 5 elements:
- ✅ **TOPIC**: Article matches research topic (title matches proposal theme)
- ✅ **AUTHORS**: At least first 2-3 authors correct
- ✅ **YEAR**: Publication year correct
- ✅ **ABSTRACT**: Article abstract is relevant to proposal
- ✅ **PMID**: PubMed unique identifier (required)
- ⚠️ **DOI**: Most articles have DOI (optional)

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

## 4-Step Verification Process

### Step 1: Open PubMed with Search Term
```bash
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/?term=Orem+self-care+model+nursing"
```

### Step 2: Get Page Snapshot
```bash
openclaw browser --browser-profile chrome snapshot --compact
```
Note: Search box ref is typically `e14`, Search button ref is `e15`

### Step 3: Enter Search Keywords

**Option A: Use type --submit (Recommended)**
```bash
openclaw browser --browser-profile chrome type e14 "Orem self-care model diabetes hip fracture" --submit
```

**Option B: Use type + click**
```bash
openclaw browser --browser-profile chrome type e14 "Orem self-care model"
openclaw browser --browser-profile chrome click e15
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

### Step 5: Extract and Verify 5 Elements

From detail page, extract:
- ✅ Full title
- ✅ All authors
- ✅ Journal with volume/issue/pages
- ✅ Publication date
- ✅ **Abstract** (for relevance verification)
- ✅ DOI
- ✅ PMID

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

## 8-Step Detailed Process (Full)

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
openclaw browser --browser-profile chrome type e14 "Orem self-care model diabetes hip fracture nursing"
```

### Step 4: Submit Search

**Option A: Use --submit**
```bash
openclaw browser --browser-profile chrome type e14 "Orem self-care model" --submit
```

**Option B: Click search button**
```bash
openclaw browser --browser-profile chrome click e15
```

### Step 5: Wait for Page Load
```bash
openclaw browser --browser-profile chrome wait --load networkidle
```

### Step 6: Get Search Results Snapshot
```bash
openclaw browser --browser-profile chrome snapshot --compact
```

### Step 7: Click Article Title
```bash
openclaw browser --browser-profile chrome click [article-ref]
```

### Step 8: Get Article Details and Verify
```bash
openclaw browser --browser-profile chrome snapshot --compact

# Verify 5 elements:
# 1. TOPIC: Does title match proposal theme?
# 2. AUTHORS: Do first 2-3 authors match?
# 3. YEAR: Does year match?
# 4. ABSTRACT: Is abstract relevant to proposal?
# 5. DOI/PMID: Is identifier verifiable?

# Record result:
# [1] Authors. Title[J]. Journal, Year.
#     Status: ALL VERIFIED or FAILED
```

## Verification Result Format

```markdown
## [Number] [VERIFIED/FAILED]

**Title**: [Full Title]
- **Authors**: [First 3 authors, et al.]
- **Journal**: [Journal Name], [Year], [Vol]([Issue]): [Pages]
- **PMID**: [PMID Number]
- **DOI**: [DOI Number]
- **Abstract**: [First 2-3 sentences...]
- **Relevance Check**:
  - Population matches: YES/NO
  - Intervention matches: YES/NO
  - Outcomes match: YES/NO
- **Status**: [TOPIC✓ AUTHORS✓ YEAR✓ ABSTRACT✓ DOI✓] or [FAILED]

**Failed Example**:
[2] Authors. Title[J]. Journal, 2021.
    FAILED: Abstract discusses pediatric diabetes,
    but proposal focuses on elderly hip fracture patients.
    → REPLACEMENT SEARCH NEEDED
```

## Example Verification

### Search with --submit
```bash
openclaw browser --browser-profile chrome type e14 "Orem self-care model nursing" --submit
```

### Abstract Verification
```
ABSTRACT: This study examined the effects of Orem's self-care theory on 
elderly patients with hip fractures. 120 participants were randomly 
assigned to intervention or control group...

RELEVANCE CHECK:
✓ Population: Elderly hip fracture patients ✓
✓ Intervention: Orem's self-care theory ✓
✓ Outcomes: Functional recovery ✓
→ RELEVANT → VERIFIED
```

### Recorded Verification
```markdown
## [1] VERIFIED

**Title**: Effects of Orem's self-care theory on elderly hip fracture patients
- **Authors**: Wang Y, Zhang X, Liu J, et al.
- **Journal**: J Clin Nurs, 2022, 31(15): 2156-2165
- **PMID**: 35012345
- **DOI**: 10.1111/jocn.16235
- **Abstract**: This study examined the effects of Orem's self-care theory...
- **Relevance Check**:
  - Population: Elderly hip fracture patients ✓
  - Intervention: Orem's self-care theory ✓
  - Outcomes: Functional recovery ✓
- **Status**: TOPIC✓ AUTHORS✓ YEAR✓ ABSTRACT✓ DOI✓

**Reference**:
Wang Y, Zhang X, Liu J, et al. Effects of Orem's self-care theory on elderly hip fracture patients[J]. J Clin Nurs, 2022, 31(15): 2156-2165. DOI: 10.1111/jocn.16235. PMID: 35012345.
```

## Troubleshooting

### Issue 1: Abstract NOT Relevant
**Symptom**: Article discusses different population/intervention
**Solution**:
1. Mark as FAILED
2. Document why not relevant
3. Search for replacement
4. Re-verify ALL references

### Issue 2: Tab Disappears
**Symptom**: `Error: tab not found`
**Solution**:
1. Use PMID URL directly
2. Open new tab manually
3. Continue verification

### Issue 3: No Results
**Symptom**: Search returns 0 results
**Solution**:
1. Simplify keywords
2. Try broader terms
3. Check spelling

### Issue 4: DOI Not Available
**Cause**: Some older articles lack DOI
**Solution**: Use PMID as primary identifier (still verifiable)

## Important Notes

1. **5 Elements Required**: TOPIC, AUTHORS, YEAR, ABSTRACT, DOI/PMID
2. **Abstract Critical**: Must check relevance to proposal
3. **If Not Relevant → FAILED**: Don't include irrelevant references
4. **PMID Reliable**: Every PubMed article has unique PMID
5. **Bot Detection**: PubMed may close tabs, use PMID URLs

## Golden Rule

```bash
type --submit "keywords" → wait --load → snapshot → click → wait → snapshot → verify 5 elements
```

## Verification Checklist

- [ ] Article accessible via PMID or DOI
- [ ] **TOPIC**: Title matches proposal theme
- [ ] **AUTHORS**: First 3 author names correct
- [ ] **YEAR**: Publication year correct
- [ ] **ABSTRACT**: Content relevant to proposal
  - [ ] Same population
  - [ ] Same/similar intervention
  - [ ] Similar outcomes measured
- [ ] DOI obtained and verifiable
- [ ] PMID confirmed

## Comparison: CNKI vs PubMed vs Wanfang

| Aspect | CNKI | PubMed | Wanfang |
|--------|------|---------|---------|
| **5-Element Verify** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Search Method** | type --submit | type --submit | type --submit |
| **Abstract Check** | ✅ Required | ✅ Required | ✅ Required |
| **Tab Behavior** | Same tab | Same tab | **NEW TAB** |
| **Primary ID** | None | ✅ PMID | None |
| **Chinese Coverage** | ✅ Strong | Limited | ✅ Strong |
| **English Coverage** | Limited | ✅ Strong | Limited |
