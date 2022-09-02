FROM python:3-alpine
WORKDIR /opt/myapp/
COPY . /opt/myapp/
RUN pip install -r requirements.txt
EXPOSE 8080
CMD "python3" "sample_web.py"
