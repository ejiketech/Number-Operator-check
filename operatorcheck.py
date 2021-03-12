# Prompt input
num1 = int(input("Enter Number1:  "))
num2 = int(input("Enter Number2:  "))
num3 = int(input("Enter Number3:  "))

#Function
def my_operator(num1, num2, num3):
    add = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    div = num1 / num2
    if (add == num3 and mult == num3):
        return"+" + "*"
    elif (add == num3):
        return "+"
    elif (sub == num3):
        return "-"
    elif (mult == num3):
        return "*"
    elif (div == num3):
        return "/"

    else:
        return None


print(my_operator(num1, num2, num3))
