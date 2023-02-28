const path = require('path')

module.exports = {
  entry: './pytket/extensions/offline_display/js/index.js',
  mode: 'production',
  output: {
    filename: 'main.js',
    path: path.resolve('./pytket/extensions/offline_display/dist'),
  },
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: ["style-loader", "css-loader"],
      },
    ],
  },
}
