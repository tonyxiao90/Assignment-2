import turtle
import math


def indented_edge(t, length, depth):
    """Draw one edge with an inward equilateral-triangle indentation (recursive)."""
    if depth == 0:
        t.forward(length)
        return

    third = length / 3.0

    indented_edge(t, third, depth - 1)

    # INWARD indentation for a CCW (left-turning) polygon:
    t.left(60)
    indented_edge(t, third, depth - 1)

    t.right(120)
    indented_edge(t, third, depth - 1)

    t.left(60)
    indented_edge(t, third, depth - 1)


def draw_pattern_polygon(sides, side_length, depth):
    screen = turtle.Screen()
    screen.title("Recursive Inward Indentation Polygon")
    screen.setup(1000, 800)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.pensize(2)

    # Better centering for many cases
    radius = side_length / (2 * math.sin(math.pi / sides))
    t.penup()
    t.goto(-side_length / 2, -radius / 2)
    t.setheading(0)
    t.pendown()

    turn = 360 / sides
    for _ in range(sides):
        indented_edge(t, side_length, depth)
        t.left(turn)

    screen.mainloop()


def main():
    
    sides = int(input("Enter the number of sides: "))
    side_length = float(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    draw_pattern_polygon(sides, side_length, depth)

if __name__ == "__main__":
    main()
