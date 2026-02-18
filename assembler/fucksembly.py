def assemble(text):
    lines = text.split("\n")
    lines = list(filter(None, lines))
    output = ""    

    
    position = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        tokens = line.split(" ")
        opcode = tokens[0]
        args = tokens
        args.pop(0)
        try:
            val = int(args[0])
        except:
            val = 1
        
        i += 1

        if opcode == "pnt":
            if position > val:
                for n in range(position - val):
                    output += "<"
                    position -= 1
            if position < val:
                for n in range(val - position):
                    output += ">"
                    position += 1

        if opcode == "mvr":
            for n in range(val):
                output += ">"
                position += 1
        if opcode == "mvl":
            for n in range(val):
                output += "<"
                position -= 1

        if opcode == "set":
            output += "[-]"
            if val > 0:
                for n in range(val):
                    output += "+"
            if val < 0:
                for n in range(val):
                    output += "-"
        
        if opcode == "inc":
            for n in range(val):
                output += "+"
        if opcode == "dec":
            for n in range(val):
                output += "-"
        
        if opcode == "[":
            output += "["
        if opcode == "]":
            output += "]"

        if opcode == "out":
            output += "."
        if opcode == "inp":
            output += ","

    return output
