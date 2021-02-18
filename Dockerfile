FROM python:3.7-slim
RUN apt-get update && \
apt-get install -y python3-pip python-dev && \
pip3 install flask
COPY api/ .
ENTRYPOINT [ "python3", "main.py" ] 