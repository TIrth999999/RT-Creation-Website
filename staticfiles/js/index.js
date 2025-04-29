let slides = Array.from(document.getElementsByClassName("content-wrapper"));
let counter = 0;

const goNext = () => {
    counter++;
    if(counter >= slides.length){
        counter=0;
        slideImg();
    }
    else{
        slideImg();
    }
};

slides.forEach(
    (x,index)=>{
        x.style.left = `${index*100}%`;
    }
);

setInterval(goNext, 3000);
const slideImg = ()=>{
    slides.forEach(
        (x) => {
            x.style.transform = `translateX(-${counter*100}%)`;
        }
    )
};
