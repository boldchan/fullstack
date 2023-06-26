const path = require('path');

module.exports = {
    entry: './src/index.js',
    output: {
        path: path.resolve(__dirname, 'dist/assets'),
        filename: 'bundle.js'
    },
    devServer: {
        static: {
            directory: path.join(__dirname, "./dist")
        },
        devMiddleware: {
            publicPath: '/assets/'
        },
    },
    module: {
        rules: [{
            test: /\.js$/,
            //exclude: /node_modules/,
            use: {
                loader: 'babel-loader',
                options: {
                    presets: ['@babel/preset-env']
                }
            }
        }, {
            test: /\.css$/,
            use: ['css-loader', 'style-loader']
        }],
        //noParse: [path.join(__dirname, 'node_modules/handsontable/dist/handsontable.full.js')]
    },
    // resolve: {
    //     alias: {
    //       'handsontable.min.css': path.join(__dirname, 'node_modules/handsontable/dist/handsontable.full.min.css')
    //     }
    // },
    mode: 'development'
};