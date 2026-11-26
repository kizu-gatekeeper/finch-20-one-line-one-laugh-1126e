"""One funny line, written out to entry.txt for make.fun."""

import os


LINE = "I told my smart speaker a secret, and now it whispers ads for therapy in a voice that sounds exactly like my mother."


def main():
    # Guard: never emit a blank entry.
    if not LINE.strip():
        raise ValueError("entry line must not be empty")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
