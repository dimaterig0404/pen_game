import random
class Coin:
    coin_ot=0
    coin_hp=0
    coin_energia=0
    x=0
    y=0
    def __init__(self,map,a):
        self.coin_hp=random.randint(10,80)
        self.coin_energia=random.randint(10,100)
        self.x=a-1
        self.y=a-1
        map[self.x][self.y]=self.coin_ot

        self.coin_hp = random.randint( 10, 80 )
        self.coin_energia = random.randint( 10, 100 )
        self.x = a - 2
        self.y = a-1
        map[self.x][self.y] = self.coin_ot

        self.coin_hp = random.randint( 10, 80 )
        self.coin_energia = random.randint( 10, 100 )
        self.x = a-3
        self.y = a - 1
        map[self.x][self.y] = self.coin_ot
