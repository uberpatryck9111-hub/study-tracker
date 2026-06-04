def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_list(lst):
    if lst == []:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

def reverse(s):
    if s == "":
        return ""
    else:
        return reverse(s[1:]) + s[0]

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    print("--- Factorial ---")
    print(factorial(5))   # 120
    print(factorial(0))   # 1

    print("\n--- Sum List ---")
    print(sum_list([1, 2, 3, 4]))   # 10
    print(sum_list([]))             # 0

    print("\n--- Reverse ---")
    print(reverse("hello"))    # olleh
    print(reverse("python"))   # nohtyp

    print("\n--- Fibonacci ---")
    print(fib(1))    # 1
    print(fib(6))    # 8
    print(fib(10))   # 55