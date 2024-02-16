
class Figure:
   color: str = 'white'
   position_on_the_table = 1,1
   _max_positions = 8,1
   _Error = False

   def Error(self, moving):
      if moving[0] > self._max_positions[0] or moving[0] < self._max_positions[-1] or moving[-1] > self._max_positions[0] or moving[-1] < self._max_positions[-1]:
         print('error')
         self._Error = True
      else:
         self._Error = False

   def change_color(self):
      if self.color == 'white':
         self.color = "black"
      else:
         self.color = 'white'



class King(Figure):

   def movement(self, moving):
      if self._Error:
         pass
      elif abs(self.position_on_the_table[0] - moving[0]) == 1 and self.position_on_the_table[-1] == moving[-1] or abs(self.position_on_the_table[-1] - moving[-1]) == 1 and self.position_on_the_table[0] == moving[0] or abs(self.position_on_the_table[0] - moving[0]) == 1 and abs(self.position_on_the_table[-1] - moving[-1]) == 1:
         self.position_on_the_table = moving


class Queen(Figure):

   def movement(self, moving):
      if self._Error:
         pass
      elif self.position_on_the_table[0] == moving[0] or self.position_on_the_table[-1] == moving[-1] or abs(self.position_on_the_table[0] - moving[0]) == abs(self.position_on_the_table[-1] - moving[-1]):
         self.position_on_the_table = moving




class Peshka(Figure):

   def movement(self, moving):
      if self._Error:
         pass
      elif self.position_on_the_table[0] - moving[0]== -1 and moving[-1] == self.position_on_the_table[-1] and self.color == 'white':
         self.position_on_the_table = moving
      elif self.position_on_the_table[0] - moving[0]== 1 and moving[-1] == self.position_on_the_table[-1] and self.color == 'black':
         self.position_on_the_table = moving
      else:
         print("error")



class Tura(Figure):

   def movement(self, moving):
      if self._Error:
         pass
      elif self.position_on_the_table[0] == moving[0] or self.position_on_the_table[-1] == moving[-1]:
         self.position_on_the_table = moving


class Ferz(Figure):

   def movement(self, moving):
      if self.__Error == 'True':
         pass
      if abs(self.position_on_the_table[0] - moving[0]) == abs(self.position_on_the_table[-1] - moving[-1]):
         self.position_on_the_table = moving



class Horse(Figure):
   
   def movement(self,moving):
      if self._Error:
         pass
      elif abs(moving[0] - self.position_on_the_table[0]) == 2 and abs(moving[-1]- self.position_on_the_table[-1]) == 1 or abs(moving[0] - self.position_on_the_table[0]) == 1 and abs(moving[-1]- self.position_on_the_table[-1]) == 2:
         self.position_on_the_table = moving



# ?

# queen = Queen()



# position = 8,1
# position1 = 5,4
# position2 = 1,4
# position3 = 8,8


# queen.Error(position)
# queen.movement(position)
# print(queen.position_on_the_table)
# queen.Error(position1)
# queen.movement(position1)
# print(queen.position_on_the_table)
# queen.Error(position2)
# queen.movement(position2)
# print(queen.position_on_the_table)
# queen.Error(position3)
# queen.movement(position3)
# print(queen.position_on_the_table)



# ?

# king = King()



# position = 2,1
# position1 = 3,2
# position2 = 1,9


# king.Error(position)
# king.movement(position)
# print(king.position_on_the_table)
# king.Error(position1)
# king.movement(position1)
# print(king.position_on_the_table)
# king.Error(position2)
# king.movement(position2)
# print(king.position_on_the_table)
# ?

# horse = Horse()

# position = 3,2
# position1 = 10,4
# position2 = 2,4

# horse.Error(position)
# horse.movement(position)
# print(horse.position_on_the_table)
# horse.Error(position1)
# horse.movement(position1)
# print(horse.position_on_the_table)
# horse.Error(position2)
# horse.movement(position2)
# print(horse.position_on_the_table)

# ?

# ferz = Ferz()


# position = 7,7
# position1 = 9,5
# position2 = 8,6


# ferz.movement(position)
# print(ferz.position_on_the_table)
# ferz.movement(position1)
# print(ferz.position_on_the_table)
# ferz.movement(position2)
# print(ferz.position_on_the_table)


# ?

# tura = Tura()

# position = 1,8
# position1 = 3,8
# position2 = 9,5

# tura.movement(position)
# print(tura.position_on_the_table)
# tura.movement(position1)
# print(tura.position_on_the_table)
# tura.movement(position2)
# print(tura.position_on_the_table)


# print(tura.position_on_the_table)


# ?
# peshka = Peshka()


# position = 2,1
# position1 = 2,1
# position2 = 3,1


# peshka.change_color()
# peshka.movement(position)
# print(peshka.position_on_the_table)
# peshka.change_color()
# peshka.movement(position1)
# print(peshka.position_on_the_table)
# peshka.movement(position2)
# print(peshka.position_on_the_table)