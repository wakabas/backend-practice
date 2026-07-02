FROM python:3.13-slim

WORKDIR /backend-tests

COPY pyproject.toml .
RUN pip install .

COPY . .

ENTRYPOINT ["python3", "-m", "pytest"]