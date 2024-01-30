from model import Line, Point, Window


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0, 0), Point(800, 600)), "red")
    win.draw_line(Line(Point(0, 600), Point(800, 0)), "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
