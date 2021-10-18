import random
A = "A"   #postavicky
B = "B"
hA = "a"  #postavicky v domceku (kvoli prehladnosti)
hB = "b"

#####################################################################
###                          Grid Maker                           ###
#####################################################################

def grid(n):
    gr=[]         # prazdny grid
    c=0
    for i in range(n):
        i=[]      # prazdny riadok v gride
        c=c+1     # counter-pocitadlo riadkov
        f= n//2
        if(1<c<n):
            for j in range(n):
                if(j==f):
                    if(c==f+1):
                        i.append("X")
                    else:
                        i.append("D")
                elif(c==f+1):
                    if(0<j<n-1):
                        i.append("D")
                    else:
                        i.append("*")
                elif(c==f or c==f+2):
                    i.append("*")
                elif(j==f-1 or j==f+1):
                    i.append("*")
                else:
                    i.append(" ")
        elif(c==1 or c==n):
            for j in range(n):
                if(f-2<j<f+2):
                    i.append("*")
                else:
                    i.append(" ")
        else:
            for j in range(n):
                i.append(" ")
        gr.append(i)
    return gr

def printGrid(gr):            # funkcia na tlacenie hracej plochy/gridu
    for i in range(len(gr)):
        for j in gr[i]:
            print(j,end=" ")
        print()

def setPlayers(gr):           # funkcia setPlayers, pozostatok rekurzie
    f = len(gr)
    f2 = (len(gr))//2       #half
    gr[0][f2+1] = A
    gr[f-1][f2-1] = B
    return gr
	
def cubeThrow():              # funkcia Hodu kockou.
    num=random.randint(1,6)
    if num == 6:
        return num + cubeThrow()
    return num

#####################################################################
###                     Move defined for pawn A                   ###
#####################################################################

# hraciu plochu som si rozdelil na 4 casti/kvadranty, z dovodu
# rozdielnych vlastnosti pohybu panacika na tychto kvadrantoch

# jednotlive kvadranty vracaju dalsi ak ich vlastny pohyb uz
# nieje mozne vykonat. posledny kvadrant pre panacika vracia
# pohyb do domceku/ToHouse

def moveQAa(gr,n,pawn): #in quadrant A
    f= len(gr)
    f2= len(gr)//2
    number=0
    for y in range(0,f2+1):
        for x in range(f2+1,f):
            if gr[y][x]!=" "and gr[y][x]!="D"and gr[y][x]!="X" and gr[y][x]!="a" and gr[y][x]!="b":
                number = number+1
                if number == n :
                    gr[y][x]=pawn
                    return gr
    return moveQBa(gr,abs((f-1)-n),pawn)

def moveQBa(gr,n,pawn): #in quadrant B
    f= len(gr)
    f2= len(gr)//2
    number=0
    for y in range(f2+1,f):
        for x in (range(f-1,f2-1,-1)):
            if gr[y][x]!=" "and gr[y][x]!="D"and gr[y][x]!="X" and gr[y][x]!="a" and gr[y][x]!="b":
                number = number+1
                if number == n :
                    gr[y][x]=pawn
                    return gr
    return moveQCa(gr,abs((f-1)-n),pawn)

def moveQCa(gr,n,pawn): #in quadrant C
    f= len(gr)
    f2= len(gr)//2
    number=0
    for y in range(f-1,f2-1,-1):
        for x in range(f2-1,-1,-1):
            if gr[y][x]!=" "and gr[y][x]!="D"and gr[y][x]!="X" and gr[y][x]!="a" and gr[y][x]!="b":
                number = number+1
                if number == n :
                    gr[y][x]=pawn
                    return gr
    return moveQDa(gr,abs((f-1)-n),pawn)

def moveQDa(gr,n,pawn): #in quadrant D
    f= len(gr)
    f2= len(gr)//2
    number=0
    for y in range(f2-1,-1,-1):
        for x in range(0,f2+1):
            if gr[y][x]!=" "and gr[y][x]!="D"and gr[y][x]!="X" and gr[y][x]!="a" and gr[y][x]!="b":
                number = number+1
                if number == n :
                    gr[y][x]=pawn
                    return gr
    return toHouse(gr,abs((f-1)-n),pawn)

#####################################################################
###                     Move defined for pawn B                   ###
#####################################################################

def moveQAb(gr,n,pawn): #in quadrant A
    f= len(gr)
    f2= len(gr)//2
    number=0
    for y in range(0,f2+1):
        for x in range(f2+1,f):
            if gr[y][x]!=" "and gr[y][x]!="D"and gr[y][x]!="X" and gr[y][x]!="a" and gr[y][x]!="b":
                number = number+1
                if number == n :
                    gr[y][x]=pawn
                    return gr
    return moveQBb(gr,abs((f-1)-n),pawn)

def moveQBb(gr,n,pawn): #in quadrant B
    f= len(gr)
    f2= len(gr)//2
    number=0
    for y in range(f2+1,f):
        for x in (range(f-1,f2-1,-1)):
            if gr[y][x]!=" "and gr[y][x]!="D"and gr[y][x]!="X" and gr[y][x]!="a" and gr[y][x]!="b":
                number = number+1
                if number == n :
                    gr[y][x]=pawn
                    return gr
    return toHouse(gr,abs((f-1)-n),pawn)

def moveQCb(gr,n,pawn): #in quadrant C
    f= len(gr)
    f2= len(gr)//2
    number=0
    for y in range(f-1,f2-1,-1):
        for x in range(f2-1,-1,-1):
            if gr[y][x]!=" "and gr[y][x]!="D"and gr[y][x]!="X" and gr[y][x]!="a" and gr[y][x]!="b":
                number = number+1
                if number == n :
                    gr[y][x]=pawn
                    return gr
    return moveQDb(gr,abs((f-1)-n),pawn)

def moveQDb(gr,n,pawn): #in quadrant D
    f= len(gr)
    f2= len(gr)//2
    number=0
    for y in range(f2-1,-1,-1):
        for x in range(0,f2+1):
            if gr[y][x]!=" "and gr[y][x]!="D"and gr[y][x]!="X" and gr[y][x]!="a" and gr[y][x]!="b":
                number = number+1
                if number == n :
                    gr[y][x]=pawn
                    return gr
    return moveQAb(gr,abs((f-1)-n),pawn)

#####################################################################
###             To House Move defined for both                    ###
#####################################################################

def toHouse(gr,n,pawn): #pohyb do domceka po prejdeni celej dlzky pola
    f= len(gr)
    f2= len(gr)//2
    number=0
    if pawn==A:         # player A
        for y in range(0,f2):
            for x in range(f2,f2+1):
                if gr[y][x]!=" "and gr[y][x]!="*"and gr[y][x]!="X"and gr[y][x]!="a":
                    number+=1
                    if number == n:
                        gr[y][x]=pawn
                        return gr
                    if n > (f-3)/2:
                        gr[f2-1][f2]=pawn
                        return gr
    if pawn==B:         # player B
        for y in range(f-1,f2,-1):
            for x in range(f2+1,f2-1,-1):
                if gr[y][x]!=" "and gr[y][x]!="*"and gr[y][x]!="X" and gr[y][x]!="b":
                    number+=1
                    if number == n:
                        gr[y][x]=pawn
                        return gr
                    if n > (f-3)/2:
                        gr[f2+1][f2]=pawn
                        return gr
    return "o"#return "o" je pozostatok handmade debuggingu

#####################################################################
###             Pawn    Move defined for both                     ###
#####################################################################

def pawnMoveA(gr,n,pawn):                 # player A
    try:
        return moveQAa(gr,n,pawn)
    except(TypeError,IndexError):
        try:
            return moveQBa(gr,n,pawn)
        except(TypeError,IndexError):
            try:
                return moveQCa(gr,n,pawn)
            except(TypeError,IndexError):
                try:
                    return moveQDa(gr,n,pawn)
                except(TypeError,IndexError):
                    toHouse(gr,n,pawn)
def pawnMoveB(gr,n,pawn):                 # player B
    try:
        return moveQCb(gr,n,pawn)
    except(TypeError,IndexError):
        try:
            return moveQDb(gr,n,pawn)
        except(TypeError,IndexError):
            try:
                return moveQAb(gr,n,pawn)
            except(TypeError,IndexError):
                try:
                    return moveQBb(gr,n,pawn)
                except(TypeError,IndexError):
                    toHouse(gr,n,pawn)

#####################################################################
###                 Really useful functions in here               ###
#####################################################################

#GRIDCLEANER cisti pole od "tiena" postavicky ktora sa prave hybala
def gridCleaner(gr,pawn):
    f = len(gr)
    f2 = len(gr)//2
    for y in range(f):
        for x in range(f):
            if gr[y][x] == pawn:
                gr[y][x]="*"
                if pawn == A:
                    if y in range(1,f2) and x == f2:
                        gr[y][x] = "a"
                if pawn == B:
                    if y in range(f2,f-1) and x == f2:
                        gr[y][x] = "b"
                        # "ak si nieco vymazal v oblasti kde su domceky
                        # A,B tak to laskavo daj naspet." ¯\_(ツ)_/¯
                
                        #prepisem si postavicky v domceku na toLower aby
                        #spravne fungoval pohyb                   
    return gr

# hra_Acka je druha uloha naseho projektu, medzifunkcia podla ktorej
# som definoval hru oboch hracov. tuto nieje definovane vyhadzovanie
# kedze hra iba jeden hrac sam sosebou  @(^_^)@
def hra_Acka(gr):
    throws=[]
    f = len(gr)
    gl =  (f*4)-4 

    while sum(throws) <=gl:
        throws.append(cubeThrow())
        num = len(throws)-1
        print("You threw",throws[num],"moving now!!")
        printGrid(pawnMoveA(gridCleaner(gr,A),sum(throws),A))
        if sum(throws) >= gl:
            print("You won the game",A,"congratulations!")

def hra_A_vs_B(gr):
    throws_A=[]  # pocitadla pohybu po gride, listy
    throws_B=[]
    clocks = 1   # hodiny, urcuju kto je na tahu, ako v sachu
    win = False  # boolean vyhry
 
    f = len(gr)
    gl = (f*4)-4

    maxPawns = (f-3)//2
    pawns_A=0    #(x-3)//2  hodnota ktoru tu chceme. nase pocitadlo
    pawns_B=0    #panacikov. kto dosiahne tohto poctu a uspesne vojde
                 #s poslednym do domceka vyhrava.
    while True:
        if clocks % 2 != 0 :   # hrac A sa hybe s neparnym clockom
            while sum(throws_A) <=gl and clocks % 2 != 0 and win == False:
                clocks+=1
                throws_A.append(cubeThrow())
                num = len(throws_A)-1
                print("You threw",throws_A[num],"moving now A !!")
                printGrid(pawnMoveA(gridCleaner(gr,A),sum(throws_A),A))

                # A a B sa mozu stretnut na ploche a ich stret je
                # popisany vztahom ze rozdiel suctu vsetkych pohybov
                # konkretnych panacikov je [2*(len(grid))-2], toto
                # funguje pre grid vselijakych neparnych rozmerov
                # s ramenami sirky 3 
                if (abs(sum(throws_A) -sum(throws_B)) == (2*f) -2 ):
                    throws_B=[]
                    print("Fatality! You knocked out enemy player.")
                    print("        ̿ ̿̿ ̿’̿’̵͇̿̿з=(◣_◢)=ε/̵͇̿̿/’̿’̿ ̿ ̿̿﻿ ̿̿ ̿̿ ")
                if sum(throws_A) > gl:
                    # ak jeden panak uz dosiahol domcek, zvys pocitadlo
                    # panakov o jedna a zacni sa hybat s novym.
                    throws_A=[]
                    pawns_A+=1
                if pawns_A == maxPawns :
                    print("You won the game",A,"congratulations!")
                    win = True

        ##########################################################
                    
        if clocks % 2 == 0 :   # hrac B sa hybe s parnym clockom
            while sum(throws_B) <=gl and clocks % 2 == 0 and win == False:
                clocks+=1
                throws_B.append(cubeThrow())
                num = len(throws_B)-1
                print("You threw",throws_B[num],"moving now B !!")
                printGrid(pawnMoveB(gridCleaner(gr,B),sum(throws_B),B))
                if (abs(sum(throws_A) -sum(throws_B)) == (2*f) -2 ):
                    throws_A=[]
                    print("Fatality! You knocked out enemy player.")
                    print("        ̿ ̿̿ ̿’̿’̵͇̿̿з=(◣_◢)=ε/̵͇̿̿/’̿’̿ ̿ ̿̿﻿ ̿̿ ̿̿ ")
                if sum(throws_B) > gl:
                    pawns_B+=1
                    throws_B=[]
                if pawns_B == maxPawns :
                    print("You won the game",B,"congratulations!")
                    win = True

gameGrid = grid(9) # hracia plocha ktoru si vzdy pred hrou vytvorim

hra_A_vs_B(gameGrid) # spustenie hry


