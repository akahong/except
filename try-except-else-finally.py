#encoding:utf_8

#try-except-finally使用：
#try:
#    try_suit
#except:
#    do_except
#finally:
#    do_finally
#若try语句没有捕获异常，执行完try代码段后，执行finally
#若try捕获异常，首先执行except处理错误，然后执行finally
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
finally:
    try:
        print 'file close'
        f.close()
    except NameError,e:
        print 'catch error:',e
"""

#try-except-else-finally使用：
#try:
#    try_suit
#except:
#    do_except
#else:
#    do_else
#finally:
#    do_finally
#若try语句没有捕获异常，执行完try代码段后，执行else代码段，最后执行finally
#若try捕获异常，首先执行except处理错误，然后执行finally

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
    print 'no error'
finally:
    try:
        print 'file close'
        f.close()
    except NameError,e:
        print 'catch error:',e
