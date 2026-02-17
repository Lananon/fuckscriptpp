from bflang.bf import execute
from fscriptc.fscriptc import compile
from assembler.fucksembly import assemble

from sys import argv 


def main():
    if len(argv) > 1:
        bf_file = open(argv[1]).read()
        # execute(compile(bf_file))
        print(assemble(bf_file))
    else:
        print("Usage: python3 main.py [file.bf]")

if __name__ == "__main__":
    main()
