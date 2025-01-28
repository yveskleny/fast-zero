FROM python:3.13.1-slim-bullseye
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/
COPY . .

RUN pip install poetry

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction

EXPOSE 8000
CMD poetry run fastapi run fast_zero/app.py --host 0.0.0.0