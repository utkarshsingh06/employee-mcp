import sqlite3

DB_NAME = "employee.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row #This allows us to access columns by name instead of index
    return conn

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    
def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    employees = [
        (1, "Alice", "Engineering", 90000, "alice@company.com"),
        (2, "Bob", "HR", 65000, "bob@company.com"),
        (3, "Charlie", "Finance", 78000, "charlie@company.com"),
        (4, "David", "Engineering", 95000, "david@company.com"),
        (5, "Eva", "Marketing", 70000, "eva@company.com"),
        (6, "Rakesh", "Engineering", 9500, "rakes@company.com"),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO employees
        (id, name, department, salary, email)
        VALUES (?, ?, ?, ?, ?)
    """, employees)
    conn.commit()
    conn.close()
    
def get_all_employees():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, department, salary, email
        FROM employees
    """)

    employees = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return employees

def get_employee_by_id(employee_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
        SELECT id, name, department, salary, email
        FROM employees
        WHERE id=?
        """ ,(employee_id,))      
    
    employee=cursor.fetchone()
    conn.close()
    if employee is None:
        return None

    return dict(employee)

def get_employees_by_department(department):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
        SELECT id, name, department, salary, email
        FROM employees
        WHERE department=?
        """ ,(department,))
    
    employees = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return employees

def add_employees(name, department, salary, email):

    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
        INSERT INTO employees (name, department, salary, email)
        Values(?,?,?,?)
        """,(name,department,salary,email))
    conn.commit()
    conn.close()
    return "Employee added successfully."

def update_employees_salary(salary,employee_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
        UPDATE employees
        SET salary=?
        WHERE id=?
        """,(salary,employee_id))
    
    conn.commit()
    conn.close()
    return "Employee updated successfully."

def delete_employees_by_id(employee_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
        DELETE FROM employees
        WHERE id=?
        """,(employee_id,))
    
    conn.commit()
    conn.close()
    return "Employee deleted successfully janab."
    
