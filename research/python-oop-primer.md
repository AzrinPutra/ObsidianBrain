# Python面向对象编程入门指南

## 1. 类（Class）与对象（Object）
- 类比：蓝图（类） vs 具体房屋（对象）
- 代码示例：
class Smartphone:
    pass

my_phone = Smartphone()

## 2. __init__方法与属性
- 类比：手机出厂设置（初始化配置）
- 代码示例：
class Smartphone:
    def __init__(self, brand):
        self.brand = brand

phone = Smartphone('Xiaomi')

## 3. 实例变量 vs 类变量
- 类比：个人手机壳（实例） vs 默认出厂壁纸（类）
- 代码示例：
class Smartphone:
    default_os = 'Android'
    
    def __init__(self, model):
        self.model = model

## 4. 继承概念
- 类比：旗舰机型继承基础款功能
- 代码示例：
class CameraPhone(Smartphone):
    def take_photo(self):
        print("Taking 48MP photo")

## 5. 封装实践
- 类比：隐藏电池管理芯片
- 代码示例：
class Battery:
    def __init__(self):
        self.__health = 100
    
    def check_health(self):
        return self.__health
