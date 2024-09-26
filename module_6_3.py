class Horse:
    def __int__(self):
        super().__init__()
        self.x_distance = 0
        self.sound = 'Frrr'


    def run(self, dx):
        self.x_distance =+dx

class Eagle:
    def __int__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance = +dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self):
        super().run(dx)
        Eagle.fly(dy)

    def get_pos(self):
        print(self.x_distance, self.y_distance)

    def voice(self):
        print(super().sound)

p1 = Pegasus()
print(Pegasus.mro())


print(p1.get_pos())
#p1.move(10, 15)
#print(p1.get_pos())
#p1.move(-5, 20)
#print(p1.get_pos())

#p1.voice()

#print(Pegasus.mro())

