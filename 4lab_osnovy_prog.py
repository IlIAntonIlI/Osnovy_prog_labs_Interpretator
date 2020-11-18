## ===  Нехай х0=с;     x1=d;      xk=q*xk-1+r*xk-2+b;   k=2,3…         ===
## ===  Дано дійсні числа q, r, b, c, d, натуральне n>=2. Отримати xn.  === 


first_num=float(input("Enter first number: "))                      # Значення першого x
second_num=float(input("Enter second number: "))                    # Значення другого x
coef_q=float(input("Enter coefficient q: "))                        # Значення коефіцієнта q у формулі
coef_r=float(input("Enter coefficient r: "))                        # Значення коефіцієнта r у формулі
num_b=float(input("Enter number b: "))                              # Значення числа b у формулі
num_it=int(input("Enter the number of x you are looking for: "))    # Номер шуканого х
if num_it>=2:
    x0=first_num                                                    # Значення числа x позапопереднього даному
    x1=second_num                                                   # Значення числа x попереднього даному
    for k in range(num_it):
        x_k=coef_q*x1+coef_r*x0+num_b;                              # Знаходження х під номером k
        x0=x1                                                       # Збереження значення попереднього х
        x1=x_k                                                      # Збереження значення х з номером k
    print("Number you are looking for: ", x_k)    
else: print("Number of x must be >=2")
