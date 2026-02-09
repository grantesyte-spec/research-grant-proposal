# Research Grant Proposal Generator

**Skill ID**: research-grant-proposal

Generate academic research grant proposals in Chinese based on REAL literature research and validated references.

---

## Quick Start

```
User provides topic → Search databases → Generate proposal → Export to Word
```

---

## Workflow (3 Steps)

### Step 1: Research
```
read cnki.md      # CNKI search → cnki_results.md
read pubmed.md    # PubMed search → pubmed_results.md
read wanfang.md   # Wanfang search → wanfang_results.md
```

### Step 2: Aggregate
```
read cnki_results.md
read pubmed_results.md
read wanfang_results.md
# Combine into research_notes.md
```

### Step 3: Generate
```
# Using research_notes.md
# Export to: ~/Desktop/[Topic]课题申请书.docx
```

---

## When to Use

| Need | Use |
|------|-----|
| Chinese nursing literature | cnki.md |
| English biomedical literature | pubmed.md |
| Chinese supplementary | wanfang.md |
| Generate final proposal | SKILL.md |

---

## Citation Format

```
[1] Authors. Title[J]. Journal, Year, Volume: Pages. DOI. Verification: URL
```

---

## Directory Structure

```
research-grant-proposal/
├── SKILL.md                 # Main skill (full specification)
├── README.md                # This file (quick reference)
├── verification_steps/
│   ├── cnki.md             # CNKI guide
│   ├── pubmed.md           # PubMed guide
│   └── wanfang.md          # Wanfang guide
└── scripts/
    └── generate_proposal.py
```

---

## Golden Rules

1. Research FIRST → then generate
2. Verify ALL references before citing
3. Use RIGHT file for RIGHT database
4. Record findings in *_results.md files
