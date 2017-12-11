
class Tip:
    def __init__(self, amount, tipPercent, taxPercent):
        self.amount=amount
        self.tipPercent=tipPercent
        self.taxPercent=taxPercent

    def calculateTax(self):
        if self.taxPercent >= 1:
            self.taxPercent=self.taxPercent / 100.0
        self.tax=self.amount * self.taxPercent

    def calculateTip(self):
        if self.tipPercent >=1:
            self.tipPercent=self.tipPercent / 100.0
        self.tip=self.amount * self.tipPercent

    def calculateTotal(self):
        self.total=self.amount + self.tip + self.tax
    

    def getTax(self):
        return self.tax

    def getTip(self):
        return self.tip
    
    def getTotal(self):
        return self.total

    def __str__(self):
        self.calculateTax()
        self.calculateTip()
        self.calculateTotal()
        return ("Amount: " + str(self.amount) + 
               " Tax: " + str(self.tax) + " Tip: " + str(self.tip) + 
               " Total: " + str(self.total))



    
        
