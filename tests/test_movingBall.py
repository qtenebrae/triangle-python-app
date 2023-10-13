from tkinter import Canvas
from src.MovingBall import MovingBall
import pytest
import math


def test_move_ball():
    canvas = Canvas()
    ball = MovingBall(canvas, 0, 0, 100, 0, 0, 100, 50, 50, 1, 2)
    ball.move_ball()
    assert ball.x == 51 and ball.y == 48


def test_distance_to_segment():
    canvas = Canvas()
    ball = MovingBall(canvas, 0, 0, 100, 0, 0, 100, 50, 50, 0, 0)
    assert ball.distance_to_segment(0, 0, 100, 100, 200, 200) == math.sqrt(20000)


def test_clear_ball():
    canvas = Canvas()
    ball = MovingBall(canvas, 0, 0, 100, 0, 0, 100, 50, 50, 1, 2)
    ball.clear_ball()
    assert len(canvas.find_all()) == 0


def test_distance_to_segment_same_points():
    canvas = Canvas()
    ball = MovingBall(canvas, 0, 0, 100, 0, 0, 100, 50, 50, 0, 0)
    assert ball.distance_to_segment(0, 0, 0, 0, 0, 0) == 0
