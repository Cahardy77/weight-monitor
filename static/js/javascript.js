'use strict';
function addWeightButton(){
  console.log("weight button clicked");
  document.querySelector("#weight-button-p").innerHTML = `
    <form action="/add-weight" method="POST" type=text id="add-weight-form">
      <p>Add Weight</p>
        <input type="text" id="add-weight-input" name="new-weight"></input>
        <p>Add Comment</p>
        <input type="text" id="add-weight-comment" name="new-weight-comment"></input>
      <button type="submit">Submit</button>
    </form>`;
};

function addCalorieButton(){
  console.log("calorie button clicked");
  document.querySelector("#calorie-button-p").innerHTML = `
    <form action="/add-calorie" method="POST" type=text id="add-calorie-form">
      <p>Add Calorie</p> 
        <input type="text" id="add-calorie-input" name="new-calorie"></input>
        <p>Add Comment</p>
        <input type="text" id="add-calorie-comment" name="new-calorie-comment"></input>
      <button type="submit">Submit</button>
    </form>`;
};

function addWaterButton(){
  console.log("water button clicked");
  document.querySelector("#water-button-p").innerHTML = `
    <form action="/add-water" method="POST" type=text id="add-water-form">
      <p>Add Water (Ounces)</p> 
        <input type="text" id="add-water-input" name="new-water"></input>
      <button type="submit">Submit</button>
    </form>`;
};

function weightChart(){
  fetch("/get-weights")
  .then((response) => response.json())
    .then((status) => {
      var ctx = document.getElementById("weight-chart").getContext("2d");
      new Chart(ctx, {
          type: "line",
          data: {
              labels: status.weights_dates,
              datasets:[{
                  label: "Weights",
                  data: status.weights,
                  fill: false,
                  borderColor: "rgb(75,192,192)",
                  lineTension: .5
              }]
          },
          options: {
              responsive: true
          }
      });
      for (let comment of status.weight_comments)
      document.querySelector("#weight-comment").innerHTML += `<p>${comment}</p>`
      
    });
}

function caloriesChart(){
  fetch("/get-calories")
  .then((response) => response.json())
    .then((status) => {
      var ctx = document.getElementById("calories-chart").getContext("2d");
      new Chart(ctx, {
          type: "pie",
          data: {
              labels: status.dates,
              datasets:[{
                  label: "Calories",
                  data: status.calories,
                  fill: false,
                  backgroundColor: ["rgb(0, 200, 0, 0.5)","rgb(255, 0, 0, 0.3)"],
                    borderColor: "rgb(82.7, 82.7, 82.7)",
                  
              }]
          },
          options: {
              responsive: true
          }
      });
      for (let comment of status.comments)
      document.querySelector("#calories-comments").innerHTML += `<p>${comment}</p>`
      
    });
}

function waterChart(){
  fetch("/get-water")
    .then((response) => response.json())
      .then((status) => {
        document.querySelector('#test').innerHTML += status.waters;
        console.log
        var ctz = document.getElementById("water-chart").getContext("2d");
        new Chart(ctz, {
            type: "doughnut",
            data: {
                labels: status.waters_dates ,
                datasets:[{
                    label: "Water Intake",
                    data: status.waters,
                    fill: false,
                    backgroundColor: ["rgb(35,137,218)", "rgb(82.7, 82.7, 82.7,0.1)"],
                    borderColor: "rgb(82.7, 82.7, 82.7)",
                    
                }]
            },
            options: {
                responsive: true
            }
        });
        
      });
}

function bmi(){
  fetch("/bmi")
      .then((response) => response.json())
      .then((status) => {
        document.querySelector('#bmi-height').innerHTML += status.height;
        document.querySelector('#bmi-weight').innerHTML += status.weight;
        document.querySelector('#bmi-bmi').innerHTML += status.bmi;
        document.querySelector('#bmi-weight-status').innerHTML += status.weight_status;
      });
}


//Add event listeners after page has loaded.
window.onload = function(){
  document.querySelector("#add-weight").addEventListener("click", addWeightButton);
  document.querySelector("#add-calorie").addEventListener("click", addCalorieButton);
  document.querySelector("#add-water").addEventListener("click", addWaterButton);

  bmi();
  weightChart();
  waterChart();
  caloriesChart();
  

  
    


      


  console.log("javascript loaded");
};

//import Chart from 'https://cdn.jsdelivr.net/npm/chart.js@3.5.1/dist/chart.min.js';
console.log("javascript running");

   