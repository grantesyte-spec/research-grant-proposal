# Research Grant Proposal Skill (研究课题申请书技能)

A Claude/Codex skill for generating academic research grant proposals in Chinese with in-text citations, validated references, verification URLs, and Word document export.

## Features

- 📝 **Chinese Academic Format**: Proper formatting following Chinese academic standards
- 📄 **Word Export**: Generate professional `.docx` documents
- 🔢 **In-Text Citations**: Use numbered citations [1], [2], [3]...
- ✅ **Validated References**: Step-by-step verification workflow for academic sources
- 🔗 **Verification URLs**: Every reference includes a link for manual verification
- 📊 **Metrics Tables**: Auto-generated metrics and KPI tables

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

### Verification Criteria

Include only references that:
- Published in peer-reviewed journal
- Authors can be verified
- Journal is reputable
- DOI/URL available
- Content directly relevant
- Published within last 10 years

### Example Verification

```
[3] Tseng MY, et al. Effects of a diabetes-specific care model... 
    Experimental Gerontology, 2019, 118: 31-38. 
    DOI: 10.1016/j.exger.2019.01.006. 
    验证链接: https://doi.org/10.1016/j.exger.2019.01.006
```

## Directory Structure

```
research-grant-proposal/
├── SKILL.md                    # Skill documentation with verification workflow
├── README.md                   # This file
├── push_to_github.sh         # Push to GitHub
└── scripts/
    └── generate_proposal.py   # Word document generator
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
