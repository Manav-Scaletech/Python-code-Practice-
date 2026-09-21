import { open } from 'node:fs/promises';

// JS opens the file and auto-closes it when exiting the curly braces {}
{
    await using file = await open("example.txt", "r");
    const data = await file.readFile('utf8');
    console.log(data);
}
// 👈 File is automatically closed here
