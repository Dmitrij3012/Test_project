class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

# Расширьте класс Employee, создав классы FullTimeEmployee и PartTimeEmployee.


class FullTimeEmployee(Employee):

    def get_unpaid_vacation(self, start_date, number_days):
        return f'Начало неоплачиваемого отпуска: {start_date}, '
        'продолжительность: {number_days} дней.'


class PartTimeEmployee(Employee):
    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        self.remaining_vacation_days = PartTimeEmployee.vacation_days
    # В подсказках был пункт: Чтобы вызвать инициализатор
    # родительского класса в дочернем классе,
    # используйте super().__init__(...).
    # Он не нужен.


# Пример использования:
full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
print(part_time_employee.get_vacation_details())
