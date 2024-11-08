document.addEventListener("DOMContentLoaded", function() {
    // Fade-in effect for images
    const images = document.querySelectorAll("#gallery img");

    const imageObserver = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target); // Optional: Stop observing after it fades in
            }
        });
    }, { threshold: 0.1 });

    images.forEach(image => {
        imageObserver.observe(image);
    });

    // Fade-in effect for table rows
    const rows = document.querySelectorAll("#all-meets tbody tr");

    const rowObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
            }
        });
    }, { threshold: 0.1 });

    rows.forEach(row => {
        row.classList.add("fade-in-row");
        rowObserver.observe(row);
    });

    // Fade-in effect for athlete results
    const observerOptions = {
        threshold: 0.1
    };

    const fadeInOnScroll = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("fade-in");
                observer.unobserve(entry.target); // Stop observing once element is in view
            }
        });
    };

    const observer = new IntersectionObserver(fadeInOnScroll, observerOptions);

    document.querySelectorAll(".athlete-result").forEach(athlete => {
        observer.observe(athlete);
    });
});

// Get the button:
let mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

