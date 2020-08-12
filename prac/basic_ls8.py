import sys

PRINT_STATEMENT = 1
HALT = 2
SAVE_REGISTER = 3
PRINT_REGISTER = 4
ADD = 5


# memory = [
#     1,  # PRINT STATEMENT
#     3,  # SAVE_REGISTER R2,64
#     2,  # R2
#     64,  # 64
#     4,  # PRINT REGISTER R2
#     2,  # R2
#     3,  # SAVE_REGISTER R3,55
#     3,  # R3
#     55,  # 55
#     4,  # PRINT REGISTER R3
#     3,  # R2
#     2   # HALT
# ]

statement = 'LS-8'
memory = [0] * 256
register = [0] * 8

# ----------- LOAD PROGRAM ------------------

with open('prog1') as f:
    for line in f:
        line = line.split("#")
        value = int(line[0])

        print(value)

sys.exit(0)


# ------------ RUN LOOP -----------------

program_counter = 0

running = True

while running:
    instruction = memory[program_counter]

    if instruction == PRINT_STATEMENT:  # PRINT_STATEMENT
        print(statement)
        program_counter += 1

    elif instruction == HALT:  # HALT
        running = False

    elif instruction == SAVE_REGISTER:  # SAVE_REG
        register_num = memory[program_counter + 1]
        value = memory[program_counter + 2]

        register[register_num] = value
        program_counter += 3

    elif instruction == PRINT_REGISTER:  # PRINT_REGISTER
        register_num = memory[program_counter + 1]
        print(register[register_num])

        program_counter += 2

    elif instruction == ADD:
        register_num1 = memory[program_counter + 1]
        register_num2 = memory[program_counter + 2]
        register[register_num1] += register[register_num2]
        program_counter += 3

    else:
        print(f'Unknow instruction {instruction} at address {program_counter}')
        sys.exit(1)
