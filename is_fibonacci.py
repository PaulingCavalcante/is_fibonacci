def fibonacci(n):
    if n == 0 or n == 1:
        return True
    
    sequence = [0, 1]
    next_number = sequence[-1] + sequence[-2]
    
    while next_number <= n:
        if next_number == n:
            return True
        sequence.append(next_number)
        next_number = sequence[-1] + sequence[-2]
    return False

n = int(input("Type a number:"))
result = fibonacci(n)
print("The number belongs" if result else "The number is not belong")