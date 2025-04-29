let currentIndex = 0;
        const slides = document.querySelectorAll(".content-wrapper");
        const slider = document.querySelector(".slider");
        
        function nextSlide() {
            currentIndex = (currentIndex + 1) % slides.length;
            slider.style.opacity = 0;
            setTimeout(() => {
                slider.style.transform = `translateX(-${currentIndex * 100}%)`;
            }, 500);
            setTimeout(() => {
                slider.style.opacity = 1;
            }, 1000);
        }
        
        setInterval(nextSlide,10000);