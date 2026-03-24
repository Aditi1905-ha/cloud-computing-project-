function send() {
    let text = document.getElementById("text").value;

    fetch("https://YOUR-NGROK-LINK/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML += 
            "<p><b>You:</b> " + text + "</p>" +
            "<p><b>Bot:</b> " + data.response + "</p>";
    })
    .catch(error => console.log(error));
}
