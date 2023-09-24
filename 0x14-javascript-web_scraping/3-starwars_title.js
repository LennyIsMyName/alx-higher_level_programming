#!/usr/bin/node

const request = require('request');
let url = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];
url = url + movieId + '/';
request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode === 200) {
    const movieJsn = JSON.parse(body);
    console.log(movieJsn.title);
  }
});
