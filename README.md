# Research Grant Proposal Generator

Generate academic research grant proposals in Chinese based on REAL literature research.

## ⚠️ IMPORTANT: Research-First Workflow

**You MUST do research BEFORE generating any proposal.**

### The Correct Order:

```
STEP 1: Research (Required)     ← DO THIS FIRST
  ├── Search CNKI for Chinese literature
  ├── Search PubMed for English literature  
  ├── Search Wanfang for supplementary
  └── Save findings to research_notes.md

STEP 2: Analyze & Select
  ├── Review search results
  └── Select 10-15 quality references

STEP 3: Generate Proposal
  └── Write based on REAL research findings

STEP 4: Final Verification
  └── Verify all references
```

### The Wrong Order (❌ DO NOT DO THIS):

```
User provides topic → Generate proposal → Find references
```

---

## Quick Start

1. User provides research topic
2. I search CNKI/PubMed/Wanfang for real literature
3. I record findings in research_notes.md
4. I select 10-15 verified references
5. I generate proposal based on real research
6. Export to Word at `~/Desktop/`

---

## Output Structure

Generated proposal includes:
- 1. Background & Significance
- 2. Objectives & Content
- 3. Methods & Technical Approach
- 4. Expected Outcomes & Innovation
- 5. References

---

## Citation Format

**In-Text Citations:**
`[1]`, `[2]`, `[1][2]`, `[1]-[3]`

**Reference List:**
```
[number] Authors. Title[J]. Journal Name, Year, Volume(Issue): Pages. Verification URL: https://...
```

**Examples:**
```
[1] Wang Y, Zhang X, Liu J. Effects of nursing intervention on hip fracture[J]. J Clin Nurs, 2022, 31(15): 2156-2165. Verification URL: https://pubmed.ncbi.nlm.nih.gov/35012345/

[2] Li M, Wang J. Orem self-care model in elderly hip fracture patients[J]. Chinese Journal of Nursing, 2021, 56(8): 1121-1126. Verification URL: https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&filename=ZHHL202108001
```

**Note**: All references come from actual research, not fabricated.

---

## Research Process

### Step 1: Search Databases

```bash
# CNKI
openclaw browser --browser-profile chrome open "https://kns.cnki.net/kns8s/AdvSearch?classid=WD0FTY92&rlang=CHINESE"
openclaw browser --browser-profile chrome type e18 "keywords" --submit

# PubMed  
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/"
openclaw browser --browser-profile chrome type e14 "keywords" --submit

# Wanfang
openclaw browser --browser-profile chrome open "https://www.wanfangdata.com.cn/"
```

### Step 2: Record Findings

Create `research_notes.md` with:
- Search keywords used
- Total results found
- Relevant articles with full citations
- Selected references for proposal

### Step 3: Generate Proposal

Only AFTER research is complete.

---

## Directory Structure

```
research-grant-proposal/
├── SKILL.md                        # Main skill (RESEARCH-FIRST workflow)
├── README.md                       # This file
├── verification_steps/              # Detailed verification guides
│   ├── cnki.md                    # CNKI verification
│   ├── pubmed.md                  # PubMed verification
│   └── wanfang.md                 # Wanfang verification
├── push_to_github.sh             # Push to GitHub
└── scripts/
    └── generate_proposal.py       # Word document generator
```

---

## Supported Topics

- Collaborative care models
- Prospective nursing management
- Chronic disease management
- Orthopedic nursing
- Diabetes nursing
- Osteoporosis research
- Hip fracture care

---

## Output Example

**In-text:**
```
Collaborative care models can significantly reduce postoperative complications[1][2], 
through individualized interventions by multidisciplinary teams, 
patient glycemic control rate improved to over 85%[3].
```

**References:**
```
References

[1] Moran WP, et al. Using a collaborative approach to reduce 
    postoperative complications for hip-fracture patients[J]. 
    The Joint Commission Journal, 2006, 32(11): 573-584. 
    Verification URL: https://pubmed.ncbi.nlm.nih.gov/17042159/

[2] Tseng MY, et al. Effects of a diabetes-specific care model 
    for hip fractured older patients[J]. Experimental Gerontology, 
    2019, 118: 31-38. 
    Verification URL: https://pubmed.ncbi.nlm.nih.gov/30770084/
```

---

## Push to GitHub

```bash
cd research-grant-proposal
./push_to_github.sh
```

---

## Requirements

- Python 3.7+
- python-docx library

---

## License

MIT License

---

## Contributing

Feel free to submit issues and pull requests!
