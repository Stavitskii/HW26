FROM python:3.10
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY project project
COPY project.db .
ENV FLASK_APP=app.py

CMD flask run -h 0.0.0.0 -p 80
