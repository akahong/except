#encoding:utf_8
import os

#with语句：
#with context [as var]:
#    with_suit
#with语句用来代替try-except-finally语句，使代码更加简洁
#context表达式返回是一个对象；
#var用来保存context返回对象，单个返回值或者元组
#with_suit使用var变量来对context返回对象进行操作
"""
try:
    with open('1.text') as f:
        print 'in with f.read:' ,f.read()
        f.seek(-5,os.SEEK_SET) #重定义文档并将文档中的指针向后移动5个字节
except IOError,e:
    print 'in with catch ValueError: ',e
    print 'with: ' ,f.closed
"""
#with 语句实质是上下文管理：
#上下文管理协议：包含方法__enter__()和__exit__()，支持该协议的对象要实现这两个方法
#上下文管理器：定义执行with语句时要建立的运行时上下文，负责执行with语句块上下文中的进入与退出操作
#进入上下文管理器：调用管理器__enter__()方法，如果没有设置as var语句，var变量接受__enter__()方法返回值
#退出上下文管理器：调用管理器__exit__()方法

class Mycontext(object):
    def __init__(self,name):
        self.name=name
    def __enter__(self):
        print '__enter__'
        return self
    def do_self(self):
        print 'do_self'
    def __exit__(self, exc_type, exc_val, traceback): #exc_type:错误类型；exc_val:错误值
        print '__exit__'
        print 'error: ',exc_type,' info: ',exc_val

if __name__=='__main__':
    with Mycontext('text context') as f:
        print f.name
        f.do_self()
