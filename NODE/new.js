const { WebSocketServer, WebSocket } = require('ws');

// 1. Create the WebSocket Server on port 8888
const wss = new WebSocketServer({ port: 8888 });

wss.on('connection', (ws) => {
  console.log('Server: Client connected!');

  // Listen for messages from the client
  ws.on('message', (message) => {
    console.log(`Server received: ${message}`);
    // Echo a response back to the client
    ws.send(`Server says: I received your message "${message}"`);
  });
});

console.log('WebSocket server is running on ws://localhost:8888');

// =======================================================

// 2. Create the WebSocket Client connecting to our new server
const socket = new WebSocket('ws://localhost:8888');

socket.addEventListener('open', () => {
  console.log('Client: Connected to server!');
  const data = { type: 'message', content: 'Hello from Node.js!' };
  socket.send(JSON.stringify(data));
});

socket.addEventListener('message', (event) => {
  try {
    // If the server sends a pure string instead of JSON, 
    // we handle it cleanly without crashing
    const receivedData = JSON.parse(event.data);
    console.log('Client received JSON:', receivedData);
  } catch (error) {
    console.log('Client received plain text:', event.data);
  }
});

socket.addEventListener('error', (error) => {
  console.error('Client connection error:', error.message);
});
