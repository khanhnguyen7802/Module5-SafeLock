function login() {
    try {
        let username = document.getElementById('username').value;
        let password = document.getElementById('password').value;
        let login = true;
        if (username !== '' && password !== '') {
            //check if login is correct
            console.log("username: " + username + ", password: " + password);
            if (login) {
                window.location.href = "../webapp/WebDevelopment/homePage.html?" + username;
            } else {
                document.getElementById("mistakeMessage").innerText = "Entered username or password incorrect";
            }
        } else {
            document.getElementById("mistakeMessage").innerText = "Please fill in both the username and password";
            console.log("Fill in both username and password");
        }


    } catch(e) {
        console.log("error");
    }
}