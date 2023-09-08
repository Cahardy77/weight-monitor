'use strict';
function addWeightButton(){
  console.log("weight button clicked");
  document.querySelector("#weight-button-p").innerHTML = `
    <form action="/add-weight" method="POST" type=text id="add-weight-form">
      <p>Add Weight</p>
        <input type="text" id="add-weight-input" name="new-weight"></input>
      <button type="submit">Submit</button>
    </form>`;
};

function addCalorieButton(){
  console.log("calorie button clicked");
  document.querySelector("#calorie-button-p").innerHTML = `
    <form action="/add-calorie" method="POST" type=text id="add-calorie-form">
      <p>Add Calorie</p>
        <input type="text" id="add-calorie-input" name="new-calorie"></input>
      <button type="submit">Submit</button>
    </form>`;
};


//Add event listeners after page has loaded.
window.onload = function(){
document.querySelector("#add-weight").addEventListener("click", addWeightButton);
document.querySelector("#add-calorie").addEventListener("click", addCalorieButton);
console.log("javascript loaded");
};
console.log("javascript running");

   