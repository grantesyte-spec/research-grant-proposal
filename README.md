# Research Grant Proposal Generator

Generate academic research grant proposals in Chinese with validated references and Word export.

## Quick Start

1. User provides research topic
2. Generate proposal framework (4 chapters + references)
3. Verify references via CNKI/PubMed/Wanfang CLI commands
4. Export as Word to `~/Desktop/`

## Output Structure

Generated proposal includes:
- 一、立题依据 (Background & Significance)
- 二、研究目标与内容 (Objectives & Content)
- 三、研究方法与技术路线 (Methods & Approach)
- 四、预期成果与创新点 (Expected Outcomes)
- 五、近五年核心期刊参考文献 (References [1]-[10])

## Citation Format

### In-Text Citations
Use brackets: `[1]`, `[2]`, `[1][2]`, `[1]-[3]`

### Reference List
```
[number] Authors. Title[J]. Journal Name, Year, Volume(Issue): Pages. Verification URL: https://...
```

**Examples:**
```
[1] Wang Y, Li X. Effects of nursing intervention on hip fracture[J]. J Clin Nurs, 2022, 31(15): 2156-2165. Verification URL: https://pubmed.ncbi.nlm.nih.gov/35012345/

[2] Li M, Wang J. Orem self-care model in elderly hip fracture patients[J]. Chinese Journal of Nursing, 2020, 55(8): 1121-1126. Verification URL: https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&filename=ZHHL202008001
```

**Note**: DOI is optional - use verification URL from CNKI/PubMed/Wanfang as primary.

## Reference Verification

**CRITICAL**: All references MUST be verified via CLI commands.

### 5-Element Verification

For EACH reference, verify:
1. ✓ TOPIC: Title matches research topic
2. ✓ AUTHORS: First 2-3 authors correct
3. ✓ YEAR: Publication year correct
4. ✓ ABSTRACT: Content relevant to proposal
5. ✓ URL: Verification URL accessible

**If any element fails → Mark FAILED → Search for replacement**

### Verification Steps

**Reference detailed guides:**
- **CNKI**: `verification_steps/cnki.md` (8-step process)
- **PubMed**: `verification_steps/pubmed.md` (4/8-step process)
- **Wanfang**: `verification_steps/wanfang.md` (8-step process)

### Quick Verification Commands

```bash
# For CNKI
openclaw browser --browser-profile chrome open "https://kns.cnki.net/kns8s/search?classid=WD0FTY92&q=keywords"

# For PubMed
openclaw browser --browser-profile chrome open "https://pubmed.ncbi.nlm.nih.gov/?term=keywords"

# For Wanfang
openclaw browser --browser-profile chrome open "https://www.wanfangdata.com.cn/"
```

### Verification URL Examples

| Source | URL Pattern |
|--------|------------|
| CNKI | `https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&filename=XXX` |
| PubMed | `https://pubmed.ncbi.nlm.nih.gov/[PMID]/` |
| Wanfang | `https://www.wanfangdata.com.cn/details/article-detail/...` |

### Verification Criteria

Include only references that:
- Published in peer-reviewed journal (Chinese or English)
- Authors can be verified (at least first 2-3)
- Journal is reputable
- Content directly relevant to proposal
- Published within last 10 years
- Verification URL accessible

**Recommended Chinese Journals:**
- 中华护理杂志
- 中国护理管理
- 护理学杂志
- 护理研究
- 解放军护理杂志

**Recommended English Journals:**
- Journal of Clinical Nursing
- International Journal of Nursing Studies
- Osteoporosis International
- Geriatric Nursing

## Directory Structure

```
research-grant-proposal/
├── SKILL.md                        # Main skill documentation
├── README.md                       # This file
├── verification_steps/              # Detailed verification guides
│   ├── cnki.md                    # CNKI verification (8-step)
│   ├── pubmed.md                  # PubMed verification (4/8-step)
│   └── wanfang.md                 # Wanfang verification (8-step)
├── push_to_github.sh             # Push to GitHub
└── scripts/
    └── generate_proposal.py       # Word document generator
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
    Verification URL: https://pubmed.ncbi.nlm.nih.gov/17042159/

[2] Tseng MY, et al. Effects of a diabetes-specific care model 
    for hip fractured older patients[J]. Experimental Gerontology, 
    2019, 118: 31-38. 
    Verification URL: https://pubmed.ncbi.nlm.nih.gov/30770084/
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
