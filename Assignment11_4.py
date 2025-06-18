
def power(no1,no2):
    if(no2==0):
        return 1
    else:
        return(no1 * power(no1 , no2-1))
                

def main():
    print("Enter the your number :")
    n = int(input())
    
    print("Enter the your number :")
    n1 = int(input())
    
    Ans = power(n,n1)
    print("Power is :",Ans)
   

if __name__ == "__main__":
    main()
