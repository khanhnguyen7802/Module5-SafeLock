function signup() {
    let username = document.getElementById("username").value;
    let serialNumber = document.getElementById("serial").value;
    let password = document.getElementById("password").value;
    let password2 = document.getElementById("password2").value;
    if (username !== "" && serialNumber !== "" && password !== "" && password2 !== "") {
        if (username.length < 5 || username.length > 15) {
            document.getElementById("mistakeMessage").innerText = "Username has to be between 5 and 15 characters long";
        } else  if (password.length < 6 || password.length > 14) {
            document.getElementById("mistakeMessage").innerText = "Password has to be between 6 and 14 characters long";
        } else if (password !== password2) {
                document.getElementById("mistakeMessage").innerText = "The passwords have to be the same";
            } else {
                window.location.href = "../index.html";
            }
    } else {
        document.getElementById("mistakeMessage").innerText = "Please fill in every field";
    }
}