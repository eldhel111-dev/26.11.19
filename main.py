import psycopg # psycopg : 모듈
from psycopg.rows import dict_row # rows : 모듈의 행들 dict_row 딕셔너리

# DSN : Data Source Name
DSN = "host=localhost port=5432 dbname=sportscenter user=postgres password=admin1234"

MONTH = "2026-11"

LIST_SQL = """
SELECT DISTINCT c.course_id, s.sport_name, c.course_name, c.class_days, c.fee
FROM courses c
JOIN sports s ON c.sport_id = s.sport_id 
LEFT JOIN enrollments e ON C.course_id = e.course_id
                        AND e.enroll_month = %s 
ORDER BY c.course_id;
"""
# %s 가 뭐죠?

# 수강 신청 가능 목록 조회
def list_courses(conn):
    for c in conn.execute(LIST_SQL, (MONTH,)):
        print(f"{c['course_id']:>3} | {c['sport_name']} | {c['course_name']} | {c['class_days']} | {c['fee']}원")

# TODO: 입력 로직

MEMBER_ID = 10
COURSE_ID = 1





# 수강 신청
def enroll(conn, member_id, course_id):
    # TODO: 신청한 강좌의 수강료 추출
    fee = 0
    conn.execute(
        "INSERT INTO enrollments (member_id, course_id, enroll_month, status, pay_amount)"
        "VALUES (%s, %s, %s, '수강중', %s)",
        (member_id, course_id, MONTH, fee)
    )
    print("수강신청 완료 되었습니다.")
 

def main():
    with psycopg.connect(DSN, row_factory=dict_row) as conn: # row_factory 란?
        # # 수강 목록
        # list_courses(conn)

        # 수강 신청
        enroll(conn, MEMBER_ID, COURSE_ID)
        # row = conn.execute("SELECT current_database(), current_user").fetchone()
        # print("연결 성공:", row)
        # rows = conn.execute("SELECT course_id, course_name, fee FROM courses LIMIT 5").fetchall()
        # # print(rows)
        # for row in rows:
        #     print(row["course_name"], row["fee"])
if __name__ == "__main__":

    main()

# 03 데이터베이스 일일 과제 

# 1. 회원이름으로 회원ID 추출
# 회원 이름을 입력받아서 회원 ID 를 추출해서 MEMBER_ID에 저장하세요.
# 회원 ID를 추출하는 기능은 함수로 작성하세요.


# 2. 신청한 강좌의 수강료 추출
# 신청한 강좌의 수강료를 추출해서 fee 변수에 할당(연결)해주세요.
# 중복신청은 불가능하게 먼저 확인하세요. (도전 과제)


# 3. 강좌 검색 기능
# 강좌명을 입력받아 비슷한 강좌를 검색하는 기능을 구현하세요.
# 와일드카드를 활용하셔야 합니다.