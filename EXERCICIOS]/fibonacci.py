# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...

def fibonacci(j):
    num1 = 0
    num2 = 1
    print(num1,",")
    print(num2,",")
    
    for i in range(j):
        num3 = num1 + num2
        print(num3,",")
        num1 = num2
        num2 = num3

termo = int(input("Digite até que termo da série de Fibonacci você deseja ver (>3):\n"))

fibonacci(termo-2)
