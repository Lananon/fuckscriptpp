from bflang.bf import execute
from assembler.fucksembly import assemble
from fsppc.fsppc import compile
from sys import argv 



def main():
    if len(argv) > 1:
        file = open(argv[1]).read()
        if len(argv) > 2:
            if argv[2] == "bfasm":
                execute(assemble(file))
        print(compile(file))
    else:
        print("Usage: python3 main.py [file.bf] ([mode])")

if __name__ == "__main__":
    main()
