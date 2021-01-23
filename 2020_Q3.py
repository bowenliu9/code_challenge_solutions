# 2020 Q3
input = [5, [44, 62],[34,69],[24,78], [42,44], [64,10]]

max_pair = [0,0] # since minimum is 0, 0
min_pair = [float('inf'), float('inf')]  # remember to use float('inf'), not INF, or 10000

for pair in input[2::]:
    if pair[0] > max_pair[0]:
        # larger than max_x
        max_pair[0] = pair[0]+1
    elif pair[0] < min_pair[0]:
        # smaller than min_x
        min_pair[0] = pair[0]-1
    
    if pair[1] > max_pair[1]:
        # larger than max_y
        max_pair[1] = pair[1]+1
    elif pair[1] < min_pair[1]:
        # smaller than min_y
        min_pair[1] = pair[1]-1
        
print(max_pair, min_pair)