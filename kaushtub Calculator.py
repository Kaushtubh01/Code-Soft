#Calculator 
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y

def devide(x,y):
    if y!=0:
        return x/y
    else:
        return "cannot devided by zero "


def Calculator():
    print("Please Choose An Operation Given Below:")
    print("1.Addition")
    print("2.Subtracion")
    print("3.Multiply")
    print("4.Devide")

    try :
        a=float(input("Enter your number : "))
        b=float(input("Enter your number : "))
        operation =int(input("Choose an Operation "))


        if operation == 1:
            result = add(a,b)
            print(f"Result: {a}+{b}={result}")
        elif operation == 2:
            result = sub(a,b)
            print(f"Result: {a}-{b}={result}")
        elif operation == 3:
            result = multiply(a,b)
            print(f"Result: {a}*{b}={result}")
        elif operation == 4:
            result = devide(a,b)
            print(f"Result: {a}/{b}={result}")

        else :
            print("Invalid input. Please enter valid numbers.")
        
    except ValueError :
        print("Invalid input. Please enter valid numbers.")


if __name__ == "__main__":
    Calculator()