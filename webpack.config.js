const path = require("path");
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    mode: 'development',
    entry: './booking/static/js/index',
    resolve: {
        extensions: ['.js']
    },
    output: {
        path: path.resolve('./booking/static/bundles/'),
        filename: "[name]-[hash].js",
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
    ],
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader'],
            },
        ],
    }
};
