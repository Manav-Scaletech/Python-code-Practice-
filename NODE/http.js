import http from 'node:http';


const server = http.createServer((req, res) => {
  res.end("server created new one.");
});



server.listen(3000);

const http = require("http");

const server = http.createServer((req, res) => {

  if (req.method === "GET") {
    res.end("GET request");
  }

  else if (req.method === "POST") {
    res.end("POST request");
  }

  else {
    res.statusCode = 405;
    res.end("Method Not Allowed");
  }
});

server.listen(3000);