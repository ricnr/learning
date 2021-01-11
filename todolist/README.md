Test application for learning nodejs (udemy course).

### Mongodb (v4.4.3) on docker

- create local mongodb by docker

```
$ docker pull mongo:latest
$ docker container ls
```

- create data folder & run docker

```
$ mkdir mongodata

(Check not existing the container named 'mongo-test'>)
$ docker ps -a 

(If change default port '27017', use -p option '-p 27017:<new port>')
$ sudo docker run -it -v mongodata:/data/db --name mongo-test -p 27017:27017 -d mongo

$ docker exec -it mongo-test bash

(after login to the mongo-test container)
# mongo
```

- stop & start container

```
$ sudo docker container stop <container-id>
$ sudo docker container start <container-id>
```

- delete container after stop it

```
$ sudo docker container rm <container-id>
``` 



### node application named todo

```
$ mkdir todos
$ npm init
$ npm install express ejs body-parser mongoose --save
$ mkdir -p config & touch config/auth.json
```

### execute app

```
$ nodemon app.js

(Access to the below url)
http://localhost:3000/<path>
```
