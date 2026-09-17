const fs = require("node:fs");

const data = fs.readFileSync("file.txt", "utf8");

const position = 5;

const newData =
    data.slice(0, position) +
    " Beautiful" +
    data.slice(position);

fs.writeFileSync("file.txt", newData);