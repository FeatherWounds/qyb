# 1. 判断回文数
def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

print("121是回文数吗?", is_palindrome(121))  # True
print("123是回文数吗?", is_palindrome(123))  # False
print()

# 2. 计算任意数量参数的平均值
def calculate_average(*args):
    return sum(args) / len(args) if args else 0

print("1, 2, 3, 4的平均值:", calculate_average(1, 2, 3, 4))  # 2.5
print()

# 3. 返回最长的字符串
def find_longest_string(*strings):
    return max(strings, key=len, default=None)

print("最长的字符串:", find_longest_string("apple", "banana", "cherry"))  # "banana"
print()

# 4. 创建模块
def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)