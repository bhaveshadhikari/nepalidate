from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import pytz
from utils.current_datetime import datetime_now

app = FastAPI()

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
