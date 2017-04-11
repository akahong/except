#encoding:utf-8
from random import randint

#try-excep：异常处理
#try:
#   try_suit
#except Except [e]:
#   exception_block
#try用来捕获try_suit中的错误，并且将错误交给except处理
#except用来处理异常，如果处理异常和设置捕获异常一致，使用exception_block处理异常

num=randint(1,100)
while True:
    try:
        guess=int(raw_input('enter 1~100: '))
    except ValueError,e:
        print 'enter 1~100'
        continue
    if guess>num:
        print'guess bigger: ',guess
    elif guess<num:
        print 'guess smaller: ',guess
    else:
        print  'guess ok,game over'
        break
    print '\n'