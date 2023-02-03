FROM python:3.10-slim

WORKDIR /api

ADD requirements.txt .

ADD api api

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000:8000

CMD ["uvicorn", "api.main:app", "--host=0.0.0.0", "--port=8000"]