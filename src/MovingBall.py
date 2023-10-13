import math


class MovingBall:
    """Класс, представляющий движущийся шарик на холсте.

    Attributes:
        canvas: Холст, на котором находится шарик.
        x1, y1: Координаты первой вершины треугольника на холсте.
        x2, y2: Координаты второй вершины треугольника на холсте.
        x3, y3: Координаты третьей вершины треугольника на холсте.
        x: Координата x шарика на холсте.
        y: Координата y шарика на холсте.
        vx: Скорость шарика по оси x.
        vy: Скорость шарика по оси y.
        r: Радиус шарика.

    Methods:
        distance_to_segment(x, y, x1, y1, x2, y2): Вычисляет расстояние от шарика до ребра на холсте.
        move_ball(): Двигает шарик на холсте.
        clear_ball(): Удаляет шарик с холста.
    """

    def __init__(self, canvas, x1, y1, x2, y2, x3, y3, x, y, vx, vy):
        """Инициализирует экземпляр класса MovingBall.

        Args:
            canvas: Холст, на котором находится шарик.
            x1, y1: Координаты первой вершины треугольника на холсте.
            x2, y2: Координаты второй вершины треугольника на холсте.
            x3, y3: Координаты третьей вершины треугольника на холсте.
            x: Координата x шарика на холсте.
            y: Координата y шарика на холсте.
            vx: Скорость шарика по оси x.
            vy: Скорость шарика по оси y.
        """
        self.canvas = canvas
        self.x1 = x1 + 40
        self.y1 = y1 + 40
        self.x2 = x2
        self.y2 = y2 + 40
        self.x3 = x3 + 40
        self.y3 = y3
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = 20

        self.ball = self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                            fill="medium violet red")

        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2)
        self.canvas.create_line(self.x2, self.y2, self.x3, self.y3)
        self.canvas.create_line(self.x3, self.y3, self.x1, self.y1)

    def distance_to_segment(self, x, y, x1, y1, x2, y2):
        """Вычисляет расстояние от шарика до ребра на холсте.

        Args:
            x, y: Координаты шарика на холсте.
            x1, y1: Координаты первой точки линии на холсте.
            x2, y2: Координаты второй точки линии на холсте.

        Returns:
            float: Расстояние от точки до линии на холсте.
        """
        dx = x2 - x1
        dy = y2 - y1
        if dx == 0 and dy == 0:
            return math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
        t = ((x - x1) * dx + (y - y1) * dy) / (dx ** 2 + dy ** 2)
        if t < 0:
            return math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
        elif t > 1:
            return math.sqrt((x - x2) ** 2 + (y - y2) ** 2)
        else:
            xp = x1 + t * dx
            yp = y1 + t * dy
            return math.sqrt((x - xp) ** 2 + (y - yp) ** 2)

    def move_ball(self):
        """Перемещает шарик по канвасу и отражает его от стен, если он сталкивается с ними."""
        d1 = self.distance_to_segment(self.x, self.y, self.x1, self.y1, self.x2, self.y2)
        d2 = self.distance_to_segment(self.x, self.y, self.x2, self.y2, self.x3, self.y3)
        d3 = self.distance_to_segment(self.x, self.y, self.x3, self.y3, self.x1, self.y1)
        if d1 < self.r or d2 < self.r or d3 < self.r:
            if d1 < self.r:
                nx, ny = self.y2 - self.y1, self.x1 - self.x2
            elif d2 < self.r:
                nx, ny = self.y3 - self.y2, self.x2 - self.x3
            else:
                nx, ny = self.y1 - self.y3, self.x3 - self.x1
            d = math.sqrt(nx ** 2 + ny ** 2)
            nx /= d
            ny /= d
            dot = self.vx * nx + self.vy * ny
            self.vx -= 2 * dot * nx
            self.vy -= 2 * dot * ny
        self.x += self.vx
        self.y += self.vy
        self.canvas.move(self.ball, self.vx, self.vy)
        self.canvas.update()
        self.canvas.after(30, self.move_ball)

    def clear_ball(self):
        """Удаляет шарик и все другие объекты на канвасе."""
        self.canvas.delete('all')
