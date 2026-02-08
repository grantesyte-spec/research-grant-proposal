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
[number] Authors. Article title[J]. Journal Name, Year, Volume(Issue): Pages. Verification URL: https://...
```

**Examples:**
```
[1] Wang Y, Li X. Effects of nursing intervention on hip fracture[J]. J Clin Nurs, 2022, 31(15): 2156-2165. Verification URL: https://pubmed.ncbi.nlm.nih.gov/35012345/

[2] Li M, Wang J. Orem self-care model in elderly hip fracture patients[J]. Chinese Journal of Nursing, 2020, 55(8): 1121-1126. Verification URL: https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&filename=ZHHL202008001
```

**Note**: DOI is optional - use verification URL from CNKI/PubMed/Wanfang as primary source.

## Reference Verification Workflow

**CRITICAL: All references MUST be verified via CLI commands. Do NOT fabricate references.**

### Sequential Verification Required

**IMPORTANT**: Do NOT perform concurrent verifications.

**Verification Order:**
1. **CNKI** - Complete ALL Chinese references first
2. **PubMed** - Then complete ALL English references
3. **Wanfang** - Finally complete supplementary Chinese references (if needed)

**For Each Database:**
```bash
# Complete all verifications for this database first
# Then move to the next database
# Do NOT interleave verifications
```

**Why Sequential?**
- Browser tabs may conflict between databases
- Easier to track progress and errors
- Cleaner verification records
- Avoids confusion with verification URLs

### 5-Element Verification

For EACH reference, verify these 5 elements:

1. ✅ **TOPIC**: Article title matches research topic
2. ✅ **AUTHORS**: At least first 2-3 authors correct
3. ✅ **YEAR**: Publication year correct
4. ✅ **ABSTRACT**: Abstract content relevant to proposal
5. ✅ **URL**: Verification URL accessible via browser

### Abstract Relevance Check

```
ABSTRACT verification asks:
- Does the abstract discuss the same POPULATION?
  (e.g., elderly hip fracture patients vs. children)

- Does the abstract address the same INTERVENTION?
  (e.g., Orem self-care model vs. traditional care)

- Does the abstract measure similar OUTCOMES?
  (e.g., functional recovery vs. blood pressure)

IF ANY answer is NO → Mark FAILED → Search for replacement
```

### If Abstract NOT Relevant → FAILED

When abstract does NOT match proposal:
1. Mark reference as **FAILED**
2. Document reason:
   ```
   FAILED: Abstract discusses [X] but proposal focuses on [Y]
   ```
3. Search for replacement article
4. Re-verify ALL references from beginning

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

3. **Verify 5 Elements**
   ```
   ✓ TOPIC: YES/NO (Title matches research topic)
   ✓ AUTHORS: YES/NO (First 2-3 authors match)
   ✓ YEAR: YES/NO (Publication year matches)
   ✓ ABSTRACT: YES/NO (Content relevant to proposal)
   ✓ URL: YES/NO (Verification URL accessible)
   ```

4. **Record Result**
   ```
   [1] Authors. Title[J]. Journal, Year.
       Status: VERIFIED / FAILED
       If FAILED → REASON: [Why not relevant]
   ```

5. **If FAILED**
   - Mark as FAILED
   - Document why not relevant
   - Search for replacement
   - Re-verify ALL references from beginning

### Verification Template

For each reference, record:
```
[1] Authors. Title[J]. Journal, Year.

    VERIFICATION RESULTS:
    ✓ TOPIC: YES/NO (Title matches research topic)
    ✓ AUTHORS: YES/NO (First 2-3 authors match)
    ✓ YEAR: YES/NO (Year matches)
    ✓ ABSTRACT: YES/NO (Content relevant to proposal)
    ✓ URL: YES/NO (Verification URL accessible)
    
    If ANY is NO → FAILED → Search again
    
    Status: [ALL VERIFIED] or [FAILED]
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

### Golden Rule
```bash
snapshot → type --submit "keywords" → wait --load networkidle → snapshot → click → wait → snapshot → verify 5 elements
```

## PubMed Verification Workflow

**Reference**: [PubMed Verification Steps](verification_steps/pubmed.md) for detailed 4/8-step process.

### Key Steps
```bash
# Search with keywords
openclaw browser --browser-profile chrome type e14 "keywords" --submit

# Get article by PMID directly
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/[PMID]/"
```

## Wanfang Verification Workflow

**Reference**: [Wanfang Verification Steps](verification_steps/wanfang.md) for detailed 8-step process.

**Key Difference**: Articles open in **NEW TAB**

### Key Steps
```bash
# Click article (opens in NEW TAB!)
openclaw browser --browser-profile chrome click [article-ref]

# MUST switch to new tab!
openclaw browser --browser-profile chrome tabs
openclaw browser --browser-profile chrome focus [new-tab-id]
```

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Abstract NOT relevant | Mark FAILED → Search for replacement |
| Wrong population | Mark FAILED → Different article needed |
| Wrong intervention | Mark FAILED → Different article needed |
| Wrong outcomes | Mark FAILED → Different article needed |
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
- **Features**: openclaw browser, 8-step process, --submit option, 5-element verification

### PubMed (English)
- **File**: `verification_steps/pubmed.md`
- **Scope**: English biomedical and nursing literature
- **Features**: openclaw browser, PMID-based, 4/8-step options, --submit option, 5-element verification

### Wanfang (Chinese)
- **File**: `verification_steps/wanfang.md`
- **Scope**: Chinese science & technology literature
- **Features**: Complementary to CNKI, NEW TAB behavior, tab management, 5-element verification

---

## Verification Requirements Summary

- ❌ DO NOT fabricate references
- ❌ DO NOT assume references exist without verification
- ❌ DO NOT include references with irrelevant abstracts
- ✅ MUST verify 5 elements for EACH reference
  - ✓ TOPIC: Article matches research topic
  - ✓ AUTHORS: First 2-3 authors correct
  - ✓ YEAR: Publication year correct
  - ✓ ABSTRACT: Content relevant to proposal
  - ✓ URL: Verification URL accessible (use CNKI/PubMed/Wanfang, DOI not required)
- ✅ If abstract NOT relevant → Mark FAILED → Search for replacement
- ✅ ALL references must pass 5-element verification before export
