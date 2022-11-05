class Color:
  def __init__(self, red, green, blue):
    self._red = red
    self._green = green
    self._blue = blue

  def colored(self):
    return (self._red, self._green, self._blue)