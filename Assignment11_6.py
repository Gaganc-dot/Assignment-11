
def natural(no1):
     if no1 <= 1 :
         return no1
     return no1 + natural(no1-1)
                

def main():
    print("Enter the your number :")
    n = int(input())
    
    
    Ans = natural(n)
    print("Sum of natural no is :",Ans)
   

if __name__ == "__main__":
    main()
