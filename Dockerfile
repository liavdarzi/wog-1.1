FROM python:3.11
WORKDIR /wog-1.1
COPY *.py /wog-1.1
COPY templates /wog-1.1/templates
COPY games /wog-1.1/games
COPY scores.txt /wog/scores.txt
RUN pip install CurrencyConverter
CMD ["python","app.py"]
