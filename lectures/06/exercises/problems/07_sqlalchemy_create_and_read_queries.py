"""Problem 07: Create and read data with SQLAlchemy.

Task:
1. Open a SQLAlchemy Session on `school.db`.
2. Create one Assignment for an existing student.
3. Read all students.
4. Read students with age >= 22 sorted by age descending.
5. Read assignments with joined student names.

Starter:
- Reuse `Student` and `Assignment` from `db_models.py`.
- Use `select(...)` queries.
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from db_models import Assignment, Student

DB_URL = "sqlite:///school.db"


def main() -> None:
    engine = create_engine(DB_URL, echo=False)

    with Session(engine) as session:
        student = session.execute(select(Student)).scalars().first()
        if student:
            new_assignment = Assignment(
                title="Math Homework",
                grade=95,
                student_id=student.id
            )
            session.add(new_assignment)
            print(f"Added assignment for student: {student.name}")

        all_students = session.execute(select(Student)).scalars().all()
        print("\nAll students:")
        for s in all_students:
            print(f"{s.id} - {s.name}, age {s.age}")

        filtered_students = session.execute(
            select(Student).where(Student.age >= 22).order_by(desc(Student.age))
        ).scalars().all()
        print("\nStudents aged 22 or older, sorted by age descending:")
        for s in filtered_students:
            print(f"{s.name} - {s.age}")

        # TODO 4: read assignments with student data
        assignments = session.execute(
            select(Assignment).options(joinedload(Assignment.student))
        ).scalars().all()
        print("\nAssignments with student names:")
        for a in assignments:
            print(f"{a.title} - {a.grade} (Student: {a.student.name})")
        session.commit()


if __name__ == "__main__":
    main()
