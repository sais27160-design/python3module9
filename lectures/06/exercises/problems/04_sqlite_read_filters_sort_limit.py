"""Problem 04: Practice WHERE, ORDER BY, LIMIT.

Task:
1. Get students with age >= 22
2. Sort students by age DESC
3. Return only top 3 oldest students
4. Get backend students younger than 23

Use parameterized queries for filter values.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT * FROM students WHERE age >= ?", (22,))
    oldest= cur.fetchall()
    print("Students age >= 22")
    for row in oldest:
        print(row)
    
    cur.execute("SELECT * FROM students ORDER BY age DESC LIMIT 3")
    top = cur.fetchall()
    print("Top 3 oldest students")
    for row in top:
        print(row)
    

    cur.execute(
            "SELECT * FROM students WHERE track = ? AND age < ?",
            ("backend", 23)
        )
    backend_young = cur.fetchall()
    print("Backend students age < 23")
    for row in backend_young:
        print(row)

    conn.close()


if __name__ == "__main__":
    main()
