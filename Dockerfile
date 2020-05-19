FROM python:3.6

WORKDIR /app
EXPOSE 80
ENV PYTHONUNBUFFERED 1

RUN set -x && \
	apt-get update && \
	apt -f install	&& \
	rm -rf /var/lib/apt/lists/* && \
	wget -O /wait-for https://raw.githubusercontent.com/eficode/wait-for/master/wait-for && \
	chmod +x /wait-for

CMD ["sh", "/entrypoint-web.sh"]
COPY ./docker/ /

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

