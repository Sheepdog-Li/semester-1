from rect import Rectangle

r = Rectangle(3, 5)
print(r.area())        
print(r.perimeter())   
print(r.is_square())   

s = Rectangle(4, 4)
print(s.is_square())   

# test the error
try:
    Rectangle(-1, 5)  #negative num
except ValueError:
    print("ValueError correct")

try:
    Rectangle("3", 5) #str
except TypeError:
    print("TypeError correct")