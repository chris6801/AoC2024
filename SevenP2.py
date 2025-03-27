

def create_tree(numbers):
    if not numbers:
        return []
        
    def build_tree(index, running_total):
        # Base case: if we've used all numbers, return the final value
        if index >= len(numbers):
            return [running_total]
            
        # Get the next number to operate with
        next_num = numbers[index]
        
        # Calculate children values
        add_result = running_total + next_num
        mult_result = running_total * next_num
        
        # Create node with current running_total and its children
        return [running_total, 
                build_tree(index + 1, add_result), 
                build_tree(index + 1, mult_result)]
    
    # Start with first number
    return build_tree(1, numbers[0])
    
def get_final_layer(tree):
    if not tree:
        return []
    if len(tree) == 1:  # Leaf node found
        return [tree[0]]
    return get_final_layer(tree[1]) + get_final_layer(tree[2])

with open('seven.txt') as f:
    data = f.readlines()
    data = [item.strip().split(': ') for item in data]
    result = []
    for line in data:
        sub = []
        for item in line:
            if ' ' in item:
                sub.extend(map(int, item.split()))
            else:
                sub.append(int(item))
            print('sub', sub)
        result.append(sub)
        
data = result
total = 0

for line in data:
    solution = line[0]
    nums = line[1:]
    tree = create_tree(nums)
    final_layer = get_final_layer(tree)
    if solution in final_layer:
        total += solution
        
print(total)
    
