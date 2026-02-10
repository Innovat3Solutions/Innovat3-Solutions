/* Story Timeline Component Logic */

document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.timeline-slide');
    const prevBtn = document.getElementById('timeline-prev');
    const nextBtn = document.getElementById('timeline-next');

    if (!slides.length) return;

    let currentIndex = 0;
    const totalSlides = slides.length;

    function updateSlide(index) {
        // Remove active class from all slides
        slides.forEach(slide => {
            slide.classList.remove('active');
        });

        // Add active class to current slide
        slides[index].classList.add('active');

        // Update buttons text/visibility if needed (optional)
        // For now, we'll loop or just clamp. Let's clamp for a timeline feel.

        // Update Next Button Text
        if (index < totalSlides - 1) {
            const nextYear = slides[index + 1].getAttribute('data-year');
            nextBtn.innerHTML = `${nextYear} <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>`;
            nextBtn.style.display = 'flex';
        } else {
            nextBtn.style.display = 'none';
        }

        // Update Prev Button Text
        if (index > 0) {
            const prevYear = slides[index - 1].getAttribute('data-year');
            prevBtn.innerHTML = `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg> ${prevYear}`;
            prevBtn.style.display = 'flex';
        } else {
            prevBtn.style.display = 'none';
        }
    }

    // Initialize
    updateSlide(currentIndex);

    // Event Listeners
    nextBtn.addEventListener('click', () => {
        if (currentIndex < totalSlides - 1) {
            currentIndex++;
            updateSlide(currentIndex);
        }
    });

    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateSlide(currentIndex);
        }
    });
});
