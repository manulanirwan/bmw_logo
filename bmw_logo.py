import turtle

def draw_circle(color, radius, x, y):
    """Utility function to draw a filled circle at a specific position."""
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_quadrant(color, radius, start_angle):
    """Draws a 90-degree pie slice (quadrant) for the center checkerboard."""
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(start_angle)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(radius)
    turtle.left(90)
    turtle.circle(radius, 90)
    turtle.goto(0, 0)
    turtle.end_fill()

def draw_bmw_logo():
    # Setup screen
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.title("BMW Logo in Python")
    
    # Speed up drawing
    turtle.speed(5)
    turtle.hideturtle()

    # 1. Outer Black Ring
    draw_circle("black", 150, 0, 0)

    # 2. Outer Thin Silver/Grey Border Frame
    turtle.penup()
    turtle.goto(0, -150)
    turtle.pendown()
    turtle.pensize(4)
    turtle.pencolor("#D3D3D3") # Light grey/silver
    turtle.circle(150)
    
    # 3. Inner Circle Frame (Separating text ring from center)
    turtle.penup()
    turtle.goto(0, -95)
    turtle.pendown()
    turtle.pensize(2)
    turtle.circle(95)

    # 4. Center Checkerboard Blue and White Quadrants
    # Top-Left: White, Top-Right: Blue, Bottom-Right: White, Bottom-Left: Blue
    draw_quadrant("#0066B2", 95, 0)    # Top-Right Blue
    draw_quadrant("white", 95, 90)    # Top-Left White
    draw_quadrant("#0066B2", 95, 180)  # Bottom-Left Blue
    draw_quadrant("white", 95, 270)  # Bottom-Right White

    # 5. Adding the "B M W" Text
    turtle.pencolor("white")
    
    # Letter 'M' (Exactly at the top center)
    turtle.penup()
    turtle.goto(0, 105)
    turtle.setheading(0)
    turtle.write("M", align="center", font=("Helvetica", 32, "bold"))
    
    # Letter 'B' (Tilted to the left)
    turtle.goto(-65, 85)
    turtle.write("B", align="center", font=("Helvetica", 32, "bold"))
    
    # Letter 'W' (Tilted to the right)
    turtle.goto(65, 85)
    turtle.write("W", align="center", font=("Helvetica", 32, "bold"))

    # Keep the window open
    screen.mainloop()

if __name__ == "__main__":
    draw_bmw_logo()