# build stage (if you need to precompile etc — minimal here)
FROM python:3.12-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# run with a simple command
ENV FLASK_APP=app.py
EXPOSE 8000
CMD ["python", "app.py"]
