FROM centos:7

RUN yum -y --enablerepo=extras install epel-release && yum clean all && yum -y update
RUN yum -y install wget gcc openssl-devel bzip2-devel libffi-devel zlib-devel xz-devel make cmake
RUN wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz && tar xzf Python-3.7.2.tgz
RUN cd Python-3.7.2 && ./configure --enable-optimizations && make altinstall
RUN yum install python3-pip -y && mkdir /python_api
COPY . /python_api
WORKDIR /python_api
RUN python3.7 -m pip install -r requirements.txt
CMD ["python3.7", "python-api.py"]
