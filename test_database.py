from database import ( #test_database.py  
    initialize_database,
    seed_data,
    get_all_employees,
    search_employees
)

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

employees = search_employees("Engineering")

for employee in employees:
    print(employee)
