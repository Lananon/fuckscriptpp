import string
import random

def gen_temp_name():
    output = "tmp_"
    output += "".join(random.choice(string.ascii_uppercase) for  _ in range(6))
    return output

def free(alloc, mem_dict):
    mem_dict.pop(alloc)

def find_free_mem(mem_dict):
    i = 0
    while i in list(mem_dict.values()):
        i += 1
    return i

def allocate_set(alloc_name, value, mem_dict, output):
    pos = find_free_mem(mem_dict)
    mem_dict.update({alloc_name: pos})
    output.append(f"pnt {pos}")
    output.append(f"set {value}")
    return pos

def add(pos1, pos2, target_pos, mem_dict, output):
    temp_pos = find_free_mem(mem_dict)
    
    copy(target_pos, pos1, mem_dict, output)
    output.append(f"pnt {str(temp_pos)}")
    output.append("set 0")
    output.append(f"pnt {str(pos2)}")
    output.append("[")
    output.append(f"pnt {str(target_pos)}")
    output.append("inc")
    output.append(f"pnt {str(temp_pos)}")
    output.append("inc")
    output.append(f"pnt {str(pos2)}")
    output.append("dec")
    output.append("]")
    output.append(f"pnt {str(temp_pos)}")
    output.append("[")
    output.append(f"pnt {str(pos2)}")
    output.append("inc")
    output.append(f"pnt {str(temp_pos)}")
    output.append("dec")
    output.append("]")

    return target_pos

def sub(pos1, pos2, target_pos, mem_dict, output):
    temp_pos = find_free_mem(mem_dict)
    
    copy(target_pos, pos1, mem_dict, output)
    output.append(f"pnt {str(temp_pos)}")
    output.append("set 0")
    output.append(f"pnt {str(pos2)}")
    output.append("[")
    output.append(f"pnt {str(target_pos)}")
    output.append("dec")
    output.append(f"pnt {str(temp_pos)}")
    output.append("inc")
    output.append(f"pnt {str(pos2)}")
    output.append("dec")
    output.append("]")
    output.append(f"pnt {str(temp_pos)}")
    output.append("[")
    output.append(f"pnt {str(pos2)}")
    output.append("inc")
    output.append(f"pnt {str(temp_pos)}")
    output.append("dec")
    output.append("]")

    return target_pos

def copy(target_pos, copied_pos, mem_dict, output):
    temp_pos = find_free_mem(mem_dict)

    output.append(f"pnt {str(target_pos)}")
    output.append(f"set 0")
    output.append(f"pnt {str(temp_pos)}")
    output.append(f"set 0")
    output.append(f"pnt {str(copied_pos)}")
    output.append("[")
    output.append(f"pnt {str(target_pos)}")
    output.append("inc")
    output.append(f"pnt {str(temp_pos)}")
    output.append("inc")
    output.append(f"pnt {str(copied_pos)}")
    output.append("dec")
    output.append("]")
    output.append(f"pnt {str(temp_pos)}")
    output.append("[")
    output.append(f"pnt {str(copied_pos)}")
    output.append("inc")
    output.append(f"pnt {str(temp_pos)}")
    output.append("dec")
    output.append("]")
    
    return target_pos

