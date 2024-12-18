//for better performance in front page , no important scripts

// Smooth scrolling function
document.querySelectorAll('a[href^="#intro"]').forEach(anchor => {
anchor.addEventListener('click', function (e) {
    e.preventDefault();

    document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth',
        block: 'start', // Scroll to the start of the target element
        inline: 'start' // Scroll to the start of the target element
    });
});
});

document.querySelectorAll('a[href^="#about"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
      e.preventDefault();

      document.querySelector(this.getAttribute('href')).scrollIntoView({
          behavior: 'smooth',
          block: 'start', // Scroll to the start of the target element
          inline: 'start' // Scroll to the start of the target element
      });
  });
});

document.querySelectorAll('a[href^="#contact"]').forEach(anchor => {
anchor.addEventListener('click', function (e) {
    e.preventDefault();

    document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth',
        block: 'start', // Scroll to the start of the target element
        inline: 'start' // Scroll to the start of the target element
    });
});
});

document.querySelectorAll('a[href^="#home"]').forEach(anchor => {
anchor.addEventListener('click', function (e) {
    e.preventDefault();

    document.querySelector('body').scrollIntoView({
        behavior: 'smooth',
        block: 'start', // Scroll to the start of the target element
        inline: 'start' // Scroll to the start of the target element
    });
});
});

//**********************************************//


function startWebcam() {
    const videoElement = document.getElementById("webcam");
    // Check if the video element exists
    if (!videoElement) {
        console.error("Video element not found!");
        return;
    }

    navigator.mediaDevices
        .getUserMedia({ video: true })
        .then((stream) => {
            videoElement.srcObject = stream; // Attach stream to video element
        })
        .catch((err) => {
            console.error("Webcam access denied!", err);
        });
}