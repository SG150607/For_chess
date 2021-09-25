# CHESS THE GAME


# ♙ - пешка белая
# ♔ - король белый
# ♕ - ферзь белый
# ♖ - ладья белый
# ♗ - слон белый
# ♘ - конь белый

# ♟ - пешка черная
# ♚ - король черный
# ♛ - ферзь черный
# ♜ - ладья черная
# ♝ - слон черный
# ♞ - конь черный

# ================ WHITE ================

class White_Pont:
    def __init__(self, x, y):
        self.icon = "♙"
        self.x = x
        self.y = y


class White_King:
    def __init__(self, x, y):
        self.icon = "♔"
        self.x = x
        self.y = y


class White_Queen:
    def __init__(self, x, y):
        self.icon = "♕"
        self.x = x
        self.y = y


class White_Root:
    def __init__(self, x, y):
        self.icon = "♖"
        self.x = x
        self.y = y


class White_Elephant:
    def __init__(self, x, y):
        self.icon = "♗"
        self.x = x
        self.y = y


class White_Horse:
    def __init__(self, x, y):
        self.icon = "♘"
        self.x = x
        self.y = y


# ================ BLACK ================

class Black_Pont:
    def __init__(self, x, y):
        self.icon = "♟"
        self.x = x
        self.y = y


class Black_King:
    def __init__(self, x, y):
        self.icon = "♚"
        self.x = x
        self.y = y


class Black_Queen:
    def __init__(self, x, y):
        self.icon = "♛"
        self.x = x
        self.y = y


class Black_Root:
    def __init__(self, x, y):
        self.icon = "♜"
        self.x = x
        self.y = y


class Black_Elephant:
    def __init__(self, x, y):
        self.icon = "♝"
        self.x = x
        self.y = y


class Black_Horse:
    def __init__(self, x, y):
        self.icon = "♞"
        self.x = x
        self.y = y


# ============== RULES ================
print('''Дорогие имбецилы! Вы такие тупые, что не знаете правила игры времен денозавров и ваших предков!
Поэтому сегодня и только сегодня специально для вас мы напишем правила этой прекрасной игры.
В ней 7 фигур: пешка(Pont), ладья(Root), слон(Elephant), конь(Horse), король(King) и королева/ферзь(Queen)
Каждая фигура ходит по разному(https://youtu.be/xn423wPvNcs): пешка ходит 1 раз вперед, но пока она не дошла до середины поля может с''')

# 0 - белый
# 1 - черный

# -White
white_pont1 = White_Pont(1, 7)
white_pont2 = White_Pont(2, 7)
white_pont3 = White_Pont(3, 7)
white_pont4 = White_Pont(4, 7)
white_pont5 = White_Pont(5, 7)
white_pont6 = White_Pont(6, 7)
white_pont7 = White_Pont(7, 7)
white_pont8 = White_Pont(8, 7)

white_king = White_King(4, 8)
white_queen = White_Queen(5, 8)
white_rootL = White_Root(8, 8)
white_rootR = White_Root(1, 8)
white_elephantL = White_Elephant(3, 8)
white_elephantR = White_Elephant(6, 8)
white_horseL = White_Horse(2, 8)
white_horseR = White_Horse(7, 8)

# -Black
black_pont1 = Black_Pont(1, 2)
black_pont2 = Black_Pont(2, 2)
black_pont3 = Black_Pont(3, 2)
black_pont4 = Black_Pont(4, 2)
black_pont5 = Black_Pont(5, 2)
black_pont6 = Black_Pont(6, 2)
black_pont7 = Black_Pont(7, 2)
black_pont8 = Black_Pont(8, 2)

black_king = Black_King(4, 1)
black_queen = Black_Queen(5, 1)
black_rootL = Black_Root(1, 1)
black_rootR = Black_Root(8, 1)
black_elephantL = Black_Elephant(3, 1)
black_elephantR = Black_Elephant(6, 1)
black_horseL = Black_Horse(2, 1)
black_horseR = Black_Horse(7, 1)

# ================= variables ====================
a1 = '◻'
a2 = '◼'
a3 = '◻'
a4 = '◼'
a5 = '◻'
a6 = '◼'
a7 = '◻'
a8 = '◼'

b1 = '◼'
b2 = '◻'
b3 = '◼'
b4 = '◻'
b5 = '◼'
b6 = '◻'
b7 = '◼'
b8 = '◻'

c1 = '◻'
c2 = '◼'
c3 = '◻'
c4 = '◼'
c5 = '◻'
c6 = '◼'
c7 = '◻'
c8 = '◼'

d1 = '◼'
d2 = '◻'
d3 = '◼'
d4 = '◻'
d5 = '◼'
d6 = '◻'
d7 = '◼'
d8 = '◻'

e1 = '◻'
e2 = '◼'
e3 = '◻'
e4 = '◼'
e5 = '◻'
e6 = '◼'
e7 = '◻'
e8 = '◼'

f1 = '◼'
f2 = '◻'
f3 = '◼'
f4 = '◻'
f5 = '◼'
f6 = '◻'
f7 = '◼'
f8 = '◻'

g1 = '◻'
g2 = '◼'
g3 = '◻'
g4 = '◼'
g5 = '◻'
g6 = '◼'
g7 = '◻'
g8 = '◼'

h1 = '◼'
h2 = '◻'
h3 = '◼'
h4 = '◻'
h5 = '◼'
h6 = '◻'
h7 = '◼'
h8 = '◻'
num = 1

top_bar = [[[''], ['      1'], [' 2'], [' 3'], [' 4'], [' 5'], [' 6'], [' 7'], [' 8']],
           [[''], [''], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'],
            ['-'], ['-'], ['-'], ['-'], ['-']]]
board = [[[a1], [b1], [c1], [d1], [e1], [f1], [g1], [h1]],
         [[a2], [b2], [c2], [d2], [e2], [f2], [g2], [h2]],
         [[a3], [b3], [c3], [d3], [e3], [f3], [g3], [h3]],
         [[a4], [b4], [c4], [d4], [e4], [f4], [g4], [h4]],
         [[a5], [b5], [c5], [d5], [e5], [f5], [g5], [h5]],
         [[a6], [b6], [c6], [d6], [e6], [f6], [g6], [h6]],
         [[a7], [b7], [c7], [d7], [e7], [f7], [g7], [h7]],
         [[a8], [b8], [c8], [d8], [e8], [f8], [g8], [h8]]]
bottom_bar = [
    [[''], [''], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'], ['-'],
     ['-'], ['-'], ['-'], ['-']]]

for line in top_bar:
    for elem in line:
        print(*elem, end=" ")
    print("")

for line in board:
    print(num, end=" ")
    print("| ", end='')
    for elem in line:
        print(*elem, end=" ")
    num += 1
    print("|")

for line in bottom_bar:
    for elem in line:
        print(*elem, end=" ")
    print("")