#练习题1
x = 10
y = "10"
z = True

print(f"x 的类型是: {type(x)}")  # <class 'int'>
print(f"y 的类型是: {type(y)}")  # <class 'str'>
print(f"z 的类型是: {type(z)}")  # <class 'bool'>
#练习题2
π = 3.14
radius = float(input("请输入圆的半径: "))
area = π * radius ** 2
print(f"圆的面积为: {area}")
#练习题3
num_str = "3.14"

# 转换为浮点数
float_num = float(num_str)
print(f"转换为浮点数: {float_num} (类型: {type(float_num)})")  # 3.14 <class 'float'>

# 转换为整数
int_num = int(float_num)
print(f"转换为整数: {int_num} (类型: {type(int_num)})")  # 3 <class 'int'>

# 观察差异
print(f"转换差异: 浮点数保留小数部分 {float_num}, 而整数部分截断为 {int_num}")