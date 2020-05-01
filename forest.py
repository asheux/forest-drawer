import turtle
import math
import random
from utilities import Draw

WW, WH = 800, 600
RW, RH = 700, 485
TC = (-50, 260)
BC = (50, 260)
ARGPARSE = dict()


class TurtleGraphic(Draw):
    def __init__(self):
        self.bird_checked = False
        self.tree_checked = True
        self.circle_pen_color = 'black'
        self.r = 7
        super().__init__(WW, WH)

    def handle_click(self, x, y):
        print(f'Detected a click at {x, y}')

        def is_inside():
            """
            checks if the current click coordinate is inside the rectangle 
            """
            return (-(RW / 2) < x < RW / 2) and (-(RH / 2) < y < RH / 2)

        cbx, cby = (-285, 270)
        lh = random.randint(50, 100)
        stw = random.randint(4, 8)
        sth = random.randint(50, 100)

        if is_inside():
            if self.bird_checked:
                self.stamp_turtle(x, y, '#0B2F3A')
                print('Bird')
            else:
                self.tree(x, y, stw, sth, lh)
                print('Tree')
        else:
            # check either of these variable to true if the circle is clicked
            self.tree_checked = self.check_circle(x, y, self.r, TC)
            self.bird_checked = self.check_circle(x, y, self.r, BC)

            if self.bird_checked:
                # update the state of the circle when clicked
                self.new_state_circle(self.t, BC[0], BC[1], '#086A87')
                self.new_state_circle(self.t, TC[0], TC[1], '#F6E3CE')
                self.stamp_turtle(cbx, cby, '#0B2F3A')
            else:
                self.stamp_turtle(cbx, cby, '#F6E3CE')
            if self.tree_checked:
                # update the state of the circle when clicked
                self.new_state_circle(self.t, TC[0], TC[1], '#086A87')
                self.new_state_circle(self.t, BC[0], BC[1], '#F6E3CE')

    def new_state_circle(self, t, cx, cy, c):
        t.up()
        t.goto(cx, cy)
        t.down()
        t.fillcolor(c)
        t.begin_fill()
        t.speed('fastest')
        t.circle(self.r)
        t.end_fill()

    def check_circle(self, x, y, radius, c) -> bool:
        """
        Check if the user clicked inside the circle
        """
        cx, cy = c
        sqx = (x - cx)**2
        sqy = (y - cy - 8)**2

        return math.sqrt(sqx + sqy) < radius

    def click(self, screen):
        """
        listen to clicks
        """
        screen.listen()
        screen.onscreenclick(self.handle_click)

    def display(self):
        """
        The main display
        """
        window_color = '#F6E3CE'
        rec_fillc = '#F6E3CE'
        rec_pen_color = 'black'
        rec_pen_color = 'black'
        circle_pen_color = 'black'
        window_title = 'Turtle graphics'
        tree = f"{5 * ' '}Tree"
        bird = f"{5 * ' '}Bird"
        degrees = 90
        screen = self.window

        self.click(screen)

        self.window_display(window_color, window_title)
        self.draw_rectangle(2, -350, -250, RW, RH, rec_pen_color, rec_fillc,
                            degrees)
        self.draw_circle(TC[0], TC[1], self.r, self.circle_pen_color,
                         self.tree_checked)
        self.writer(tree)
        self.draw_circle(BC[0], BC[1], self.r, self.circle_pen_color, False)
        self.writer(bird)
        self.disable_animation()

        turtle.done()  # clock the display


def main():
    tg = TurtleGraphic()
    tg.display()


if __name__ == '__main__':
    main()
