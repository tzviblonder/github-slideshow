import random,time

cpuTurn=['7','8','9','4','5','6','1','2','3']

commentary=['Good choice!','I see what youre doing there..', 'Why would you go there?','Clever!','Cant believe I didnt see that one coming!',
'You must have something in mind.','You may want to re-think your strategy.','Couldnt have picked a better spot myself.']

print('To play, select a number that corresponds to a place on the board (as shown) and press Enter:')
print('')

while True:
    tictactoe={'7':'7','8':'8','9':'9','4':'4','5':'5','6':'6',
'1':'1','2':'2','3':'3'}

    topRow='   ' + str(tictactoe['7']) + '|' + str(tictactoe['8'])+'|' + str(tictactoe['9'])
    divideLine=('  -------')
    middleRow= '   '+ str(tictactoe['4'])+'|'+str(tictactoe['5'])+'|'+str(tictactoe['6'])
    bottomRow= '   ' + str(tictactoe['1'])+'|' + str(tictactoe['2'])+'|'+str(tictactoe['3'])

    print()
    print(topRow)
    print(divideLine)
    print(middleRow)
    print(divideLine)
    print(bottomRow)
    print()
    break

topRow='   ' + str(tictactoe['7']) + '|' + str(tictactoe['8'])+'|' + str(tictactoe['9'])
divideLine=('  -------')
middleRow= '   '+ str(tictactoe['4'])+'|'+str(tictactoe['5'])+'|'+str(tictactoe['6'])
bottomRow= '   ' + str(tictactoe['1'])+'|' + str(tictactoe['2'])+'|'+str(tictactoe['3'])

tictactoe={'7':' ','8':' ','9':' ','4':' ','5':' ','6':' ',
'1':' ','2':' ','3':' '}

while True:
    time.sleep(.6)
    print()
    print('   X turn')
    print('     ',end='')
    xturn=input()
    cpuTurn.remove(xturn)
    tictactoe[xturn]='X'

    if tictactoe['7']=='X' and tictactoe['8']=='X' and tictactoe['9']=='X' or tictactoe['4']=='X' and tictactoe['5']=='X' and tictactoe['6']=='X'or tictactoe['1']=='X' and tictactoe['2']=='X' and tictactoe['3']=='X'or tictactoe['7']=='X' and tictactoe['5']=='X' and tictactoe['3']=='X'or tictactoe['9']=='X' and tictactoe['5']=='X' and tictactoe['1']=='X'or tictactoe['7']=='X' and tictactoe['4']=='X' and tictactoe['1']=='X'or tictactoe['8']=='X' and tictactoe['5']=='X' and tictactoe['2']=='X'or tictactoe['9']=='X' and tictactoe['6']=='X' and tictactoe['3']=='X':
        topRow= '   ' + str(tictactoe['7'])+'|' + str(tictactoe['8'])+'|' + str(tictactoe['9'])
        middleRow= '   ' + str(tictactoe['4'])+'|'+str(tictactoe['5'])+'|'+str(tictactoe['6'])
        bottomRow= '   ' + str(tictactoe['1'])+'|' + str(tictactoe['2'])+'|'+str(tictactoe['3'])
        print()
        print(topRow)
        print(divideLine)
        print(middleRow)
        print(divideLine)
        print(bottomRow)
        print()
        time.sleep(.6)
        print('X wins!')
        break
    else:
        topRow= '   ' + str(tictactoe['7'])+'|' + str(tictactoe['8'])+'|' + str(tictactoe['9'])
        middleRow= '   ' + str(tictactoe['4'])+'|'+str(tictactoe['5'])+'|'+str(tictactoe['6'])
        bottomRow= '   ' + str(tictactoe['1'])+'|' + str(tictactoe['2'])+'|'+str(tictactoe['3'])
        time.sleep(.6)
        print()
        print(topRow)
        print(divideLine)
        print(middleRow)
        print(divideLine)
        print(bottomRow)
        print()
        print(commentary[random.randint(0,7)])
        if ' ' not in tictactoe.values():
            print()
            print('Tie!')
            break

    time.sleep(.6)
    print()
    print('   O turn')
    print('     ',end='')
    oturn=input()
    cpuTurn.remove(oturn)
    tictactoe[oturn]='O'
    if tictactoe['7']=='O' and tictactoe['8']=='O' and tictactoe['9']=='O' or tictactoe['4']=='O' and tictactoe['5']=='O' and tictactoe['6']=='O'or tictactoe['1']=='O' and tictactoe['2']=='O' and tictactoe['3']=='O'or tictactoe['7']=='O' and tictactoe['5']=='O' and tictactoe['3']=='O'or tictactoe['9']=='O' and tictactoe['5']=='O' and tictactoe['1']=='O'or tictactoe['7']=='O' and tictactoe['4']=='O' and tictactoe['1']=='O'or tictactoe['8']=='O' and tictactoe['5']=='O' and tictactoe['2']=='O'or tictactoe['9']=='O' and tictactoe['6']=='O' and tictactoe['3']=='O':
        topRow= '   ' + str(tictactoe['7'])+'|' + str(tictactoe['8'])+'|' + str(tictactoe['9'])
        middleRow= '   ' + str(tictactoe['4'])+'|'+str(tictactoe['5'])+'|'+str(tictactoe['6'])
        bottomRow= '   ' + str(tictactoe['1'])+'|' + str(tictactoe['2'])+'|'+str(tictactoe['3'])
        time.sleep(.6)
        print()
        print(topRow)
        print(divideLine)
        print(middleRow)
        print(divideLine)
        print(bottomRow)
        print('O wins!')
        break
    else:
        topRow= '   ' + str(tictactoe['7'])+'|' + str(tictactoe['8'])+'|' + str(tictactoe['9'])
        middleRow= '   ' + str(tictactoe['4'])+'|'+str(tictactoe['5'])+'|'+str(tictactoe['6'])
        bottomRow= '   ' + str(tictactoe['1'])+'|' + str(tictactoe['2'])+'|'+str(tictactoe['3'])
        time.sleep(.6)
        print()
        print(topRow)
        print(divideLine)
        print(middleRow)
        print(divideLine)
        print(bottomRow)
        print()
        print(commentary[random.randint(0,7)])
        if ' ' not in tictactoe.values():
            print()
            print('Tie!')
            break