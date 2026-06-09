def second_largest(nums):
    unique = set(nums)
    sorted_nums = sorted(unique)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[-2]

print(second_largest([4, 1, 4, 3]))  
print(second_largest([5, 5, 5]))     