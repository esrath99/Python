class phone:
    def call(self):
        print("you can call")
    def message(self):
         print("You can message")
class samsung(phone):
    def photo(self):
        super().call()
        super().message()
        print("You can take photo")

s=samsung()
#s.message()
#s.call()
s.photo()