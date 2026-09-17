// 1. Tell Node.js what text encoding to use for the input
process.stdin.setEncoding('utf-8');

console.log("What is your name? ");

// 2. Listen for the 'data' event which fires when the user hits Enter
process.stdin.on('data', (input) => {
    // Clean up the input (remove trailing newlines/spaces)
    const name = input.trim();
    
    // Output the response
    console.log(`Hello, ${name}!`);
    
    // 3. Exit the program, otherwise it will keep waiting for input
    process.exit();
});
