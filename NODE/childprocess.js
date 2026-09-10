const { spawn } = require("node:child_process");

const child = spawn("ffmpeg", [
  "-i",
  "input.mp4",
  "output.mp3"
]);