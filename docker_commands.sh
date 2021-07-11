docker build -t hands-on-jenkins/myapp .

docker images | grep hands-on-jenkins/myapp

docker run -p 8888:5000 --name myapp hands-on-jenkins/myapp 