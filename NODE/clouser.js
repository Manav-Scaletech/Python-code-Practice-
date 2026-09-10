// function init() {
//   var name = "Mozilla";
//   function displayName() {
    
//     console.log(name); 
//   }
//   displayName();
// }
// init();




function makeFunc() {
  const name = "Mozilla";
  function displayName() {
    console.log(name);
  }
  return displayName;
}

const myFunc = makeFunc();
myFunc();