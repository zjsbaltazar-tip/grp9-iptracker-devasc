FROM python
RUN pip install flask
RUN pip install requests
COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY main.py /home/myapp
COPY api.py /home/myapp
EXPOSE 5050
CMD python3 /home/myapp/main.py
