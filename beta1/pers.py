from sposob import clas,level
from color import out_red,out_yellow,out_blue,out_bur,out_purpul


class man:
    name = ''
    ot = ''
    x = 0
    y = 0
    dol = 0
    hp=0
    energia=0
    do=''

    def __init__(self, map):
        self.op0=0
        self.op1=0
        self.op5=0
        self.energia = 0
        for i in clas:
            out_red(i)
        while True:
            self.classication = input('entet class')
            self.hp=clas[self.classication][0]
            self.energia=clas[self.classication][1]
            if self.classication==KeyError:
                print('no object')
                pass
            out_red('you hp'),print(self.hp)
            out_blue('you energy'),print(self.energia)


            break
        for i in level:
            out_purpul(i)
        self.dol = input('enter level')
        self.op0 = self.hp + level[self.dol][0]
        self.op1 =self.energia + level[self.dol][1]
        out_red('you hp have changed on '),print(self.op0)
        out_blue('you energy have changed on'),print(self.op1)
        self.name = input('enter name person ')
        self.ot=input('enter view person')
        map[self.x][self.y] = self.ot

    def move(self,map):

        self.do = input('where will you go wasd and use ulta q')
        if self.do == "w":
            if self.x == 0:
                out_red('you do not go')
            else:
                map.mas1[self.x][self.y] = 0
                self.x -= 1
                map.mas1[self.x][self.y] = self.ot

        elif self.do == "s":
            if self.x ==map.a-1 :
                out_red('you do not go')
            else:
                map.mas1[self.x][self.y] = 0
                self.x += 1
                map.mas1[self.x][self.y] = self.ot
        elif self.do == "d":
            if self.y ==map.a-1 :
                out_red('you do not go')
            else:
                map.mas1[self.x][self.y] = 0
                self.y += 1
                map.mas1[self.x][self.y] = self.ot
        elif self.do == "a":
            if self.y ==0:
                out_red('you do not go')
            else:
                map.mas1[self.x][self.y] = 0
                self.y -= 1
                map.mas1[self.x][self.y] = self.ot

        elif clas=='man' and self.do=='q':
            self.bom_1=input('нажми на кнобку wasd для закладки бомбы ')
            if self.bom_1 == "w":
                if self.x == 0:
                    out_red('ты не поставиш')
                else:
                    map.mas1[self.x][self.y] = 0
                    self.x -= 1
                    map.mas1[self.x][self.y] = self.ot
                    self.op5=self.op1-10

            elif self.bom_1 == "s":
                if self.x == map.a - 1:
                    out_red('ты не поставиш')
                else:
                    map.mas1[self.x][self.y] = 0
                    self.x += 1
                    map.mas1[self.x][self.y] = self.ot
                    self.op5 = self.op1 - 10
            elif self.bom_1 == "d":
                if self.y == map.a - 1:
                    out_red('ты не поставиш')
                else:
                    map.mas1[self.x][self.y] = 0
                    self.y += 1
                    map.mas1[self.x][self.y] = self.ot
                    self.op5 = self.op1 - 10
            elif self.bom_1 == "a":
                if self.y == 0:
                    out_red('ты не поставиш')
                else:
                    map.mas1[self.x][self.y] = 0
                    self.y -= 1
                    map.mas1[self.x][self.y] = self.ot
                    self.op5 = self.op1 - 10
            print('ваше хп',self.op0,'',self.op5)
        elif clas=='sun mum friend'and self.do=='q':
            self.bom_2=input('нажми на кнобку wasd для заражении територии  ')
            if self.bom_2 == "w":
                if self.x == 0:
                    out_red('ты не поставиш')
                else:
                    map.mas1[self.x][self.y] = 0
                    self.x -= 1
                    map.mas1[self.x][self.y] = self.ot
                    self.op5=self.op1-15

            elif self.bom_2 == "s":
                if self.x == map.a - 1:
                    out_red('ты не поставиш')
                else:
                    map.mas1[self.x][self.y] = 0
                    self.x += 1
                    map.mas1[self.x][self.y] = self.ot
                    self.op5 = self.op1 - 15
            elif self.bom_2 == "d":
                if self.y == map.a - 1:
                    out_red('ты не поставиш')
                else:
                    map.mas1[self.x][self.y] = 0
                    self.y += 1
                    map.mas1[self.x][self.y] = self.ot
                    self.op5 = self.op1 - 15
            elif self.bom_2 == "a":
                if self.y == 0:
                    out_red('ты не поставиш')
                else:
                    map.mas1[self.x][self.y] = 0
                    self.y -= 1
                    map.mas1[self.x][self.y] = self.ot
                    self.op5 = self.op1 - 15
            print('ваше хп',self.op0,'',self.op5)
        elif clas=='gopnik' and self.do=='q':
            self.bom_3=input('нажми на кнобку wasd для прыжка на 2 клетки   ')
            if self.bom_3 == "w":
                if self.x == 0:
                    out_red('ты не пройдеш')
                else:
                    map.mas1[self.x][self.y] = 0
                    self.x -= 2
                    map.mas1[self.x][self.y] = self.ot
                    self.op5=self.op1-20

            elif self.bom_3 == "s":
                if self.x == map.a - 1:
                    out_red('ты не пройдеш')
                else:
                    map.mas1[self.x][self.y] = 0
                    self.x += 2
                    map.mas1[self.x][self.y] = self.ot
                    self.op5 = self.op1 - 20
            elif self.bom_3 == "d":
                if self.y == map.a - 2:
                    out_red('ты не поставиш')
                else:
                    map.mas1[self.x][self.y] = 0
                    self.y += 2
                    map.mas1[self.x][self.y] = self.ot
                    self.op5 = self.op1 - 20
            elif self.bom_3 == "a":
                if self.y == 0:
                    out_red('ты не поставиш')
                else:
                    map.mas1[self.x][self.y] = 0
                    self.y -= 2
                    map.mas1[self.x][self.y] = self.ot
                    self.op5 = self.op1 - 15
            print('ваше хп',self.op0,'',self.op5)
        elif clas=='bum' and self.do == 'q':
            print('этот класс не может ни чего сделать ')

