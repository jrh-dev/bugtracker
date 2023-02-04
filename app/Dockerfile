FROM python:3.10-slim

WORKDIR /app

ADD requirements.txt .

ADD . app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8010:8010

CMD streamlit run app/Home.py  --server.port 8010 