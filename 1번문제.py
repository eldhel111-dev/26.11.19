import psycopg 
from psycopg.rows import dict_row 

DSN = "host=localhost port=5432 dbname=sportscenter user=postgres password=admin1234"

MEMBER_ID = """
SELECT member_id, name
FROM members
ORDER BY member_id
"""

name = input(f"회원 이름")

def member_name(conn):
    for m in conn.execute(MEMBER_ID):
        if name == m['name'] :
            print(f"{m['member_id']}")

        else : print(f"없는 회원입니다")
        return 0


def main():
    with psycopg.connect(DSN, row_factory=dict_row) as conn: 
        member_name(conn)







if __name__ == "__main__":
    main()
