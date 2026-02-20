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

def set_var(var_name, value, var_dict):
    address = var_dict[var_name]
    output = "\npnt " + str(address) + "\nset " + str(value)
    return output
    

def parse(text):
    
    statements = text.replace("\n", "").split(";")
    return statements

def evaluate_expression(expression, mem_dict, mode):
    address = 0
    output = ""

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

    if is_number(components[0]):
        temp_mem_location = sc.find_free_mem(mem_dict)
        output += "\npnt " + str(temp_mem_location)
        output += "\nset " + components[0]
    
    if mode == "address":
        return address
    if mode == "output":
        return output
    if mode == "components":
        return components
    


def compile(text):
    output = ""
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
                    var_pos = sc.find_free_mem(var_dict)
                    var_dict.update({tokens[1]: var_pos})
                    output += set_var(tokens[1], int(tokens[3]), var_dict)
        


    return output

print(evaluate_expression("2 + 2 + 2", "", "components"))
