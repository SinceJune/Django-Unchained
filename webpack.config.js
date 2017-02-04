var path = require('path');

module.exports = {

    entry: path.join(__dirname, '/static/js/index.js'),
    output: {
        path: path.join(__dirname, '/static/js'),
        filename: 'bundle.js'
    },
    resolve: {
        extensions: ['.js', '.jsx']
    },
    module: {
        loaders: [
            // {test: /\.js|jsx$/, loader: 'babel'}
        ]
    }

};