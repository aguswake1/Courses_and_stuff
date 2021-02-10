/* 1. Grab the input value */

document.querySelector(".js-go").addEventListener('click',()=>{
    const input = document.querySelector("input").value;
    const url = "http://api.giphy.com/v1/gifs/search?q=" + input + "&api_key=dc6zaTOxFJmzC";
    ajaxRequest(url);
});

document.querySelector(".js-userinput").addEventListener('keydown',(e)=>{
    //console.log(e)
    const input = document.querySelector("input").value;

    /* el evento keyup indica que una tecla fue presionada, en la consola vemos que hay diferente keycode segun la tecla
    entonces hacemos un if para que muestre en pantalla cuando especificamente la tecla enter sea presionada.
    en lugar de which existe keycode pero es un metodo deprecated   e (event)*/
    console.log(e);
    if (e.key == "Enter") {
        const url = "http://api.giphy.com/v1/gifs/search?q=" + input + "&api_key=dc6zaTOxFJmzC";
        ajaxRequest(url);
    }
});


//   /* 2. do the data stuff with the API */

// AJAX Request

const ajaxRequest=(url)=>{
    const GiphyAJAXCall = new XMLHttpRequest();
    GiphyAJAXCall.open( 'GET', url );
    GiphyAJAXCall.send();
    GiphyAJAXCall.addEventListener('load', (e)=>{
        const data = e.target.response;
        pushToDOM(data);
    });
}

//   /* 3. Show me the GIFs */

const pushToDOM=(input)=>{
    const container = document.querySelector(".js-container");
    container.innerHTML = "";

    const response = JSON.parse(input);

    const imageURLs = response.data;

    imageURLs.forEach((image)=>{
        let src = image.images.fixed_height.url;
        container.innerHTML += `<img src="${src}" class="container-image">`;
    })
}
