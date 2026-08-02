from mcp.server.fastmcp import FastMCP  # Import fast MCP class from python SDK

from database import (add_employees, delete_employees_by_id, get_all_employees,
                      get_employee_by_id, get_employees_by_department,
                      initialize_database, seed_data, update_employees_salary)

mcp = FastMCP("Employee Server") #create a server


@mcp.tool() #registering a tool
def hello() -> str: #definging the tool function with return type as string
    """
    Returns a welcome message.
    """
    return "Hello from Employee MCP Server Utkarsh!"

@mcp.tool()
def list_employees():
    """
    Returns all employees.
    """
    print(">>> List employees tool was called!")
    return get_all_employees()

@mcp.tool()
def get_employee(employee_id: int):
    """
    Returns an employee by ID.
    """
    return get_employee_by_id(employee_id)

@mcp.tool()
def search_employees_by_department(department: str):
    """
    Returns employees by department.
    """
    return get_employees_by_department(department)
@mcp.tool()
def add_employee(name: str, department: str, salary: float, email: str):
    print(f">>> add_employee called: {name}, {department}, {salary}, {email}")
    """
    Adds a new employee to the database.
    """
    return add_employees(name, department, salary, email)

@mcp.tool()
def update_employee_salary(salary: float, employee_id: int):
    """
    Updates an employee's salary by ID.
    """
    return update_employees_salary(salary, employee_id)

@mcp.tool()
def delete_employee(employee_id: int):
    """
    Deletes an employee by ID.
    """
    return delete_employees_by_id(employee_id)
    

if __name__ == "__main__":
    print(">>> Server starting...")
    initialize_database()#initialize the database when the server starts
    seed_data()
    mcp.run() #start the server