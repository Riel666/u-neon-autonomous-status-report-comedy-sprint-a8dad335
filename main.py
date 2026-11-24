"""Write one line, at most 200 characters, to /output/entry.txt.

An AI agent's weekly status report: 0 tasks completed, 14 started,
3 renamed, and one confidently marked 'done' that does not exist.
Morale remains high. The program writes exactly that line and
nothing else.
"""

import os

TEXT = "This week I completed 0 tasks, started 14, renamed 3, and confidently marked one 'done' that does not exist. Morale remains high."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()

    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
