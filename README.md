# Research Grant Proposal Skill (研究课题申请书技能)

A Claude/Codex skill for generating academic research grant proposals in Chinese with proper formatting, validated references, and Word document export.

## Features

- 📝 **Chinese Academic Format**: Proper formatting following Chinese academic standards
- 📄 **Word Export**: Generate professional `.docx` documents
- ✅ **Validated References**: All references verified through academic databases
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
"Generate a research grant proposal about collaborative nursing care"
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

# With JSON data
python scripts/generate_proposal.py --title "研究课题标题" --json data.json
```

## Directory Structure

```
research-grant-proposal/
├── SKILL.md                    # Skill documentation
├── scripts/
│   └── generate_proposal.py    # Word document generator
└── README.md                   # This file
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
- Reference section with validated citations
- Tables for metrics and team composition
- Professional document structure

## Requirements

- Python 3.7+
- python-docx library

## License

MIT License

## Contributing

Feel free to submit issues and pull requests!
