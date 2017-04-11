#encoding:utf_8

#try:
#    try_suit
#finally:
#    do_finally
#如果try语句没有捕获错误，代码执行do_finally语句
#如果try语句捕获错误，程序首先执行do_finally语句，然后将捕获到的错误交给python解释器处理

#try-finally语句:
#规则：try-finally无论是否检测到异常，都会执行finally代码
#作用：为异常处理事件提供清理机制，用来关闭文件或者释放系统资源

try:
    f=open('1.text')
    print int(f.read())
finally:
    print 'file close '
    f.close()