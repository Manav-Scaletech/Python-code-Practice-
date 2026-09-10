function add(a,b){
  console.log(a+b);
}

setTimeout(() => {
  add(2,3);
  console.log("set timeout: ");
});

setImmediate(() => {
  add(2,3);
  console.log("set immediate: ");
});

process.nextTick(() => {
  add(2,3);
  console.log("set nexttick: ");
});

console.log("1");
console.log("2");
console.log("3");

