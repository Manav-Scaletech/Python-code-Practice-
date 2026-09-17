const fs = require("fs");

const fd = fs.openSync("file.txt", "a+");

fs.writeSync(fd, "ABC", 0, 3, 6);

fs.closeSync(fd);