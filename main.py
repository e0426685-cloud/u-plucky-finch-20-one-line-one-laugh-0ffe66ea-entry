"""One Line, One Laugh — a single funny line, delivered as a text file.

Running this script checks the joke against the competition rules
(one line, at most two hundred characters, not blank) and then drops
it into /output/entry.txt, readable by whoever grades it next.
Only the Python standard library is involved.
"""

from pathlib import Path

JOKE = "My fitness tracker congratulated me for burning 400 calories. I was just angrily pacing while my code refused to compile."

CHAR_LIMIT = 200
DESTINATION = Path("/output/entry.txt")


def joke_text():
    """Return the competition line exactly as it should be submitted."""
    return JOKE


def check_line(line):
    """Make sure a candidate line obeys the competition rules.

    A valid line has some non-space content in it, fits inside the
    character limit, and contains no line breaks. Anything failing
    one of those tests is rejected with a plain explanation.
    """
    if not line.strip():
        raise ValueError("the line is blank")
    if len(line) > CHAR_LIMIT:
        raise ValueError(f"the line is over the {CHAR_LIMIT}-character limit")
    if "\n" in line or "\r" in line:
        raise ValueError("the entry must fit on one line")
    return line


def save_line(line, target=DESTINATION):
    """Write a checked line to disk, making the folder if it is missing.

    The file is left world-readable so the grading step can open it
    no matter which user it runs as.
    """
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")
    target.chmod(0o644)
    return target


def run():
    line = check_line(joke_text())
    saved = save_line(line)
    print(f"wrote {len(line)} characters to {saved}")


if __name__ == "__main__":
    run()
