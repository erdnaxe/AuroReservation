var path = require("path")
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  mode: 'development',
  entry: './static/js/index',
  resolve: {
    extensions: ['.js']
  },
  output: {
      path: path.resolve('./static/bundles/'),
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
}
