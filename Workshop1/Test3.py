def calc(operation, x, y):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == 'x':
        return x * y
    elif operation == '/':
        return x / y

def get_data():
    with open('Test3.txt', 'r') as file:
        return [line.strip() for line in file]

def get_next_instruction(last_instruction, data):
    if last_instruction == -1:
        return 0
    else:
        split = data[last_instruction + 1].rstrip().split(" ")
        if split[1] == "calc":
            return int(calc(split[2], int(split[3]), int(split[4])))
        else:
            return int(split[1])

def run():
    seen = []
    data = get_data()
    instruction = get_next_instruction(-1, data)
    while data[instruction] not in seen:
        print("Executing instruction " + data[instruction] + " on line " + str(instruction))
        seen.append(data[instruction])
        instruction = get_next_instruction(instruction, data)
        print(instruction, data[instruction])

    print("Instruction: " + data[instruction])
    print("Line: " + str(instruction))


if __name__ == "__main__":
    run()