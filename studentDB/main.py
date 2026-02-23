from fastapi import FastAPI, HTTPException, status
from database import get_connection
from schemas import StudentCreate, StudentResponse

app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"Message": "Welcome to Student API"}

@app.get("/students", response_model= list[StudentResponse], status_code=status.HTTP_200_OK)
def get_students():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM STUDENTS")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

#Parameterized queries are safe because:
# 👉 The SQL query structure is sent separately from the data.
# 👉 The driver treats user input strictly as data, not executable SQL.

@app.post("/students", status_code=status.HTTP_200_OK)
def add_student(student:StudentCreate):
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        query = "INSERT INTO students (NAME, AGE, MOBILE_NO, EMAIL) VALUES ( %s, %s, %s, %s);"
        cursor.execute(query, (student.NAME, student.AGE, student.MOBILE_NO, student.EMAIL))
        connection.commit()
        # student_id = cursor.lastrowid
        # cursor.execute("SELECT * FROM students WHERE ID = %s", (student_id,))
        # result = cursor.fetchone()
        cursor.close()
        connection.close()
        return {"data": "successfully added data"} # result
    except Exception as e:
        raise HTTPException(status_code=500, detail= f"DataBase Error: {str(e)}")
    finally:
        if connection:
            connection.close()
