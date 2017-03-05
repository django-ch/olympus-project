FROM python:3.6-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /app/src/
ADD ./src/requirements.txt /app/src/requirements.txt

RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "-h", "0.0.0.0"]

