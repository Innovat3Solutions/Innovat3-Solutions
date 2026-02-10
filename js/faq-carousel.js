
document.addEventListener('DOMContentLoaded', () => {
    const track = document.querySelector('.faq-track');
    const cards = Array.from(document.querySelectorAll('.faq-card'));
    const prevBtn = document.querySelector('.faq-nav-btn.prev');
    const nextBtn = document.querySelector('.faq-nav-btn.next');

    let currentIndex = 0; // The index of the active card

    // Initialize: Set the first card as active
    updateCarousel(currentIndex);

    // Click handler for individual cards
    cards.forEach((card, index) => {
        card.addEventListener('click', () => {
            currentIndex = index;
            updateCarousel(currentIndex);
        });
    });

    // Navigation Buttons
    nextBtn.addEventListener('click', () => {
        if (currentIndex < cards.length - 1) {
            currentIndex++;
            updateCarousel(currentIndex);
        } else {
            // Optional: Loop back to start
            currentIndex = 0;
            updateCarousel(currentIndex);
        }
    });

    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateCarousel(currentIndex);
        } else {
            // Optional: Loop to end
            currentIndex = cards.length - 1;
            updateCarousel(currentIndex);
        }
    });

    function updateCarousel(index) {
        // 1. Update active class
        cards.forEach(c => c.classList.remove('active'));
        cards[index].classList.add('active');

        // 2. Center the active card in the view
        // We want the active card centered. 
        // Calculate transparent offset:
        // center of track = (card width / 2) + (index * (card width + gap))
        // We want to translate track so that 'center of track' aligns with 'center of container'

        // Simplified Logic:
        // Card Width = 320px (inactive), roughly. 380px (active).
        // Let's assume a standard step size for simplicity or calculate dynamically.

        const cardWidth = 320;
        const gap = 32; // 2rem

        // This calculation is a bit tricky with variable widths (active vs inactive).
        // Let's use getBoundingClientRect for precision if we weren't doing a pure CSS transform logic.
        // For smoother performace, let's assume the center point moves by (320 + 32) per index.

        // However, the active card is WIDER (380px).
        // So the offset depends on WHICH card is active. 
        // Actually, CSS flex layout handles the widths. We just need to shift the track.

        // Let's rely on centering the target element.

        if (window.innerWidth > 768) {
            // Desktop Transform Logic
            // We want the center of the active card to be at the center of the wrapper.
            // wrapper width / 2

            const wrapper = document.querySelector('.faq-carousel-wrapper');
            const wrapperCenter = wrapper.offsetWidth / 2;

            // Calculate distance to center of active card from start of track
            // We can sum widths of previous cards + gaps + half of active card

            let distance = 0;
            for (let i = 0; i < index; i++) {
                distance += 320 + 32; // Inactive width + gap
            }
            distance += 380 / 2; // Half of active width

            // Wait, this assumes all previous are inactive.
            // But when we click one, it becomes active.
            // So mechanically, the track is: [Inactive][Inactive][ACTIVE][Inactive]

            // The transform should simply shift the track so the active one is centered.
            // transformX = wrapperCenter - distance

            const offset = wrapperCenter - distance;
            track.style.transform = `translateX(${offset}px)`;
        } else {
            // Mobile: Scroll into view
            cards[index].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
        }
    }
});
