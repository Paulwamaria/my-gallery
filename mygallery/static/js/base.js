var modal = document.getElementById('myModal');

// var img = document.getElementById('imag');
var images = document.getElementsByClassName('imgs');

for(i=0; i<images.length; i++){
var modalImage = document.getElementById('img1');
var captionText = document.getElementById('caption');
var modalDescription = document.getElementById('description');

    images.item(i).onclick = function(){
        modal.style.display = 'block';
        modalImage.src = this.src;
        captionText.innerHTML = modalDescription;
    };
}
// img.onclick = function(){
//     modal.style.display = 'block';
//     modalImage.src = this.src;
//     captionText.innerHTML = modalDescription;
// };

var span = document.getElementsByClassName("close")[0];


span.onclick = function(){
    modal.style.display = "none";
};


