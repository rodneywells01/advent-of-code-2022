def parse_input(): 
    with open('day5/input.txt') as f:
        lines = f.readlines()
        separation_line = 0 
        num_columns = 0
        
        for idx in range(len(lines)):
            # Determine number of cols and separation line in the input file. 
            if len(lines[idx]) and lines[idx][1] == "1": 
                num_columns = int(lines[idx].rstrip()[-1])
                separation_line = idx 
                break 
            
        raw_stacks, raw_commands = lines[:separation_line], lines[separation_line + 2:]
        start_idx = 1 
        space_to_next_char = 4
        formatted_stacks = list() 
        
        # Format the columns into lists.
        for column in range(num_columns):
            current_idx = start_idx + column * space_to_next_char
            stack = list() 
            
            for stack_num in range(separation_line): 
                next_char = raw_stacks[separation_line - (stack_num + 1)][current_idx]        
                if next_char.isalpha():
                    stack.append(next_char)
                else: 
                    break
                
            formatted_stacks.append(stack) 
            
    return formatted_stacks, [line.rstrip() for line in raw_commands]

def parse_command(raw_command): 
    command = raw_command.split()
    qty = int(command[1])
    source = int(command[3]) - 1
    destination = int(command[5]) - 1 
    return qty, source, destination

def solve_part_one(stacks, commands):
    for command in commands:
        qty, source, destination = parse_command(command)
        source_size = len(stacks[source])
        
        # Move each crate
        for crate_idx in range(qty): 
            stacks[destination].append(stacks[source][source_size - crate_idx - 1])
            stacks[source].pop()
        
    return stacks

def solve_part_two(stacks, commands):
    for command in commands:
        qty, source, destination = parse_command(command)
        source_size = len(stacks[source])
        
        # Move all crates together. 
        stacks[destination] = stacks[destination] + stacks[source][source_size-qty:]
        stacks[source] = stacks[source][:source_size-qty]
        
    return stacks
    
stacks, commands = parse_input() 
sorted_part_one = solve_part_one(stacks, commands)
top_crates = ''.join(stack[-1] for stack in stacks)
print(f"Part One Top Crates: {top_crates}")

stacks, commands = parse_input() 
sorted_part_two = solve_part_two(stacks, commands)
top_crates = ''.join(stack[-1] for stack in stacks)
print(f"Part Two Top Crates: {top_crates}")
