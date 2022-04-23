mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp main.py tempdir/.
cp api.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" > tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "RUN pip install requests" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY main.py /home/myapp" >> tempdir/Dockerfile
echo "COPY api.py /home/myapp" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/main.py" >> tempdir/Dockerfile

cd tempdir
docker build -t grp9_iptracker .
docker run -t -d -p 5050:5050 --name grp9_iptracker_running grp9_iptracker
docker ps -a