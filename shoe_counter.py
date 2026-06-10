from collections import Counter
n = int(input())
shoe_size = list(map(int, input().split()))  # fix: int, not int(
shoe_counter = Counter(shoe_size)            # fix: shoe_size not shoe_counter_size
x = int(input())
income = 0
for i in range(x):
    size, price = map(int, input().split())
    if shoe_counter[size] > 0:               
        income += price
        shoe_counter[size] -= 1              

print(income)