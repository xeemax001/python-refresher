name = "zeeshan"
age = 20
print("Hellooo my name is {} and I am {} years old".format(name,age))
print("WELL ITS COOL!")
a = 50
b=90
if age>18:
    print("Congrats you are an adukt now :-D")
    
'''
hello its not gonna be compile
'''

def sum(a,b):
    print(a+b)
sum(a,b)


#lists

life = ["Money","peace","big home","cars","every facility","truely obying Allah"]
life.insert(0, "ALLAH with me")
print(life)
print(life[0])
del(life[1])
print(life)

print(len(life))


#loopsss!

for love in life:
    print(love)
    
for even in range(1,1000):
    print(even%2==0)
    
age = 0
while age<15:
    print("Life is awesome for year {}".format(age))
    age = age + 1
print("As you are now 15 so the life seems to be absolute shit")


lifeDic = {"Happiness":("Money","peace","big home","cars","every facility","truely obying Allah")}
print(lifeDic["Happiness"])



#classes


class Life:
    
    def awesomeness(self, str):
        print('The meaning of awesomness to me is "Money","peace","big home","cars","every facility","truely obying Allah"' + str)
mylife = Life()
mylife.awesomeness("But you need to be in owkaat!!!")



class BuyCar:
    def __init__(self,color,brand,model):
        self.color = color
        self.brand = brand
        self.model = model
    def awesomeCar(self,str):
        print("I am the fastest car here!" + str)
buyMeAcar = BuyCar("red", "honda", 2020)
buyMeAcar.awesomeCar("I am gonna buy a")
print(buyMeAcar.color)
print(buyMeAcar.brand)
print(buyMeAcar.model)