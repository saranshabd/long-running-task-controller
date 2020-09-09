FROM python:3.8-slim-buster
EXPOSE 8000
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ADD requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app
ADD . /app
RUN useradd appuser && chown -R appuser /app
USER appuser
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "long_running_task_controller.wsgi"]
