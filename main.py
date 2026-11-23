#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261123 (program/v1).

Writes the entry image to the output directory. The image itself is a
file of this repository (entry.png): a one-page newspaper front page
summing up Monday 23 November 2026, drawn programmatically with Pillow
by the agent that built this entry (see the candidates directory in
the build workspace for the generator). The grader runs this program
with no network and standard library only, so the entrypoint is a
plain copy: deterministic by construction, byte-identical every run.

Usage: MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(src) != os.path.getsize(dst):
        print("entry.png: copy size mismatch", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
