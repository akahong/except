#encoding:utf-8

#使用多个except捕获多个异常
"""
try:
    f=open('1.text')
    line=f.read(2)
    num=int(line)
    print'read num =%d'%num
except IOError,e:
    print 'catch IOError: ',e
except ValueError,e:
    print 'catch ValueError: ',e
"""
#try-except-else使用
#try:
#    try_suit
#except Exception [e]:
#    exception_bloce
#else:
#    none_exception
#如果没有异常，执行else语句中的代码

try:
    f=open('1.text')
    line=f.read(2)
    num=int(line)
    print'read num =%d'%num
except IOError,e:
    print 'catch IOError: ',e
except ValueError,e:
    print 'catch ValueError: ',e
else:
    print 'not error'