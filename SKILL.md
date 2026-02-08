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
   
   # For CNKI links:
   openclaw browser --profile chrome open "https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&filename=XXX"
   ```

2. **Take Snapshot to Confirm Details**
   ```bash
   openclaw browser --profile chrome snapshot --compact
   ```

3. **Verify TWO Key Elements (MANDATORY):**
   ```
   ✓ TOPIC/MATCHES research topic
   ✓ AUTHORS at least first 2-3 match citation
   ✓ YEAR of publication matches
   ✓ JOURNAL name matches
   ```

4. **Record Verification Result**
   ```
   [1] AUTHOR. TITLE[J]. JOURNAL, YEAR.
       Status: VERIFIED / FAILED
       URL Accessed: YES/NO
       TOPIC Confirmed: YES/NO (article is about the right topic)
       AUTHORS Confirmed: YES/NO (authors match citation)
       If FAILED → Must find replacement
   ```

5. **If Verification FAILS:**
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
    Snapshot Taken: YES
    TOPIC Confirmed: YES/NO (article discusses the research topic)
    AUTHORS Confirmed: YES/NO (at least first 2-3 authors match)
    YEAR Confirmed: YES/NO
    Status: VERIFIED / FAILED
    If FAILED → REPLACEMENT: [NEW-REF]
```

### Example of Proper Verification

**WRONG (Fabricated):**
```
[1] Wang Y, et al. Title[J]. J Nurs, 2022. 验证链接: https://doi.org/fake-doi
← AI did NOT access the URL, reference may not exist
```

**CORRECT (Verified):**
```
[1] Wang Y, Li X, Zhang Y, et al. Effects of Orem's self-care theory on hip fracture patients[J]. J Clin Nurs, 2022.
    Verification URL: https://doi.org/10.1111/jocn.16235
    CLI Command: openclaw browser --profile chrome open "https://doi.org/10.1111/jocn.16235"
    Snapshot: Article title, authors (Wang Y, Li X, Zhang Y), journal, year all visible
    TOPIC Confirmed: YES (article is about Orem self-care theory for hip fracture)
    AUTHORS Confirmed: YES (Wang Y, Li X, Zhang Y match citation)
    YEAR Confirmed: YES (2022 matches)
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

**重要提示**: 请参考 `verification_steps/cnki.md` 获取完整的浏览器工具使用步骤。

### 快速参考
```bash
# 黄金法则：每次页面变化后必须重新 snapshot
snapshot → type → click → wait --load networkidle → snapshot
```

**详细步骤**: [查看 CNKI 验证步骤文档](verification_steps/cnki.md)

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| JSON API errors | Use CLI mode: `openclaw browser --browser-profile chrome <command>` |
| Missing path in write | Always include: `write(content="text", path="/file.txt") |
| Typo in numbers | Verify: 亿/万, %, decimals |

## Output Location

```
~/Desktop/[课题名称]课题申请书.docx
```

- **文件**：`verification_steps/doi.md`
- **适用范围**：通过DOI验证文献真实性
- **特点**：最权威的文献验证方式

### 万方数据（即将推出）
- **文件**：`verification_steps/wanfang.md`
- **适用范围**：中文科技文献验证
- **特点**：与CNKI互补
