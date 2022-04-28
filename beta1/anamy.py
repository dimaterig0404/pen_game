import random
from sposob import clas_an,level_an

class Vrag:

    x = 3
    y = 3
    hp_an=0
    energia_an=0
    ot_an = 'v'

    def mav_an(self, map):
        do_an = random.randint(0,5)
        self.x=map.a-1
        self.y=map.a-1
        if do_an == 4:
            if self.x == 0:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.x -= 1
                map.mas1[self.x][self.y] = self.ot_an

        elif do_an == 1:
            if self.x == map.a - 1:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.x += 1
                map.mas1[self.x][self.y] = self.ot_an
        elif do_an == 2:
            if self.y == map.a - 1:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.y += 1
                map.mas1[self.x][self.y] = self.ot_an
        elif do_an ==3:
            if self.y == 0:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.y -= 1
                map.mas1[self.x][self.y] = self.ot_an
        elif do_an==4:
            if self.x == 0:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.x -= 1
                map.mas1[self.x][self.y] = self.ot_an
class Small_vrag(Vrag):

    def __init__(self):

        for i in clas_an:
            print( i )
        self.classication = input('enter class enemy ')
        self.hp_an = clas_an[self.classication][0]
        self.energia_an = clas_an[self.classication][1]
        self.ot_an=input('enter enemy ot ')

    def mad_1(self,map):

        do_an = random.randint(0, 5)
        if do_an == 1:
            if self.x == 0:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.x -= 1
                map.mas1[self.x][self.y] = self.ot_an

        elif do_an == 4:
            if self.x == map.a - 1:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.x += 1
                map.mas1[self.x][self.y] = self.ot_an
        elif do_an == 2:
            if self.y == map.a - 1:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.y += 1
                map.mas1[self.x][self.y] = self.ot_an
        elif do_an == 3:
            if self.y == 0:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.y -= 1
                map.mas1[self.x][self.y] = self.ot_an

    def mad_2(self, ):
        print('зауч')
        self.hp_an = 100
        self.energia_an = 100
        self.level = 1
        map[self.x][self.y] = map.pole.a
class Mid_vrag(Vrag):

    def __init__(self):
        self.hp_an = 200
        self.energia_an=200


    def mad_2(self,map):
        do_an = random.randint(0, 4)
        if do_an == 1:
            if self.x == 0:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.x -= 1
                map.mas1[self.x][self.y] = self.ot_an

        elif do_an == 4:
            if self.x == map.a - 1:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.x += 1
                map.mas1[self.x][self.y] = self.ot_an
        elif do_an == 2:
            if self.y == map.a - 1:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.y += 1
                map.mas1[self.x][self.y] = self.ot_an
        elif do_an == 3:
            if self.y == 0:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.y -= 1
                map.mas1[self.x][self.y] = self.ot_an
class Big_vrag(Vrag):

    def __init__(self):
        self.hp_an = 200
        self.energia_an=200
        map[self.x][self.y] = self.ot_an

    def mad_3(self, map):
        do_an = random.randint(0,5)
        if do_an == 1:
            if self.x == 0:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.x -= 1
                map.mas1[self.x][self.y] = self.ot_an

        elif do_an == 1:
            if self.x == map.a - 1:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.x += 1
                map.mas1[self.x][self.y] = self.ot_an
        elif do_an == 2:
            if self.y == map.a - 1:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.y += 1
                map.mas1[self.x][self.y] = self.ot_an
        elif do_an ==3:
            if self.y == 0:
                pass
            else:
                map.mas1[self.x][self.y] = ' '
                self.y -= 1
                map.mas1[self.x][self.y] = self.ot_an





