#练习题1
numbers = [x for x in range(1, 101)]
even_numbers = [x for x in numbers if x % 2 == 0]
print("1-100之间的所有偶数:")
print(even_numbers)
print()

#练习题2
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

sample_list = [3, 2, 1, 2, 4, 3, 5, 1]
print("原始列表:", sample_list)
print("去重后的列表:", remove_duplicates(sample_list))
print()

#练习题3
keys = ["a", "b", "c"]
values = [1, 2, 3]
merged_dict = dict(zip(keys, values))
print("合并后的字典:")
print(merged_dict)
print()

#练习题4
student = ("张三", 20, 89.5)
name, age, score = student
print("学生信息解包:")
print(f"姓名: {name}")
print(f"年龄: {age}")
print(f"成绩: {score}")