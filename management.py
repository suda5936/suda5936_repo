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
    num = int(input('학번 : '))
    name = input('이름 : ')
    English = int(input('영어 점수 : '))
    C = int(input('C 점수 : '))
    py = int(input('Python 점수 : '))
    return num, name, English, C, py

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
    for score in avg:
        rank.append(sorted_avg.index(score) + 1)  

def output():
    print("\n성적관리 프로그램")
    print("=========================================================================")
    print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("=========================================================================")
    for i in range(5):
        print(f"{num[i]}\t\t{name[i]}\t{English[i]}\t{C[i]}\t{py[i]}\t"
              f"{total[i]}\t{avg[i]:.2f}\t{grade[i]}\t{rank[i]}")
    print("")

for i in range(5):
    print(f"\n{i + 1}번째 학생 점수 입력")
    student_num, student_name, eng_score, c_score, py_score = inputscore()
    
    num.append(student_num)
    name.append(student_name)
    English.append(eng_score)
    C.append(c_score)
    py.append(py_score)
    
    total_avg(eng_score, c_score, py_score)
    gradecal(avg[-1])  

rankcal()
output()
