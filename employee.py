class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount

if __name__ == "__main__":
    emp = Employee("john", "doe", 50000)
    emp.give_raise()
    print(f"{emp.first_name} {emp.last_name} now has a salary of {emp.salary}")
