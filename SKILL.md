---
name: research-grant-proposal
description: Generate Chinese-language academic nursing grant proposals based on research literature from CNKI, PubMed, and Wanfang. Use when the user asks for proposal writing, literature-backed sections, technical routes, or reference lists.
---

## Hard Rules (MUST FOLLOW)

1. Run databases in sequence only: **CNKI → PubMed → Wanfang**.
2. Keep **one browser tab only** during the full run.
3. Do not run database research in parallel.
4. Keep the same `targetId` across browser actions to prevent context drift.
5. Treat page operability by actionable refs, not by visual overlays.
6. Do not open article links via normal click if they may spawn a new tab; prefer `navigate` with the extracted URL in the same tab.
7. If a new tab opens accidentally, immediately close it and continue in the original `targetId`.
8. For **CNKI** and **Wanfang**, select **Chinese-language papers only**.
9. For **CNKI** and **Wanfang**, select **core-journal papers only** (for example: WJCI / 北大核心 / 科技核心 / CSCD / CSSCI, or an equivalent core label visible on the platform).
10. **All user project files MUST be stored in `workspace/research-projects/[课题名称]/`**.
    - NEVER store research data inside the skill directory (`skills/research-grant-proposal/`).
    - The skill directory is for tool definitions only; user data goes in workspace.
    - Use exec tool to run `openclaw browser ...` CLI commands as specified in research_guides.
11. **禁止混用浏览器工具接口**：
    - 全程统一使用 `exec` 工具执行 `openclaw browser ...` CLI 命令
    - 禁止混用 `browser` 工具（Agent Toolkit）
    - 混用会导致 CDP 协议错误，浏览器控制失败

## File Storage Convention

**Purpose:** Prevent user research data from being overwritten when skill is updated/reinstalled.

**Directory Structure:**
```
workspace/
├── research-projects/              ← 用户研究数据（每个课题独立目录）
│   └── [课题名称或日期]/
│       ├── cnki_results.md
│       ├── pubmed_results.md
│       ├── wanfang_results.md
│       ├── grant_proposal.md
│       ├── research_notes.md
│       └── issue_keywords.md
└── skills/                         ← 技能定义（仅模板/工具）
    └── research-grant-proposal/
        ├── SKILL.md
        ├── research_guides/
        └── research_notes_template.md
```

**Workflow for Each Project:**
1. Create directory: `workspace/research-projects/[课题名]/`
2. All output files go there (cnki_results.md, pubmed_results.md, etc.)
3. Read templates from skill directory, write outputs to project directory
4. When skill updates, user data remains safe in workspace

## Minimum Literature Requirements

- CNKI: 5-7 researched papers (**Chinese + core journals**)
- PubMed: 5-7 researched papers
- Wanfang: 5-7 researched papers (**Chinese + core journals**)
- Total: 15-21 researched references

## Workflow

### Step 0: 课题拆解与关键词规划 (NEW - 通用模板)

**目的：** 在开始检索前，系统化分析课题并生成检索矩阵

1. 读取 `issue_keywords.md` 通用模板
2. 根据用户课题，提取以下要素：
   - 理论基础
   - 护理理论
   - 研究对象
   - 干预措施
   - 应用场景
3. 使用模板中的规则生成关键词：
   - 理论扩展（同一理论的不同表达）
   - 概念组合（要素之间的排列组合）
   - 同义词扩展（疾病/人群的同义词）
4. 生成检索矩阵（按优先级排序）
5. 保存为 `issue_keywords.md`

**输出：** `issue_keywords.md`（后续检索的输入）
**写入位置：** `workspace/research-projects/[课题名]/issue_keywords.md`

### Step 1: Database Research (MANDATORY ORDER)

**前提：** Step 0 必须先完成，生成 `issue_keywords.md`

Read all three research guide files in order, using the keyword matrix from Step 0:

1. `research_guides/cnki.md` → produce `cnki_results.md`
   - 读取 `issue_keywords.md` 中的检索矩阵
   - 按优先级顺序执行检索
   
2. `research_guides/pubmed.md` → produce `pubmed_results.md`
   - 读取 `issue_keywords.md` 中的检索矩阵
   - 按优先级顺序执行检索
   
3. `research_guides/wanfang.md` → produce `wanfang_results.md`
   - 读取 `issue_keywords.md` 中的检索矩阵
   - 按优先级顺序执行检索

**Evidence-level research is mandatory for every selected paper.**

- **CNKI**: Wait **5 seconds** for each page to load after navigation. Capture `Abstract key points` (1-3 bullets) + `Relevance to topic` (one sentence). Capture `Core journal label`.
- **PubMed**: Capture `Abstract key points` (1-3 bullets) + `Relevance to topic` (one sentence).
- **Wanfang**: Capture `Abstract key points` (1-3 bullets) + `Relevance to topic` (one sentence). Capture `Core journal label`.

- If required evidence text is inaccessible, mark as **NOT RELEVANT** and replace it.
- If Chinese-language or core-journal constraints are not met for CNKI/Wanfang, mark as **NOT RELEVANT** and replace it.

### Step 2: Aggregate (MANDATORY GATE)

Read all three result files and produce `research_notes.md` using `research_notes_template.md`.
**Write to:** `workspace/research-projects/[课题名]/research_notes.md`

**Do not draft the proposal before all three result files exist and pass minimum counts.**

### Step 3: Draft Proposal (ONLY AFTER Step 2 Complete)

Generate final proposal sections using only researched references:
**Write to:** `workspace/research-projects/[课题名]/grant_proposal.md`

1. Main research content and objectives
2. **Rationale** (including purpose, significance, domestic/international overview, **market forecast**, and development trend)
3. R&D content and expected outputs
4. Methods and technical route (with process diagram)
5. Core references in the last 5 years

**In-text citation mapping is mandatory in proposal body.**
- Key claims must include bracket citations like `[1]`, `[3,7]`.
- Reference list numbering must map one-to-one with in-text citations.

## Complete Workflow Diagram

```
用户课题
    ↓
[Step 0] 课题拆解
    ↓
读取 issue_keywords.md 模板
    ↓
提取要素：理论基础 + 护理理论 + 研究对象 + 干预措施
    ↓
生成关键词：理论扩展 + 概念组合 + 同义词扩展
    ↓
生成检索矩阵（优先级排序）
    ↓
输出 issue_keywords.md
    ↓
[Step 1] 数据库检索
    ↓
cnki.md → 读取issue_keywords → 检索矩阵执行 → cnki_results.md
pubmed.md → 读取issue_keywords → 检索矩阵执行 → pubmed_results.md
wanfang.md → 读取issue_keywords → 检索矩阵执行 → wanfang_results.md
    ↓
[Step 2] 综合分析
    ↓
合并三个结果文件 + 分析研究空白 + 提炼创新点
    ↓
输出 research_notes.md
    ↓
[Step 3] 撰写申请书
    ↓
生成最终课题申请书
```

## Research Checklist

- [ ] `issue_keywords.md` exists (from Step 0)
- [ ] `cnki_results.md` exists with 5+ researched papers
- [ ] `pubmed_results.md` exists with 5+ researched papers
- [ ] `wanfang_results.md` exists with 5+ researched papers
- [ ] CNKI has 5+ papers with `ABSTRACT✓`, `CHINESE✓`, `CORE✓` and written abstract key points
- [ ] PubMed has 5+ papers with `ABSTRACT✓` and written abstract key points
- [ ] Wanfang has 5+ papers with `ABSTRACT✓`, `CHINESE✓`, `CORE✓` and written abstract key points
- [ ] `research_notes.md` merges all sources and includes evidence-to-claim mapping
- [ ] Final references count is 15+
- [ ] Proposal body includes in-text bracket citations mapped to final reference list

## Output

- Markdown draft in current session
- Optional DOCX export via `scripts/generate_proposal.py` or `textutil`

### 生成Word文档 (推荐)

完成markdown申请书后，使用 `generate_proposal.py` 脚本转换为Word文档：

**命令格式：**
```bash
cd /Users/abc/.openclaw/workspace/skills/research-grant-proposal/scripts
python3 generate_proposal.py --title "课题名称" --markdown "课题markdown文件路径" --output "输出文件路径"
```

**示例：**
```bash
python3 generate_proposal.py \
  --title "基于动机行为转化理论的Orem自理模式支持在股骨颈骨折合并糖尿病患者护理中的应用" \
  --markdown "/Users/abc/.openclaw/workspace/research-projects/股骨颈骨折合并糖尿病-Orem自理模式/grant_proposal.md" \
  --output "/Users/abc/.openclaw/workspace/research-projects/股骨颈骨折合并糖尿病-Orem自理模式/grant_proposal.docx"
```

**前提：** 需要安装 python-docx 模块
```bash
pip3 install python-docx
```

### Required Sections (Must Include)

1. **Main research content and objectives** (课题主要研究内容和预期目标)
2. **Rationale** (课题立题依据) - including:
   - Purpose (目的)
   - Significance (意义)
   - Domestic/international overview (国内外概况)
   - **Market forecast** (市场预测) ← ADDED
   - Development trend (发展趋势)
3. **R&D content and expected outputs** (课题研究、开发内容和预期成果)
4. **Methods and technical route** (研究方法和技术路线) - with process diagram
5. **Core references in the last 5 years** (近五年核心期刊参考文献)
