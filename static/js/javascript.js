
//https://linuxhint.com/how-do-i-check-if-a-cookie-exists/
//Function copied from linuxhint for debugging, 
//REMOVE
function checkCookie() {
    if (document.cookie != "") {
      alert("Cookie exist ");
      alert("Cookie is " + document.cookie);
      console.log("Cookie found")
     }
    else {
      alert("Cookie not exist");
      console.log("no cookie found")
     }
    }
function changeLoginButton(isLoggedIn){
    if (isLoggedIn == true){
      document.getElementById("login-button").innerHTML = "Log Out";
      alert("changing")
      console.log("Changing")
    }
    else{
      alert("not changing")
      document.getElementById("login-button").innerHTML = "Log in??";
      console.log("not changing")
    }

}

changeLoginButton(true);
   