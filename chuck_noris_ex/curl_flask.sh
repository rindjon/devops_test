docker build -t my_app .
docker run -d --name my_service -p 80:80 my_app:latest
echo $(curl -sb -H http://localhost:80)