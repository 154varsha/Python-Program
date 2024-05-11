def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2
 #create dictionry    
operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
num1=int(input("what is first number you want to choose? "))

for symbol in operations:
    print(symbol)
operation_symbol=input("pick an operation from above line ")
num2=int(input("what is second number you want to choose? "))

calculation_function=operations[operation_symbol]  
first_answer=calculation_function(num1,num2)
print(f"{num1} {operation_symbol} {num2}= {first_answer}")
operation_symbol=input("pick aanother operation symbol ")
num3=int(input("choose another number "))

calculation_function=operations[operation_symbol]
second_answer=calculation_function(calculation_function(num1,num2),num3)
print(f"{first_answer}{operation_symbol}{num3} = {second_answer}")

