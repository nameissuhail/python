def game(myl):
    print('This is the list')
    for i in range(0, len(myl), 3):
        print(myl[i:i + 3])
    print(myl)
def pch1():
    choice='wrong'
    while choice not in myl:
        choice=input('Enter a position for Player1')
        if choice not in myl:
            print('out of range')
    return int(choice)
def replace1(myl,position1):
    userch1=input(' Player1 Enter String you want to enter X or O')
    if position1<=len(myl):
            if userch1 not in ['X', 'O']:
              print('Invalid only enter X or O')
              userch1=input(' Player1 Enter String you want to enter X or O')
            else:
                myl[position1]=userch1
            return myl  
def pch2():
    choice='wrong'
    while choice not in myl:
        choice=input('Enter a position for Player2')
        if choice not in myl:
            print('out of range')
    return int(choice)
def replace2(myl,position2):
    userch=input(' Player2 Enter String you want to enter X or O')
    if position2<=len(myl):
        
      if userch not in ['X', 'O']:
        print('Enter Valid Strings X or O')
        userch=input(' Player2 Enter String you want to enter X or O')
      else:
        myl[position2]=userch
      return myl
def check_winner(myl):
    for i in range(0, 9, 3):
      #ROWS
          if myl[i] == myl[i + 1] == myl[i + 2]:
            return myl[i]
    for i in range(3):
      #COLUMS
          if myl[i] == myl[i + 3] == myl[i + 6]:
            return myl[i]
          #DIAGONALS
          if myl[0] == myl[4] == myl[8]:
            return myl[0]
          if myl[2] == myl[4] == myl[6]:
            return myl[2]
          else:
              print('TIE')
    return None
def plach():
    choice='wrong'
    while choice not in ['Y','N']:
        choice=input('Would you like to keep playing Y or N')
        if choice not in ['Y','N']:
            print('choose Y or N')
        if choice=='Y':
            return True
        elif choice=='N':
            return False
lesgo=True
myl=['0','1','2',
     '3','4','5',
     '6','7','8']
while lesgo:
    game(myl)
    position1=pch1()
    myl=replace1(myl,position1)
    winner=check_winner(myl)
    if winner:
      print(f'Player 1 wins')
      break
    game(myl)
    position2=pch2()
    myl=replace2(myl,position2)
    winner=check_winner(myl)
    if winner:
      print(f'Player 2 wins')
      break
    game(myl)
    lesgo=plach()
    
            
