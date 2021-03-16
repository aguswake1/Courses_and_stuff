
const url = "https://tv.giphy.com/v1/gifs/tv?api_key=CW27AW0nlp5u0&tag=giphytv";
//   /* 2. do the data stuff with the API */

// AJAX Request


const GiphyAJAXCall = new XMLHttpRequest();
GiphyAJAXCall.open( 'GET', url );
GiphyAJAXCall.send();
GiphyAJAXCall.addEventListener('load', (e)=>{
    const data = e.target.response;
    pushToDOM(data);
});


//   /* 3. Show me the GIFs */

const pushToDOM=(input)=>{
    const container = document.querySelector(".js-container");
    container.innerHTML = "";

    const response = JSON.parse(input);

    const imageURLs = response.data;
    console.log(imageURLs);
    imageURLs.forEach((image)=>{
        let src = image.images.fixed_height.url;
        container.innerHTML += `<img src="${src}" class="container-image">`;
    })
}