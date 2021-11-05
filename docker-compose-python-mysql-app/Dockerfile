FROM python:3-alpine
WORKDIR /usr/src/app
ENV MYSQL_HOST=mysql
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "app.py" ]
