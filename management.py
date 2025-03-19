#조건 : 5명의 학생 교과목 점수를 입력받아 
#       총점,평균,학점,등수를 계산하는 프로그램 작성
# list = [학생1, 학생2, 학생3, 학생4, 학생5]

total = [] #영어,C, Python 점수 총합
avg = []   #세 과목의 평균 점수
grade = [] #평균점수에 따른 학점
rank = []  #평균점수에 따른 전체 등수
Stu_count = 0   # 몇번째 학생까지 입력했는지 판단하기 위한 변수

while True: #점수 입력
    if Stu_count == 5:
        Stu_count = 0 #아래 출력에서 한번 더 쓰기 위해 0으로 초기화
        break
    
    print(Stu_count+1,"번째 학생 점수 입력")
    English = int(input('영어 점수 : '))
    C = int(input('C 점수 : '))
    py = int(input('python 점수 : '))
    print("")
    total.append(English + C + py)
    avg.append(total[Stu_count]/3)
    if avg[Stu_count] >= 90 :
        grade.append("A")

    elif avg[Stu_count] >= 80 :
         grade.append("B")

    elif avg[Stu_count] >= 70 :
         grade.append("C")

    elif avg[Stu_count] >= 60 :
         grade.append("D")

    elif avg[Stu_count] < 60 :
         grade.append("F")
    Stu_count += 1 
#등수 구하기
#sub_avg를 내림차순 정렬
#sub_avg의 인덱스가 등수를 의미
#avg 와 sub_avg의 값이 일치하는 순간을 찾아 sub_avg의 인덱스값을 rank[]에 저장
sub_avg = avg.copy() 
sub_avg.sort(reverse=True)
for i in range(5):
    for j in range(5):
        if avg[i] == sub_avg[j]:
            j +=1
            rank.append(j)
            break
        else :
            j +=1
            continue
             
print("\n")
while True:  #결과 출력
    if Stu_count == 5:
        break
    print(Stu_count+1,"번째 학생")
    print("총점 : ", total[Stu_count])
    print("평균 : ","%.2f"%avg[Stu_count])
    print("(평균)학점 : ",grade[Stu_count])
    print("등수 : ", rank[Stu_count],"등")
    print("")
    Stu_count += 1 







