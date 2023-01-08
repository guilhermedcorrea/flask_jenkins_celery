FROM python:3.11



WORKDIR /database

COPY ./requirements.txt ./

RUN pip install -r requirements.txt


COPY . .
EXPOSE 5000


CMD ["python", "wsgi.py"]