from mcp.server.fastmcp import FastMCP #Import fast MCP class from python SDK
from database import (
    initialize_database,
    seed_data,
    get_all_employees,
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
    return get_all_employees()
    

if __name__ == "__main__":
    initialize_database()#initialize the database when the server starts
    seed_data()
    mcp.run() #start the server