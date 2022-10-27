FROM python:3.10.8

EXPOSE 8501

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["streamlit", "run"]
CMD ["Home.py"]