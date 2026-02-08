---
name: research-grant-proposal
description: Generate academic research grant proposals in Chinese with validated references and Word export.
---

# Research Grant Proposal Generator

Generate professional academic research grant proposals in Chinese with proper formatting, validated references, and Word document export.

## Quick Start

1. User provides research topic and requirements
2. Generate proposal with in-text citations [1], [2], etc.
3. Verify all references via CLI commands
4. Export as Word (.docx) to `~/Desktop/`

## Output Structure

Generated proposal includes:
- Research title and objectives
- Background and significance (立题依据)
- Research content and expected outcomes
- Methodology and technical approach
- References section with [1]-[10] and verification URLs

## Citation Format

### In-Text Citations
Use brackets: `[1]`, `[2]`, `[1][2]`, `[1]-[3]`

### Reference List
```
[number] Authors. Article title[J]. Journal Name, Year, Volume(Issue): Pages. DOI. Verification URL: https://...
```

**Examples:**
```
[1] Wang Y, Li X. Effects of nursing intervention on hip fracture[J]. J Clin Nurs, 2022, 31(15): 2156-2165. DOI: 10.1111/jocn.16235. Verification URL: https://doi.org/10.1111/jocn.16235

[2] Li M, Wang J. Orem self-care model in elderly hip fracture patients[J]. Chinese Journal of Nursing, 2020, 55(8): 1121-1126. DOI: 10.3761/j.issn.0254-1769.2020.08.001. Verification URL: https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&filename=ZHHL202008001
```

## Reference Verification Workflow

**CRITICAL: All references MUST be verified via CLI commands. Do NOT fabricate references.**

### Step 1: Generate Draft
Generate proposal with references marked as "PENDING VERIFICATION".

### Step 2: Verify Each Reference (MANDATORY)

For EACH reference:

1. **Access Verification URL via CLI**
   ```bash
   openclaw browser --browser-profile chrome open "[verification-url]"
   ```

2. **Take Snapshot**
   ```bash
   openclaw browser --browser-profile chrome snapshot --compact
   ```

3. **Verify Three Key Elements**
   - ✓ TOPIC: Article matches research topic
   - ✓ AUTHORS: At least first 2-3 authors match citation
   - ✓ YEAR: Publication year matches

4. **Record Result**
   ```
   [1] Authors. Title[J]. Journal, Year.
       Status: VERIFIED / FAILED
       URL Accessed: YES
       TOPIC Confirmed: YES/NO
       AUTHORS Confirmed: YES/NO
       YEAR Confirmed: YES/NO
   ```

5. **If FAILED**
   - Mark as FAILED
   - Search for replacement
   - Re-verify ALL references from beginning

### Verification Template

For each reference, record:
```
[1] Authors. Title[J]. Journal, Year.
    Verification URL: https://...
    CLI Command: openclaw browser --browser-profile chrome open "URL"
    Snapshot Taken: YES
    TOPIC Confirmed: YES/NO
    AUTHORS Confirmed: YES/NO
    YEAR Confirmed: YES/NO
    Status: VERIFIED / FAILED
    If FAILED → REPLACEMENT: [NEW-REF]
```

### Database Search for Replacements

```bash
# CNKI
openclaw browser --browser-profile chrome open "https://kns.cnki.net/kns8s/search?classid=WD0FTY92&q=keywords"

# PubMed
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/?term=keywords"

# Wanfang
openclaw browser --browser-profile chrome open "https://www.wanfangdata.com.cn/"
```

## CNKI Verification Workflow

**Reference**: [CNKI Verification Steps](verification_steps/cnki.md) for detailed 8-step process.

**Key Difference**: CNKI uses `openclaw browser` for verification.

### Golden Rule
```bash
snapshot → type --submit "keywords" → wait --load networkidle → snapshot
```

## PubMed Verification Workflow

**Reference**: [PubMed Verification Steps](verification_steps/pubmed.md) for detailed process.

**Key Difference**: Uses `openclaw browser` with PMID-based URLs.

### Key Steps
```bash
# Open PubMed
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/"

# Search with keywords
openclaw browser --browser-profile chrome type e14 "keywords" --submit

# Get article by PMID directly
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/[PMID]/"
```

## Wanfang Verification Workflow

**Reference**: [Wanfang Verification Steps](verification_steps/wanfang.md) for detailed 8-step process.

**Key Difference**: Articles open in **NEW TAB** (unlike CNKI). Tab management required.

### Key Steps
```bash
# Open Wanfang
openclaw browser --browser-profile chrome open "https://www.wanfangdata.com.cn/"

# Search with keywords
openclaw browser --browser-profile chrome type [search-box-ref] "keywords" --submit

# Click article (opens in NEW TAB!)
openclaw browser --browser-profile chrome click [article-ref]

# MUST switch to new tab!
openclaw browser --browser-profile chrome tabs
openclaw browser --browser-profile chrome focus [new-tab-id]
```

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| JSON API errors | Use CLI mode: `openclaw browser --browser-profile chrome <command>` |
| Missing path in write | Always include: `write(content="text", path="/file.txt")` |
| Typo in numbers | Verify: 亿/万, %, decimals |
| Refs invalid after navigation | Re-run `snapshot` after page changes |
| Wanfang new tab | Use `tabs` and `focus [tab-id]` to switch tabs |
| Bot detection | Use simplified keywords, try different databases |

## Output Location

```
~/Desktop/[Topic Name]课题申请书.docx
```

## Independent Verification Steps

### CNKI (Chinese)
- **File**: `verification_steps/cnki.md`
- **Scope**: Chinese nursing research verification
- **Features**: openclaw browser automation, 8-step process, --submit option

### PubMed (English)
- **File**: `verification_steps/pubmed.md`
- **Scope**: English biomedical and nursing literature
- **Features**: openclaw browser, PMID-based verification, 4/8-step options, --submit option

### Wanfang (Chinese)
- **File**: `verification_steps/wanfang.md`
- **Scope**: Chinese science & technology literature
- **Features**: Complementary to CNKI, NEW TAB behavior, tab management

### DOI (Coming Soon)
- **File**: `verification_steps/doi.md`
- **Scope**: DOI-based verification
- **Features**: Most authoritative source

---

## Verification Requirements Summary

- ❌ DO NOT fabricate references
- ❌ DO NOT assume references exist without verification
- ✅ MUST verify each reference via CLI
- ✅ MUST confirm TOPIC, AUTHORS, YEAR
- ✅ ALL references must pass verification before export
