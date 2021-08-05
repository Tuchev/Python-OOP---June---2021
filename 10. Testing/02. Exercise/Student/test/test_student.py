from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Test")

    def test_init(self):
        self.assertEqual("Test", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_init_with_course(self):
        student = Student("Test", {"python": ["note1"]})

        self.assertEqual("Test", self.student.name)
        self.assertEqual({"python": ["note1"]}, student.courses)

    def test_init_with_none_course(self):
        student = Student("Test", None)

        self.assertEqual("Test", self.student.name)
        self.assertEqual({}, student.courses)

    def test_enroll_duplicate_course(self):
        self.student.courses = {"python": ["note1"]}
        result = self.student.enroll("python", ["note2"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"python": ["note1", "note2"]}, self.student.courses)

    def test_enroll_new_course_with_notes(self):
        result = self.student.enroll("python", ["note1"])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"python": ["note1"]}, self.student.courses)

    def test_enroll_new_course_without_adding_notes(self):
        result = self.student.enroll("python", ["note1"], "no")
        self.assertEqual("Course has been added.", result)
        self.assertEqual({"python": []}, self.student.courses)

    def test_enroll_new_course_with_adding_notes(self):
        result = self.student.enroll("python", ["note1", "note2"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"python": ["note1", "note2"]}, self.student.courses)

    def test_enroll_in_existing_course_with_adding_notes(self):
        self.student.enroll("python", ["note1", "note2"], "Y")
        result = self.student.enroll("python", ["note3"], "Y")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"python": ["note1", "note2", "note3"]}, self.student.courses)

    def test_add_notes(self):
        self.student.courses = {"python": []}
        result = self.student.add_notes("python", "note1")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual({"python": ["note1"]}, self.student.courses)

    def test_add_notes_with_not_existing_courses_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Java", "note1")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual({}, self.student.courses)

    def test_leave_course(self):
        self.student.courses = {"python": []}
        result = self.student.leave_course("python")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)

    def test_leave_course_with_not_existing_courses_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Java")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertEqual({}, self.student.courses)


if __name__ == '__main__':
    main()
