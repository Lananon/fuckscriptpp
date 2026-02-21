from collections import defaultdict

def execute(bf_file):
    code = bf_file
    data = defaultdict(int)
    ptr = 0

    current_op = 0
    while current_op < len(code):
        if code[current_op] == "+" :
            data[ptr] += 1
        elif code[current_op] == "-" :
            data[ptr] -= 1
        elif code[current_op] == ">" :
            ptr += 1
        elif code[current_op] == "<" :
            ptr -= 1
        elif code[current_op] == "." :
            print(data[ptr])
        elif code[current_op] == ",":
            data[ptr] = ord(input())
        elif code[current_op] == "[":
            if data[ptr] == 0:
                count = 1
                while count > 0:
                    current_op += 1
                    if code[current_op] == "[":
                        count += 1
                    elif code[current_op] == "]":
                        count -= 1
        elif code[current_op] == "]":
            if data[ptr] != 0:
                count = 1
                while count > 0:
                    current_op -= 1
                    if code[current_op] == "]":
                        count += 1
                    elif code[current_op] == "[":
                        count -= 1
        else:
            pass
        current_op += 1
    
