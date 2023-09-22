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

  window.onload = isLoggedIn();