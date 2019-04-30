#!/usr/bin/python
#-*-coding:utf8;-*-
def bf2py(code):
    depth = 0
    bf_code = "import sys\nfields = [0]\nindex = 0\n"
    for char in code:
        if char == ">":
            bf_code += "\t"*depth + "index += 1\n" + "\t"*depth + "if len(fields) - 1 < index:\n" + "\t"*depth + "\tfields.append(0)\n"
        elif char == "<":
            bf_code += "\t"*depth + "index -= 1\n"
        elif char == "+":
            bf_code += "\t"*depth + "fields[index] += 1\n"
        elif char == "-":
            bf_code += "\t"*depth + "fields[index] -= 1\n"
        elif char == ",":
            bf_code += "\t"*depth + "fields[index] = ord(sys.stdin.read(1))\n"
        elif char == ".":
            bf_code += "\t"*depth + "sys.stdout.write(chr(fields[index]))\n"
        elif char == "[":
            bf_code += "\t"*depth + "while fields[index] != 0:\n"
            depth += 1
        elif char == "]":
            if bf_code[-26:] == "while fields[index] != 0:\n":
                bf_code += "\t"*depth + "pass\n"
            depth -= 1
        else:
            pass
    return bf_code
    
def strip_code(code):
    clean_code = ""
    for char in code:
        if char in [">","<","+","-",".",",","[","]"]:
            clean_code += char
    return clean_code

def check_loops(code):
    depth = 0
    for char in code:
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
        else:
            pass
        if depth < 0:
            break
    return depth == 0
    
def ook2bf(code):
    in_group = False
    group = ["",""]
    bf_code = ""
    for ook in code.split(" "):
        if in_group:
            in_group = False
            group[1] = ook
            if group == ["Ook.","Ook."]:
                bf_code += "+"
            elif group == ["Ook!","Ook!"]:
                bf_code += "-"
            elif group == ["Ook.","Ook?"]:
                bf_code += ">"
            elif group == ["Ook?","Ook."]:
                bf_code += "<"
            elif group == ["Ook!","Ook?"]:
                bf_code += "["
            elif group == ["Ook?","Ook!"]:
                bf_code += "]"
            elif group == ["Ook!","Ook."]:
                bf_code += "."
            elif group == ["Ook.","Ook!"]:
                bf_code += ","
            else:
                pass
            group = ["",""]
        else:
            in_group = True
            group[0] = ook
    return bf_code
    
def bf2ook(code):
    ook_code = ""
    for char in code:
        if char == ">":
            bf_code += "Ook. Ook? "
        elif char == "<":
            bf_code += "Ook? Ook. "
        elif char == "+":
            bf_code += "Ook. Ook. "
        elif char == "-":
            bf_code += "Ook! Ook! "
        elif char == ".":
            bf_code += "Ook! Ook. "
        elif char == ",":
            bf_code += "Ook. Ook! "
        elif char == "[":
            bf_code += "Ook! Ook? "
        elif char == "]":
            bf_code += "Ook? Ook! "
        else:
            pass
    return bf_code[:-1]                #to remove " " from end
    
__all__ = ["bf2py","check_loops","strip_code","ook2bf","bf2ook"]

if __name__ == "__main__":
    exec(bf2py(input()))