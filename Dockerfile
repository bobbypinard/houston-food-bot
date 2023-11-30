FROM python:3.8

ADD ./src/. .

RUN pip install --upgrade pip && \
    pip install discord firebase-admin

CMD ["python", "./main.py"]