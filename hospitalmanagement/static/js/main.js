 document.addEventListener("DOMContentLoaded", function() {
        var myCarousel = document.querySelector("#home-carousel");
        var carousel = new bootstrap.Carousel(myCarousel, {
            interval: 3000,  // Auto-slide every 3 seconds
            pause: "hover"   // Pause when hovering
        });
    });
