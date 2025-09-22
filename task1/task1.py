class calculate():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def sum(self):
        return(self.num1+self.num2)
    def sub(self):
        return(self.num1-self.num2)
    def mul(self):
        return(self.num1*self.num2)
    def div(self):
        if self.num2 != 0:
            return(self.num1/self.num2)
        else:
            return("not dividible by 0")
    def rem(self):
        return(self.num1%self.num2)

if __name__=='__main__':
    while True:
        num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
        calculator = calculate(num1, num2)
        op = input("Enter the symbol {+ , - , * , / , % , exit}: ").strip()
        if op.lower() == "exit":
            print("Exiting...")
            break
        elif op == "+":
            print("Result: ", calculator.sum())
        elif op == "-":
            print("Result: ", calculator.sub())
        elif op == "*":
            print("Result: ", calculator.mul())
        elif op == "/":
            print("Result: ", calculator.div())
        elif op == "%":
            print("Result: ", calculator.rem())
        else:
            print("Invalid operation. Please try again.")