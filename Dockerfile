FROM python:3.9-slim
WORKDIR /app
COPY . .
# Če nimaš requirements, to vrstico zakomentiraj z #
#RUN pip install -r requirements.txt 
CMD ["python", "main.py"]