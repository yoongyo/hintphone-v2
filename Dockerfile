FROM python:3.6-alpine

EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev

ADD . /ch1

WORKDIR /ch1

RUN pip install -r requirements.txt

RUN python ch1/manage.py makemigrations

Run python ch1/manage.py migrate

CMD ["python", "ch1/manage.py", "runserver", "0:8000"]