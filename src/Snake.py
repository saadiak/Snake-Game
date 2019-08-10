#Snake.py
import random
class Snake:
    def __init__(self):
        self._top_left_x = 0.5
        self._top_left_y = 0.5
        self._width = 0.1
        self._height = 0.05
    def width(self):
        return self._width
    def height(self):
        return self._height
    def top_left_x(self):
        return self._top_left_x
    def top_left_y(self):
        return self._top_left_y
    def add_width(self):
        self._width += 0.01
    def add_height(self):
        self._height += 0.01
    def move_right(self):
        self._top_left_x += 0.01
    def move_left(self):
        self._top_left_x -= 0.01
    def move_down(self):
        self._top_left_y += 0.01
    def move_up(self):
        self._top_left_y -= 0.01

class Food:
    def __init__(self):
        self._top_left_x = random.uniform(0.04, 0.96)
        self._top_left_y = random.uniform(0.04, 0.96)
        self._width = 0.02
        self._height = 0.02
    def top_left_x(self):
        return self._top_left_x
    def top_left_y(self):
        return self._top_left_y
    def width(self):
        return self._width
    def height(self):
        return self._height

class GameState:
    def __init__(self):
        self._Snake= Snake()
        self._Food= Food()
    def Snake(self):
        return self._Snake
    def Food(self):
        return self._Food
    def eaten(self):
        print('yo')
        if self._Snake.top_left_x() + 0.01 <= self._Food.top_left_x() and self._Snake.top_left_x() - 0.01 >= self._Food.top_left_x():
            print('sup')
            if self._Snake.top_left_y() == self._Food.top_left_y():
                print ('hi')
                self._Food = Food()
                print('done')
    
