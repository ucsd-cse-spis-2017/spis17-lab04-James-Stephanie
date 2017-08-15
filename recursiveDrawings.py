import turtle

def spiral(t, initialLength, angle, multiplier):
    t.speed(0)
    t.forward(initialLength)
    t.right(angle)
    spiral(t, initialLength*multiplier, angle, multiplier)
    
if __name__ == "__main__":
    t = turtle.Turtle()
    spiral(t, 1, 61, 1.01)
