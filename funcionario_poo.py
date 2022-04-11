# - Uma classe abstrata deve herdar de ABC (Abstract Base Classes) ok
#
# - Analise o problema do empregado e o cálculo do seu salário. ok
#
# - A superclasse Employee representa um funcionário em tempo integral ou por hora. ok
# A classe Employee deve ser uma classe abstrata porque existem apenas funcionários ok
# em tempo integral e funcionários horistas, não existem empregados gerais. ok
# A classe Employee deve ter um método concreto que retorne o nome completo de ok
# um funcionário. Além disso, deve ter um método que calcule o salário. O método ok
# cálcula salário deve ser um método abstrato. ok
#
# Implemente:
# 1- A classe Employee com os atributos first_name e Last_name ok
# - O Construtor e os métodos gets e sets ok
# - O método concreto full_name ok
# - O métod abstrato compute_salary ok
# 5- Um objeto da classe Employee ok
# - A classe FulltimeEmployee com os atributos first_name, Last_name e salary ok
# - O Construtor e os métodos gets e sets ok
# - A RN (Regra de Negócio) do salário é o salário fixo mais um bônus de 200 reais ok
# - Um objeto da classe FulltimeEmployee ok

# - A classe HourlyEmployee com os atributos first_name, Last_name, worked_hours, rate ok
# - O Construtor e os métodos gets e sets ok
# - A RN (Regra de Negócio) do salário é worked_hours vezes rate ok
# - Um objeto da classe HourlyEmployee ok

# - A classe Payroll com o atributo employee_list ok
# - O construtor não recebe nada e o método get_employee_list ok
# - O método add para adicionar um empregado a lista

# - Adicione os obejtos criados (os empregados) a lista de Payroll
# - O método print_payroll que mostra a folha de pagamento com o nome completo e
# o salário do funcionário.

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @abstractmethod
    def compute_salary(self):
        ...


class FulltimeEmployee(Employee):

    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary

    def compute_salary(self):
        return self.salary + 200


class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, value):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.value = value

    def get_worked_hours(self):
        return self.worked_hours

    def set_worked_hours(self, new_worked_hours):
        self.worked_hours = new_worked_hours

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def compute_salary(self):
        return self.worked_hours * self.value


class Payroll:
    def __init__(self):
        self.employee_list = []

    def add(self, employee):
        self.employee_list.append(employee)

    def print_payroll(self):
        print('------------------------------------\n    *** FOLHA DE PAGAMENTO ***\n')
        for e in self.employee_list:
            print(f'{e.full_name()}            \t ${e.compute_salary()}')


if __name__ == '__main__':
    # employee1 = Employee('Bla', 'Bla Bla')
    # TypeError: Can't instantiate abstract class Employee with abstract method comput_salary
    # print(employee1)

    employee2 = FulltimeEmployee('Fulano', 'de Tal', 2000)
    print(f'\n    *** EMPREGADOS CADASTRADOS ***\n\n- EMPREGADO 2\nNOME COMPLETO: {employee2.full_name()}'
          f'\nCÁLCULO SALÁRIO: R$ {employee2.compute_salary()}')

    employee3 = HourlyEmployee('Ciclano', 'Sauro', 160, 30)
    print(f'\n- EMPREGADO 3\nNOME COMPLETO: {employee3.full_name()}'
          f'\nCÁLCULO SALÁRIO: R$ {employee3.compute_salary()}\n')

    payroll = Payroll()
    payroll.add(employee2)
    payroll.add(employee3)

    payroll.print_payroll()
