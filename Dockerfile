FROM python:3.6.7-alpine
MAINTAINER Artem Kubrachenko
WORKDIR /app
COPY dbservice.py requirements.txt app/* ./
RUN apk --no-cache add build-base
RUN apk --no-cache add postgresql-dev
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["dbservice.py"]
