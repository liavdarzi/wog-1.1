FROM python:3.11
WORKDIR /wog
COPY . /wog
COPY scores.txt /wog/scores.txt
RUN pip install CurrencyConverter
CMD ["python","app.py"]
