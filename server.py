from mcp.server.fastmcp import FastMCP #Import fast MCP class from python SDK
from database import (
    initialize_database,
    seed_data,
    get_all_employees,
    get_employee_by_id,
    get_employees_by_department
)
mcp = FastMCP("Employee Server") #create a server


@mcp.tool() #registering a tool
def hello() -> str: #definging the tool function with return type as string
    """
    Returns a welcome message.
    """
    return "Hello from Employee MCP Server!"

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
    return get_employees_by_departments(department)
    

if __name__ == "__main__":
    print(">>> Server starting...")
    initialize_database()#initialize the database when the server starts
    seed_data()
    mcp.run() #start the server