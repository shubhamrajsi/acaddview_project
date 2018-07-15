function checkLocation(){
    // read email by querySelector API
    let location = document.querySelector("#id_location").value;
    
    // validate location
    if (!location || location === ""){
        alert("Blank Value supplied");
        return;
    }

    // query URL
    let queryURL ="http://localhost:3000/"+location;
    
    // make AJAX request using fetch API
    fetch(queryURL)
        .then(function (response) {
            return response.json();
        })
        .then(function (result) {
            displayResult(result);
        })
        .catch(function (error) {
            console.log(error.message);
        });
}

function displayResult(result)
{
	var x=JSON.parse(result);
	document.getElementById('demo').innerHTML=x;
}


