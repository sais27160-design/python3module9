"""Problem 05: Basic aggregates and GROUP BY.

Task:
1. Count all students
2. Compute average age
3. Compute min and max age
4. Count students per track (GROUP BY track)

Print each result.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM students")
    total = cur.fetchone()[0]
    print("Total students:", total)

    cur.execute("SELECT AVG(age) FROM students")
    avg_age = cur.fetchone()[0]
    print("Average age:", round(avg_age, 2))

    cur.execute("SELECT MIN(age), MAX(age) FROM students")
    min_age, max_age = cur.fetchone()
    print("Min age:", min_age)
    print("Max age:", max_age)

    cur.execute("SELECT track, COUNT(*) FROM students GROUP BY track")
    track_counts = cur.fetchall()
    
    print("\nStudents per track:")
    for track, count in track_counts:
        print(f"{track}: {count}")

    conn.close()


if __name__ == "__main__":
    main()
