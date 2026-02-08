# Research Grant Proposal Skill (研究课题申请书技能)

A Claude/Codex skill for generating academic research grant proposals in Chinese with validated references and Word document export.

## Features

- 📝 **Chinese Academic Format**: Proper formatting following Chinese academic standards
- 📄 **Word Export**: Generate professional `.docx` documents
- ✅ **Validated References**: Step-by-step verification workflow for academic sources
- 🎯 **Pre-built Templates**: Ready-to-use templates for nursing/medical research
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
"Create a grant proposal titled 'Collaborative Care Combined with Prospective Nursing Management in Type 2 Diabetes Patients with Osteoporotic Intertrochanteric Femoral Fractures'"
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

## Reference Verification

All references MUST be verified before including in proposals.

### Verification Steps

1. **Search**: Use Google Scholar, ScienceDirect, CNKI
2. **Verify**: Check authenticity, DOI, citation count
3. **Document**: Record verification status for each reference
4. **Quality Check**: Ensure peer-reviewed, relevant, accessible

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
    【验证: Google Scholar】被引用15次
```

## Directory Structure

```
research-grant-proposal/
├── SKILL.md                    # Skill documentation with verification workflow
├── README.md                   # This file
├── push_to_github.sh          # Push to GitHub
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

## Output Format

Generated Word documents include:
- Chinese academic formatting (宋体字体)
- Hierarchical headings (16pt/14pt/12pt)
- Reference section with verified citations
- Tables for metrics and team composition
- Professional document structure

## Requirements

- Python 3.7+
- python-docx library

## Push to GitHub

```bash
cd research-grant-proposal
./push_to_github.sh
```

## License

MIT License

## Contributing

Feel free to submit issues and pull requests!
