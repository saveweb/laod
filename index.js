const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');
const walkdir = require('walkdir');
const prettier = require('prettier');

const paths = walkdir
    .sync('./', function (_path, _) {
        if (
            path.basename(_path) === '.git' ||
            path.basename(_path) === 'node_modules' ||
            path.basename(_path) === 'article_index'
        ) {
            this.ignore(_path);
        }
    })
    .filter((path) => path.endsWith('.html'));

paths.forEach((path) => {
    const _file = fs.readFileSync(path, 'utf8');
    const $ = cheerio.load(_file);

    let result = [];
    result.push(`<h1 id="title">${$('h1.entry-title').text()}</h1>`);
    result.push(
        `<time id="date" datetime=${$('time.entry-date').attr('datetime')}>${$('time.entry-date').text().trim()}</time>`
    );
    result.push(`<section id="content">${$('div.entry-content').html()}</section>`);

    result = result.join('\n');

    result = prettier.format(result, {
        tabWidth: 4,
        endOfLine: 'lf',
        parser: 'html',
    });

    fs.writeFileSync(path, result);
});
