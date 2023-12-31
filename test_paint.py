import unittest

import pytest

from paint import Circle, Engine2D


class TestEgnine2D(unittest.TestCase):

    def test_canvas_size(self):
        """Тестируем размер холста"""

        paint = Engine2D(300, 400)
        self.assertEqual((paint.canvas.width, paint.canvas.height), (300, 400),
                         'Размер холста не совпадает')

    def test_figures_added(self):
        """Фигуры добавляются в список для отрисовки"""

        paint = Engine2D(300, 400)
        figures_before = len(paint.canvas.canvas_list)
        circle = Circle(0, 1, 5)
        paint.canvas.add(circle)
        figures_after = len(paint.canvas.canvas_list)
        self.assertNotEqual(figures_before, figures_after,
                            'Фигура не добавлена в список для отрисовки')

    def test_clean(self):
        """Функция очищает список после отрисовки фигур"""

        paint = Engine2D(300, 400)
        circle = Circle(0, 1, 5)
        paint.canvas.add(circle)
        paint.draw()
        figures_after = len(paint.canvas.canvas_list)
        self.assertEqual(figures_after, 0,
                         'Фигура не добавлена в список для отрисовки')

    def test_change_color(self):
        paint = Engine2D(300, 400)
        color_before = paint.canvas.color
        paint.change_color('green')
        color_after = paint.canvas.color
        self.assertNotEqual(color_before, color_after,
                            'Цвет карандаша изменен')


if __name__ == '__main__':
    pytest.main()
