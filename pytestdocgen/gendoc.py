from datetime import datetime
from itertools import chain, zip_longest
from pathlib import Path
from typing import Iterable, List, Tuple

import jinja2

from pytestdocgen.object import TestCase, TestDir

here: Path = Path(__file__).parent
# Jinja env with minor tweaks
j_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(str(here / "templates")),
    trim_blocks=True,
    lstrip_blocks=True,
)
# A template for test case
tc_template = j_env.get_template("test_case.md")
utc_now: str = datetime.utcnow().strftime("UTC %Y-%m-%d %H:%M:%S")


def next_section_to_template(
    former_section: Iterable[str], current_section: Iterable[str]
) -> Iterable[Tuple[int, str]]:
    """
    Find a section (structured directory scheme) to be rendered
    Args:
        former_section: A last section we rendered
        current_section: A current section we are working on

    Yields:
        Index(depth, 0-based) and the name of section

    """
    for fs_idx_value, cs_idx_value in zip_longest(
        enumerate(former_section), enumerate(current_section)
    ):
        if not fs_idx_value or (
            cs_idx_value and fs_idx_value[1] != cs_idx_value[1]
        ):
            yield cs_idx_value


def general_header(td: TestDir) -> str:
    """Produce general header"""
    title = "Test case documentation\n"
    title += len(title) * "=" + "\n"

    return (
        f'{title}<div style="text-align: right">'
        f"<p>version: {utc_now}</p>"
        f"</div>\n"
    )


def general_footer(td: TestDir) -> str:
    """Produce general footer"""
    return f"*documentation created by PyTestDocGen@{utc_now}*"


def worth_to_put_in_snippet(code_line: str) -> bool:
    """Check if a line of source code is worth to be in a code snippet"""
    if "async " in code_line or "def " in code_line:
        return True
    if code_line.strip().startswith("assert"):
        return True

    return False


def tc_to_markdown(tc: TestCase):
    """Render test case to markdown"""
    file_name = "/".join(
        chain([tc.file.root_dir.name], tc.rel_dir, [tc.file.file_name])
    )
    tc_position = (
        f"{tc.pos[0][0]}:{tc.pos[0][1]} - {tc.pos[1][0]}:{tc.pos[1][1]}"
    )
    code_snippet = "\n".join(
        [x for x in tc.code.splitlines() if worth_to_put_in_snippet(x)]
    )

    return tc_template.render(
        name=tc.name,
        file=file_name,
        pos=tc_position,
        snippet=code_snippet,
        summary=tc.parsed_doc.summary,
        description=tc.parsed_doc.description,
        sections=tc.parsed_doc.sections,
        decorators=tc.decorators,
    )


def td_to_markdown(
    td: TestDir, custom_header: str = None, custom_footer: str = None
) -> str:
    """
    Render TestDir to the Markdown string
    Args:
        td: Instantiated TestDir object
        custom_header: Custom header to put in the output
        custom_footer: Custom footer to put in the output

    Returns:
        Markdown string

    """
    result: List[str] = [custom_header] if custom_header else [
        general_header(td)
    ]
    result.append("\n")
    former_section: Iterable[str] = []
    former_page: str = ""

    for section in td.test_cases:
        for section_to_render in next_section_to_template(
            former_section, section
        ):
            if section_to_render[0] == 0:
                result.append("\n***\n")
            section_name = section_to_render[1].replace("_", " ")
            section_name = section_name[0].upper() + section_name[1:]

            section_str = "#" * (section_to_render[0] + 1) + " "
            section_str += section_name + "\n\n"

            result.append(section_str)
        former_section = section
        for tc in td.test_cases[section]:
            assert isinstance(tc, TestCase)
            if former_page != tc.file.page_name:
                result.append(
                    "#" * 4
                    + " Test Page: "
                    + tc.file.page_name.replace("_", " ")
                    + "\n"
                )
                former_page = tc.file.page_name
            result.append(tc_to_markdown(tc))

    if custom_footer:
        result.append(custom_footer)
    else:
        result.append(general_footer(td))
    result.append("\n")
    return "".join(result)
