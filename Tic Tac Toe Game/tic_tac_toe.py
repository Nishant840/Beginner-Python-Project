def main():
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    turn = 1

    print("Welcome to Tic Tac Toe")
    cnt = 0
    while True:
        printBoard(xState, zState)

        if turn == 1 :
            print("X's chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1
            cnt += 1
        else :
            print("Y's chance")
            value = int(input("Please enter a value: "))
            zState[value] = 1
            cnt += 1

        win = checkWin(xState,zState)
        turn = 1- turn
        if win != -1 :
            print("Match Over")
            break;
        if cnt == 9:
            print("match tie")
            break;


def printBoard(xState, zState):
    zero = 'X' if xState[0]==1 else 'O' if zState[0]==1 else 0
    one = 'X' if xState[1]==1 else 'O' if zState[1]==1 else 1
    two = 'X' if xState[2]==1 else 'O' if zState[2]==1 else 2
    three = 'X' if xState[3]==1 else 'O' if zState[3]==1 else 3
    four = 'X' if xState[4]==1 else 'O' if zState[4]==1 else 4
    five = 'X' if xState[5]==1 else 'O' if zState[5]==1 else 5
    six = 'X' if xState[6]==1 else 'O' if zState[6]==1 else 6
    seven = 'X' if xState[7]==1 else 'O' if zState[7]==1 else 7
    eight = 'X' if xState[8]==1 else 'O' if zState[8]==1 else 8

    print(f"{zero} | {one} | {two}")
    print("--|---|---")
    print(f"{three} | {four} | {five}")
    print("--|---|---")
    print(f"{six} | {seven} | {eight}")

def checkWin(xState,zState):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X won the match")
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O won the match")
            return 0
        
    return -1

def sum(a,b,c):
    return a+b+c

if __name__ == "__main__":
    main()
