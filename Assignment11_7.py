
def triangle(no1,i=1):
    if (i!= no1+1):
        print("* "*i)
        return triangle (no1,i+1)

def main():
    print("Enter the your number :")
    n = int(input())
    
    triangle(n)
   

if __name__ == "__main__":
    main()
