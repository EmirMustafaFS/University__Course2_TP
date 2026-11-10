import json

from fastapi import FastAPI
from pydantic import BaseModel

with open("DTB.json", encoding="utf-8") as file:
    data = json.load(file)

y = data["tasks"]
x = data["x"]

with open("tables.json", encoding="utf-8") as file:
    tables = json.load(file)

students = tables["Студент"]
teachers = tables["Преподаватель"]
courses = tables["Курс"]
schedules = tables["Расписание"]
records = tables["Запись"]

app = FastAPI()

@app.get("/tasks")
async def get_tasks():
    return y

class Task(BaseModel):
    task_name: str
    task_id: int 


@app.post("/tasks")
async def create_task(task: Task):
    task_id = task.task_id
    task_id = len(y) + 1
    new_task = {
        "name": task.task_name,
        "id": task_id
    }
    if new_task["id"] not in x:
        y.append(new_task)
    return new_task

@app.put("/tasks")
async def update_item(task: Task, id: int):
    for i in y:
        if i["id"] == id:
            i["name"] = task.task_name
            return i
    return "task not found: " + str(id)

@app.delete("/tasks")
def delete_item(id: int):
    for i in y:
        if i["id"] == id:
            x.append(i["id"])
            y.remove(i)
    return "success deleted id: " + str(id)

@app.get("/x")
async def show_deleted_tasks():
    return x


class Student(BaseModel):
    FullName: str
    Возраст: int


@app.get("/Студент")
async def get_students():
    return students


@app.post("/Студент")
async def create_student(student: Student):
    new_student = {
        "ID_Студент": len(students) + 1,
        "FullName": student.FullName,
        "Возраст": student.Возраст
    }
    students.append(new_student)
    return new_student


@app.put("/Студент")
async def update_student(student: Student, id: int):
    for i in students:
        if i["ID_Студент"] == id:
            i["FullName"] = student.FullName
            i["Возраст"] = student.Возраст
            return i
    return "student not found: " + str(id)


@app.delete("/Студент")
def delete_student(id: int):
    for i in students:
        if i["ID_Студент"] == id:
            students.remove(i)
            return "success deleted id: " + str(id)
    return "student not found: " + str(id)


class Teacher(BaseModel):
    FullName: str
    Возраст: int


@app.get("/Преподаватель")
async def get_teachers():
    return teachers


@app.post("/Преподаватель")
async def create_teacher(teacher: Teacher):
    new_teacher = {
        "ID_Преподаватель": len(teachers) + 1,
        "FullName": teacher.FullName,
        "Возраст": teacher.Возраст
    }
    teachers.append(new_teacher)
    return new_teacher


@app.put("/Преподаватель")
async def update_teacher(teacher: Teacher, id: int):
    for i in teachers:
        if i["ID_Преподаватель"] == id:
            i["FullName"] = teacher.FullName
            i["Возраст"] = teacher.Возраст
            return i
    return "teacher not found: " + str(id)


@app.delete("/Преподаватель")
def delete_teacher(id: int):
    for i in teachers:
        if i["ID_Преподаватель"] == id:
            teachers.remove(i)
            return "success deleted id: " + str(id)
    return "teacher not found: " + str(id)


class Course(BaseModel):
    ID_Day: int
    ID_Преподаватель: int
    Специальность: str


@app.get("/Курс")
async def get_courses():
    return courses


@app.post("/Курс")
async def create_course(course: Course):
    new_course = {
        "ID_Курс": len(courses) + 1,
        "ID_Day": course.ID_Day,
        "ID_Преподаватель": course.ID_Преподаватель,
        "Специальность": course.Специальность
    }
    courses.append(new_course)
    return new_course


@app.put("/Курс")
async def update_course(course: Course, id: int):
    for i in courses:
        if i["ID_Курс"] == id:
            i["ID_Day"] = course.ID_Day
            i["ID_Преподаватель"] = course.ID_Преподаватель
            i["Специальность"] = course.Специальность
            return i
    return "course not found: " + str(id)


@app.delete("/Курс")
def delete_course(id: int):
    for i in courses:
        if i["ID_Курс"] == id:
            courses.remove(i)
            return "success deleted id: " + str(id)
    return "course not found: " + str(id)


class Schedule(BaseModel):
    ID_Запись: int
    ID_Студент: int
    Monday: str
    Tuesday: str
    Wednesday: str
    Thursday: str
    Friday: str


@app.get("/Расписание")
async def get_schedules():
    return schedules


@app.post("/Расписание")
async def create_schedule(schedule: Schedule):
    new_schedule = {
        "ID_Day": len(schedules) + 1,
        "ID_Запись": schedule.ID_Запись,
        "ID_Студент": schedule.ID_Студент,
        "Monday": schedule.Monday,
        "Tuesday": schedule.Tuesday,
        "Wednesday": schedule.Wednesday,
        "Thursday": schedule.Thursday,
        "Friday": schedule.Friday
    }
    schedules.append(new_schedule)
    return new_schedule


@app.put("/Расписание")
async def update_schedule(schedule: Schedule, id: int):
    for i in schedules:
        if i["ID_Day"] == id:
            i["ID_Запись"] = schedule.ID_Запись
            i["ID_Студент"] = schedule.ID_Студент
            i["Monday"] = schedule.Monday
            i["Tuesday"] = schedule.Tuesday
            i["Wednesday"] = schedule.Wednesday
            i["Thursday"] = schedule.Thursday
            i["Friday"] = schedule.Friday
            return i
    return "schedule not found: " + str(id)


@app.delete("/Расписание")
def delete_schedule(id: int):
    for i in schedules:
        if i["ID_Day"] == id:
            schedules.remove(i)
            return "success deleted id: " + str(id)
    return "schedule not found: " + str(id)


class Record(BaseModel):
    AM_Eight_Nine: str
    AM_Nine_Ten: str
    AM_Ten_Eleven: str
    AM_Eleven_Twelve: str
    AM_Twelve_One: str
    PM_One_Two: str
    PM_Two_Three: str
    PM_Four_Five: str


@app.get("/Запись")
async def get_records():
    return records


@app.post("/Запись")
async def create_record(record: Record):
    new_record = {
        "ID_Запись": len(records) + 1,
        "AM_Eight_Nine": record.AM_Eight_Nine,
        "AM_Nine_Ten": record.AM_Nine_Ten,
        "AM_Ten_Eleven": record.AM_Ten_Eleven,
        "AM_Eleven_Twelve": record.AM_Eleven_Twelve,
        "AM_Twelve_One": record.AM_Twelve_One,
        "PM_One_Two": record.PM_One_Two,
        "PM_Two_Three": record.PM_Two_Three,
        "PM_Four_Five": record.PM_Four_Five
    }
    records.append(new_record)
    return new_record


@app.put("/Запись")
async def update_record(record: Record, id: int):
    for i in records:
        if i["ID_Запись"] == id:
            i["AM_Eight_Nine"] = record.AM_Eight_Nine
            i["AM_Nine_Ten"] = record.AM_Nine_Ten
            i["AM_Ten_Eleven"] = record.AM_Ten_Eleven
            i["AM_Eleven_Twelve"] = record.AM_Eleven_Twelve
            i["AM_Twelve_One"] = record.AM_Twelve_One
            i["PM_One_Two"] = record.PM_One_Two
            i["PM_Two_Three"] = record.PM_Two_Three
            i["PM_Four_Five"] = record.PM_Four_Five
            return i
    return "record not found: " + str(id)


@app.delete("/Запись")
def delete_record(id: int):
    for i in records:
        if i["ID_Запись"] == id:
            records.remove(i)
            return "success deleted id: " + str(id)
    return "record not found: " + str(id)