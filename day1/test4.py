# 1. 给定字符串 s1
s1 = "Python is a powerful programming language"
s2 = "Let's learn together"

# (1) 提取单词 "language"
words = s1.split()
last_word = words[-1]
print("最后一个单词:", last_word)

# (2) 将s1与s2连接，并重复输出3次
combined = s1 + " " + s2
print((combined + "\n") * 3)

# (3) 输出所有以p或P开头的单词
p_words = [word for word in words if word.lower().startswith('p')]
print("以p或P开头的单词:", p_words)
print()

# 2. 对字符串 s3 进行操作
s3 = "Hello, World! This is a test string. "

# (1) 去除字符串前后的空格
s3_stripped = s3.strip()
print("去除空格后的字符串:", s3_stripped)

# (2) 将所有字符转换为大写
s3_upper = s3_stripped.upper()
print("大写转换后的字符串:", s3_upper)

# (3) 查找子串 "test" 的起始下标
test_index = s3_stripped.find("test")
print("'test'的起始下标:", test_index)

# (4) 将 "test" 替换为 "practice"
s3_replaced = s3_stripped.replace("test", "practice")
print("替换后的字符串:", s3_replaced)

# (5) 以空格为分隔符分割字符串，并使用 "--" 连接
s3_split = s3_stripped.split()
s3_joined = "--".join(s3_split)
print("分割并连接后的字符串:", s3_joined)