import sys


f = open('program.b','r')
program = f.read()

def match_closing_bracket(program, index):
    stack = []
    stack.append(index)
    index -= 1

    while index >= 0:
        if program[index] == ']':
            stack.append(index)
        elif program[index] == '[':
            if(len(stack) == 1):
                return index
            stack.pop()
        index -= 1

def match_bracket(program, index):
    stack = []
    stack.append(index)
    index += 1

    while index < len(program):
        if program[index] == '[':
            stack.append(index)
        elif program[index] == ']':
            if(len(stack) == 1):
                return index
            stack.pop()
        index += 1



tape = [0] * 30000
pointer = 0




p_pointer = 0
while p_pointer < len(program):

    c = program[p_pointer]

    if c == '>':
        pointer += 1
    elif c == '<' and pointer > 0:
        pointer -= 1
    elif c == '+':
        tape[pointer] += 1
    elif c == '-':
        tape[pointer] -= 1
    elif c == '.':
        sys.stdout.write(chr(tape[pointer] % 256))
        
    elif c == ',':
        tape[pointer] = ord(raw_input("Type a char: ")[0])
        
    elif c == '[':
        if tape[pointer] == 0:
            p_pointer = match_bracket(program, p_pointer)

    elif c == ']':
        if not tape[pointer] == 0:
            p_pointer = match_closing_bracket(program, p_pointer)


    p_pointer += 1





    
