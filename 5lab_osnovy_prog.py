# ===  Задача.  Ввести натуральні числа m та n. Як результат вивести   ===
# ===  усі натуральні числа,що менші за m, сума цифр яких дорівнює n.  ===


m=int(input("Enter number m: "))           # Межа чисел, які будемо перевіряти (1,m)
n=int(input("Enter number n: "))           # Сума цифер числа, за якою ми будемо шукати числа-результати
if((m>0) and (n>0)):
      for i in range(1,m,1):
            new_i=i                        # Змінна для обробки значення i без його втрати
            num_i=0                        # Сума цифр числа i
            while (new_i>0):               # Знаходженя суми цифр числа і
                num_i=num_i+new_i%10;
                new_i=new_i//10
            if (num_i==n):
                print(i, end=" ")          # Перевірка умови рівності суми цифер числа та n
else:
      print("Wrong data, please enter numbers >0") 
       
