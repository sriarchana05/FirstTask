from Shapes.circle import Circle
from Shapes.rectangle import Rectangle
from Shapes.square import Square
  

if __name__ == "__main__":

    print("Calculate Perimeter of...")
    print("1. rectangle")
    print("2. circle")
    print("3. square")
    
    shape=int(input())
    if(shape==1):
        length = int(input("Enter the length of the rectangle(in cm): 2"))
        bredth = int(input("Enter the breadth of the rectangle(in cm): "))
        rectangle = Rectangle(length,bredth)
        output = rectangle.calculatePerimeter(length, bredth)
        print(output)
        

    elif(shape==2):
        radius = int(input("Enter the radius of the circle(in cm): "))
        circle = Circle(radius)
        output = circle.calculatePerimeter(radius)
        print(output)


    elif(shape==3):
        side = int(input("Enter the side of the square(in cm): "))
        square = Square(side)
        output = square.calculatePerimeter(side)
        print(output)

    else:
        print("Invalid shape")
    

    
