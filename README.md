# Research Grant Proposal Skill (研究课题申请书技能)

A Claude/Codex skill for generating academic research grant proposals in Chinese with **in-text citations**, **validated references** (both English and Chinese), **verification URLs**, and **Word document export**.

## Features

- 📝 **Chinese Academic Format**: Proper formatting following Chinese academic standards
- 📄 **Word Export**: Generate professional `.docx` documents
- 🔢 **In-Text Citations**: Use numbered citations [1], [2], [3]...
- ✅ **Validated References**: Step-by-step verification workflow for academic sources
- 🇨🇳 **Chinese References Support**: Full support for CNKI, Wanfang, and Chinese journal references
- 🔗 **Verification URLs**: Every reference includes a link for manual verification
- 📊 **Metrics Tables**: Auto-generated metrics and KPI tables

## ⚠️ Important: Best Practices

### 1. Do NOT Use web_fetch
- ❌ Never use `web_fetch` tool
- ✅ Use browser tools instead (`browser` with `action=open`, `action=snapshot`)

### 2. Verify All Parameters
- ✅ Always include ALL required parameters for `write()` calls
- ✅ Example: `write(content="text", path="/file.txt")`
- ❌ Never call `write()` without complete parameters

### 3. Validate Content
- ✅ The generator includes validation for:
  - Reference format and completeness
  - Numerical data accuracy
  - Verification URL presence
  - Common typos (e.g., "4型糖尿病" → "4亿人")

## Installation

### For OpenClaw/Claude Code Users

1. Copy this skill to your skills directory:
   ```bash
   cp -r research-grant-proposal ~/.claude/skills/
   ```

2. Restart Claude Code to discover the new skill

### For Claude Web Users

Import the skill through Claude's skill management interface.

## Usage

### Basic Usage

```
"Generate a research grant proposal about collaborative nursing care with verified references"
```

### Advanced Usage

```
"Create a grant proposal titled 'Collaborative Care Combined with Prospective Nursing Management in Type 2 Diabetes Patients with Osteoporotic Intertrochanteric Femoral Fractures' with in-text citations [1]-[20] and verification URLs"
```

### Command Line

```bash
# Interactive mode
python scripts/generate_proposal.py --interactive

# With title
python scripts/generate_proposal.py --title "研究课题标题"

# With custom output
python scripts/generate_proposal.py --title "研究课题标题" --output ~/Desktop/proposal.docx

# Skip validation (not recommended)
python scripts/generate_proposal.py --title "研究课题标题" --no-validate
```

## Citation Format

### In-Text Citations

**Format:** Use numbered citations in brackets [1]

**Examples:**
```
协同护理模式已被证明可显著改善患者预后[1][2]
多学科协作团队是实施该模式的关键[3][4][5]
参考Tseng等[6]的研究设计...
```

### Reference List

**Format:** Numbered list with verification URLs

```
[1] Author(s). Title[J]. Journal, Year, Vol(Issue): Pages. DOI. 
    验证链接: https://...

[2] Author(s). Title[J]. Journal, Year, Vol(Issue): Pages. 
    验证链接: https://...
```

## Reference Verification

All references MUST be verified before including in proposals.

### Verification Steps

1. **Search**: Use Google Scholar, ScienceDirect, CNKI
2. **Verify**: Check authenticity, DOI, citation count
3. **Document**: Record verification URL for each reference
4. **Quality Check**: Ensure peer-reviewed, relevant, accessible

### Verification URL Examples

| Source | URL |
|--------|-----|
| Google Scholar | `https://scholar.google.com/scholar?q=Title+Author+Year` |
| ScienceDirect | `https://www.sciencedirect.com/science/article/pii/XXX` |
| DOI | `https://doi.org/[DOI]` |
| PubMed | `https://pubmed.ncbi.nlm.nih.gov/PMID/` |
| **CNKI** | `https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=...` |
| **Wanfang** | `https://www.wanfangdata.com.cn/index/index.do` |

### Chinese References Support

**Search Chinese Literature:**
- CNKI: https://kns.cnki.net/kns8s/search?classid=WD0FTY92
- Wanfang: https://www.wanfangdata.com.cn/index/index.do
- Google Scholar: https://scholar.google.com/scholar?q=site:cnki.net+关键词

**Chinese Reference Format:**
```
[序号] 作者1, 作者2, 作者3. 文章题目[J]. 期刊名称, 年, 卷(期): 起止页码. DOI. 验证链接: https://...
```

**Example Chinese Reference:**
```
[2] 王青, 李明华, 陈晓红. 多学科协作护理模式在2型糖尿病合并髋部骨折
    患者中的应用研究[J]. 中华护理杂志, 2020, 55(3): 321-326. 
    DOI: 10.3761/j.issn.0254-1769.2020.03.001. 
    验证链接: https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLAST2021&filename=ZHHL202003001
```

### Verification Criteria

Include only references that:
- Published in peer-reviewed journal (Chinese or English)
- Authors can be verified
- Journal is reputable
- DOI/URL available
- Content directly relevant
- Published within last 10 years

**Recommended Chinese Journals:**
- 中华护理杂志
- 中国护理管理
- 护理学杂志
- 护理研究
- 解放军护理杂志

### Example Verification

```
[3] Tseng MY, et al. Effects of a diabetes-specific care model... 
    Experimental Gerontology, 2019, 118: 31-38. 
    DOI: 10.1016/j.exger.2019.01.006. 
    验证链接: https://doi.org/10.1016/j.exger.2019.01.006
```

## Best Practices Checklist

Before submitting any generated proposal:

- [ ] No use of web_fetch tool
- [ ] All write() calls include complete parameters (path/file_path + content)
- [ ] All numerical data verified (no typos like "4型糖尿病" → "4亿人")
- [ ] All references verified through Google Scholar/ScienceDirect/DOI
- [ ] All references include verification URLs
- [ ] In-text citations [1], [2], [3]... match reference list
- [ ] Reference titles are complete and properly formatted
- [ ] Document structure follows Chinese academic standards

## Directory Structure

```
research-grant-proposal/
├── SKILL.md                    # Skill documentation with verification workflow
├── README.md                   # This file
├── push_to_github.sh          # Push to GitHub
└── scripts/
    └── generate_proposal.py   # Word document generator with validation
```

## Supported Topics

- Collaborative care models (协同护理模式)
- Prospective nursing management (前瞻性护理管理)
- Chronic disease management (慢性病管理)
- Orthopedic nursing (骨科护理)
- Diabetes nursing (糖尿病护理)
- Osteoporosis research (骨质疏松研究)
- Hip fracture care (髋部骨折护理)

## Output Example

**In-text:**
```
协同护理模式可显著降低术后并发症发生率[1][2]，通过多学科
协作团队的个体化干预，患者的血糖控制达标率提高至85%以上[3]。
```

**References:**
```
五、近五年核心期刊参考文献

[1] Moran WP, et al. Using a collaborative approach to reduce 
    postoperative complications for hip-fracture patients[J]. 
    The Joint Commission Journal, 2006, 32(11): 573-584. 
    验证链接: https://scholar.google.com/scholar?q=Moran+2006+hip+fracture

[2] Tseng MY, et al. Effects of a diabetes-specific care model 
    for hip fractured older patients[J]. Experimental Gerontology, 
    2019, 118: 31-38. 
    验证链接: https://doi.org/10.1016/j.exger.2019.01.006
```

## Push to GitHub

```bash
cd research-grant-proposal
./push_to_github.sh
```

## Requirements

- Python 3.7+
- python-docx library

## License

MIT License

## Contributing

Feel free to submit issues and pull requests!
