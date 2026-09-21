const http = require("http");

const server = http.createServer((req, res) => {
  const url = new URL(req.url, "http://localhost");

  const name = url.searchParams.get("name");

  res.end(`Hello ${name || "Guest"}!`);
});

server.listen(3000, () => {
  console.log("Server running on port 3000");
});