import turtle


class Draw():
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.window = turtle.Screen()
        self.t = turtle.Turtle(visible=False)

    def window_display(self, color, title):
        """
        Display the window
        """
        self.window.bgcolor(color)  # windows background color
        self.window.title(title)
        self.window.setup(self.w, self.h)  # set windows width and height
        self.window.tracer(
            False
        )  # Helps to disable animation at the start of the application

    def draw_triangle(self, *args):
        """
        Create the triangle
        """
        (cx, cy, w, pen_color, fill_color) = args

        self.start_postion(
            cx, cy
        )  # set the start coordinates where the turtle will begin drawing

        t = self.t

        # the outer for loop draws the next triangle
        for i in range(3):
            t.speed('fastest')  # draw fast enough
            t.pencolor(pen_color)
            t.fillcolor(fill_color)
            t.begin_fill()

            # this inner for loop draws the triangle
            for sides in range(3):
                t.pensize(0)
                t.forward(w)
                t.left(120)
            t.end_fill()

            t.penup()
            t.right(-120)
            t.forward(w / 2)
            t.left(-120)
            t.forward(w / 4)
            t.pendown()

    def tree(self, *args):
        """
        Draw the tree for to display on the window
        """
        (x, y, stw, sth, lh) = args
        pencolor = 'grey'
        fill_color = 'green'
        stc = '#610B0B'
        degrees = -90
        s = 0

        self.draw_rectangle(s, x + (lh / 2), y, stw, sth, stc, stc, degrees)
        self.draw_triangle(x, y, lh, pencolor, fill_color)

    def start_postion(self, cx, cy):
        """
        Set the start point to begin drawing
        """
        self.t.up()
        self.t.goto(
            cx,
            cy)  # goto tells the turtle to move to the specified coordinates
        self.t.down()

    def draw_rectangle(self, *args):
        """
        Rectangle function
        """
        (s, cx, cy, w, h, pen_color, fill_color, degrees) = args

        self.start_postion(cx, cy)

        self.t.fillcolor(fill_color)
        self.t.begin_fill()
        for i in range(2):
            self.t.pencolor(pen_color)
            self.t.pensize(s)
            self.t.forward(w)
            self.t.left(degrees)
            self.t.forward(h)
            self.t.left(degrees)
        self.t.end_fill()

    def draw_circle(self, *args):
        (cx, cy, radius, pen_color, tree) = args

        self.start_postion(cx, cy)

        tc = self.t
        tc.pencolor(pen_color)
        tc.pensize(1)

        if tree:
            tc.fillcolor('#086A87')
            tc.begin_fill()
            tc.circle(radius)
            tc.end_fill()
        else:
            tc.circle(radius)

    def disable_animation(self):
        """
        A function to disable animation
        """
        self.window.tracer(True)

    def writer(self, text):
        """
        Writer the labels
        """
        self.t.write(text,
                     align='left',
                     font=(
                         "Arial",
                         8,
                         'normal',
                         'bold',
                         'italic',
                     ))

    def left_keypress(self):
        print('Left key detected')
        turtle.tiltangle(20)

    def stamp_turtle(self, cx, cy, color):
        """
        Create a copy of the turtle
        """
        self.window.tracer(False)
        coords = ((-22, -39), (-20, -7), (-7, 3), (-11, 7), (-12, 9),
                  (-11, 10), (-9, 10), (-3, 7), (10, 24), (30, 16), (13, 18),
                  (4, 0), (14, -6), (6, -13), (0, -4), (-14, -13), (-22, -39))
        self.window.register_shape('turtle', coords)

        turtle.listen()
        turtle.onkeypress(self.left_keypress, 'Left')

        turtle.up()
        turtle.goto(cx, cy)
        turtle.down()
        turtle.shape('turtle')
        turtle.color(color)
        turtle.stamp(
        )  # here is the copy created, also returns the stamped turtle id

        self.window.tracer(True)  # disable animation

    def distance(self, x1, y1, x2, y2):
        pass

    def save_state(self):
        pass

    def restore_state(self):
        pass
