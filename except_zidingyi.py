#encoding:utf-8

#标准异常：python内建异常，程序执行前就已经存在
#自定义异常
#python允许自定义异常，用于描述python中没有涉及的异常
#自定义异常必须继承Exception类
#自定义异常常只能主动触发

class CustomError(Exception):
    def __init__(self,info):
        Exception.__init__(self)
        self.errorinfo=info
        print id(self) #打印对象id

    def __str__(self):
        return 'CustomError:%s'%self.errorinfo

try:
    raise CustomError('test CustomError')
except CustomError,e:
    print 'CustomError:%d,%s'%(id(e),e)