let currentSlide = 0;
const slides = document.querySelectorAll('.card');
const totalSlides = slides.length;

function showSlide(index) {
    const slider = document.querySelector('.slider');
    if (index >= totalSlides) {
        currentSlide = 0;
    } else if (index < 0) {
        currentSlide = totalSlides - 1;
    } else {
        currentSlide = index;
    }

    // Update slider position
    slider.style.transform = `translateX(${-currentSlide * 50}%)`;

    // Update active card (remove blur)
    slides.forEach((slide, i) => {
        if (i === currentSlide) {
            slide.classList.add('active');
        } else {
            slide.classList.remove('active');
        }
    });
}

function nextSlide() {
    showSlide(currentSlide + 1);
}

function prevSlide() {
    showSlide(currentSlide - 1);
}

// Initialize the first slide as active
showSlide(currentSlide);