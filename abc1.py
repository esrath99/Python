class large:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def __gt__(self,other):
        return self.num1>other.num1 and self.num2>other.num2
    def __str__(self):
        return (f"Num1={self.num1},Num2={self.num2}")
    def displar(self):
        print(f"Num1={self.num1},Num2={self.num2}")
ab=large(100,90)
bg=large(70,80)
print(ab>bg)
