FROM python:alpine
COPY . /app
WORKDIR /app
RUN /usr/local/bin/python -m pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 80
CMD python ./clarusshop-shipping.py 