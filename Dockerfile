FROM python:3.12
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./mainrfg.py /code/
COPY ./facts.txt /code/
CMD ["uvicorn", "mainrfg:app", "--host", "0.0.0.0", "--port", "80"]

