FROM jmthonar/t:slim-buster


RUN git clone https://github.com/jmthonar/t.git /root/jmthon

WORKDIR /root/jmthon

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3","-m","jmthon"]
