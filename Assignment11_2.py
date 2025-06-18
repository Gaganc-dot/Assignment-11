fact = 1
def factorial(no):
    global fact
    if (no >= 1):
        fact = fact * no
        no = no - 1
        factorial(no)
    return fact

def main():
    print("Enter the your number :")
    n = int(input())
    
    Ans = factorial(n)
    print("Factorial is :",Ans)
   

if __name__ == "__main__":
    main()
