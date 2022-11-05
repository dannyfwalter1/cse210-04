import pyray
from game.shared.point import Point

class KeyboardService: 
  def __init__(self, cell_size = 1):
    self._cell_size = cell_size

  def get_movement(self):
    nx = 0
    ny = 0
    
    if pyray.is_key_pressed(pyray.KEY_RIGHT):
      nx = 1

    if pyray.is_key_pressed(pyray.KEY_LEFT):
      nx = -1
    
    if pyray.is_key_pressed(pyray.KEY_UP):
      ny = 1

    if pyray.is_key_pressed(pyray.KEY_DOWN):
      ny = -1
    
    direction = Point(nx, ny)

    direction = direction.get_x * direction.get_y * self.cell_size

    return direction