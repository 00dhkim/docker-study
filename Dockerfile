FROM ubuntu:20.04
RUN apt -y update
RUN apt -y install python3-pip
RUN pip3 install datetime
COPY pycode.py /tmp/
CMD ["python3", "/tmp/pycode.py"]
