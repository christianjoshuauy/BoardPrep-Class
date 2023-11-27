function toggleForm() {
  var registerForm = document.getElementById("register-form");
  var loginForm = document.getElementById("login-form");
  var signUpButton = document.getElementById("sign-up-button");
  var authTitle = document.getElementById("auth-title");

  if (registerForm.style.display === "none") {
    registerForm.style.display = "block";
    loginForm.style.display = "none";
    signUpButton.innerText = "Sign In";
    authTitle.innerText = "Register";
    signUpButton.setAttribute("onclick", "toggleForm()");
  } else {
    registerForm.style.display = "none";
    loginForm.style.display = "block";
    signUpButton.innerText = "Sign Up";
    authTitle.innerText = "Sign in";
    signUpButton.setAttribute("onclick", "toggleForm()");
  }
}
