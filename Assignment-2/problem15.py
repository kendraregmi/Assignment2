# 15. Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?

class Customer:
   
    #methods
    def inti(self, customerName, customerAge, customerDOB, customerIncome, customerCitizenshipNo):
       self.name= customerName
       self.age= customerAge
       self.birthdate= customerDOB
       self.income= customerIncome
       self.citizenshipNo= customerCitizenshipNo 

    def cashDeposit(self):
        pass

    def cashWithdraw(self):
        pass

    def balanceEnquiry(self):
        pass

    def chequeWithdraw(self):
        pass
    
    def chequeDeposit(self):
        pass