
def sum(no):
    if (no== 0):
        return 0
    else:
         return (no % 10 + sum(int(no/10)))
                

def main():
    print("Enter the your number :")
    n = int(input())
    
    Ans = sum(n)
    print("sum of digit no is :",Ans)
   

if __name__ == "__main__":
    main()
