class Square():
    def __init__(self, width, color):
        self.width = width
        self.color = color

oSquare1 = Square(5, 'red')
print(oSquare1)


oSquare2 = oSquare1
print(oSquare2)
