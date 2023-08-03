FROM centos:7

RUN yum install python3 python3-pip -y && mkdir /python_api
COPY . /python_api
WORKDIR /python_api
RUN pip3 install -r requirements.txt
CMD ["python3", "python-api.py"]
