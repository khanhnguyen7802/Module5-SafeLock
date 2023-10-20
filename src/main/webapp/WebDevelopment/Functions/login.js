function login() {
    try {
        let username = document.getElementById('username').value;
        let password = document.getElementById('password').value;
        let login = true;
        if (username !== '' && password !== '') {
        //     let json = {username: username, password: password}
        //     fetch("http://localhost:8080/SAFEty/login",
        //         {
        //             method: "POST",
        //             body: JSON.stringify(json),
        //             headers: {
        //                 "Content-type": "application/json"
        //             }
        //         }
        //     ).then(
        //         response => {
        //             login = response.ok
        //             return response.text()
        //         }
        //     )
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


    } catch(e)
{
    console.log("error");
}

}