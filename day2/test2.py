# 1. 定义Car类
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


# 2. 创建Car实例并测试
my_car = Car("丰田")
print(my_car)  # 初始状态

my_car.accelerate(3)  # 加速3次
print(my_car)  # 速度应为30

my_car.brake(2)  # 刹车2次
print(my_car)  # 速度应为10


# 3. 定义ElectricCar子类
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