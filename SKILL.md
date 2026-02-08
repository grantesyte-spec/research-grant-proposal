---
name: research-grant-proposal
description: Generate academic research grant proposals in Chinese with validated references and Word export.
---

# Research Grant Proposal Generator (研究课题申请书生成器)

Generate professional academic research grant proposals in Chinese with proper formatting, validated references with URLs, and Word document export.

## Quick Start

1. Provide research topic and requirements
2. Skill generates proposal with in-text citations [1], [2], etc.
3. All references include verification URLs for manual check
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
[序号] 作者. 文章题目[J]. 期刊名称, 年, 卷(期): 起止页码. DOI. 验证链接: https://...
```

**Examples:**
```
[1] Wang Y, Li X. Effects of nursing intervention on hip fracture[J]. J Clin Nurs, 2022, 31(15): 2156-2165. DOI: 10.1111/jocn.16235. 验证链接: https://doi.org/10.1111/jocn.16235

[2] 李明华, 王建国. Orem自理模式在老年髋部骨折患者护理中的应用[J]. 中华护理杂志, 2020, 55(8): 1121-1126. DOI: 10.3761/j.issn.0254-1769.2020.08.001. 验证链接: https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&filename=ZHHL202008001
```

## Reference Verification Workflow

**Critical: AI MUST verify references by ACTUALLY accessing URLs. Do NOT fabricate references.**

### AI Self-Correction Loop

```
┌─────────────────────────────────────────────────────────────┐
│                    VERIFICATION LOOP                          │
│                                                             │
│  ┌──────────────────┐                                       │
│  │ Generate Draft   │ ← Initial proposal                     │
│  └────────┬─────────┘                                       │
│           ↓                                                 │
│  ┌──────────────────────────────────────────────────┐      │
│  │ FOR EACH REFERENCE:                                 │      │
│  │ 1. Access verification URL (CLI)                   │      │
│  │ 2. Confirm article EXISTS at URL                   │      │
│  │ 3. Verify authors, year, journal match            │      │
│  │ 4. Check DOI resolves correctly                    │      │
│  └──────────────────────────────────────────────────┘      │
│           ↓                                                 │
│  ┌──────────────────┐    ┌──────────────────────┐         │
│  │ ALL Refs OK?     │──NO→│ Search + Add New Ref │         │
│  └────────┬─────────┘     │ Re-verify ALL        │         │
│           ↓ YES            └──────────────────────┘         │
│  ┌──────────────────┐                                       │
│  │ Export Document  │                                       │
│  └──────────────────┘                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Step 1: Generate Draft with Candidate References

Generate proposal with references. Mark all as "PENDING VERIFICATION".

### Step 2: Verify Each Reference (MANDATORY)

For EACH reference, you MUST:

1. **Access Verification URL via CLI**
   ```bash
   # For DOI links:
   openclaw browser --profile chrome open "https://doi.org/[DOI]"
   # WAIT for page to load
   # CONFIRM article title is visible
   
   # For CNKI links:
   openclaw browser --profile chrome open "https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&filename=XXX"
   # CONFIRM article details page loads
   # Verify authors, year, journal match citation
   ```

2. **Record Verification Result**
   ```
   [1] AUTHOR. TITLE[J]. JOURNAL, YEAR.
       Status: VERIFIED / FAILED
       URL Accessed: YES/NO
       Article Confirmed: YES/NO
       If FAILED → Must find replacement
   ```

3. **If Verification FAILS:**
   - Mark reference as FAILED
   - Search for valid replacement
   - Add new reference
   - RE-START verification loop from beginning
   - Continue until ALL references pass

### Step 3: Mandatory Verification Commands

**YOU MUST execute these commands for EACH reference:**

```bash
# 1. Try to access the verification URL
openclaw browser --profile chrome open "[verification-url]"

# 2. Take snapshot to confirm article exists
openclaw browser --profile chrome snapshot --compact

# 3. Check if article details are visible in snapshot
# If NOT visible → REFERENCE IS INVALID
```

**CRITICAL: If verification URL returns:**
- 404 error → FAILED → Find replacement
- Blank page → FAILED → Find replacement  
- Article not found → FAILED → Find replacement

### Step 4: NEVER Fabricate References

**Rules:**
- ❌ DO NOT generate references without accessing verification URLs
- ❌ DO NOT assume a reference exists
- ❌ DO NOT use placeholder URLs
- ✅ ONLY include references you have PERSONALLY verified via CLI
- ✅ If you cannot verify a reference → Say "I could not verify this reference" and find an alternative

### Verification Template (Required)

For each reference, record:

```
[1] AUTHOR. TITLE[J]. JOURNAL, YEAR.
    Verification URL: https://...
    CLI Command Executed: openclaw browser --profile chrome open "URL"
    Article Confirmed: YES/NO (based on snapshot)
    If NO → Reference FAILED → REPLACEMENT: [NEW-REF]
```

### Example of Proper Verification

**WRONG (Fabricated):**
```
[1] Wang Y, et al. Title[J]. J Nurs, 2022. 验证链接: https://doi.org/fake-doi
← AI did NOT access the URL, reference may not exist
```

**CORRECT (Verified):**
```
[1] Wang Y, et al. Title[J]. J Nurs, 2022.
    Verification URL: https://doi.org/10.1111/jocn.16235
    CLI Command: openclaw browser --profile chrome open "https://doi.org/10.1111/jocn.16235"
    Snapshot Confirms: YES (article title "Effects of Orem's..." visible)
    Status: VERIFIED ✓
```

### Database Search for Replacements

When a reference fails verification, search for valid alternatives:

```bash
# Google Scholar
openclaw browser --profile chrome open "https://scholar.google.com/scholar?q=topic+keywords+year"

# CNKI
openclaw browser --profile chrome open "https://kns.cnki.net/kns8s/search?classid=WD0FTY92&q=topic+keywords"

# Select article from results
# Access its verification URL
# Add to proposal if confirmed
```

## Browser Tool Usage

**⚠️ Important: Use CLI mode, not JSON API**

```bash
# Open URL
openclaw browser --profile chrome open "https://kns.cnki.net/kns8s/search"

# Get page structure
openclaw browser --profile chrome snapshot --compact

# Type/Click (use ref from snapshot)
openclaw browser --profile chrome type e8 "关键词" --target-id <tab-id>
openclaw browser --profile chrome click e10 --target-id <tab-id>
```

**Do NOT use:** `web_fetch` tool

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| JSON API errors | Use CLI mode: `openclaw browser --profile chrome <command>` |
| Missing path in write | Always include: `write(content="text", path="/file.txt") |
| Typo in numbers | Verify: 亿/万, %, decimals |

## Output Location

```
~/Desktop/[课题名称]课题申请书.docx
```

## Best Practices Checklist

Before submitting:
- [ ] **EACH reference verified via CLI** - You MUST execute `openclaw browser --profile chrome open "[url]"` for every reference
- [ ] **Article confirmed in snapshot** - Take snapshot and confirm article details are visible
- [ ] **NO fabricated references** - Never include references without actual verification
- [ ] **Failed references replaced** - If URL fails, find and add new reference
- [ ] All in-text citations match reference list
- [ ] Document follows Chinese academic standards

## Reference Quality Sources

### English Journals
- Journal of Clinical Nursing
- International Journal of Nursing Studies
- Osteoporosis International
- Geriatric Nursing

### Chinese Core Journals
- 中华护理杂志
- 中国护理管理
- 护理学杂志
- 中华糖尿病杂志
- 中国实用护理杂志
