from map import pole
from pers import man

from anamy import Vrag
from anamy import Small_vrag
from anamy import Big_vrag
from anamy import Mid_vrag
from coin import Coin
from sposob import clas,level,Sposob,clas_an,level_an,Sposob_an,game

from color import out_red,out_yellow,out_blue,out_bur

en1 = Vrag()

#en3=Mid_vrag(clas_an,hard_an,Sposob_an)
#en4=Big_vrag()

map_1=pole()
person=man(map_1.mas1)
en2 = Small_vrag()

coin_1=Coin(map_1.mas1,map_1.a)


while True:
    if person.do=='e':

        out_bur( "you class:",  ),print(person.classication)
        out_yellow('you name:'),print(person.name)
        out_red('you hp:'),print(person.op0)
        out_blue('you energy:'),print(person.op1)
        print( ' ' )
        out_bur( 'you enemy:'),print(en2.classication )
        out_red( 'hp enemy:'),print(en2.hp_an )
        out_blue( 'energy enemy:' ),print(en2.energia_an )
        rop=input('continue y/n')
        if rop=='y':
            pass
        else:
            break
    out_red('e')

    map_1.print_mas()
    person.move(map_1)
    en2.mav_an(map_1)
    Coin( map_1.mas1, map_1.a )

    #print( 'win' )
    #print( 'ты открыл чит код для этой игры 10 введи его когда будеш выберать классы' )
    #print('ты прошел игру ',pers.name,'поздравляю ')
    #print( 'ты открыл чит код для этой игры 0 введи его когда будеш выберать сложность' )




