def problem1():
    a = int(input())
    b = int(input())
    if(a > b):
        print(b)
    else:
        print(a)
        
def problem2():
    a = int(input())
    if(a < 0):
        print(-1)
    elif(a > 0):
        print(1)
    else:
        print(a)
        
def problem3():
    a = int(input())
    b = int(input())
    c = int(input())
    if(a < b and a < c):
        print(a)
    elif(b < a and b < c):
        print(b)
    else:
        print(c)
    
def problem4():
    a = int(input())
    b = int(input())
    c = int(input())
    if(a == b or b == c or a == c):
        if(a == b and b == c):
            print(3)
        else:
            print(2)
    else:
        print(0)

def problem5():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if((x1 == x2) != (y1 == y2)):
        print('YES')
    else:
        print('NO')
        
def problem6():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    if(((x1-x2)+(y1-y2))%2 == 0):
        print('YES')
    else:
        print('NO')