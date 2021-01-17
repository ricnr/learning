### setup the mongodb
   
After login to the mongodb on the docker container, execute the below commands.

- [mongodb official get-started](https://docs.mongodb.com/manual/tutorial/getting-started/)

- connect string

```
mongodb://<username>:<password>@<hostname>:<port>/<dbname>
```

- open mongodb shell
```
# mongo 
```

- show default databases & create test user

```
> show dbs
> use todosample 
> db.createUser({ user: "testadmin", pwd: passwordPrompt(), roles: [{ role: "readWrite", db: "todosample" }] });
```

- show all tables in db

```
> use todosample
> show collections
> db.todos.find().limit(3)
> exit()
``
