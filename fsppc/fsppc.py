from sys import exit
from sys import stderr
from . import shortcuts as sc 

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def comp_error(error):
    stderr.write("ERROR: " + error)
    exit()

def parse(text):
    
    statements = text.replace("\n", "").split(";")
    return statements

def evaluate_expression(expression, mem_dict, mode, output):
    address = 0

    valid_operators = ["+", "-", "==", "!=", "||"]    
    components = []
    current_component = ""
    is_after_operator  = False
    for i in expression:
        if i != " " :
            current_component += i
        else:
            if not is_after_operator:
                if current_component in valid_operators:
                    is_after_operator = True
                components.append(current_component)
                current_component = ""
            
    components.append(current_component)

    if len(components) < 2:
        if is_number(components[0]):
            tempname = sc.gen_temp_name()
            return sc.allocate_set(tempname, components[0], mem_dict, output)
    elif len(components) == 3 and components[1] in valid_operators:
        
        match components[1]:
            case "+":
                target = sc.allocate_set("add_target", 0, mem_dict, output)
                pos1 = evaluate_expression(components[0], mem_dict, "address", output)
                pos2 = evaluate_expression(components[2], mem_dict, "address", output)
                result = sc.add(pos1, pos2, target, mem_dict, output)
                return result
            case _:
                comp_error("expression error: invalid operator")
        
    else:
        comp_error("expression error: invalid expression")
        


    if mode == "address":
        return address
    if mode == "components":
        return components


def compile(text):
    output = []
    statements = parse(text)
    # dict keeping track of variables and their location on the bf memory tape
    var_dict = {}
    for i in statements:
        tokens = i.split(" ")
        
        # declare new variable
        if tokens[0] == "var":
            if tokens[2] == "=":
                if tokens[1] in var_dict:
                    comp_error("variable defined twice")
                if not tokens[1] in var_dict:
                    sc.allocate_set(tokens[1], tokens[3], var_dict, output)
        
    text_output = "\n".join(output)
    return text_output

