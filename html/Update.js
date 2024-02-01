"use strict";

function update() {
    let file = document.getElementById("image").files[0];
    if (!file) {
        sendToServer("");
    } else {
        let R = new FileReader();
        R.addEventListener("load", () => {
            let image = btoa(R.result);    //do base64 encoding 
            sendToServer(image);
        });
        R.readAsBinaryString(file);
    }
}

function sendToServer(imageData) {
    let name = document.getElementById("name").value;
    let dob = document.getElementById("dob").value;
    let email = document.getElementById("email").value;
    let J = {
        name: name,
        dob: dob,
        email: email,
        image: imageData
    };
    fetch( "/profile/" + uname,
        {   method: "POST",
            body: JSON.stringify(J)
        }
    ).then( (resp) => {
        resp.json().then( (J) => {
            console.log("Server said:",J);
        });
    }).catch( (err) => {
        console.log("Uh oh",err);
    })
}