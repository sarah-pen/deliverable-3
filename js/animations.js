document.addEventListener("DOMContentLoaded", function() {

    // Fade-in effect for gallery images
    const images = document.querySelectorAll("#gallery img");

    // Observer for images to apply fade-in effect when in view
    const imageObserver = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");  
                observer.unobserve(entry.target);       
            }
        });
    }, { threshold: 0.1 });

    // Observe each image in the gallery
    images.forEach(image => {
        imageObserver.observe(image);
    });

    // Fade-in effect for table rows in #all-meets section
    const rows = document.querySelectorAll("#all-meets tbody tr");

    // Observer for table rows to apply fade-in effect when in view
    const rowObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");  
            }
        });
    }, { threshold: 0.1 });

    // Add 'fade-in-row' class to each row and observe them
    rows.forEach(row => {
        row.classList.add("fade-in-row"); 
        rowObserver.observe(row);
    });

    // Fade-in effect for athlete results
    const observerOptions = {
        threshold: 0.1  
    };

    // Callback function for athlete results observer
    const fadeInOnScroll = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("fade-in");  
                observer.unobserve(entry.target);      
            }
        });
    };

    // Observer for athlete results
    const observer = new IntersectionObserver(fadeInOnScroll, observerOptions);

    // Observe each element with the class 'athlete-result'
    document.querySelectorAll(".athlete-result").forEach(athlete => {
        observer.observe(athlete);
    });
});

// Scroll-to-top button functionality

// Get the button element by ID
let mybutton = document.getElementById("button-to-top");

// Show the button when the user scrolls down 40px from the top of the document
window.onscroll = function() { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
        mybutton.style.display = "block";  
    } else {
        mybutton.style.display = "none";  
    }
}

// Scroll to the top of the document when the button is clicked
function topFunction() {
    document.body.scrollTop = 0;        
    document.documentElement.scrollTop = 0; 
}
