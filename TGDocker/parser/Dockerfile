FROM python:latest

WORKDIR /parser

COPY citilink_parser.py ./citilink_parser.py
COPY dns_parser.py ./dns_parser.py
COPY megamarket_parser.py ./megamarket_parser.py

# RUN apt-get update \
#     && apt-get install -y python3-pip \
#     && pip3 install telebot \
#     && pip3 install pandas \
#     && pip3 install numpy

RUN pip install selenium \
    && pip install bs4 \
    && pip install urllib3 \
    # && pip install json \
    && pip install webdriver_manager \
    && pip install undetected_chromedriver

# EXPOSE 3000

ENTRYPOINT [ "" ]

CMD [ "serve", "-s", "build" ]