# CHANGE LAST SECOND ELEMENT TO 100

# lst = [20, 30, 60, 89, 40, 60, 90]
# lst.pop(-2)
# lst.insert(-1,100)
# print(lst)

# SUM OF SECOND HALF ELEMENT

# lst = [20, 30, 60, 89, 40, 100, 90]
# sum = 0
# for i in range(3, 7):
#     sum += lst[i]
# print(sum) 


# class Book:
#     def __init__(self,t,p):
#         self.title = t
#         self.price = p
#     def __add__(self,other):  
#         return self.price + other.price 
#     def __add__(self,other):  
#             return self.title + other.title
# b1 = Book("Core Python",200)        
# b2 = Book("Advance Python",600)  
# print(b1+b2)

# HOMEWORK 

class Num:
    def __init__(self, n):
        self.n = n

    # Arithmetic Operators
    def __add__(self, other):
        return self.n + other.n

    def __sub__(self, other):
        return self.n - other.n

    def __mul__(self, other):
        return self.n * other.n

    def __truediv__(self, other):
        return self.n / other.n

    def __floordiv__(self, other):
        return self.n // other.n

    def __mod__(self, other):
        return self.n % other.n

    def __pow__(self, other):
        return self.n ** other.n

    # Comparison Operators
    def __eq__(self, other):
        return self.n == other.n

    def __ne__(self, other):
        return self.n != other.n

    def __lt__(self, other):
        return self.n < other.n

    def __gt__(self, other):
        return self.n > other.n

    def __le__(self, other):
        return self.n <= other.n

    def __ge__(self, other):
        return self.n >= other.n
 
a = Num(10)
b = Num(20)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Less Than:", a < b)
print("Greater Than:", a > b)
print("Less or Equal:", a <= b)
print("Greater or Equal:", a >= b)

































