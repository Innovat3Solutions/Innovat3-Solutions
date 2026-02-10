/**
 * Story Timeline Animation
 * Horizontal animated timeline with staggered reveal
 */

document.addEventListener('DOMContentLoaded', () => {
    const timelineSection = document.querySelector('.story-timeline-section');
    const timelineProgress = document.querySelector('.timeline-progress');
    const timelineNodes = document.querySelectorAll('.timeline-node');

    if (!timelineSection) return;

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -100px 0px',
        threshold: 0.2
    };

    const animateTimeline = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Animate progress line
                if (timelineProgress) {
                    setTimeout(() => {
                        timelineProgress.classList.add('animated');
                    }, 200);
                }

                // Stagger animate each node
                timelineNodes.forEach((node, index) => {
                    setTimeout(() => {
                        node.classList.add('visible');
                    }, 400 + (index * 200)); // 200ms delay between each node
                });

                // Stop observing after animation triggered
                observer.unobserve(entry.target);
            }
        });
    };

    const observer = new IntersectionObserver(animateTimeline, observerOptions);
    observer.observe(timelineSection);

    // Re-initialize Lucide icons for dynamically loaded content
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
});
