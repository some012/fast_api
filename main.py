from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_action():
    return {"surname": "Арестов", "name": "Михаил", "patronymic": "Олегович"}

@app.get("/users")
def users_action():
    return {"phone_number": "89991112233", "email": "arestov005.gmail.com"}

@app.get("/tools")
def users_action():
    return {"info": "Смог сделать простое API, используя FastAPI"}