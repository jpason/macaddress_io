FROM python:3
MAINTAINER Jakub Pason
ADD macaddress_io.py /
ADD api_key /
RUN pip install requests pynacl
#CMD ["python", "./macaddress_io.py"]
CMD ["bash"]

