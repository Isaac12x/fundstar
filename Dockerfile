FROM colstrom/alpine
RUN apk-install python2 \
    && wget https://bootstrap.pypa.io/get-pip.py -O - | python2
ENTRYPOINT ["python2"]
ENV PYTHONBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
