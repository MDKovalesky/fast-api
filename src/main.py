from fastapi import FastAPI


app = FastAPI()

students = [
    {'name': 'student1', 'age': 16},
    {'name': 'student2', 'age': 17},
    {'name': 'student3', 'age': 15}
]

@app.get('/students')
def user_list():
    return {'students': students}