document.addEventListener('DOMContentLoaded', () => {

    // Select all containers marked for animation
    const animatedContainers = document.querySelectorAll('.animated-list-container');

    if (animatedContainers.length === 0) return;

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15 // Trigger when 15% of the container is visible
    };

    const animateList = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const container = entry.target;
                container.classList.add('visible');

                // Find all direct children marked as animated items, or default to all direct children if none marked
                let items = container.querySelectorAll('.animated-item');

                // If no specific items marked, assume all direct children
                if (items.length === 0) {
                    items = Array.from(container.children);
                }

                items.forEach((item, index) => {
                    // Stagger delay: 150ms between each item
                    setTimeout(() => {
                        item.classList.add('visible');
                        item.classList.add('animated-item'); // Ensure class exists if fallback used
                    }, index * 150);
                });

                // Stop observing after firing
                observer.unobserve(container);
            }
        });
    };

    const observer = new IntersectionObserver(animateList, observerOptions);
    animatedContainers.forEach(container => observer.observe(container));
});
