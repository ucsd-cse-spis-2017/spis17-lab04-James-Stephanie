import turtle

def snowflake(t, sideLength, levels):
    snowflakeSide(t, sideLength, levels)
    t.left(120)
    snowflakeSide(t, sideLength, levels)
    t.left(120)
    snowflakeSide(t, sideLength, levels)
    t.left(120)

def snowflakeSide(t, sideLength, levels):
    
    # Base Case
    if levels == 0:
        return t.forward(sideLength)
    else:
        snowflakeSide(t, sideLength/3, levels - 1)
        t.right(60)
        snowflakeSide(t, sideLength/3, levels - 1)
        t.left(120)
        snowflakeSide(t, sideLength/3, levels - 1)
        t.right(60)
        snowflakeSide(t, sideLength/3, levels - 1)
    
if __name__ == "__main__":
    t = turtle.Turtle()
    snowflake(t, 280, 4)
