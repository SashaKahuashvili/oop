class Student:
    def __init__(self, name: str, age: int, groupnumber: str):
        self.name = name
        self.age = age
        self.groupnumber = groupnumber

    def go_to_the_class(self):
        if self.groupnumber == "12345":
            print(f"I am here! {self.name=}")
        elif self.groupnumber == "54321":
            print(f"CANCEL")

    @classmethod
    def test_method(cls):
        print("Call test method")


student_1 = Student("Ivan", 20, "12345")
student_2 = Student("Masha", 25, "54321")

student_1.go_to_the_class()
student_2.go_to_the_class()

student_2.test_method()

Student.test_method()