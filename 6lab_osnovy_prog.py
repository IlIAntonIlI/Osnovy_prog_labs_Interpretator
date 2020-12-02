from math import sqrt       # Приєднання функції кореня квадратного       
def f(x,y):                 # Функція f
    rez=x**2-y**2
    return rez
def g(x,y,z):               # Функція g
    rez=(x+y)/(4*z*x)
    return rez
a=int(input("Enter number a: "))  # Змінна a
b=int(input("Enter number b: "))  # Змінна b
c=int(input("Enter number c: "))  # Змінна c
d=int(input("Enter number d: "))  # Змінна d
num_1=f(a,b)                      
num_2=f(c,d)
num_3=g(a,b,c)
num_4=f(b,c)
num_5=f(a,c)
y=((num_1+num_2)/sqrt(num_3))+((c-num_3+1)/(num_4-num_1))*(1+(sqrt(num_3)/(num_4-num_5))) # Обчислення y за формулою заданою в задачі
print("y= ",y)
