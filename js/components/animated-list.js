/**
 * Animated List Component
 * Inspired by Magic UI's AnimatedList
 * Creates a staggered spring animation effect for list items
 */

document.addEventListener('DOMContentLoaded', () => {
    const animatedContainers = document.querySelectorAll('.animated-list-container');

    if (animatedContainers.length === 0) return;

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -50px 0px', // Trigger slightly before fully in view
        threshold: 0.1
    };

    const animateList = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const container = entry.target;

                // Get all items to animate
                let items = container.querySelectorAll('.animated-item');

                // Fallback to direct children if no items marked
                if (items.length === 0) {
                    items = Array.from(container.children);
                    items.forEach(item => item.classList.add('animated-item'));
                }

                // Stagger delay configuration
                const baseDelay = 100; // ms between each item
                const maxDelay = 800;  // Maximum total delay

                items.forEach((item, index) => {
                    // Calculate delay with diminishing returns for many items
                    const delay = Math.min(index * baseDelay, maxDelay);

                    setTimeout(() => {
                        item.classList.add('visible');
                    }, delay);
                });

                // Stop observing after animation triggered
                observer.unobserve(container);
            }
        });
    };

    const observer = new IntersectionObserver(animateList, observerOptions);

    // Observe all containers
    animatedContainers.forEach(container => {
        observer.observe(container);
    });
});
