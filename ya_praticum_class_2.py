class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        # Сюда добавьте новый атрибут remaining_vacation_days
        self.remaining_vacation_days = Employee.vacation_days
    # Сюда добавьте методы consume_vacation и get_vacation_details.

    def consume_vacation(self, wasted_days):
        self.remaining_vacation_days -= wasted_days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'
# Пример использования класса:
# employee = Employee('Роберт', 'Крузо', 'м')


employee = Employee(first_name='Роберт', second_name='Крузо', gender='м')
# employee.consume_vacation(7)

employee.consume_vacation(7)
# print(employee.get_vacation_details())

print(employee.get_vacation_details())
