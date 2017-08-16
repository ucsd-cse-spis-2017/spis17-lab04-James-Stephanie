import turtle

def go(t, sideLength, level):
    triangle(t, sideLength, level)
    t.left(120)
def triangle(t, sideLength, level):
    if level == 1:
        return t.forward(sideLength)
    else:
        t.forward()
        t.right()
        triangle(t, sideLength / 2, level - 1)
if __name__ == "__main__":
    t = turtle.Turtle()
    triangle(t, 250, 2)
