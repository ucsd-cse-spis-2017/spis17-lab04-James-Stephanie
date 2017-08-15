import turtle

def tree(t, trunkLength, height):
    if (height == 0):
        return
    t.forward(trunkLength)
    t.right(45)
    tree(t, trunkLength/2, height-1)
    t.left(90)
    tree(t, trunkLength/2, height-1)
    t.right(45)
    t.backward(trunkLength)

if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(1)
    t.left(90)
    tree(t, 200, 5)
