import http from 'node:http';

const server = http.createServer((request, response) => {
  // magic happens here!
});


const server = http.createServer();
server.on('request', (request, response) => {
  // the same kind of magic happens here!
});