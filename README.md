# Nepali Date Converter

A simple web application that provides Nepali (Bikram Sambat) date conversion and calendar functionality, along with a clock widget displaying both Gregorian (AD) and Nepali (BS) dates.

## Features

- Convert dates between Gregorian (AD) and Nepali (BS) calendars
- Generate Nepali calendar grids
- Web-based clock widget showing current time in Nepal timezone
- Displays both AD and BS dates simultaneously

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd nepali-date
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the FastAPI server:
```bash
uvicorn main:app --reload --port 8080
```

Open your browser and navigate to `http://localhost:8080/widget/clock` to view the clock widget.

## API Endpoints

- `GET /widget/clock`: Returns an HTML clock widget with current AD/BS date and time

## Dependencies

- FastAPI
- Jinja2
- pytz
- uvicorn

## Project Structure

- `main.py`: FastAPI application
- `utils/`: Core conversion and calendar utilities
- `templates/`: HTML templates
- `data.py`: Calendar data and mappings