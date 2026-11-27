"""Тесты CRUD для сущностей учебного проекта."""
from models import Student, Subject, Teacher


def test_add_student(session):
    """Добавление новой записи в students."""
    name = "Test Student Add"
    student = Student(name=name)
    session.add(student)
    try:
        session.commit()
        found = session.query(Student).filter_by(name=name).first()
        assert found is not None
        assert found.name == name
    finally:
        session.query(Student).filter_by(name=name).delete(
            synchronize_session=False
        )
        session.commit()


def test_update_subject(session):
    """Изменение существующей записи в subjects."""
    old_name = "Test Subject Old"
    new_name = "Test Subject Updated"

    subject = Subject(name=old_name)
    session.add(subject)
    session.commit()
    subject_id = subject.id

    try:
        subject.name = new_name
        session.commit()

        updated = (
            session.query(Subject).filter_by(id=subject_id).first()
        )
        assert updated is not None
        assert updated.name == new_name
    finally:
        session.query(Subject).filter_by(id=subject_id).delete(
            synchronize_session=False
        )
        session.commit()


def test_delete_teacher(session):
    """Удаление записи из teachers."""
    name = "Test Teacher Delete"
    teacher = Teacher(name=name)
    session.add(teacher)
    session.commit()
    teacher_id = teacher.id

    try:
        session.delete(teacher)
        session.commit()

        found = (
            session.query(Teacher).filter_by(id=teacher_id).first()
        )
        assert found is None
    finally:
        # На случай падения теста — дочищаем запись.
        session.query(Teacher).filter_by(id=teacher_id).delete(
            synchronize_session=False
        )
        session.commit()
        