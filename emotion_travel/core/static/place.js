//for better performance in front page , no important scripts

// Smooth scrolling function
document.querySelectorAll('a[href^="#intro"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth",
            block: "start", // Scroll to the start of the target element
            inline: "start", // Scroll to the start of the target element
        });
    });
});

document.querySelectorAll('a[href^="#about"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth",
            block: "start", // Scroll to the start of the target element
            inline: "start", // Scroll to the start of the target element
        });
    });
});

document.querySelectorAll('a[href^="#contact"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth",
            block: "start", // Scroll to the start of the target element
            inline: "start", // Scroll to the start of the target element
        });
    });
});

document.querySelectorAll('a[href^="#home"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();

        document.querySelector("body").scrollIntoView({
            behavior: "smooth",
            block: "start", // Scroll to the start of the target element
            inline: "start", // Scroll to the start of the target element
        });
    });
});

// *******************************************************

// for next and prev button 
let currentCard = 0;
const cards = document.querySelectorAll('.name-img');
const totalCards = cards.length;

function showCard(index) {
    const card = document.querySelector('.card');
    if (index >= totalCards) {
        currentCard = 0;
    } else if (index < 0) {
        currentCard = totalCards - 1;
    } else {
        currentCard = index;
    }

    // Calculate the translation distance
    const cardWidth = cards[0].offsetWidth; // Get the width of a single card
    const marginRight = 10; // Margin between cards (from CSS)
    const translateXValue = -currentCard * (cardWidth + marginRight); // Adjust for card width and margin
    card.style.transform = `translateX(${translateXValue}px)`;

    console.log(translateXValue)
    console.log(currentCard)
    // Update active card (remove blur)
    cards.forEach((c, i) => {
        if (i === currentCard) {
            c.classList.add('active');
        } else {
            c.classList.remove('active');
        }
    });
}

// Event listeners for buttons
document.querySelector('.next').addEventListener('click', () => {
    showCard(currentCard + 1);
});

document.querySelector('.prev').addEventListener('click', () => {
    showCard(currentCard - 1);
});


// Initialize the first card as active
showCard(currentCard);
