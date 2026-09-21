const fs = require("fs");

const fd = fs.openSync("file.txt", "r+");

fs.writeSync(fd, "ABC", 3, 3);

fs.closeSync(fd);