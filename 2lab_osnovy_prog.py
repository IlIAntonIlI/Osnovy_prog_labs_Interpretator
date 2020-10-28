a=float(input("Enter first number: ")) #Введення змінної для першого числа та надання йому значення методом вводу
b=float(input("Enter second number: ")) #Введення змінної для другого та надання йому значення методом вводу
c=float(input("Enter third number: ")) #Введення змінної для третього числа та надання йому значення методом вводу
if (a==b):  #Перевірка на рівність чисел а та b
    Rivnist=True# Змінна для результату
    
else :
    if (a==c):#Перевірка на рівність чисел а та c
         Rivnist=True

    else:
        if (b==c):#Перевірка на рівність чисел b та c
            Rivnist=True
            
        else: Rivnist=False
print (Rivnist) #Якщо серед даних чисел є пара рівних між собою виведе True, інакше - False
    
