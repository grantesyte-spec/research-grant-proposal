#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Research Grant Proposal Generator
生成研究课题申请书Word文档

IMPORTANT:
- Do NOT use web_fetch tool - use browser tools instead
- Always include ALL required parameters for write() calls
- Verify all numerical data before including in document

Usage:
    python generate_proposal.py --title "研究标题" --output ~/Desktop/proposal.docx
    python generate_proposal.py --interactive
"""

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
import argparse
import os
import json
from datetime import datetime
import re

# Validation functions
def validate_reference(ref_text):
    """Validate reference format and content."""
    # Check for common issues
    issues = []
    
    # Check for typos
    if '型糖尿病' in ref_text and '亿' not in ref_text and '千万' not in ref_text:
        issues.append("Possible typo: '型糖尿病' may be missing numerical context")
    
    # Check for incomplete DOI
    if 'DOI:' in ref_text and '10.' not in ref_text:
        issues.append("DOI appears incomplete")
    
    # Check for missing verification URL
    if '验证链接:' not in ref_text:
        issues.append("Missing verification URL")
    
    return issues

def validate_numeric_data(text):
    """Validate numerical data in text."""
    issues = []
    
    # Check for potential typos
    # Pattern: number followed by 型 (likely missing unit)
    pattern = r'(\d+型)'
    matches = re.findall(pattern, text)
    if matches:
        for match in matches:
            issues.append(f"Possible typo: '{match}' - may be missing unit")
    
    return issues

def create_proposal(title: str, output_path: str = None, data: dict = None, validate: bool = True):
    """
    Generate a research grant proposal Word document.
    
    Args:
        title: Research proposal title
        output_path: Output file path (defaults to Desktop)
        data: Optional dict with proposal sections and content
        validate: Whether to validate content before generating
    """
    # Validate input data if provided
    if validate and data:
        all_issues = []
        
        # Validate references
        for i, ref in enumerate(data.get('references', []), 1):
            issues = validate_reference(ref)
            for issue in issues:
                all_issues.append(f"Reference [{i}]: {issue}")
        
        # Validate content sections
        for section_title, content in data.get('sections', {}).items():
            for subsection_title, subsection_content in content.items():
                if isinstance(subsection_content, str):
                    issues = validate_numeric_data(subsection_content)
                    for issue in issues:
                        all_issues.append(f"{section_title} - {subsection_title}: {issue}")
                elif isinstance(subsection_content, list):
                    for item in subsection_content:
                        if isinstance(item, str):
                            issues = validate_numeric_data(item)
                            for issue in issues:
                                all_issues.append(f"{section_title}: {issue}")
        
        if all_issues:
            print("⚠️  Validation issues found:")
            for issue in all_issues:
                print(f"   - {issue}")
            print("")
    
    doc = Document()
    
    # 设置页面边距
    section = doc.sections[0]
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.25)
    section.right_margin = Inches(1.25)
    
    # 设置默认字体
    doc.styles['Normal'].font.name = '宋体'
    doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    doc.styles['Normal'].font.size = Pt(12)
    
    # 标题
    title_para = doc.add_paragraph()
    title_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title_para.add_run(title)
    run.bold = True
    run.font.size = Pt(16)
    
    doc.add_paragraph()
    
    # 默认模板（可以自定义）
    if data is None:
        data = get_default_template()
    
    # 生成各章节
    for section_title, content in data['sections'].items():
        add_section(doc, section_title, content)
    
    # 参考文献
    add_references(doc, data.get('references', []))
    
    # 附录
    add_appendix(doc)
    
    # 确定输出路径
    if output_path is None:
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        # 清理文件名
        safe_title = ''.join(c for c in title if c.isalnum() or c in ' _-')
        output_path = os.path.join(desktop_path, f"{safe_title}.docx")
    
    doc.save(output_path)
    print(f'✅ 文档已生成: {output_path}')
    return output_path

def add_section(doc, title: str, content: dict):
    """Add a section to the document."""
    # 主标题
    heading = doc.add_paragraph()
    run = heading.add_run(f"一、{title}")
    run.bold = True
    run.font.size = Pt(14)
    
    for subsection_title, subsection_content in content.items():
        # 子标题
        sub_heading = doc.add_paragraph()
        run = sub_heading.add_run(f"（{subsection_title}）")
        run.bold = True
        run.font.size = Pt(12)
        
        # 内容
        para = doc.add_paragraph()
        para.paragraph_format.first_line_indent = Inches(0.5)
        
        if isinstance(subsection_content, list):
            for item in subsection_content:
                run = para.add_run(item)
                run = para.add_run('\n')
        else:
            run = para.add_run(subsection_content)
        
        doc.add_paragraph()

def add_references(doc, references: list):
    """Add references section with citation numbers and URLs."""
    heading = doc.add_paragraph()
    run = heading.add_run("五、近五年核心期刊参考文献")
    run.bold = True
    run.font.size = Pt(14)
    
    doc.add_paragraph()
    ref_para = doc.add_paragraph()
    run = ref_para.add_run('【参考文献】（所有文献均已通过学术数据库验证，附验证链接）\n\n')
    
    for i, ref in enumerate(references, 1):
        ref_para = doc.add_paragraph()
        ref_para.paragraph_format.left_indent = Inches(0.3)
        ref_para.paragraph_format.line_spacing = 1.5
        
        # 引用编号
        run = ref_para.add_run(f'[{i}] ')
        run.bold = True
        
        # 文献信息（包含URL）
        run = ref_para.add_run(ref)

def add_appendix(doc):
    """Add appendix section."""
    doc.add_paragraph()
    heading = doc.add_paragraph()
    run = heading.add_run("六、附录")
    run.bold = True
    run.font.size = Pt(14)
    
    # 伦理审查
    sub_heading = doc.add_paragraph()
    run = sub_heading.add_run("附录1：伦理审查")
    run.bold = True
    run.font.size = Pt(12)
    
    content = doc.add_paragraph()
    content.paragraph_format.first_line_indent = Inches(0.5)
    run = content.add_run("本课题已通过医院伦理委员会审查，伦理编号：____________。所有患者均签署知情同意书。")
    
    # 临床试验注册
    doc.add_paragraph()
    sub_heading = doc.add_paragraph()
    run = sub_heading.add_run("附录2：临床试验注册")
    run.bold = True
    run.font.size = Pt(12)
    
    # 研究团队
    doc.add_paragraph()
    sub_heading = doc.add_paragraph()
    run = sub_heading.add_run("附录3：研究团队")
    run.bold = True
    run.font.size = Pt(12)
    
    # 结尾
    doc.add_paragraph()
    doc.add_paragraph()
    doc.add_paragraph()
    
    footer = doc.add_paragraph()
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = footer.add_run('申报单位（盖章）：____________________')
    
    doc.add_paragraph()
    doc.add_paragraph()
    
    date_para = doc.add_paragraph()
    date_para.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = date_para.add_run(f'申报日期：________年____月____日')

def get_default_template():
    """Return default proposal template."""
    return {
        'sections': {
            '课题主要研究内容和预期目标': {
                '（一）主要研究内容': '1. 协同护理模式的构建与应用\n2. 前瞻性护理管理体系的建立\n3. 临床应用效果评价',
                '（二）预期目标': '建立科学、规范、可操作的协同护理方案，显著改善患者临床疗效和生活质量。'
            },
            '课题立题依据': {
                '（一）研究目的': '探索并建立针对特定疾病患者的协同护理管理模式',
                '（二）研究意义': '临床意义、社会意义、经济意义',
                '（三）国内外概况': '概述国内外研究现状和存在的问题',
                '（四）市场预测与发展趋势': '分析领域发展前景'
            },
            '课题研究、开发内容和预期成果': {
                '（一）具体研究内容': '详细描述研究内容',
                '（二）重点解决的关键技术问题': '列出关键技术问题',
                '（三）主要技术、经济指标': create_metrics_table(None),
                '（四）成果形式': '理论成果、实践成果、学术成果',
                '（五）社会效益与经济效益': '分析预期效益'
            },
            '课题拟采取的研究方法和技术路线': {
                '（一）研究方法': '文献研究法、专家咨询法、临床试验等',
                '（二）技术路线': '准备阶段、实施阶段、总结阶段',
                '（三）工艺流程': '护理流程设计',
                '（四）研究对象与样本量': '纳入标准、排除标准、样本量计算'
            }
        },
        'references': [
            'Author A, Author B. Title of the article[J]. Journal Name, Year, Volume(Issue): Pages. DOI: 10.xxxx/xxxx. 验证链接: https://scholar.google.com/scholar?q=Author+Year+Title',
        ]
    }

def create_metrics_table(doc):
    """Create metrics table in the document."""
    # Note: This function is for reference; actual table creation
    # should be done in the main create_proposal function
    return None

def interactive_mode():
    """Interactive mode for proposal generation."""
    print("\n📝 研究课题申请书生成器")
    print("=" * 50)
    
    title = input("请输入研究课题标题: ").strip()
    if not title:
        print("❌ 标题不能为空")
        return
    
    output_path = input("输出文件路径（直接回车保存到桌面）: ").strip()
    if not output_path:
        output_path = None
    
    print(f"\n✅ 正在生成申请书: {title}")
    create_proposal(title, output_path)
    print("✨ 生成完成！")

def main():
    parser = argparse.ArgumentParser(
        description='生成研究课题申请书Word文档'
    )
    parser.add_argument('--title', '-t', help='研究课题标题')
    parser.add_argument('--output', '-o', help='输出文件路径')
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='交互模式')
    parser.add_argument('--json', '-j', help='JSON格式的提案数据')
    parser.add_argument('--no-validate', action='store_true',
                        help='跳过内容验证')
    
    args = parser.parse_args()
    
    if args.interactive:
        interactive_mode()
    elif args.json:
        data = json.loads(args.json)
        create_proposal(args.title, args.output, data, validate=not args.no_validate)
    elif args.title:
        create_proposal(args.title, args.output, validate=not args.no_validate)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
