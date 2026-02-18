from sys import exit
from sys import stderr

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def comp_error(error):
    stderr.write("ERROR: " + error)
    exit()

def set_var(var_name, value, var_list):
    address = var_list.index(var_name)
    output = "\npnt " + str(address) + "\nset " + str(value)
    return output
    

def parse(text):
    
    statements = text.replace("\n", "").split(";")
    return statements

def compile(text):
    output = ""
    statements = parse(text)
    # list keeping track of variables and their location on the bf memory tape
    var_list = []
    for i in statements:
        tokens = i.split(" ")
        
        # declare new variable
        if tokens[0] == "var":
            if tokens[2] == "=":
                if tokens[1] in var_list:
                    comp_error("variable defined twice")
                if not tokens[1] in var_list:
                    var_list.append(tokens[1])
                    output += set_var(tokens[1], int(tokens[3]), var_list)
        
        # set existing variable
        if tokens[0] in var_list:
            if tokens[1] == "=":
                if is_number(tokens[2]):
                    output += set_var(tokens[0], int(tokens[2]), var_list)


    return output

