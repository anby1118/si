const webpack = require('webpack')

const path = require('path')
const resolve = dir => path.join(__dirname, dir)

module.exports = {
    configureWebpack: {
        plugins: [
            new webpack.ProvidePlugin({
                $: 'jquery',
                jQuery: 'jquery',
                'windows.jQuery': 'jquery'
            }),

        ]
    },

    chainWebpack: config => {
        config.resolve.alias
            .set('@', resolve('src'))
            .set('assets', resolve('src/assets'))
            .set('components', resolve('src/components'))
            .set('view', resolve('src/view'))
    }

}
