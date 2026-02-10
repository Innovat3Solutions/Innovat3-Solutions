document.addEventListener('DOMContentLoaded', () => {
    // 1. Navbar Scroll Effect
    const navbar = document.getElementById('navbar');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.padding = '8px 0';
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = '0 4px 6px -1px rgba(0,0,0,0.1)';
        } else {
            navbar.style.padding = 'var(--spacing-md) 0';
            navbar.style.background = 'rgba(255, 255, 255, 0.8)';
            navbar.style.boxShadow = 'none';
        }
    });

    // 2. Mobile Menu Toggle - FULLY FUNCTIONAL
    const mobileBtn = document.querySelector('.mobile-toggle');
    const navLinks = document.querySelector('.nav-links');
    const body = document.body;

    if (mobileBtn && navLinks) {
        // Toggle mobile menu
        mobileBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            mobileBtn.classList.toggle('active');
            navLinks.classList.toggle('active');

            // Prevent body scroll when menu is open
            if (navLinks.classList.contains('active')) {
                body.style.overflow = 'hidden';
            } else {
                body.style.overflow = '';
            }
        });

        // Handle dropdown clicks in mobile menu
        const dropdownTriggersInNav = navLinks.querySelectorAll('.dropdown-trigger');
        dropdownTriggersInNav.forEach(trigger => {
            trigger.addEventListener('click', (e) => {
                if (window.innerWidth <= 767) {
                    e.preventDefault();
                    const dropdown = trigger.nextElementSibling;
                    if (dropdown && dropdown.classList.contains('dropdown-menu')) {
                        dropdown.classList.toggle('active');

                        // Close other dropdowns
                        navLinks.querySelectorAll('.dropdown-menu').forEach(menu => {
                            if (menu !== dropdown) {
                                menu.classList.remove('active');
                            }
                        });
                    }
                }
            });
        });

        // Close menu when clicking on a regular link (not dropdown)
        navLinks.querySelectorAll('a:not(.dropdown-trigger)').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 767) {
                    mobileBtn.classList.remove('active');
                    navLinks.classList.remove('active');
                    body.style.overflow = '';
                }
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (window.innerWidth <= 767 &&
                navLinks.classList.contains('active') &&
                !e.target.closest('.nav-links') &&
                !e.target.closest('.mobile-toggle')) {
                mobileBtn.classList.remove('active');
                navLinks.classList.remove('active');
                body.style.overflow = '';
            }
        });

        // Close menu on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && navLinks.classList.contains('active')) {
                mobileBtn.classList.remove('active');
                navLinks.classList.remove('active');
                body.style.overflow = '';
            }
        });

        // Reset menu state on window resize
        window.addEventListener('resize', () => {
            if (window.innerWidth > 767) {
                mobileBtn.classList.remove('active');
                navLinks.classList.remove('active');
                body.style.overflow = '';
                // Close all dropdowns
                navLinks.querySelectorAll('.dropdown-menu').forEach(menu => {
                    menu.classList.remove('active');
                });
            }
        });
    }

    // 3. Tab System for Niches
    const tabs = document.querySelectorAll('.tab');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active from all
            tabs.forEach(t => t.classList.remove('active'));
            // Add to clicked
            tab.classList.add('active');

            // In a real app, filter the .niche-showcase contents
            // For now, we just toggle the UI state
        });
    });

    // 4. Smooth Anchor Scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // 5. Hero Text Carousel
    const words = document.querySelectorAll('.carousel-word');
    let currentIndex = 0;

    if (words.length > 0) {
        setInterval(() => {
            // CURRENT WORD: exit wrap
            const currentWord = words[currentIndex];
            currentWord.classList.remove('active');
            currentWord.classList.add('exit');

            // Wait for transition to complete before resetting position
            setTimeout(() => {
                currentWord.classList.remove('exit');
            }, 500);

            // NEXT WORD
            currentIndex = (currentIndex + 1) % words.length;
            const nextWord = words[currentIndex];
            nextWord.classList.add('active');

        }, 2500); // Change every 2.5 seconds
    }
    // 6. Number Counter Animation (Bento Grid)
    const counters = document.querySelectorAll('.counter');
    const speed = 200; // The lower the slower

    const animateCounters = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = +counter.getAttribute('data-target');
                const count = +counter.innerText.replace(/,/g, ''); // Remove commas

                const inc = target / speed;

                const updateCount = () => {
                    const c = +counter.innerText.replace(/,/g, '');
                    if (c < target) {
                        counter.innerText = Math.ceil(c + inc).toLocaleString();
                        setTimeout(updateCount, 20);
                    } else {
                        counter.innerText = target.toLocaleString();
                    }
                };

                updateCount();
                observer.unobserve(counter);
            }
        });
    };

    const counterObserver = new IntersectionObserver(animateCounters, {
        threshold: 0.5
    });

    counters.forEach(counter => {
        counterObserver.observe(counter);
    });

    // 7. Flickering Grid
    if (typeof FlickeringGrid !== 'undefined') {
        new FlickeringGrid('.cta-box', {
            color: '132, 204, 22', // #84CC16
            squareSize: 4,
            gridGap: 5,
            flickerChance: 0.4,
            maxOpacity: 0.4
        });

        // Ensure content is above canvas
        const ctaContent = document.querySelector('.cta-content');
        if (ctaContent) {
            ctaContent.style.position = 'relative';
            ctaContent.style.zIndex = '2';
        }
        const ctaImage = document.querySelector('.cta-image');
        if (ctaImage) {
            ctaImage.style.position = 'relative';
            ctaImage.style.zIndex = '2';
        }
    }

    // 8. Stats Rolling Animation (Scale up with scroll)
    const statNumbers = document.querySelectorAll('.stat-big .number');

    const animateStats = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const element = entry.target;
                const rawText = element.innerText;

                // Parse suffix and value
                let value = 0;
                let suffix = '';

                if (rawText.includes('%')) {
                    value = parseInt(rawText);
                    suffix = '%';
                } else if (rawText.includes('+')) {
                    value = parseInt(rawText);
                    suffix = '+';
                } else if (rawText.includes('K')) {
                    value = parseInt(rawText);
                    suffix = 'K'; // Handle "10K" -> 10 + K
                } else {
                    value = parseInt(rawText.replace(/,/g, ''));
                }

                if (isNaN(value)) return;

                // Animate
                const duration = 2000;
                const startTime = performance.now();

                const step = (currentTime) => {
                    const elapsed = currentTime - startTime;
                    const progress = Math.min(elapsed / duration, 1);
                    // Ease out quart
                    const ease = 1 - Math.pow(1 - progress, 4);

                    const currentVal = Math.floor(ease * value);
                    element.innerText = currentVal + suffix;

                    if (progress < 1) {
                        requestAnimationFrame(step);
                    } else {
                        element.innerText = value + suffix; // Ensure final value
                    }
                };

                requestAnimationFrame(step);
                observer.unobserve(element);
            }
        });
    };

    const statsObserver = new IntersectionObserver(animateStats, {
        threshold: 0.5
    });

    statNumbers.forEach(stat => {
        statsObserver.observe(stat);
    });

    // 9. Niche View All Dropdown Toggle (DESKTOP ONLY)
    // Converted to generic dropdown toggle for click behavior
    // Mobile is handled separately above (lines 37-56)
    const dropdownTriggers = document.querySelectorAll('.dropdown-trigger, .niche-dropdown-trigger');

    dropdownTriggers.forEach(trigger => {
        trigger.addEventListener('click', (e) => {
            // Skip on mobile - handled by the mobile-specific handler above
            if (window.innerWidth <= 767) {
                return;
            }

            const dropdown = trigger.nextElementSibling;

            if (dropdown) {
                e.preventDefault();
                e.stopPropagation();

                // Close other open dropdowns (accordian style behavior optional, but good for UX)
                document.querySelectorAll('.dropdown-menu.active').forEach(openMenu => {
                    if (openMenu !== dropdown) {
                        openMenu.classList.remove('active');
                    }
                });

                dropdown.classList.toggle('active');
            }
        });
    });

    // Close on click outside
    document.addEventListener('click', (e) => {
        // Close all dropdowns if click is outside
        if (!e.target.closest('.nav-item.dropdown')) {
            document.querySelectorAll('.dropdown-menu.active').forEach(menu => {
                menu.classList.remove('active');
            });
        }
    });

    // Close on Escape
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            document.querySelectorAll('.dropdown-menu.active').forEach(menu => {
                menu.classList.remove('active');
            });
        }
    });

    // 10. Multi-Step Form Logic
    const initMultiStepForm = () => {
        const form = document.getElementById('consultationForm');
        if (!form) return;

        const steps = Array.from(form.querySelectorAll('.form-step'));
        const progressBar = document.getElementById('progressBar');
        const stepIndicator = document.getElementById('stepIndicator');
        const totalSteps = steps.length;
        let currentStepIndex = 0; // 0-based index

        // Helper to update UI
        const updateUI = (newIndex) => {
            // Toggle visibility
            steps.forEach((step, index) => {
                if (index === newIndex) {
                    step.classList.add('active');
                    // Add animation class if moving forward
                    step.style.animation = 'fadeIn 0.5s ease forwards';
                } else {
                    step.classList.remove('active');
                    step.style.animation = 'none';
                }
            });

            // Update Progress
            const progress = ((newIndex + 1) / totalSteps) * 100;
            if (progressBar) progressBar.style.width = `${progress}%`;

            // Update Indicator
            if (stepIndicator) stepIndicator.innerText = `${newIndex + 1}/${totalSteps}`;

            currentStepIndex = newIndex;
        };

        // Helper to Validate
        const validateCurrentStep = () => {
            const currentStepEl = steps[currentStepIndex];
            const inputs = currentStepEl.querySelectorAll('input, textarea');
            let isValid = true;

            inputs.forEach(input => {
                if (input.hasAttribute('required') && !input.value.trim()) {
                    isValid = false;
                    input.style.borderColor = '#ef4444'; // Red error
                    input.classList.add('shake-error'); // Optional: Add CSS for shake

                    // Reset on input
                    input.addEventListener('input', () => {
                        input.style.borderColor = '';
                        input.classList.remove('shake-error');
                    }, { once: true });
                }
            });

            return isValid;
        };

        // Attach Event Listeners to Buttons
        form.addEventListener('click', (e) => {
            const btn = e.target.closest('button');
            if (!btn) return;

            if (btn.classList.contains('next-btn')) {
                e.preventDefault(); // Prevent submit if it's a next button
                if (validateCurrentStep()) {
                    if (currentStepIndex < totalSteps - 1) {
                        updateUI(currentStepIndex + 1);
                    }
                }
            } else if (btn.classList.contains('prev-btn') || btn.innerText.includes('Back')) {
                e.preventDefault();
                if (currentStepIndex > 0) {
                    updateUI(currentStepIndex - 1);
                }
            }
        });

        // Handle Enter Key for inputs (prevent submit, trigger next)
        form.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && e.target.tagName !== 'TEXTAREA') {
                e.preventDefault();
                const nextBtn = steps[currentStepIndex].querySelector('.next-btn');
                if (nextBtn) nextBtn.click();
            }
        });

        // Submit Handler
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = form.querySelector('button[type="submit"]');
            const originalHTML = btn.innerHTML;

            btn.innerHTML = 'Booking...';
            btn.disabled = true;
            btn.style.opacity = '0.7';

            // Simulate API Call
            setTimeout(() => {
                // Determine success message based on niche (optional)
                alert("Strategy Call Request Received! We'll be in touch with your customized plan shortly.");
                btn.innerHTML = 'Booked!';
                btn.style.background = '#84cc16'; // Success Green
                btn.style.color = '#fff';

                // Reset form after delay
                setTimeout(() => {
                    form.reset();
                    btn.innerHTML = originalHTML;
                    btn.disabled = false;
                    btn.style.opacity = '1';
                    btn.style.background = '';
                    btn.style.color = '';
                    updateUI(0);
                }, 3000);
            }, 1500);
        });
    };

    initMultiStepForm();

});
