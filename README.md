# A-login-demo

## 学习文档

- Flask: https://flask.palletsprojects.com/en/2.2.x/
- Flask-PyMongo: https://flask-pymongo.readthedocs.io/en/latest/

## 项目结构

```markdown
- app.py  定义flask应用实例
- config.py  储存配置
- requirements.txt  依赖
- src
 - templates
 - static
 - main  主蓝图
  - __init__.py
  - errors.py
  - views.py
 - __init__.py
 - models.py
- tests
 - __init__.py
 - test.py
```

## 项目运行

```shell
flask run
```

## 创建应用实例

### 简单创建

```python
from flask import Flask

app = Flask(__name__)
```

#### 缺点
1. 应用实例在全局空间创建
2. 无法动态修改配置

### 使用工厂函数创建

#### 优势

1. 可以在脚本中先修改配置，后创建应用实例
2. 可使用工厂函数创建多个应用实例
3. 从而我们可以同时测试不同的配置

## 蓝本

> 由于工厂函数的使用，我们对路由函数提出了更高的需求，路由函数不再只能服务于单一的路由，而是应该可以由我们在使用工厂函数创建应用实例时自行选择注册添加其为路由

蓝本就此诞生，在我看来，蓝本不仅仅是路由函数的替代品，他更是开启了flask的组件化编程。

一组功能类似的路由函数我们可以放在一起组成一个蓝本，由此可见，蓝本类似于应用，但是其服务于应用，更像是应用的插件来被我们定义与使用。

```python
from flask import Blueprint


main = Blueprint('main', __name__)  # 'main': 蓝本名称 __name__: 蓝本所在的包或模块 
```

### `__name__`

1. 作为主程序运行: __main__
2. 作为模块被导入: 模块名
3. 比如说main作为蓝本被工厂函数使用时, main/__init__.py 中的 __name__ 就是模块名 main 
