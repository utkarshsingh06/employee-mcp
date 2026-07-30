from database import ( #test_database.py  
    initialize_database,
    seed_data,
    get_all_employees
)

initialize_database()
seed_data()

employees = get_all_employees()

print("Employees in Database:")
print("-" * 50)

for employee in employees:
    print(employee)
    