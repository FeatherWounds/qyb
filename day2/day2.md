# 学习笔记

## python

### 一、函数与模块

#### 1.函数定义与调用
```python
# 判断回文数
def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

print("121是回文数吗?", is_palindrome(121))  # True
print("123是回文数吗?", is_palindrome(123))  # False
print()
```

#### 2.模块与导入
```python
# 创建模块
def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)

from test1 import area, perimeter

print("矩形面积:", area(5, 3))      # 15
print("矩形周长:", perimeter(5, 3))  # 16
```

### 二、面向对象编程基础

#### 1.属性与方法
```python
# 定义Car类
class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand  # 品牌
        self.speed = speed  # 速度

    def accelerate(self, m):
        """加速方法，m次每次增加10"""
        self.speed += 10 * m
        return self

    def brake(self, n):
        """刹车方法，n次每次减少10，不低于0"""
        self.speed = max(0, self.speed - 10 * n)
        return self

    def __str__(self):
        return f"{self.brand}汽车，当前速度: {self.speed}"
```

#### 2.继承：子类继承父类的属性和方法
```python
# 定义ElectricCar子类
class ElectricCar(Car):
    def __init__(self, brand, speed=0, battery=50):
        super().__init__(brand, speed)
        self.battery = battery  # 电量

    def charge(self, times=1):
        """充电方法，每次增加20，不超过100"""
        self.battery = min(100, self.battery + 20 * times)
        return self

    def __str__(self):
        return f"{self.brand}电动汽车，当前速度: {self.speed}，电量: {self.battery}%"


# 测试ElectricCar
my_electric = ElectricCar("特斯拉")
print(my_electric)  # 初始状态

my_electric.accelerate(2).charge(3)  # 加速2次，充电3次
print(my_electric)  # 速度20，电量110会被限制为100

my_electric.brake(1)  # 刹车1次
print(my_electric)  # 速度10，电量100
```
### 三、文件操作与异常处理和模块与标准库
```python
# 批量更改图片文件名为txt文件中里面的名字，注意顺序一致
import os
import re

def natural_sort_key(s):
    def convert(text):
        if text.isdigit():
            num_val = int(text)
            # 如果是以0开头的数字，返回一个特殊的元组使其排在普通数字之前
            if text.startswith('0') and len(text) > 1:
                return (num_val - 0.5, text)
            return (num_val, text)
        return text.lower()

    return [convert(p) for p in re.split('([0-9]+)', s)]

def rename_images():
    # 设置文件路径
    folder_path =r"C:\Users\FeatherWounds\OneDrive\桌面\新建文件夹"
    txt_path = r"C:\Users\FeatherWounds\OneDrive\桌面\新建文本文档.txt"

    # 读取txt文件中的新名称
    with open(txt_path, 'r', encoding='utf-8') as f:
        new_names = [name.strip() for name in f.readlines() if name.strip()]

    # 获取所有图片文件并按Windows自然顺序排序
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    image_files.sort(key=natural_sort_key)  # 使用自然排序

    # 确保文件数量匹配
    if len(image_files) != len(new_names):
        print(f"警告：图片数量({len(image_files)})与名字数量({len(new_names)})不匹配！")
        return

    # 首先显示排序和重命名预览
    print("\n=== 文件重命名预览 ===")
    for i, (old_name, new_name) in enumerate(zip(image_files, new_names), 1):
        print(f"[{i}] {old_name} -> {new_name}.png")

    # 询问用户是否继续
    user_input = input("\n请确认排序是否正确？(y/n): ")
    if user_input.lower() != 'y':
        print("操作已取消")
        return

    # 执行实际的重命名操作
    print("\n=== 开始重命名文件 ===")
    for i, (old_name, new_name) in enumerate(zip(image_files, new_names), 1):
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, f"{new_name}.png")

        try:
            os.rename(old_path, new_path)
            print(f"[{i}] 成功: {old_name} -> {new_name}.png")
        except Exception as e:
            print(f"[{i}] 失败: {old_name} -> {new_name}.png")
            print(f"错误信息: {str(e)}")

if __name__ == "__main__":
    rename_images()
```
## numpy

### 1.数组创建与属性分析
```python
import numpy as np
#创建3x4的二维数组
arr = np.arange(1, 13).reshape(3, 4)
print("原始数组:\n", arr)

#任务1：打印数组属性
print("\n1. 数组属性:")
print("形状:", arr.shape)
print("维度:", arr.ndim)
print("数据类型:", arr.dtype)

#任务2：元素乘以2
print("\n2. 元素乘以2:\n", arr * 2)

#任务3：重塑为4x3
reshaped_arr = arr.reshape(4, 3)
print("\n3. 重塑后的数组(4x3):\n", reshaped_arr)
```
### 2.数组索引与切片
```python
import numpy as np
# 创建4x4数组
array = np.array([[1, 2, 3, 4], 
                 [5, 6, 7, 8], 
                 [9, 10, 11, 12], 
                 [13, 14, 15, 16]])

# 任务1：提取第2行(索引为1)
print("1. 第2行:\n", array[1, :])

# 任务2：提取第3列(索引为2)
print("\n2. 第3列:\n", array[:, 2])

# 任务3：提取子数组(行1-2, 列2-3)
print("\n3. 子数组:\n", array[0:2, 1:3])

# 任务4：条件替换
array[array > 10] = 0
print("\n4. 修改后的数组:\n", array)
```
### 3.数组运算与广播
```python
import numpy as np
# 创建数组A和B
A = np.arange(1, 7).reshape(3, 2)
B = np.array([10, 20])

print("数组A:\n", A)
print("数组B:\n", B)

# 任务1：逐元素相加
print("\n1. A + B:\n", A + B)

# 任务2：逐元素相乘
print("\n2. A * B:\n", A * B)

# 任务3：每行与B的点积
print("\n3. 点积结果:\n", np.dot(A, B))
```