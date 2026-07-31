from server import list_employees,search_employees #test the logic of the list_employees tool


employees = search_employees("Engineering")

for employee in employees:
    print(employee)