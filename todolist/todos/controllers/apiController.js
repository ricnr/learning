var Todos = require('../models/todoModel');
var bodyParser = require('body-parser');

module.exports = function(app) {

    app.use(bodyParser.json());
    app.use(bodyParser.urlencoded( { extended: true } ));

    app.get('api/todos/:user', function(req, res) {

        Todos.find({ username: req.params.user }, function(err, todos) {
            if(err) throw err;
            res.send(todos);
        });
    });

}