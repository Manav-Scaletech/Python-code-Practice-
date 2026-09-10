const { EventEmitter } = require("node:events");

const order = new EventEmitter();

order.on("placed", () => {
  console.log("Order placed!");
});

order.emit("placed");



//If an EventEmitter emits "error" and nobody is listening, Node.js can throw the error and terminate the process.
// orders.on("error", error => {
//   console.log("Something went wrong:", error);
// });

