def blocks_used():
    blocks_remaining = int(input("Enter the number of blocks remaining: "))
    current_layer = 1
    blocks_required = current_layer * current_layer
    if blocks_remaining == 0:
        return 0
    while blocks_remaining >= (current_layer ** 2):
        blocks_remaining -= current_layer ** 2
        print(blocks_remaining)
        current_layer += 1
        print(current_layer)
    return blocks_remaining

print(blocks_used())