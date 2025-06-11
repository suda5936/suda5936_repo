##################
# 프로그램명: 성적관리 프로그램 (MySQL 연동)
# 작성자: 소프트웨어학부/2022041036_김현식
# 작성일: 2025/06/12
# 프로그램 설명: MySQL을 사용하여 n명의 학생에게 세개의 교과목 정보들을 입력받고 관리하는 프로그램
##################

import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.cursor = None
        
    def connect_database(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='grade_management',
                user='root',  # MySQL 사용자명
                password='password'  # MySQL 비밀번호
            )
            
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("MySQL 데이터베이스 연결 성공")
                self.create_table()
                return True
                
        except Error as e:
            print(f"데이터베이스 연결 오류: {e}")
            return False
    
    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            student_num INT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            eng INT NOT NULL,
            c INT NOT NULL,
            py INT NOT NULL,
            total INT NOT NULL,
            avg DECIMAL(5,2) NOT NULL,
            grade CHAR(1) NOT NULL,
            rank_num INT DEFAULT 0
        )
        """
        try:
            self.cursor.execute(create_table_query)
            self.connection.commit()
        except Error as e:
            print(f"테이블 생성 오류: {e}")
    
    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL 연결이 종료되었습니다.")

class Student:
    def __init__(self, student_num, name, eng, c, py):
        self.student_num = student_num
        self.name = name
        self.eng = eng
        self.c = c
        self.py = py
        self.total = self.calculate_total()
        self.avg = self.calculate_average()
        self.grade = self.calculate_grade()
        self.rank = 0

    def calculate_total(self):
        """총점 계산 함수"""
        return self.eng + self.c + self.py

    def calculate_average(self):
        """평균 계산 함수"""
        return self.total / 3

    def calculate_grade(self):
        """학점 계산 함수"""
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
        self.db = DatabaseManager()
        if not self.db.connect_database():
            print("데이터베이스 연결에 실패했습니다.")
            exit()

    def input_student(self):#입력함수
        try:
            student_num = int(input("학번 : "))
            
            # 중복 학번 체크
            if self.check_duplicate_student(student_num):
                print("이미 존재하는 학번입니다.")
                return
                
            name = input("이름 : ")
            eng = int(input("영어 점수 : "))
            c = int(input("C 점수 : "))
            py = int(input("Python 점수 : "))
            
            student = Student(student_num, name, eng, c, py)
            self.insert_student(student)
            self.calculate_ranks()
            print("학생 정보가 추가되었습니다.")
            
        except ValueError:
            print("올바른 숫자를 입력해주세요.")
        except Error as e:
            print(f"학생 추가 오류: {e}")

    def insert_student(self, student):#삽입 함수
        insert_query = """
        INSERT INTO students (student_num, name, eng, c, py, total, avg, grade, rank_num)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (student.student_num, student.name, student.eng, student.c, 
                 student.py, student.total, student.avg, student.grade, student.rank)
        
        self.db.cursor.execute(insert_query, values)
        self.db.connection.commit()

    def delete_student(self):#삭제 함수
        try:
            student_num = int(input("삭제할 학생의 학번을 입력하세요: "))
            
            delete_query = "DELETE FROM students WHERE student_num = %s"
            self.db.cursor.execute(delete_query, (student_num,))
            
            if self.db.cursor.rowcount > 0:
                self.db.connection.commit()
                print("학생 삭제 완료.")
                self.calculate_ranks()
            else:
                print("해당 학번의 학생이 없습니다.")
                
        except ValueError:
            print("올바른 학번을 입력해주세요.")
        except Error as e:
            print(f"학생 삭제 오류: {e}")

    def calculate_ranks(self):#등수계산
        try:
            rank_query = """
            UPDATE students s1
            INNER JOIN (
                SELECT student_num, 
                    RANK() OVER (ORDER BY avg DESC) as new_rank
                FROM students
            ) s2 ON s1.student_num = s2.student_num
            SET s1.rank_num = s2.new_rank
            """
            self.db.cursor.execute(rank_query)
            self.db.connection.commit()
        
        except Error as e:
            print(f"등수 계산 오류: {e}")

    def search_student(self):#탐색
        target = input("찾을 학생의 학번 또는 이름: ")
        
        try:
            # 학번으로 검색 시도
            if target.isdigit():
                search_query = "SELECT * FROM students WHERE student_num = %s"
                self.db.cursor.execute(search_query, (int(target),))
            else:
                # 이름으로 검색
                search_query = "SELECT * FROM students WHERE name = %s"
                self.db.cursor.execute(search_query, (target,))
            
            result = self.db.cursor.fetchone()
            
            if result:
                print("\n[검색 결과]")
                print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
                print("=========================================================================")
                print(f"{result[0]}\t{result[1]}\t{result[2]}\t{result[3]}\t{result[4]}\t"
                      f"{result[5]}\t{result[6]:.2f}\t{result[7]}\t{result[8]}")
            else:
                print("해당하는 학생을 찾을 수 없습니다.")
                
        except Error as e:
            print(f"학생 검색 오류: {e}")

    def count_high_achievers(self):#80점 이상 카운트
        try:
            count_query = "SELECT COUNT(*) FROM students WHERE avg >= 80"
            self.db.cursor.execute(count_query)
            count = self.db.cursor.fetchone()[0]
            print(f"평균 점수가 80점 이상인 학생 수: {count}")
            
        except Error as e:
            print(f"학생 수 조회 오류: {e}")

    def print_all(self):#전체 출력
        try:
            select_query = "SELECT * FROM students ORDER BY rank_num"
            self.db.cursor.execute(select_query)
            results = self.db.cursor.fetchall()
            
            print("\n성적관리 프로그램")
            print("=========================================================================")
            print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
            print("=========================================================================")
            
            for row in results:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t"
                      f"{row[5]}\t{row[6]:.2f}\t{row[7]}\t{row[8]}")
            print("")
            
        except Error as e:
            print(f"출력 오류: {e}")

    def sort_by_total(self):#성적순 정렬
        try:
            select_query = "SELECT * FROM students ORDER BY total ASC"
            self.db.cursor.execute(select_query)
            results = self.db.cursor.fetchall()
            
            print("\n총점 기준 오름차순 정렬 결과:")
            print("=========================================================================")
            print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
            print("=========================================================================")
            
            for row in results:
                print(f"{row[0]}\t\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t"
                      f"{row[5]}\t{row[6]:.2f}\t{row[7]}\t{row[8]}")
            print("총점 기준 오름차순 정렬 완료.")
            
        except Error as e:
            print(f"정렬 오류: {e}")

    def check_duplicate_student(self, student_num):#중복체크함수
        try:
            check_query = "SELECT COUNT(*) FROM students WHERE student_num = %s"
            self.db.cursor.execute(check_query, (student_num,))
            count = self.db.cursor.fetchone()[0]
            return count > 0
        except Error as e:
            print(f"중복 체크 오류: {e}")
            return False

    def close(self):
        """데이터베이스 연결 종료"""
        self.db.close_connection()

def main():
    manager = GradeManager()
    
    try:
        print("초기 학생 데이터를 입력하시겠습니까? (y/n): ", end="")
        if input().lower() == 'y':
            num_students = int(input("입력할 학생 수: "))
            for i in range(num_students):
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
                
    except KeyboardInterrupt:
        print("\n프로그램이 중단되었습니다.")
    finally:
        manager.close()

if __name__ == "__main__":
    main()
