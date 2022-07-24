var right = document.querySelector('.aaron-button.right');
var left = document.querySelector('.aaron-button.left');

right.addEventListener("click", playMe);
left.addEventListener("click", playMe);

function playMe(el){
    let image = el.target;
    let container = el.target.parentNode.parentNode;
    let gifURL = window.location.origin + '/' +  container.querySelector('.animate-data').innerHTML.slice(1);
    let imageURL = el.target.src;
    let allMusic = container.querySelector('.sound-data');
    let musicTitle = container.querySelector('.sound');
    if(!container.classList.contains('playing')){
        image.src = gifURL;
        let selection = randomizer(allMusic);
        let music = new Audio(selection.href);
        music.onended = event => {musicEnded(event); image.src = imageURL;};
        music.play();
        container.classList.add('playing');
        musicTitle.innerHTML = " > " + selection.innerHTML;
    }
}

var randomizer = function (obj) {
    let random = Math.floor(1 + Math.random() * obj.childElementCount);
    child = obj.querySelector(':nth-child(' + random + ')');
    return child;

};

var musicEnded = function (e) {
    let playing = document.querySelectorAll('.playing');
    [].forEach.call(playing, function(el) {
        el.classList.remove("playing");
    });
};

setTimeout(function() {
    location. reload();
}, 60000);