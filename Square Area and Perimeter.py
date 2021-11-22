class Square:
        a = 0
        b = 0
        def __init__(self , side):
                self.side = side
                self.a = side * side
                self.b = side * 4
        def Area(self):
                print('Hi ' , name , ', Area of the Square is : %0.2f' % self.a)
        def Perimeter(self):
                print('And the Perimeter of the Square is : %0.2f' % self.b)

name = input('Enter your name pls : ')

while True:
        side = float(input('Enter the side of the Square : '))

        square = Square(side)
        square.Area()
        square.Perimeter()

        Continue = input('If you want to start over, enter y or not enter n : ')
        if Continue != 'y' and Continue!= 'n':
                Continue = input('Enter y or n , pls : ')
        if Continue == 'n':
                break

print('Thank you for choosing us' , name , '!')