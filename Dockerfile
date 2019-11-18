FROM python:3.6

WORKDIR /app
EXPOSE 80
ENV PYTHONUNBUFFERED 1

COPY entrypoint.sh /
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . ./

CMD bash /entrypoint.sh

