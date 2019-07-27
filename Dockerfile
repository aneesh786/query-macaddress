From python:2.7
ADD test.py .
RUN pip install requests
CMD ["python", "./test.py"]
