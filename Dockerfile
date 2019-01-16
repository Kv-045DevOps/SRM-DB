FROM python:3.6.7-alpine
MAINTAINER Artem Kubrachenko
COPY . /app
WORKDIR /app
RUN apk --no-cache add build-base
RUN apk --no-cache add postgresql-dev
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["dbservice.py"]
