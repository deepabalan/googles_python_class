

def remove_adjacent(nums):
    i = 0
    t = []
    for num in nums:
        if num not in t:
            t.append(num)
    return t
print remove_adjacent([1, 2, 2, 3])
print remove_adjacent([2, 2, 3, 3, 3])
print remove_adjacent([])
