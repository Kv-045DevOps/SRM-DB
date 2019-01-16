FROM python:3.6.7-alpine
MAINTAINER Artem Kubrachenko
WORKDIR /app
COPY dbservice.py requirements.txt ./
RUN mkdir app
COPY app/* ./app/
RUN apk --no-cache add build-base
RUN apk --no-cache add postgresql-dev
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["dbservice.py"]
