document.addEventListener('DOMContentLoaded', () => {

    // Support both old and new stats sections
    const statsSections = document.querySelectorAll('.stats-grid, .stats-bento-section');
    if (statsSections.length === 0) return;

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.2
    };

    const animateStats = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {

                // 1. Animate Retention Circle (both small and large)
                const circles = entry.target.querySelectorAll('.circle');
                circles.forEach(circle => {
                    setTimeout(() => {
                        circle.style.strokeDasharray = "95, 100";
                    }, 300);
                });

                // 2. Animate Bars
                const bars = entry.target.querySelectorAll('.bar');
                bars.forEach((bar, index) => {
                    setTimeout(() => {
                        const height = bar.getAttribute('data-height');
                        bar.style.height = height;
                    }, index * 100); // Stagger effect
                });

                // 3. Animate Counter
                const counters = entry.target.querySelectorAll('.counter-anim');
                counters.forEach(counter => {
                    const target = parseInt(counter.getAttribute('data-target'));
                    const duration = 2000; // 2 seconds
                    const start = 0;
                    const startTime = performance.now();

                    const updateCounter = (currentTime) => {
                        const elapsed = currentTime - startTime;
                        const progress = Math.min(elapsed / duration, 1);

                        // Ease out quart
                        const ease = 1 - Math.pow(1 - progress, 4);

                        const current = Math.floor(ease * target);
                        counter.textContent = current;

                        if (progress < 1) {
                            requestAnimationFrame(updateCounter);
                        } else {
                            counter.textContent = target; // Ensure exact match
                        }
                    };

                    requestAnimationFrame(updateCounter);
                });

                // 4. Animate Clock
                const clocks = entry.target.querySelectorAll('.clock-hand');
                clocks.forEach(hand => {
                    setTimeout(() => {
                        hand.style.transform = "rotate(360deg)";
                    }, 200);
                });

                // 5. Animate Line Chart
                const chartLines = entry.target.querySelectorAll('.chart-line');
                chartLines.forEach(line => {
                    setTimeout(() => {
                        line.style.strokeDashoffset = "0";
                    }, 200);
                });

                const chartDots = entry.target.querySelectorAll('.chart-dot');
                chartDots.forEach(dot => {
                    dot.classList.add('visible');
                });

                // Stop observing after animation triggers
                observer.unobserve(entry.target);
            }
        });
    };

    const observer = new IntersectionObserver(animateStats, observerOptions);
    statsSections.forEach(section => observer.observe(section));

});
