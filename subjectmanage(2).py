total = []  # 총점 
avg = []    # 평균 점수 
grade = []  # 학점 
rank = []   # 등수 

num = []      # 학번 
name = []     # 이름 
English = []  # 영어 점수 
C = []        # C언어 점수 
py = []       # Python 점수 

def inputscore(): 
    student_num = int(input('학번 : '))
    student_name = input('이름 : ')
    eng_score = int(input('영어 점수 : '))
    c_score = int(input('C 점수 : '))
    py_score = int(input('Python 점수 : '))
    return student_num, student_name, eng_score, c_score, py_score

def total_avg(English, C, py):
    total_score = English + C + py
    avg_score = total_score / 3
    total.append(total_score)
    avg.append(avg_score)

def gradecal(avg_score):
    if avg_score >= 90:
        grade.append("A")
    elif avg_score >= 80:
        grade.append("B")
    elif avg_score >= 70:
        grade.append("C")
    elif avg_score >= 60:
        grade.append("D")
    else:
        grade.append("F")

def rankcal():
    sorted_avg = sorted(avg, reverse=True)  # 내림차순
    rank.clear()
    for score in avg:
        rank.append(sorted_avg.index(score) + 1)

def sort_total():#총점 기준으로 오름차순 정렬
    sort = sorted(range(len(total)), key=lambda i: total[i])
    num[:] = [num[i] for i in sort]
    name[:] = [name[i] for i in sort]
    English[:] = [English[i] for i in sort]
    C[:] = [C[i] for i in sort]
    py[:] = [py[i] for i in sort]
    total[:] = [total[i] for i in sort]
    avg[:] = [avg[i] for i in sort]
    grade[:] = [grade[i] for i in sort]
    rank[:] = [rank[i] for i in sort]

def insert_stu(): #학생 삽입 함수
    student_num, student_name, eng_score, c_score, py_score = inputscore()
    num.append(student_num)
    name.append(student_name)
    English.append(eng_score)
    C.append(c_score)
    py.append(py_score)
    total_avg(eng_score, c_score, py_score)
    gradecal(avg[-1])
    rankcal()

def delete_stu(): #학생 삭제 함수
    student_num = int(input("삭제할 학생의 학번을 입력하세요: "))
    if student_num in num:
        index = num.index(student_num)
        del num[index], name[index], English[index], C[index], py[index]
        del total[index], avg[index], grade[index], rank[index]
        rankcal() #학생이 사라졌으므로 등수 다시 계산
    else:
        print("해당 학번의 학생이 없습니다.")

def search_stu(): #학생 탐색 함수
    tmp = input("찾을 학생의 학번 또는 이름: ")
    found = False
    for i in range(len(num)):
        if str(num[i]) == tmp or name[i] == tmp:
            print(f"학번: {num[i]}, 이름: {name[i]}, 영어: {English[i]}, C: {C[i]}, Python: {py[i]}, 총점: {total[i]}, 평균: {avg[i]:.2f}, 학점: {grade[i]}, 등수: {rank[i]}")
            found = True
    if not found:
        print("해당하는 학생을 찾을 수 없습니다.")

def count_total():
    count = sum(1 for score in avg if score >= 80)
    print(f"평균 점수가 80점 이상인 학생 수: {count}")

def output():
    print("\n성적관리 프로그램")
    print("=========================================================================")
    print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("=========================================================================")
    for i in range(len(num)):
        print(f"{num[i]}\t\t{name[i]}\t{English[i]}\t{C[i]}\t{py[i]}\t"
              f"{total[i]}\t{avg[i]:.2f}\t{grade[i]}\t{rank[i]}")
    print("")

# 초기 5명 데이터 입력
for i in range(5):
    print(f"\n{i + 1}번째 학생 점수 입력")
    insert_stu()
while 1:
    print("\n1. 학생 추가  2. 학생 삭제  3. 출력  4. 80점 이상 학생 수 조회  5. 학생 검색  6. 총점 기준 정렬(오름차순순)  7. 종료")
    choice = int(input("메뉴를 선택하세요: "))
    if choice == 1:
        insert_stu()
    elif choice == 2:
        delete_stu()
    elif choice == 3:
        output()
    elif choice == 4:
        count_total()
    elif choice == 5:
        search_stu()
    elif choice == 6:
        sort_total()
    elif choice == 7:
        break
    else:
        print("다시 선택.")
