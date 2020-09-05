
№34
a=int(input())

b=int(input())

c=int(input())

d=int(input())

if a + b == c + d or a + c == b + d or a + d == c + b:

    print("True")

else:

    print("False")


№ 36
a=int(input())

b=int(input())

c=int(input())

d=int(input())


if (a % 2 != 0 and b % 2 != 0) or (a % 2 != 0 and c % 2 != 0) or (a % 2 != 0 and d % 2 != 0) or (b % 2 != 0 and c % 2 != 0) or (b % 2 != 0 and d % 2 != 0) or (c % 2 != 0 and d % 2 != 0):

    print ("True")

else:

    print("False")


№ 51
c=int(input("Eranish Tiv nermuci ara - "))


if c % 10 == c // 10 % 10 + c // 100:

    t=True

    print(t)


№ 52
c=int(input("Eranish Tiv nermuci ara - "))

if c % 10 == c // 10 % 10  or c % 10 == c // 100 or c // 10 % 10 == c // 100:

     t=True

     print(t)

else:

    t=False

    print(t)


№ 53

k=((c % 10) + (c // 10 % 10) + (c // 100))

if c > k:

    print(c / k)

else:

    print(c) / k)


№ 54
c=int(input("Eranish Tiv nermuci ara - "))

a = c % 10

b = c // 10 % 10

d = c // 100


if a > b:

    print ((a + b + d) / c)

else:

    print(c)



№ 62
a = int(input()) 

if a < 5000:

    z = a % 10

    c = a // 100 % 10

    print( a / (z + c))


else:

    x = a // 10 % 10

    v = a // 1000

    print ( a / (x + v))



№ 63

a = int(input())

count = 0

while a != 0:

    c = a % 10

    a //= 10

    if c == 1:

        print("1") 

        break

print("0")


№ 66 
a = int (input())

while a != 0:
    z = a % 10 
    c = a // 1000  
    
    if z == 4 and c == 4:
        print ("Yes")
        
    else:
        print("No")






№ 67

a = int(input())
 
x = a

count = 0

z = 0

while a != 0:

    z = a % 10

    a //= 10

    count += z 

if  x == count ** 2:

        print("Yes")

else:

        print("No")
        
  
