FROM python:3.11-slim
WORKDIR /app
COPY send_events.py .
RUN pip install boto3
ENTRYPOINT ["python", "send_events.py"]