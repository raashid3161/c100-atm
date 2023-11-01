class Atm(object):

    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber = pinNumber

    def cashWithdraw(self):
        print("Withdraw cash?")

    def cashDeposit(self):
        cashdepo = int(input("How many dollars would you like to deposit: "))
        print(cashdepo)
        print(f"${cashdepo} was successfully deposited")
    def balanceEnquiry(self):
        print("your balance 50,000")

P1 = Atm("54","12")
print(P1.cashDeposit())

