# create a class employee with attributes emp_id, name, salary and also
#! define method to access the properties of employee


class Employee:
    def __init__(self, emp_id=None, name=None, salary=None):
        self.__id = emp_id
        self.__name = name
        self.__salary = salary

    def setEmpId(self, emp_id):
        self.__id = emp_id

    def setEmpName(self, name):
        self.__name = name

    def setSalary(self, salary):
        self.__salary = salary

    def getEmpId(self):
        return self.__id

    def getEmpName(self):
        return self.__name

    def getSalary(self):
        return self.__salary


if __name__ == "__main__":
    emp1 = Employee()
    emp2 = Employee()
    emp3 = Employee()

    emp1.setEmpId("2023-IT-169")
    emp1.setEmpName("Imran")
    emp1.setSalary(58000)

    emp2.setEmpId("2023-BA-956")
    emp2.setEmpName("Fazil")
    emp2.setSalary(78000)

    emp3.setEmpId("2023-CS-989")
    emp3.setEmpName("Jhon")
    emp3.setSalary(98000)

    print(
        f"Employee Id: {emp1.getEmpId()}\nEmployee Name: {emp1.getEmpName()}\nSalary: {emp1.getSalary()}\n")
    print(
        f"Employee Id: {emp2.getEmpId()}\nEmployee Name: {emp2.getEmpName()}\nSalary: {emp2.getSalary()}\n")
    print(
        f"Employee Id: {emp3.getEmpId()}\nEmployee Name: {emp3.getEmpName()}\nSalary: {emp3.getSalary()}\n")
