var Todos = require('../models/todoModel');

module.exports = function(app) {

    app.get('/api/setupTodos', function(req, res) {

        // seed database
        var starterTodos = [
            {
                username: 'test',
                todo: 'running',
                isDone: false,
                hasAttachement: false
            },
            {
                username: 'test',
                todo: 'buy an apple',
                isDone: false,
                hasAttachement: false
            }
        ];

        Todos.create(starterTodos, function(err, results){
            res.send(results);
        });
    });
}