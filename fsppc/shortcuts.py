def find_free_temp_mem(temp_mem_dict):
    i = -1
    while i in temp_mem_dict:
        i -= 1
    return i

def add(pos1, pos2, target_pos, temp_mem_dict):
    temp_pos = find_free_temp_mem(temp_mem_dict)
    
    output = ""
    output += copy(target_pos, pos1, temp_mem_dict)
    output += "\npnt " + str(temp_pos) + "\nset 0"
    output += "\npnt " + str(pos2)
    output += "\n[\npnt " + str(target_pos)
    output += "\ninc\npnt " + str(temp_pos) + "\ninc"
    output += "\npnt " + str(pos2) + "\ndec\n]"
    output += "\npnt " + str(temp_pos) + "\n["
    output += "\npnt " + str(pos2) + "\ninc\npnt " + str(temp_pos) + "\ndec\n]"

    return output

def sub(pos1, pos2, target_pos, temp_mem_dict):
    temp_pos = find_free_temp_mem(temp_mem_dict)
    
    output = ""
    output += copy(target_pos, pos1, temp_mem_dict)
    output += "\npnt " + str(temp_pos) + "\nset 0"
    output += "\npnt " + str(pos2)
    output += "\n[\npnt " + str(target_pos)
    output += "\ndec\npnt " + str(temp_pos) + "\ninc"
    output += "\npnt " + str(pos2) + "\ndec\n]"
    output += "\npnt " + str(temp_pos) + "\n["
    output += "\npnt " + str(pos2) + "\ninc\npnt " + str(temp_pos) + "\ndec\n]"

    return output

def copy(target_pos, copied_pos, temp_mem_dict):
    temp_pos = find_free_temp_mem(temp_mem_dict)

    output = "\n"
    output += "pnt " + str(target_pos)
    output += "\nset 0\npnt " + str(temp_pos) + "\nset 0"
    output += "\npnt " + str(copied_pos) + "\n["
    output += "\npnt " + str(target_pos) + "\ninc"
    output += "\npnt " + str(temp_pos) + "\ninc"
    output += "\npnt " + str(copied_pos) + "\ndec\n]"
    output += "\npnt " + str(temp_pos) + "\n["
    output += "\npnt " + str(copied_pos) + "\ninc"
    output += "\npnt " + str(temp_pos) + "\ndec\n]"

    return output 
    
    

mem = {}

print(sub(2, 4, 5, mem))
