#!/usr/bin/env python3
"""
Generate a DOCX grant proposal from structured sections and references.

Usage:
  python scripts/generate_proposal.py --title "Your Title" --output ~/Desktop/proposal.docx
  python scripts/generate_proposal.py --title "Your Title" --json-file proposal.json
"""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from typing import List, Dict

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH


@dataclass
class ProposalData:
    sections: Dict[str, Dict[str, str]]
    references: List[str]


def default_data() -> ProposalData:
    return ProposalData(
        sections={
            "I. Main research content and expected objectives": {
                "(1) Main research content": "Describe intervention model, target population, and implementation scope.",
                "(2) Expected objectives": "Define measurable clinical and management outcomes."
            },
            "II. Rationale": {
                "(1) Purpose and significance": "Explain why this topic matters clinically and socially.",
                "(2) Domestic and international status": "Summarize evidence landscape and key gaps.",
                "(3) Trend and development outlook": "Describe market and discipline development trends."
            },
            "III. R&D content and expected outputs": {
                "(1) Specific research content": "List work packages and deliverables.",
                "(2) Key technical problems": "List critical bottlenecks and solutions.",
                "(3) Expected outputs and benefits": "List papers, protocols, and practical value."
            },
            "IV. Methods and technical route": {
                "(1) Methods": "Describe design, population, outcomes, and statistics.",
                "(2) Technical route": "Provide step-by-step route from screening to analysis.",
                "(3) Process flow": "Add text flowchart description for implementation."
            },
        },
        references=[]
    )


def apply_doc_style(doc: Document) -> None:
    section = doc.sections[0]
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(12)


def add_title(doc: Document, title: str) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(title)
    run.bold = True
    run.font.size = Pt(16)
    doc.add_paragraph()


def add_sections(doc: Document, sections: Dict[str, Dict[str, str]]) -> None:
    for section_title, subsection_map in sections.items():
        h = doc.add_paragraph()
        hr = h.add_run(section_title)
        hr.bold = True
        hr.font.size = Pt(14)

        for subsection_title, content in subsection_map.items():
            sh = doc.add_paragraph()
            sr = sh.add_run(subsection_title)
            sr.bold = True
            sr.font.size = Pt(12)

            p = doc.add_paragraph(content if content else "")
            p.paragraph_format.first_line_indent = Inches(0.3)
            p.paragraph_format.line_spacing = 1.5

        doc.add_paragraph()


def add_references(doc: Document, refs: List[str]) -> None:
    h = doc.add_paragraph()
    hr = h.add_run("V. Core references in the last 5 years")
    hr.bold = True
    hr.font.size = Pt(14)

    if not refs:
        doc.add_paragraph("No references provided.")
        return

    for i, ref in enumerate(refs, 1):
        p = doc.add_paragraph(f"[{i}] {ref}")
        p.paragraph_format.line_spacing = 1.5


def build_docx(title: str, output: str, data: ProposalData) -> str:
    doc = Document()
    apply_doc_style(doc)
    add_title(doc, title)
    add_sections(doc, data.sections)
    add_references(doc, data.references)

    output = os.path.expanduser(output)
    os.makedirs(os.path.dirname(output), exist_ok=True)
    doc.save(output)
    return output


def load_data(json_file: str | None) -> ProposalData:
    if not json_file:
        return default_data()
    with open(json_file, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return ProposalData(
        sections=raw.get("sections", default_data().sections),
        references=raw.get("references", []),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate grant proposal DOCX")
    parser.add_argument("--title", required=True, help="Proposal title")
    parser.add_argument("--output", default="~/Desktop/grant-proposal.docx", help="Output .docx path")
    parser.add_argument("--json-file", help="JSON file containing sections and references")
    args = parser.parse_args()

    data = load_data(args.json_file)
    out = build_docx(args.title, args.output, data)
    print(f"Generated: {out}")


if __name__ == "__main__":
    main()
