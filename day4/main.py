def parse_input():
    """
    Generate a list of rucksack items.
    """
    lines = list() 
    with open('day4/input.txt') as f:
        # pairs = [pair.split("-") for pair in  [line.rstrip().split(",") for line in f.readlines()]]
        pairs = [line.rstrip().split(",") for line in f.readlines()]
        print(pairs)
        return pairs




pairs = parse_input()

# Part 1 
total_contained_pairs = 0 
for pair in pairs:
    # 2 <= 6 and 4 >= 8 or 6 <=2 and 8>=4 
    left = [int(x) for x in pair[0].split("-")]
    right = [int(x) for x in pair[1].split("-")]

    # Overlap 
    if (left[0] <= right[0] and left[1] >= right[1] ) or (right[0] <= left[0] and right[1] >= left[1]): 
        # print(pair)
        # print(left , right) 
        total_contained_pairs += 1 

print(total_contained_pairs)

# Part 2 
total_contained_pairs = 0 
for pair in pairs:
    # Intersection 
    left = [int(x) for x in pair[0].split("-")]
    right = [int(x) for x in pair[1].split("-")]

    if (left[0] <= right[1] and left[1] >= right[0] ):
        # print(pair)
        # print(left , right) 
        total_contained_pairs += 1 

print(total_contained_pairs)
            
    
    