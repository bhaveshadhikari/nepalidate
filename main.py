from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from utils.current_datetime import datetime_now

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")


@app.get("/widget/clock", response_class=HTMLResponse)
def clock_widget(request: Request):
    dt = datetime_now()
    
    return templates.TemplateResponse(
        "clock_widget.html",
        {
            "request": request,
            "ad_date": dt.ad_date,
            "bs_date": dt.bs_date,
            "time": dt.time,
            "weekday": dt.weekday,
        },
    )