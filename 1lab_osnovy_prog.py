#За заданими двома сторонами трикутника і куту( в градусах) між ними знайти довжину третьої сторони цього трикутника.

import math                   # Для використання математичних функцій
Side1= float(input("Enter first side(number must be >0 ):"))          #Вводимо змінну першої сторони і надаємо їй значення методом вводу
Side2= float(input("Enter second side(number must be >0 ):"))         #Вводимо змінну другої сторони і надаємо їй значення методом вводу  
Angle= float(input("Enter angle(number must be 0<angle<180 )):"))     #Вводимо змінну кута між першою та другою сторонами і надаємо їй значення методом вводу
Angle=Angle*math.pi/180;                                                #Переводимо кут з градусів у радіани
Side3= math.sqrt(Side1*Side1+Side2*Side2-2*Side1*Side2*math.cos(Angle)) #Обчислюємо довжину третьї сторони за теоремою косинусів
print ("Third side = ",Side3);
     
