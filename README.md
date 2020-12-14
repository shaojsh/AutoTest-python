# 模块1： AutoTest-python(web UI selenium )
# 去除webDriver特性：（反爬虫用）https://blog.csdn.net/MICHAELKING1/article/details/108322795
# 12306抢票 https://zhuanlan.zhihu.com/p/48077823
UI测试+接口测试(PYTHON 3.6)
pip freeze > requirements.txt
pip install -r requirements.txt

# 模块2:  小程序自动化技术：Airtest

# 模块3: 性能测试 locust
windows10 
python -m pip install locust  --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
locust 参数介绍：https://www.cnblogs.com/imyalost/p/9758189.html

python知识库总结：https://github.com/taizilongxu/interview_python
1.在python中函数参数传递分为
    .可变对象：sit，dict,list 函数内对对象的重新引用或者修改会永久改变该对象的值
    .不可变对象 string,tuple,number 在函数内引用时 ‘=’ 函数内引用对象可变，走出j函数后，对象引用恢复如初
2.python 中有元类的定义，譬如 list  [1,2,3] 前者时后者的元类
3.反射：所谓反射，即对自己属性方法的判断修改，python 中有非常强大的自省功能（即反射功能）  ： type(),dir(),getattr(),hasattr(),isinstance()，object.__setattr__，object.__delattr__
4.python 中的staticmethod 与classmethod
    .staticmethod 为类的静态方法，可通过object.方法名直接引用  static_foo(x):
    .classmethod  为类方法 与静态方法使用基本差别不大，表现形式略有不同 class_foo(cls,x)
    .实例方法 先初始化实例进行调用  self 引用  foo(self,x):
5.python中单画线 _ 双画线 __ 以及双边画线的区别
    . _  表示python类中的私有属性
    . __ 标识python中方法的私有方法
    . __a__ 标识python中自定义的属性
6.字符串格式化:%和.format
    %s 用来标识字符串代替符时比较方便
    format 用来标识列表替代方法
7.迭代器与生成器
    .从某种意义上来讲，迭代器就是生成器，与列表相比，它可标记下一个元素存在的内存位置，比列表更节省空间
8.*args and **kwargs
    . *args  可传递任意数量的参数 (1,2,.....) 
    . **kwargs 可传递任意数量，指定参数名字的参数 (param1 = '',param2 = '',.....)
9.装饰器 
    .所谓装饰器即函数作为参数传入对函数进行处理 @staticmethod  即为系统自带的装饰器 装饰器即为面向切面编程AOP编程
10.鸭子类型 ：支持类形式上的泛型
    .鸭子类型是python表现多态的一种形式：多态即为调用一种方法有不同的表现形式
11.python 的重载： python无重载
    .重载是在功能相同的基础上 参数形式不一样或者个数不一样为了代码简洁而成的java中的一种行为模式，在python中无重载，原因如下：
        1.python本身自带buff,参数无需定义类型
        2.python 可用 *args 的参数代表多个参数的传递
12.python中的新式类和经典类
    1.python2.x 中默认的都是新式类 除非显示继承object
    2.python3.x 中默认的都是经典类
13.python中的单例模式：单例模式应用场景：用于每次初始化都需要占用资源的实例   当一个类只有一个实例时，就是单例模式
    1.应用于logger 模块的引入也是单例模式
    2.应用于线程池
    3.应用于连接池
14.闭包概念：在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包