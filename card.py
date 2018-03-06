class Card:
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def print_card(self):
      print('|{0}-{1}|'.format(self.left, self.right))
