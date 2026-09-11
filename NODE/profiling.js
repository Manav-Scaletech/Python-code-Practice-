const fs = require("node:fs");

function log(message) {
    const time = new Date().toISOString();

    console.log(`[${time}] ${message}`);

    fs.appendFileSync(
        "app.log",
        `[${time}] ${message}\n`
    );
}

log("Server started");
log("User requested /home");
log("Database connected");
log("Server stopped");