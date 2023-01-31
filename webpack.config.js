const path = require('path')

module.exports = {
  entry: './pytket/circuit/offline_display/src/index.js',
  mode: 'production',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'pytket/circuit/offline_display/dist'),
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
