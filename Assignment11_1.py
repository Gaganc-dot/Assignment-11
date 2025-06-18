def Rec(n):
        if (n == 0):
            return
        else:
            Rec(n-1)
            print(n)
def main():
    print("Enter the your number :")
    n = int(input())
    
    Rec(n)

if __name__ == "__main__":
    main()
