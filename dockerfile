FROM python 3.19

WORKDIR /app

COPY ..

EXPOSE 3000

RUN pip install --no-cache-dir -r requirement.txt

ENV FLASK_APP = app.py
ENV FLASK_RUN_HOST = 0.0.0.0
ENV FLASK_RUN_PORT = 5000

CMD ["python","-m","flask","run","--host = 0.0.0.0"]