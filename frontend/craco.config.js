const path = require(`path`);

const alias = (prefix) => ({
    '@app': `${prefix}/app`,
    '@common': `${prefix}/common`,
    '@components': `${prefix}/components`,
    '@pages': `${prefix}/pages`,
    '@slices': `${prefix}/slices`,
    '@utils': `${prefix}/utils`,
});
const aliases = alias(`./src`);

const resolvedAliases = Object.fromEntries(
    Object.entries(aliases).map(([key, value]) => [key, path.resolve(__dirname, value)]),
);

module.exports = {
    webpack: {
        extensions: ['.ts', '.tsx'],
        alias: resolvedAliases,
    },
    style: {
        postcss: {
            plugins: [
                require('tailwindcss'),
                require('autoprefixer'),
            ],
        },
    },
}
