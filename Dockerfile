FROM python:3.10

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.search result - adam and evetxt

COPY ./ ./

#CMD [ "python", "./main.py" ]
