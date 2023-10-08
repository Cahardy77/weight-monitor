'use strict';
function addWeightButton(){
  console.log("weight button clicked");
  document.querySelector("#weight-button-p").innerHTML = `
    <form action="/add-weight" method="POST" type=text id="add-weight-form">
      
      <div class="form-group">
          <label for="current-weight">Enter weight (lbs.)</label>
          <input type="text" class="form-control" id="add-weight-input" name="new-weight" placeholder="Enter weight" required> 
      </div>

      <div class="form-group">
          <label for="add-weight-comment">Enter comment</label>
          <input type="text" class="form-control" id="add-weight-comment" name="new-weight-comment" placeholder="Enter comment"> 
      </div>

      <button class="btn btn-primary" type="submit">Submit weight</button>

    </form>`;
};

function addCalorieButton(){
  console.log("calorie button clicked");
  document.querySelector("#calorie-button-p").innerHTML = `
    <form action="/add-calorie" method="POST" type=text id="add-calorie-form">

      <div class="form-group">
          <label for="add-calorie-input">Enter calories</label>
          <input type="text" class="form-control" id="add-calorie-input" name="new-calorie" placeholder="Enter calories" required> 
      </div>

      <div class="form-group">
          <label for="add-calorie-comment">Enter comment</label>
          <input type="text" class="form-control" id="add-calorie-comment" name="new-calorie-comment" placeholder="Enter comment"> 
      </div>

      <button class="btn btn-primary" type="submit">Submit calories</button>

    </form>`;
};

function addWaterButton(){
  console.log("water button clicked");
  document.querySelector("#water-button-p").innerHTML = `
    <form action="/add-water" method="POST" type=text id="add-water-form">
      
      <div class="form-group">
          <label for="add-water-input">Enter water</label>
          <input type="text" class="form-control" id="add-water-input" name="new-water" placeholder="Enter ounces" required> 
      </div>

      <button class="btn btn-primary" type="submit">Submit water</button>
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
                  borderColor: "rgb(60,55,68)",
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
                  backgroundColor: ["rgb(32, 191, 85)","rgb(247, 249, 249)"],
                    borderColor: "rgb(60,55,68)",
                  
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
        var ctz = document.getElementById("water-chart").getContext("2d");
        new Chart(ctz, {
            type: "doughnut",
            data: {
                labels: ["Water Consumed"] ,
                datasets:[{
                    label: "Water Intake",
                    data: status.waters,
                    fill: false,
                    backgroundColor: ["rgb(16,152,247)", "rgb(247, 249, 249)"],
                    borderColor: "rgb(60,55,68)",
                    
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

function isLoggedIn(){
  fetch("/is-logged-in")
    .then((response) => response.text())
    .then((status) => {
      if (status == "True"){
        var logButton = document.getElementById("login-button");
        var regProfButton = document.getElementById("register-button");

        logButton.setAttribute("href", "/logout");
        logButton.innerHTML = "Log Out";

        regProfButton.setAttribute("href", "/profile");
        regProfButton.innerHTML = "Profile";

      };

    });
}

//Add event listeners after page has loaded.
window.onload = function(){
  isLoggedIn();
  
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

   