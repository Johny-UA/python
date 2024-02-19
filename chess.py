
class Figure:
   color: str = 'white'
   position_on_the_table = 1,1
   _max_positions = 8,1

   def change_color(self) -> None:
      self.color = 'black' if self.color == 'white' else 'white'

   def move(self, position):
      self.position_on_the_table[0] = position[0]
      self.position_on_the_table[-1] = position[-1]

   def count_absolute_difference(self, position):
      return abs(self.position_on_the_table[0] - position[0]), abs(self.position_on_the_table[-1] - position[-1])

   def checking(self, position):
      raise NotImplementedError



class Peshka(Figure):

   def checking(self, position):
      if self.position_on_the_table[0] == position[0]:
         if self.color == 'white':
            return position[-1]  == self.position_on_the_table[-1] + 1
         else:
            return position[-1] == self.position_on_the_table[-1] - 1
      else: 
         return False



class Horse(Figure):

   def checking(self, position):
      new_position = self.count_absolute_difference(position)
      return (new_position[0] == 1 and new_position[-1] == 2) or (new_position[0] == 2 and new_position[-1] == 1)


class Oficer(Figure):

   def checking(self, position):
      new_position = self.count_absolute_difference(position)
      return new_position[0] == new_position[-1] and new_position[0] > 1


class Tura(Figure):

   def checking(self, position):
      return (position[0] == self.position_on_the_table[0] and position[-1] != self.position_on_the_table[-1]) or (position[0] != self.position_on_the_table[0] and position[-1] == self.position_on_the_table[-1])


class Queen(Figure):

   def checking(self, position):
      new_position = self.count_absolute_difference(position)
      first_way = new_position[0] == new_position[-1] and new_position[0] > 1
      second_way = (position[0] == self.position_on_the_table[0] and position[-1] != self.position_on_the_table[-1]) or (position[0] != self.position_on_the_table[0] and position[-1] == self.position_on_the_table[-1])
      return first_way or second_way


class King(Figure):
   
   def checking(self, position):
      new_position = self.count_absolute_difference(position)
      return new_position[0] <= 1 and new_position[-1] <= 1 and not (not new_position[0] == 0 and not new_position[-1] == 0)