import string 

alpha_num_map = {
    "a": 1
}

letters = string.ascii_letters[:26]
numbers = [i for i in range(26)] 

for i in range(len(numbers)):
    alpha_num_map[letters[i]] = numbers[i] + 1
    alpha_num_map[letters[i].upper()] = numbers[i] + 1 + 26

print(alpha_num_map)


def parse_input():
    """
    Generate a list of rucksack items.
    """
    moves = list() 
    with open('day3/input.txt') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
        
        return lines
    
    


rucksacks = parse_input()

print (rucksacks)    

priority_sum = 0 
for rucksack in rucksacks: 
    print(rucksack)
    mid = int(len(rucksack) / 2)
    # print(mid)
    
    left_sack = set(rucksack[:mid])
    right_sack = set(rucksack[mid:]) 
    
    common_item = list(left_sack.intersection(right_sack))[0]
    priority_sum += alpha_num_map[common_item]
    
    
print(f"Part one: {priority_sum}")
    
rucksack_group = list()     
priority_sum = 0 
for rucksack in rucksacks: 
    rucksack_group.append(set(rucksack))
    
    if len(rucksack_group) == 3: 
        common_item = list(rucksack_group[0] & rucksack_group[1] & rucksack_group[2])[0]
        priority_sum += alpha_num_map[common_item]
        rucksack_group = list()


print(f"Part two: {priority_sum}")