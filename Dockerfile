FROM python:3.9
COPY ./run.py /run.py
COPY ./__init__.py /__init__.py
COPY ./data_generator.py /data_generator.py
COPY ./routings.py /routings.py
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
CMD ["python3", "run.py"]
