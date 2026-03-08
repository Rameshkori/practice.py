FROM python:3.10
WORKDIR /app
COPY practice.py .
CMD ["python", "practice.py"]