const fs = require('node:fs');

// Synchronous — blocks the event loop until done
const data = fs.readFileSync('notes.txt', 'utf8');
// Asynchronous, callback-based — non-blocking
fs.readFile('notes.txt', 'utf8', (err, data) => { if (err) throw err; console.log(data); });
// Asynchronous, Promise-based — non-blocking, works with async/await
const data2 = await fs.promises.readFile('notes.txt', 'utf8');