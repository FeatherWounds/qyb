#练习题1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print("1到100之间的素数:")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=' ')
print("\n")

#练习题2
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

print("斐波那契数列前20项:")
print(fibonacci(20))
print()

#练习题3
total = 0
num = 1
while num <= 10000:
    if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
        total += num
    num += 1

print("1-10000之间能被3或5整除但不能被15整除的数的和:", total)