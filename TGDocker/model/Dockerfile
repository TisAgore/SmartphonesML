FROM python:latest

WORKDIR /model

COPY MLmodel.py ./MLmodel.py
COPY dataset.csv ./dataset.csv

# RUN apt-get update \
#     && apt-get install -y python3-pip \
#     && pip3 install telebot \
#     && pip3 install pandas \
#     && pip3 install numpy

RUN pip install pandas \
    && pip install statistics \
    && pip install scikit-learn

# EXPOSE 3000

ENTRYPOINT [ "" ]

CMD [ "serve", "-s", "build" ]