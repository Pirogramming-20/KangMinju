const container = document.querySelector('.container');
const overlay = document.querySelector('.overlay');

container.addEventListener('mousemove', function(e){
    const x = e.offsetX
    const y = e.offsetY
    const rotateY = -1/10 * x + 20
    const rotateX = 4/30 * y - 20

    overlay.style = `background-position: ${x/5+y/5}%`

    container.style= `transform : perspective(350px) 
    rotateX(${rotateX}deg) rotateY(${rotateY}deg)`
});
container.addEventListener('mouseout', function(){
    overlay.style = `filter : opacity(0)`

    container.style= `transform : perspective(350px) 
    rotateX(0deg) rotateY(0deg)`
});

const btn = document.querySelector('.signup1-btn');
container.addEventListener('click', function(){
    btn.click();
});