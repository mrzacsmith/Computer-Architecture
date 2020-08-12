memory = [
    1,  # PRINT STATEMENT
    3,  # SAVE_REGISTER R2,64
    2,  # R2
    64,  # 64
    4,  # PRINT REGISTER R2
    2,  # R2
    3,  # SAVE_REGISTER R3,55
    3,  # R3
    55,  # 55
    4,  # PRINT REGISTER R3
    3,  # R2
    2   # HALT
]

statement = 'LS-8'

register = [0] * 8

program_counter = 0

running = True

while running:
    instruction = memory[program_counter]

    if instruction == 1:  # PRINT_STATEMENT
        print(statement)
        program_counter += 1

    elif instruction == 2:  # HALT
        running = False

    elif instruction == 3:  # SAVE_REG
        register_num = memory[program_counter + 1]
        value = memory[program_counter + 2]

        register[register_num] = value
        program_counter += 3

    elif instruction == 4:  # PRINT_REGISTER
        register_num = memory[program_counter + 1]
        print(register[register_num])

        program_counter += 2

    else:
        print(f'Unknow instruction')
