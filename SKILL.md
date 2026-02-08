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
# Google Scholar
openclaw browser --browser-profile chrome open "https://scholar.google.com/scholar?q=keywords"

# CNKI
openclaw browser --browser-profile chrome open "https://kns.cnki.net/kns8s/search?classid=WD0FTY92&q=keywords"
```

## CNKI Verification Workflow

**Reference**: [CNKI Verification Steps](verification_steps/cnki.md) for detailed 8-step process.

### Golden Rule
```bash
snapshot → type → click → wait --load networkidle → snapshot
```

**Important**: Use `--browser-profile chrome` (not `--profile`)

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| JSON API errors | Use CLI mode: `openclaw browser --browser-profile chrome <command>` |
| Missing path in write | Always include: `write(content="text", path="/file.txt")` |
| Typo in numbers | Verify: 亿/万, %, decimals |
| Refs invalid after navigation | Re-run `snapshot` after page changes |

## Output Location

```
~/Desktop/[Topic Name]课题申请书.docx
```

## Independent Verification Steps

### CNKI (Chinese)
- **File**: `verification_steps/cnki.md`
- **Scope**: Chinese nursing research verification
- **Features**: No VPN required, 8-step detailed process

### PubMed (Coming Soon)
- **File**: `verification_steps/pubmed.md`
- **Scope**: English biomedical literature
- **Features**: Complete DOI information

### DOI (Coming Soon)
- **File**: `verification_steps/doi.md`
- **Scope**: DOI-based verification
- **Features**: Most authoritative source

### Wanfang (Coming Soon)
- **File**: `verification_steps/wanfang.md`
- **Scope**: Chinese science & technology
- **Features**: Complementary to CNKI

---

## Verification Requirements Summary

- ❌ DO NOT fabricate references
- ❌ DO NOT assume references exist without verification
- ✅ MUST verify each reference via CLI
- ✅ MUST confirm TOPIC, AUTHORS, YEAR
- ✅ ALL references must pass verification before export
