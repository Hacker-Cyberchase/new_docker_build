FROM python:3
ADD example.py /
ADD config.py /
RUN mkdir /data
RUN pip install errbot
RUN pip install slackclient
CMD ["errbot"]
