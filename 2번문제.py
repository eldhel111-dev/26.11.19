# 2. 신청한 강좌의 수강료 추출
# 신청한 강좌의 수강료를 추출해서 fee 변수에 할당(연결)해주세요.
# 중복신청은 불가능하게 먼저 확인하세요. (도전 과제)


import psycopg # psycopg : 모듈
from psycopg.rows import dict_row # rows : 모듈의 행들 dict_row 딕셔너리

# DSN : Data Source Name
DSN = "host=localhost port=5432 dbname=sportscenter user=postgres password=admin1234"

PAY_AMOUNT = """
SELECT DISTINCT c.course_name, c.fee, e.pay_amount
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id 
ORDER BY fee
"""



def total_pay(conn):
    for c in conn.execute(PAY_AMOUNT):
        print(f"{c['course_name']}, {c['pay_amount']} {c['fee']}")



def main():
    with psycopg.connect(DSN, row_factory=dict_row) as conn: 
        total_pay(conn)







if __name__ == "__main__":
    main()

