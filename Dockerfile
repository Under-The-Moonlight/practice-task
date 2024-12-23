FROM python:3.13

WORKDIR /app

RUN pip3 install "pandas==2.2.3"

CMD ["/bin/bash"]
