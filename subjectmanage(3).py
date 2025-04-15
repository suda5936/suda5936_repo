 ##################

  #프로그램명: 성적관리 프로그램

  #작성자: 소프트웨어학부/2022041036_김현식

  #작성일: 2025/04/15

  #프로그램 설명: 5명의 학생에게 세개의 교과목 정보들을 입력받고 관리하는 프로그램

  ###################
class Student:
    def __init__(self, student_num, name, eng, c, py):
        self.student_num = student_num
        self.name = name
        self.eng = eng
        self.c = c
        self.py = py
        self.total = self.eng + self.c + self.py
        self.avg = self.total / 3
        self.grade = self.calculate_grade()
        self.rank = 0

    def calculate_grade(self):
        if self.avg >= 90:
            return 'A'
        elif self.avg >= 80:
            return 'B'
        elif self.avg >= 70:
            return 'C'
        elif self.avg >= 60:
            return 'D'
        else:
            return 'F'

    def __str__(self):
        return (f"{self.student_num}\t\t{self.name}\t{self.eng}\t{self.c}\t{self.py}\t"
                f"{self.total}\t{self.avg:.2f}\t{self.grade}\t{self.rank}")


class GradeManager:
    def __init__(self):
        self.students = []

    def input_student(self):
        student_num = int(input("학번 : "))
        name = input("이름 : ")
        eng = int(input("영어 점수 : "))
        c = int(input("C 점수 : "))
        py = int(input("Python 점수 : "))
        student = Student(student_num, name, eng, c, py)
        self.students.append(student)
        self.update_ranks()

    def delete_student(self):
        student_num = int(input("삭제할 학생의 학번을 입력하세요: "))
        for student in self.students:
            if student.student_num == student_num:
                self.students.remove(student)
                print("학생 삭제 완료.")
                self.update_ranks()
                return
        print("해당 학번의 학생이 없습니다.")

    def update_ranks(self):
        sorted_students = sorted(self.students, key=lambda s: s.avg, reverse=True)
        for rank, student in enumerate(sorted_students, start=1):
            student.rank = rank

    def search_student(self):
        target = input("찾을 학생의 학번 또는 이름: ")
        found = False
        for student in self.students:
            if str(student.student_num) == target or student.name == target:
                print("\n[검색 결과]")
                print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
                print("=========================================================================")
                print(student)
                found = True
        if not found:
            print("해당하는 학생을 찾을 수 없습니다.")

    def count_high_achievers(self):
        count = sum(1 for student in self.students if student.avg >= 80)
        print(f"평균 점수가 80점 이상인 학생 수: {count}")

    def print_all(self):
        print("\n성적관리 프로그램")
        print("=========================================================================")
        print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
        print("=========================================================================")
        for student in self.students:
            print(student)
        print("")

    def sort_by_total(self):
        self.students.sort(key=lambda s: s.total)
        print("총점 기준 오름차순 정렬 완료.")

# 메인 실행 부분
def main():
    manager = GradeManager()
    
    # 초기 5명 입력
    for i in range(5):
        print(f"\n{i + 1}번째 학생 점수 입력")
        manager.input_student()

    while True:
        print("\n1. 학생 추가  2. 학생 삭제  3. 출력  4. 80점 이상 학생 수 조회  "
              "5. 학생 검색  6. 총점 기준 정렬(오름차순)  7. 종료")
        choice = input("메뉴를 선택하세요: ")

        if choice == '1':
            manager.input_student()
        elif choice == '2':
            manager.delete_student()
        elif choice == '3':
            manager.print_all()
        elif choice == '4':
            manager.count_high_achievers()
        elif choice == '5':
            manager.search_student()
        elif choice == '6':
            manager.sort_by_total()
        elif choice == '7':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴를 선택해주세요.")

if __name__ == "__main__":
    main()

