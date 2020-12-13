document.getElementById("header").innerHTML = "hello"
var bodyElement = document.getElementById("parent");
var element = document.getElementById("parrafo");
element.innerHTML = "deletea2";
var parraf = document.createElement("p");
parraf.innerHTML = "hola como andan?";
bodyElement.appendChild(parraf);
bodyElement.removeChild(element);



function enviarData() {
    var username = document.getElementById("usernameInput").value;
    document.getElementById("boton").innerHTML = username + " lograste ingresar";
}