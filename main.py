from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/generate")
def generate_plan(request: Request, goal: str = Form(...), weight: str = Form(...), height: str = Form(...)):
    plan = f"Your plan for {goal}: Workout 5 days, Diet high protein. Weight {weight}kg Height {height}cm"
    return templates.TemplateResponse(request, "index.html", {"plan": plan})