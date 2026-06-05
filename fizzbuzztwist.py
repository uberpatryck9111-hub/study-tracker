def fizzbuzz(numbers):
    result = []
    for n in numbers:                          # ← missing loop
        if n % 3 == 0 and n % 5 == 0:         # ← need 'and'
            result.append("FizzBuzz")          # ← closing quote
        elif n % 3 == 0:
            result.append("Fizz")
        elif n % 5 == 0:                       # ← colon after condition
            result.append("Buzz")
        else:
            result.append(str(n))
    return result