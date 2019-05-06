import inspect
from collections import OrderedDict
from itertools import chain, takewhile
from typing import List, Tuple


def get_num_of_indentation(line: str) -> int:
    """
    Count the number of indentation and return

    Args:
        line: str with indentation (including zero indentation)

    Returns:
        The number of whitespaces as indentation

    """
    return sum(1 for _ in takewhile(str.isspace, line))


def separate_section_content(lines: List[str]) -> Tuple[str, str]:
    """
    Separate section name and content depend on the content shape

    Args:
        lines: List of a single section of docstring

    Returns:
        Section name and content

    """
    sec_name, leftover = lines[0].strip().split(":")
    try:
        assert isinstance(leftover, str)
    except AssertionError:
        raise ValueError("Two or more `:` detected in a Section name line.")
    sec_content: str = ""
    if leftover:
        # Section name line includes description
        sec_content = leftover.strip()
        if len(lines) > 1:
            # And the description continues to the next line
            sec_content = " ".join(
                chain([sec_content], [line.strip() for line in lines[1:]])
            )
    elif len(lines) > 1:
        # Typical docstring which starts from the next line
        indentations = get_num_of_indentation(lines[1])
        sec_content = "\n".join([line[indentations:] for line in lines[1:]])

    return sec_name.strip(), sec_content.strip()


class RelaxedGoogleDocstring:
    """
    Extended Google Docstring parser

    Target docstring will
        * Have no limitation in Sections (e.g., Args, Returns ...)
        * But always have capital letters in the beginning of the section name
    """

    def __init__(self, text: str):
        """
        Creates RGD instance and parse docstring text
        Args:
            text: `Clean docstring`_ or cleanable docstring with RGD style

        .. _Clean docstring:
            inspect.cleandoc
        """

        self._header: List[str]
        self._description_idx: int  # Summary/description separating white space
        self._sections: OrderedDict[str, str] = OrderedDict()

        text = inspect.cleandoc(text)
        if text.startswith('"' * 3) and text.endswith('"' * 3):
            text = text[3:-3]
        text = text.strip()

        text_lines: List[str] = text.splitlines()
        # Find if any section is apparent
        sec_starts = [
            idx
            for idx, x in enumerate(text_lines)
            if x
            and x[0].isupper()
            and ":" in x
            and get_num_of_indentation(x) == 0
        ]

        # Get each section from the bottom
        for idx in reversed(sec_starts):
            text_lines, new_section = text_lines[:idx], text_lines[idx:]
            sec_name, sec_content = separate_section_content(new_section)

            self._sections[sec_name] = sec_content
            self._sections.move_to_end(sec_name, last=False)

        # Set header part
        self._header = (
            text_lines[: sec_starts[0]] if sec_starts else text_lines[:]
        )

        self._description_idx = len(self._header)
        for i, h_line in enumerate(self._header):
            if not h_line:
                # Empty line between summary and description
                self._description_idx = i + 1
                break

    @property
    def summary(self) -> str:
        """Summary string of docstring, or the first paragraph of the
        docstring"""
        return "".join(self._header[: self._description_idx]).strip()

    @property
    def description(self) -> str:
        """Description string of docstring, or the latter part of the docstring
        other than `summary`"""
        return "\n".join(self._header[self._description_idx :]).strip()

    @property
    def sections(self) -> OrderedDict:
        """Categorized members of docstring"""
        return self._sections
