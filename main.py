from bflang.bf import execute
from assembler.fucksembly import assemble
from fsppc.fsppc import compile
from sys import argv 



def main():
    if len(argv) > 1:
        bf_file = open(argv[1]).read()
        print(compile(bf_file))
    else:
        print("Usage: python3 main.py [file.bf]")

if __name__ == "__main__":
    main()
