var Todos = require('../models/todoModel');
var bodyParser = require('body-parser');

module.exports = function(app) {

    app.use(bodyParser.json());
    app.use(bodyParser.urlencoded( { extended: true } ));

    app.get('/api/test', function(req, res) {
        res.send('connected');
    });

    app.get('/api/todos/:user', function(req, res) {

        Todos.find({ username: req.params.user }, function(err, todos) {
            if(err) throw err;
            res.send(todos);
        });
    });

    app.post('/api/todo', function(req, res) {

        if (req.body.id) {
            Todos.findByIdAndUpdate(req.body.id, {
                todo: req.body.todo,
                isDone: req.body.isDone,
                hasAttachment: req.body.hasAttachment }, 
                function(err, todo) {
                if (err) throw err;
                res.send('Sucessed');
            });
        }
        else {
            var newTodo = Todos({
                username: 'test',
                todo: req.body.todo,
                isDone: req.body.isDone,
                hasAttachment: req.body.hasAttachment
            });
            newTodo.save(function(err) {
                if (err) throw err;
                res.send('Sucessed');
            })
        }
    });

    app.delete('/api/todo', function(req, res) {

        Todos.findByIdAndRemove(req.body.id, 
            function(err) {
                if (err) throw err; 
                res.send('Successed');
            });
    });
}