import psycopg # psycopg : 모듈
from psycopg.rows import dict_row # rows : 모듈의 행들 dict_row 딕셔너리

# DSN : Data Source Name
DSN = "host=localhost port=5432 dbname=sportscenter user=postgres password=admin1234"

COURSE_NAME = "수영"

SPORT_NAME = """
SELECT c.course_name, s.sport_name
FROM courses c
LEFT JOIN sports s ON s.sport_id = c.sport_id 
ORDER BY sport_name
"""

name = input(f"수영,헬스,골프연습,스포츠댄스 중 입력하세요")

def name_search(conn):
    for n in conn.execute(SPORT_NAME):
        if name == "수영":
            print(f"{n['course_name']}")

        if name == "헬스":
            print(f"{n['c.course_name']}")

        if name == "골프연습":
            print(f"{n['c.course_name']}")

        if name == "스포츠댄스":
            print(f"{n['c.course_name']}")

        else : print(f"수영,헬스,골프연습,스포츠댄스 중 입력하세요")
        return 0


def main():
    with psycopg.connect(DSN, row_factory=dict_row) as conn: 
        name_search(conn)

## 와일드 카드를 활용 못하겠음