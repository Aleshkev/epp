import pathlib
import re
import sys
import lib


def verify_integrity(source, output):
    # TODO: This is a very slow heuristic. Please do something about it.
    import subprocess

    def run(code):
        pathlib.Path("__a.cpp").write_text(code, "utf-8")
        p = subprocess.run("g++ __a.cpp -o __a -std=c++11".split(), capture_output=True)
        return p.stderr.decode("utf-8")

    a_stderr = run(source)
    if "error" in a_stderr:
        print(f"Compilation error in the input file.")
        return

    b_stderr = run(output)

    if a_stderr != b_stderr:
        if a_stderr != b_stderr:
            print("Compiler stderr doesn't match.", "---", a_stderr, "---", b_stderr, sep="\n", file=sys.stderr)
            sys.exit(66)
    else:
        print("Verified correctly.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Improves clarity of C++ code")
    parser.add_argument("source", nargs="?", help="file to read input from; default: stdin")
    output_type = parser.add_mutually_exclusive_group()
    output_type.add_argument("output", nargs="?", help="file to write output to; default: stdout")
    parser.add_argument("--rename", "-r", action="store_true", help="improve token names? Sometimes doesn't work")
    parser.add_argument("--verify", "-v", action="store_true", help="verify whether transformation was correct? "
                                                                    "Requires globally installed g++")
    output_type.add_argument("--tokens", "-t", action="store_true", help="print tokens in debug mode?")
    parser.add_argument("--rename-operators", "-o", action="store_true", help="improve operator names? "
                                                                              "Very often doesn't work")

    args = parser.parse_args()

    source = pathlib.Path(args.source).read_text("utf-8") if args.source else sys.stdin.read()
    target = pathlib.Path(args.output) if args.output else None

    tokens = lib.tokenize(source)

    assert len(tokens) > 0, "No tokens generated: maybe input file is empty?"

    if args.rename:
        tokens = lib.rename_tokens(tokens, args.rename_operators)
    else:
        assert not args.rename_operators, "May be used only with --rename."

    if target:
        target.write_text(lib.serialize(tokens), "utf-8")
    else:
        if args.tokens:
            print("\n".join(map(str, tokens)))
            print(f"Total of {len(tokens)} tokens.")
        else:
            print(lib.serialize(tokens))

    if args.verify:
        verify_integrity(source, lib.serialize(tokens))
