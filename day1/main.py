sample_input = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def parse_input():
    all_elf_calories = list() 
    with open('day1/input.txt') as f:
        lines = f.readlines()
        elf_cals = 0 
        for line in lines:
            line = line.strip()
            if line:
                elf_cals += int(line) 
            else: 
                all_elf_calories.append(elf_cals)
                elf_cals = 0 
                
        all_elf_calories.append(elf_cals)

    return all_elf_calories


def part_one(): 
    all_elf_calories = parse_input()
    return max(all_elf_calories)

def part_two(): 
    all_elf_calories = parse_input() 
    all_elf_calories.sort(reverse=True) 
    return all_elf_calories[:3]
    
    
    
        
answer1 = part_one() 
print(f"First Answer: {answer1} calories")

answer2 = part_two()
print(f"Second Answer: {sum(answer2)} calories")
