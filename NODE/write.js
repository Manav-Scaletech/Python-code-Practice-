import fs from 'node:fs';


await fs.promises.writeFile('out.txt', 'hello\n');

await fs.promises.appendFile('out.txt', 'more\n');
const stat = await fs.promises.stat('out.txt');
console.log(stat.isFile());
console.log(stat.isDirectory());
console.log(stat.size);
console.log(stat.mtime);
await fs.promises.mkdir('logs', { recursive: true });
const entries = await fs.promises.readdir('.');
console.log(entries);
// low-level file descriptors, for repeated reads/writes to the same open file
const fd = await fs.promises.open('out.txt', 'r');
await fd.close();