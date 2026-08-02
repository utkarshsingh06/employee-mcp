from database import (add_employees, delete_employees_by_id, get_all_employees,
                      get_employee_by_id, get_employees_by_department,
                      initialize_database, seed_data, update_employees_salary)

initialize_database()
seed_data()

# employees = get_all_employees()

# print("Employees in Database:")
# print("-" * 50)

# for employee in employees:
#     print(employee)

# from database import get_employee_by_id

# print(get_employee_by_id(4))



# from database import search_employees

# print(add_employees("Rajvansh", "Engineering", 75000, "rajvansh@company.com"))
# # for employee in employees:
# #     print(employee)
# add_employees('John Doe', 'Engineering', 75000, 'john.doe@company.com')
# print(get_all_employees())


delete_employees_by_id(5)
print(get_all_employees())