FROM python:3.11
WORKDIR /wog
COPY ./wog /wog
COPY scores.txt /wog/scores.txt
CMD ["python","main.py"]


