
def count_zeros(n,c=0):
    if(n>0):
        if(n % 10 == 0):
            c= c +1
        return count_zeros(n //10,c)
    return c
                

def main():
    print("Enter the your number :")
    n = int(input())
    
    Ans = count_zeros(n)
    print("Zero Count is :",Ans)
   

if __name__ == "__main__":
    main()
