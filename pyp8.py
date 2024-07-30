#create student class that takes name and marks of 3  subjects as arguments in constructor.
#Then create method to print the average.

class id:
    def __init__(self,name,marks):
        self.marks = marks
        self.name = name
    def avg(self):
        x= 0
        for val in self.marks:
            x+=val
        
        print(self.name,"'s score is: ", x/3)



s1 = id("Ram", [100, 99, 98])
s1.avg()
#if we have to change the name of attribute first
s1.name="Shyam"
s1.avg()

class account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc
    def debit(self,minus):
        self.bal-=minus
    def credit(self,add):
        self.bal+=add
    def get_balance(self):
        return self.bal    

acc1 = account(100, 12)
print(acc1.bal)
print(acc1.acc)
acc1.debit(70)
print(acc1.bal)





        










