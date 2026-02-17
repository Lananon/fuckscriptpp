def parse(fscript_file):
    ops = []
    current_op = 0
    valid_ops = [">", "<", "+", "-", "[", "]", ".", ","]
    arg_ops = [">", "<", "+", "-"]
    
    while current_op < len(fscript_file):
        op = ""
        if fscript_file[current_op] in valid_ops:
            op = fscript_file[current_op]
            if op in arg_ops:
                while fscript_file[current_op + 1].isdigit():
                    op += fscript_file[current_op +1]
                    current_op += 1
            ops.append(op)
        current_op += 1
    return ops



def compile(fscript_file):
    valid_ops = [">", "<", "+", "-", "[", "]", ".", ","]
    arg_ops = [">", "<", "+", "-"]
    
    op_list = parse(fscript_file)
    output = ""
    for op in op_list:
        opcode = op[0]
        if opcode in valid_ops:
            if not opcode in arg_ops:
                output += opcode
            if opcode in arg_ops:
                if len(op) > 1:
                    true_len = len(op)
                    val = op[1:true_len]
                    for i in range(int(val)):
                        output += opcode
                else:
                    output += opcode

    return output
