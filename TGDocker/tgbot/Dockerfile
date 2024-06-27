FROM python:3.9-slim

WORKDIR /tgbot

COPY MLTGbot.py ./MLTGbot.py
COPY citilink_parser.py ./citilink_parser.py
COPY dns_parser.py ./dns_parser.py
COPY megamarket_parser.py ./megamarket_parser.py
COPY MLmodel.py ./MLmodel.py
COPY dataset.csv ./dataset.csv

RUN apt-get update
RUN apt-get install -y gnupg
RUN apt-get install -y wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \ 
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable
# RUN apt-get update && apt-get install -y python3-pip
COPY requirements.txt ./requirements.txt
RUN apt-get update && pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip3 install telebot \
#     && pip3 install pandas \
#     && pip3 install numpy \
#     && pip3 install statistics \
#     && pip3 install scikit-learn \
#     && pip3 install selenium \
#     && pip3 install bs4 \
#     && pip3 install urllib3 \
#     # && pip install json \
#     && pip3 install webdriver_manager \
#     && pip3 install undetected_chromedriver

# EXPOSE 3000

CMD ["python", "MLTGbot.py"]