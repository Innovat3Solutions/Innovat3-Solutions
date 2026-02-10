/**
 * Simple Count Up Animation
 * Uses Intersection Observer to trigger animation when elements scroll into view.
 * 
 * Usage:
 * Add 'count-up' class to the element containing the number.
 * Use data attributes for configuration:
 * - data-target: The final number to count to (required)
 * - data-duration: Animation duration in ms (default: 2000)
 * - data-prefix: Text to prepend (e.g., "$")
 * - data-suffix: Text to append (e.g., "%", "+")
 * - data-decimals: Number of decimal places (default: 0)
 */

document.addEventListener('DOMContentLoaded', () => {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.2
    };

    const runCounter = (el) => {
        const target = parseFloat(el.getAttribute('data-target'));
        const duration = parseInt(el.getAttribute('data-duration') || '2000');
        const prefix = el.getAttribute('data-prefix') || '';
        const suffix = el.getAttribute('data-suffix') || '';
        const decimals = parseInt(el.getAttribute('data-decimals') || '0');

        // If target is not a number, just show the content and exit
        if (isNaN(target)) {
            el.style.opacity = 1;
            return;
        }

        const start = 0;
        const startTime = performance.now();

        // Set initial state
        el.style.opacity = 1;

        const animate = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);

            // Easing function: easeOutQuart
            const ease = 1 - Math.pow(1 - progress, 4);

            const current = start + (target - start) * ease;

            // Format number
            let formattedNumber = current.toFixed(decimals);

            // Add commas for thousands
            const parts = formattedNumber.split('.');
            parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            formattedNumber = parts.join('.');

            el.textContent = `${prefix}${formattedNumber}${suffix}`;

            if (progress < 1) {
                requestAnimationFrame(animate);
            } else {
                // Ensure final value is exact
                let finalFormatted = target.toFixed(decimals);
                const finalParts = finalFormatted.split('.');
                finalParts[0] = finalParts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                el.textContent = `${prefix}${finalParts.join('.')}${suffix}`;
            }
        };

        requestAnimationFrame(animate);
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                // Add a small delay for staggering if multiple items are in row
                // We rely on the CSS transition or just run it immediately
                runCounter(el);
                observer.unobserve(el);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.count-up').forEach(el => {
        // Hide initially to prevent flash of "0" before animation if desired, 
        // or just let it start from 0. 
        // Here we'll just let the script take over.
        observer.observe(el);
    });
});
