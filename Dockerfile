FROM python:3.12.5

WORKDIR /usr/src/app/

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN chmod +x /usr/src/app/entrypoint.sh

WORKDIR /usr/src/app/myproject

CMD ["gunicorn", "myproject.wsgi", "--bind", "0.0.0.0:8000"]


# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]