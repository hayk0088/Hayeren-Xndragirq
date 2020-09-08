
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
        
  
№ 70
a = int(input())
x = 1

while a != 0:
    c = a % 10
    a //= 10 
    x *= c                      
                     
if x > 200:        
    y=0                 
    print (y)         
       
else:
    y=1
    print(y)



№ 151
n = int(input())
sum = 0

for i in range(1,n+1,1):
   if n % i == 0:
      sum += i
     
  
print(sum)    



№ 155

sum=0

for i in range(10,100):
    if i % 3 ==0:
       sum+=i
print (sum)


№ 157
sum = 1

for i in range(100,1000):
    if i % 5 != 0:
       sum *= i
print(sum)             


№159
sum = 1

for i in range(1,10):
       if i % 3 == 1 and i % 4 ==2:
              sum *= i
print(sum)



№ 160
import math
tmp = 0
for i in range(100,1000,1):
       tmp = int(math.sqrt(i * 16))  
       if tmp ** 2 == i * 16:        
           print(i)
           break
                   

№ 161
import math
tmp = 0

for i in range (1000,10000,1):
       tmp = int(math.sqrt(i * 26))
       if tmp ** 2 == i * 26:
              print(i)
              break


№ 162
import math
tmp = 0

for i in range (10000,1000,-2):
       tmp = int(math.sqrt(i * 26))
       if tmp ** 2 == i * 14:
              print(i)
              break


№ 165
n = int(input())
z = n // 4
while n != 1 : 
       if x // 3 % 2 != 0:
            print("True")

       else:
            print ("False")
                    


№ 167
x = int (input())
for i in range(1,30,1):
     if x ** i < 0:
          print("True")
          exit (0)

print("False")



№ 168
n = int(input())
flag = 1
min_simple = 2
s = 0

while min_simple <= n/2 and flag == 1:

     if n % min_simple == 0:
          flag = 0
     else:
          min_simple += 1

if flag:
     print("Parz")
else:
     print("Che")


№ 181

    
n= int(input())     
count = 0              
while n > 1:          
    n=n/2              
    count += 1       
print(count)



№ 182 

n = int(input())
max = 0
for i in range (1, n // 2 ):
    if i ** 2 < n:
        max = i
print (max)


№ 183

n = int(input())                     
half = n // 2 + 1                 
while n > 1:                           
    for k in range (1,half):          
        if 3 ** k > n:             
            print(k)
            exit(0)


№ 185
a = int(input("Mutqagreq vand drvox gumri chapy: "))
n = 1

for i in range (1,25):         
    end = n * i * a        
    n += 1                          
    while end > 1000000:            
        print (n)                  
        print(n * n * a *((100 + n) // 100))             
        exit(0)  
    

       


       







       

