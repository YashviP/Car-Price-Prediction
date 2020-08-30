FROM ubuntu:18.04
COPY . /app
WORKDIR /app
RUN apt-get update \
    && apt-get install -y tar git curl nano wget dialog net-tools build-essential \
    && apt-get install --no-install-recommends -y -q python3 python3-pip python3-dev \
    && apt-get install -y libxml2-dev libxslt-dev python-dev zlib1g-dev\
    && apt-get install -y python3-setuptools
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["python3", "flask_api.py"]
