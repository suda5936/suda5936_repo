import random

list =[['*','*','*'],['*','*','*'],['*','*','*']]
list_num =[['1','2','3'],['4','5','6'],['7','8','9']]


def print_ttt(): #수를 놓을때마다 판을 보여줌.
     for row in range(0,3):
        for cal in range(0,3):
            print(list[row][cal], end="")
        print()

def insert_ttt(num): #내가 놓는 수.
    num = str(num)
    for row in range(0,3):
        for cal in range(0,3):
            if(list_num[row][cal] == num):
              list[row][cal] = 'O'
              return True

def ai_insert(): #컴퓨터가 놓는 수.
    while(1):
        rand = str(random.randrange(1,10))
        for row in range(0,3):
            for cal in range(0,3):
                if((list_num[row][cal] == rand) and (list[row][cal] == 'O' or list[row][cal] == 'X')):
                    continue
                elif((list_num[row][cal] == rand) and (list[row][cal] != 'O')):
                    list[row][cal] = 'X'
                    return True

def check_list(check): #상대가 이미 배치해놓은 곳인지 확인하는 함수.
    check = str(check)
    for row in range(0,3):
        for cal in range(0,3):
            if((list_num[row][cal] == check) and list[row][cal] != '*'):
              return True

def tiktakto(): #직선이 나오는지 판별하는 함수.
    for row in range(0,3):
     if((list[row][0] == list[row][1] and list[row][1]== list[row][2]) and list[row][0] !='*'):
         return list[row][0]
    for cal in range(0,3):
     if((list[0][cal] == list[1][cal] and list[1][cal]== list[2][cal]) and list[0][cal] !='*'):
         return list[0][cal]
    if((list[1][1] == list [0][2] and list[0][2]==list[2][0]) and list[1][1] != '*'):
        return list[1][1]
    if((list[1][1] == list [0][0] and list[0][0]==list[2][2]) and list[1][1] != '*'):
        return list[1][1]
    return False
     
def fullcount(): #무승부를 확인해주는 함수. *이 아닌곳의 개수를 반환
    count =0
    for row in range(0,3):
        for cal in range(0,3):
            if(list[row][cal] !='*'):
                count = count + 1
    return count
        


for j in list_num: #숫자판을 통해 놓고싶은 공간 확인.
    for i in j:
            print(i, end="")
    print()
while(1):
    print()
    print("MY TURN!")
    tmp =int(input("원하는 곳의 숫자 입력(범위 밖 입력시 탈출) :"))
    print()
    if(tmp >= 10 or  tmp < 1):
        break
    elif(check_list(tmp)): #이미 수가 있으면 잘못된 위치, 재입력.
        print("잘못된 위치")
        continue
    insert_ttt(tmp)
    print_ttt()
    if(tiktakto() == 'O'): #내가 논 이후 O으로 한줄이 생기면 나의 우승.
        print("YOU WIN")
        break
    if(fullcount() ==9): #항상 내가 먼저 시작하므로 내 턴 이후 무승부가 판명남/ *이 아닌곳이 9개 있고 tiktakto함수 결과 우승자가 안나왔으므로 무승부.
        print("draw")
        break
    print("상대 턴 진행") 
    ai_insert()
    print_ttt()
    if(tiktakto() == 'X'): #상대 턴이 진행된 이후 X로 한줄이 생기면 상대방 우승.
        print("OPPONENT WIN")
        break
