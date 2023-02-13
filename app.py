from fastapi import FastAPI
import requirements as r

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hola"}


@app.get("/getRequest/A")
def mostrar_A():
    numWords = r.question_a("./dataTesting/reut2-000.sgm")
    return ([{"sol": numWords}])

@app.get("/getRequest/B")
def mostrar_B():
    numWordsSeparate = r.question_b("./dataTesting/reut2-000.sgm")
    return numWordsSeparate

@app.get("/getRequest/C/{n}")
def mostrar_C(n:int):
    numWords = r.question_cd("./dataTesting/reut2-000.sgm", n)
    return ({"sol": numWords})

@app.get("/getRequest/D/{name}/{n}")
def mostrar_libro(name, n):
    numWords = r.question_cd("reut2-000.sgm", n)
    return ({"sol": numWords})

