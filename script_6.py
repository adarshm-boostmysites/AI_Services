# Continue with the rest of the JavaScript file
remaining_js = """
    // Dark theme testimonials with enhanced animations
    setupDarkTestimonials() {
        const testimonialCards = document.querySelectorAll('.testimonial-card');
        const dots = document.querySelectorAll('.dot');
        
        if (testimonialCards.length === 0 || dots.length === 0) return;

        let isUserInteracting = false;

        // Dot navigation with neon effects
        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                this.showDarkTestimonial(index, testimonialCards, dots);
                this.currentTestimonial = index;
                isUserInteracting = true;
                this.restartTestimonialInterval();
                
                // Add click glow effect
                dot.style.boxShadow = '0 0 20px #00ffff';
                setTimeout(() => {
                    dot.style.boxShadow = '';
                }, 500);
                
                setTimeout(() => { isUserInteracting = false; }, 8000);
            });
        });

        // Auto-slide with dark theme transitions
        this.testimonialInterval = setInterval(() => {
            if (!isUserInteracting) {
                this.currentTestimonial = (this.currentTestimonial + 1) % testimonialCards.length;
                this.showDarkTestimonial(this.currentTestimonial, testimonialCards, dots);
            }
        }, 6000);

        // Touch/swipe support
        this.setupDarkSwipeGestures(testimonialCards, dots);

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (e.target.closest('.testimonials-container')) {
                if (e.key === 'ArrowLeft') {
                    this.currentTestimonial = this.currentTestimonial === 0 ? testimonialCards.length - 1 : this.currentTestimonial - 1;
                    this.showDarkTestimonial(this.currentTestimonial, testimonialCards, dots);
                    isUserInteracting = true;
                    this.restartTestimonialInterval();
                } else if (e.key === 'ArrowRight') {
                    this.currentTestimonial = (this.currentTestimonial + 1) % testimonialCards.length;
                    this.showDarkTestimonial(this.currentTestimonial, testimonialCards, dots);
                    isUserInteracting = true;
                    this.restartTestimonialInterval();
                }
            }
        });
    }

    showDarkTestimonial(index, cards, dots) {
        // Hide all cards with fade effect
        cards.forEach(card => {
            card.classList.remove('active');
            card.style.opacity = '0';
            card.style.transform = 'translateY(30px) scale(0.95)';
        });
        
        dots.forEach(dot => {
            dot.classList.remove('active');
            dot.style.boxShadow = '';
        });

        // Show selected card with enhanced animation
        setTimeout(() => {
            if (cards[index] && dots[index]) {
                cards[index].classList.add('active');
                cards[index].style.opacity = '1';
                cards[index].style.transform = 'translateY(0) scale(1)';
                dots[index].classList.add('active');
                dots[index].style.boxShadow = '0 0 15px #00ffff';
            }
        }, 200);
    }

    setupDarkSwipeGestures(cards, dots) {
        let startX = 0;
        let endX = 0;
        let startTime = 0;

        const container = document.querySelector('.testimonials-container');
        
        if (container) {
            container.addEventListener('touchstart', (e) => {
                startX = e.touches[0].clientX;
                startTime = Date.now();
            }, { passive: true });

            container.addEventListener('touchend', (e) => {
                endX = e.changedTouches[0].clientX;
                const timeDiff = Date.now() - startTime;
                
                if (timeDiff < 500) {
                    const threshold = 50;
                    const diff = startX - endX;

                    if (Math.abs(diff) > threshold) {
                        if (diff > 0) {
                            this.currentTestimonial = (this.currentTestimonial + 1) % cards.length;
                        } else {
                            this.currentTestimonial = this.currentTestimonial === 0 ? cards.length - 1 : this.currentTestimonial - 1;
                        }
                        this.showDarkTestimonial(this.currentTestimonial, cards, dots);
                        this.restartTestimonialInterval();
                    }
                }
            }, { passive: true });
        }
    }

    restartTestimonialInterval() {
        clearInterval(this.testimonialInterval);
        this.testimonialInterval = setInterval(() => {
            const cards = document.querySelectorAll('.testimonial-card');
            const dots = document.querySelectorAll('.dot');
            this.currentTestimonial = (this.currentTestimonial + 1) % cards.length;
            this.showDarkTestimonial(this.currentTestimonial, cards, dots);
        }, 6000);
    }

    // IMPROVED Dark theme scroll effects with navbar glassmorphism
    setupDarkScrollEffects() {
        let lastScrollY = window.scrollY;
        let ticking = false;
        
        const handleDarkScroll = () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    const navbar = document.getElementById('navbar');
                    const currentScrollY = window.scrollY;

                    if (navbar) {
                        // Enhanced navbar effects - keep navbar visible for better UX
                        if (currentScrollY > 50) {
                            navbar.classList.add('scrolled');
                        } else {
                            navbar.classList.remove('scrolled');
                        }

                        // Ensure navbar stays in position for navigation
                        navbar.style.transform = 'translateX(-50%) translateY(0)';
                    }

                    // ADDED: Force services visibility on scroll
                    if (currentScrollY > 100) {
                        this.ensureServicesVisibility();
                    }

                    lastScrollY = currentScrollY;
                    ticking = false;
                });
                ticking = true;
            }
        };

        window.addEventListener('scroll', handleDarkScroll, { passive: true });
    }

    // Dark theme mobile menu
    setupDarkMobileMenu() {
        const hamburger = document.getElementById('hamburger');
        const navMenu = document.getElementById('nav-menu');

        if (hamburger && navMenu) {
            hamburger.addEventListener('click', (e) => {
                e.stopPropagation();
                this.toggleDarkMobileMenu();
            });

            // Close menu when clicking outside
            document.addEventListener('click', (e) => {
                if (!hamburger.contains(e.target) && !navMenu.contains(e.target)) {
                    this.closeDarkMobileMenu();
                }
            });

            // Close menu on escape
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') {
                    this.closeDarkMobileMenu();
                }
            });

            // Close on window resize
            window.addEventListener('resize', this.debounce(() => {
                if (window.innerWidth > 768) {
                    this.closeDarkMobileMenu();
                }
            }, 250));
        }
    }

    toggleDarkMobileMenu() {
        const hamburger = document.getElementById('hamburger');
        const navMenu = document.getElementById('nav-menu');
        
        if (hamburger && navMenu) {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
            
            if (navMenu.classList.contains('active')) {
                document.body.style.overflow = 'hidden';
                navMenu.style.animation = 'fadeInNeon 0.3s ease';
            } else {
                document.body.style.overflow = '';
                navMenu.style.animation = 'fadeOutNeon 0.3s ease';
            }
        }
    }

    closeDarkMobileMenu() {
        const hamburger = document.getElementById('hamburger');
        const navMenu = document.getElementById('nav-menu');
        
        if (hamburger && navMenu) {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
            document.body.style.overflow = '';
        }
    }

    // IMPROVED Dark theme hero buttons with proper navigation
    setupDarkHeroButtons() {
        const exploreBtn = document.querySelector('.cta-primary');
        const portfolioBtn = document.querySelector('.cta-secondary');

        if (exploreBtn) {
            exploreBtn.addEventListener('click', (e) => {
                e.preventDefault();
                
                // Add neon pulse effect
                exploreBtn.style.animation = 'neonPulse 0.6s ease';
                setTimeout(() => {
                    exploreBtn.style.animation = '';
                }, 600);

                const servicesSection = document.querySelector('#services');
                if (servicesSection) {
                    const navbar = document.querySelector('.navbar');
                    const navbarHeight = navbar ? navbar.offsetHeight : 80;
                    const offset = navbarHeight + 60; // Increased offset
                    const targetPosition = servicesSection.offsetTop - offset;
                    this.smoothDarkScroll(targetPosition);
                    
                    // Ensure services are visible after scroll
                    setTimeout(() => {
                        this.ensureServicesVisibility();
                    }, 1000);
                }
            });
        }

        if (portfolioBtn) {
            portfolioBtn.addEventListener('click', (e) => {
                e.preventDefault();
                
                // Add neon glow effect
                portfolioBtn.style.boxShadow = '0 0 30px #00ffff, 0 10px 20px rgba(0, 0, 0, 0.3)';
                setTimeout(() => {
                    portfolioBtn.style.boxShadow = '';
                }, 600);

                const portfolioSection = document.querySelector('#portfolio');
                if (portfolioSection) {
                    const navbar = document.querySelector('.navbar');
                    const navbarHeight = navbar ? navbar.offsetHeight : 80;
                    const offset = navbarHeight + 60; // Increased offset
                    const targetPosition = portfolioSection.offsetTop - offset;
                    this.smoothDarkScroll(targetPosition);
                }
            });
        }
    }

    // Dark theme form validation
    setupDarkFormValidation() {
        const inputs = document.querySelectorAll('#user-name, #user-email, #service-select');
        const textarea = document.getElementById('project-description');

        inputs.forEach(input => {
            input.addEventListener('blur', () => {
                this.validateDarkField(input);
            });

            input.addEventListener('input', () => {
                this.clearDarkFieldError(input);
            });

            // Dark theme focus effects
            input.addEventListener('focus', () => {
                input.style.borderColor = '#00ffff';
                input.style.boxShadow = '0 0 0 3px rgba(0, 255, 255, 0.2)';
                input.style.background = 'rgba(255, 255, 255, 0.08)';
            });

            input.addEventListener('blur', () => {
                if (!input.classList.contains('error')) {
                    input.style.borderColor = '';
                    input.style.boxShadow = '';
                    input.style.background = 'rgba(255, 255, 255, 0.05)';
                }
            });
        });

        // Add character counter for textarea
        if (textarea) {
            this.addDarkCharacterCounter(textarea);
        }
    }

    validateDarkField(field) {
        const value = field.value.trim();
        let isValid = true;
        let errorMessage = '';

        this.clearDarkFieldError(field);

        if (field.hasAttribute('required') && !value) {
            isValid = false;
            errorMessage = 'This field is required';
        }

        if (field.type === 'email' && value) {
            const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
            if (!emailRegex.test(value)) {
                isValid = false;
                errorMessage = 'Please enter a valid email address';
            }
        }

        if (field.id === 'user-name' && value) {
            if (value.length < 2) {
                isValid = false;
                errorMessage = 'Name must be at least 2 characters long';
            }
        }

        if (!isValid) {
            this.showDarkFieldError(field, errorMessage);
        }

        return isValid;
    }

    showDarkFieldError(field, message) {
        field.classList.add('error');
        field.style.borderColor = '#ff00ff';
        field.style.boxShadow = '0 0 0 3px rgba(255, 0, 255, 0.2)';
        field.style.background = 'rgba(255, 0, 255, 0.05)';
        
        const errorElement = document.createElement('div');
        errorElement.className = 'dark-field-error';
        errorElement.textContent = message;
        errorElement.style.cssText = `
            color: #ff00ff;
            font-size: 12px;
            margin-top: 8px;
            animation: neonGlow 0.3s ease-in-out;
            text-shadow: 0 0 10px #ff00ff;
            font-weight: 500;
        `;
        
        field.parentElement.appendChild(errorElement);
    }

    clearDarkFieldError(field) {
        field.classList.remove('error');
        field.style.borderColor = '';
        field.style.boxShadow = '';
        field.style.background = 'rgba(255, 255, 255, 0.05)';
        
        const existingError = field.parentElement.querySelector('.dark-field-error');
        if (existingError) {
            existingError.remove();
        }
    }

    addDarkCharacterCounter(textarea) {
        const maxLength = 500;
        const counter = document.createElement('div');
        counter.className = 'dark-character-counter';
        counter.style.cssText = `
            font-size: 12px;
            color: rgba(255, 255, 255, 0.5);
            text-align: right;
            margin-top: 8px;
            font-weight: 500;
        `;
        
        textarea.parentElement.appendChild(counter);

        const updateCounter = () => {
            const remaining = maxLength - textarea.value.length;
            counter.textContent = `${remaining} characters remaining`;
            
            if (remaining < 50) {
                counter.style.color = '#ffff00';
                counter.style.textShadow = '0 0 5px #ffff00';
            } else if (remaining < 0) {
                counter.style.color = '#ff00ff';
                counter.style.textShadow = '0 0 5px #ff00ff';
            } else {
                counter.style.color = 'rgba(255, 255, 255, 0.5)';
                counter.style.textShadow = '';
            }
        };

        textarea.addEventListener('input', updateCounter);
        textarea.setAttribute('maxlength', maxLength);
        updateCounter();
    }

    // Dark theme animations and parallax
    setupDarkAnimations() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.animateDarkElement(entry.target);
                    
                    // Add stagger effect
                    if (entry.target.parentElement && 
                        (entry.target.parentElement.classList.contains('services-grid') ||
                         entry.target.parentElement.classList.contains('portfolio-grid'))) {
                        const siblings = Array.from(entry.target.parentElement.children);
                        const index = siblings.indexOf(entry.target);
                        entry.target.style.transitionDelay = `${index * 100}ms`;
                    }

                    // ADDED: Special handling for service cards
                    if (entry.target.classList.contains('service-card')) {
                        entry.target.style.display = 'block';
                        entry.target.style.visibility = 'visible';
                        entry.target.style.opacity = '1';
                    }
                }
            });
        }, {
            threshold: 0.2,
            rootMargin: '0px 0px -50px 0px'
        });

        // Observe elements for animation
        const elementsToAnimate = document.querySelectorAll('.service-card, .portfolio-item, .stat-card');
        elementsToAnimate.forEach(element => {
            this.prepareDarkElementForAnimation(element);
            observer.observe(element);
        });
    }

    prepareDarkElementForAnimation(element) {
        // Don't hide service cards completely
        if (element.classList.contains('service-card')) {
            element.style.opacity = '0.8';
            element.style.visibility = 'visible';
            element.style.display = 'block';
        } else {
            element.style.opacity = '0';
        }
        element.style.transform = 'translateY(50px) scale(0.9)';
        element.style.transition = 'all 0.8s cubic-bezier(0.16, 1, 0.3, 1)';
    }

    animateDarkElement(element) {
        element.style.opacity = '1';
        element.style.transform = 'translateY(0) scale(1)';
        
        // Add neon glow effect on animation
        setTimeout(() => {
            element.style.boxShadow = '0 10px 30px rgba(0, 255, 255, 0.1)';
            setTimeout(() => {
                element.style.boxShadow = '';
            }, 1000);
        }, 400);
    }

    setupDarkParallax() {
        let ticking = false;

        const handleDarkParallax = () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    const scrolled = window.pageYOffset;
                    
                    // Floating shapes parallax
                    const shapes = document.querySelectorAll('.floating-shape');
                    shapes.forEach((shape, index) => {
                        const speed = 0.2 + (index * 0.1);
                        const yPos = -(scrolled * speed);
                        const rotation = scrolled * 0.02 + (index * 45);
                        shape.style.transform = `translateY(${yPos}px) rotate(${rotation}deg)`;
                    });

                    // Neon orbs parallax
                    const orbs = document.querySelectorAll('.neon-orb');
                    orbs.forEach((orb, index) => {
                        const speed = 0.1 + (index * 0.05);
                        const yPos = -(scrolled * speed);
                        orb.style.transform = `translateY(${yPos}px) scale(${1 + scrolled * 0.0001})`;
                    });

                    ticking = false;
                });
                ticking = true;
            }
        };

        window.addEventListener('scroll', handleDarkParallax, { passive: true });
    }

    // Dark theme counters with neon effects
    setupDarkCounters() {
        const statNumbers = document.querySelectorAll('.stat-number');
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.animateDarkCounter(entry.target);
                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.8 });

        statNumbers.forEach(number => {
            counterObserver.observe(number);
        });
    }

    animateDarkCounter(element) {
        const text = element.textContent;
        const hasPlus = text.includes('+');
        const hasPercent = text.includes('%');
        const isTime = text.includes('/');
        
        if (isTime) return;

        const finalValue = parseInt(text.replace(/[^\\d]/g, ''));
        if (isNaN(finalValue)) return;

        const duration = 2000;
        const steps = 60;
        const stepValue = finalValue / steps;
        const stepDuration = duration / steps;

        let currentValue = 0;
        const timer = setInterval(() => {
            currentValue += stepValue;
            if (currentValue >= finalValue) {
                currentValue = finalValue;
                clearInterval(timer);
                
                // Add final neon glow effect
                element.style.textShadow = '0 0 20px currentColor, 0 0 30px currentColor';
                setTimeout(() => {
                    element.style.textShadow = '';
                }, 2000);
            }
            
            let displayValue = Math.floor(currentValue);
            if (hasPlus) displayValue += '+';
            if (hasPercent) displayValue += '%';
            
            element.textContent = displayValue;
        }, stepDuration);
    }

    // Add dynamic dark theme CSS animations
    addDarkThemeStyles() {
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideInNeon {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }

            @keyframes slideOutNeon {
                from {
                    transform: translateX(0);
                    opacity: 1;
                }
                to {
                    transform: translateX(100%);
                    opacity: 0;
                }
            }

            @keyframes neonGlow {
                0%, 100% { text-shadow: 0 0 5px currentColor; }
                50% { text-shadow: 0 0 20px currentColor, 0 0 30px currentColor; }
            }

            @keyframes neonPulse {
                0%, 100% { box-shadow: 0 0 20px rgba(0, 255, 255, 0.3); }
                50% { box-shadow: 0 0 40px rgba(0, 255, 255, 0.6), 0 0 60px rgba(0, 255, 255, 0.4); }
            }

            @keyframes fadeInNeon {
                from {
                    opacity: 0;
                    backdrop-filter: blur(0px);
                }
                to {
                    opacity: 1;
                    backdrop-filter: blur(20px);
                }
            }

            @keyframes fadeOutNeon {
                from {
                    opacity: 1;
                    backdrop-filter: blur(20px);
                }
                to {
                    opacity: 0;
                    backdrop-filter: blur(0px);
                }
            }

            /* Enhanced scrollbar */
            ::-webkit-scrollbar-thumb:active {
                background: linear-gradient(135deg, #ffff00, #ff00ff);
            }

            /* Dark theme focus enhancements */
            .btn:focus-visible {
                outline: 2px solid #00ffff;
                outline-offset: 3px;
                box-shadow: 0 0 20px rgba(0, 255, 255, 0.4);
            }

            /* Mobile menu dark enhancements */
            @media (max-width: 768px) {
                .nav-menu.active {
                    border: 1px solid rgba(0, 255, 255, 0.3);
                    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5), inset 0 0 50px rgba(0, 255, 255, 0.05);
                }
            }

            /* Enhanced navbar positioning */
            .navbar {
                transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
            }

            /* FORCED Services Section Visibility */
            #services {
                display: block !important;
                visibility: visible !important;
                opacity: 1 !important;
            }

            #services .services-grid {
                display: grid !important;
                visibility: visible !important;
                opacity: 1 !important;
            }

            #services .service-card {
                display: block !important;
                visibility: visible !important;
                opacity: 1 !important;
            }
        `;
        document.head.appendChild(style);
    }

    // Utility functions
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
}

// Initialize the dark theme landing page
document.addEventListener('DOMContentLoaded', () => {
    const landing = new DarkThemeAILanding();
    
    // ADDED: Additional fallback to ensure services visibility
    setTimeout(() => {
        landing.ensureServicesVisibility();
    }, 1000);
    
    // ADDED: Periodic check for services visibility
    setInterval(() => {
        const servicesSection = document.getElementById('services');
        if (servicesSection && (servicesSection.style.display === 'none' || 
            servicesSection.style.visibility === 'hidden' || 
            servicesSection.style.opacity === '0')) {
            landing.ensureServicesVisibility();
        }
    }, 5000);
});

// Fallback for immediate execution
if (document.readyState === 'complete') {
    const landing = new DarkThemeAILanding();
    setTimeout(() => {
        landing.ensureServicesVisibility();
    }, 500);
}
"""

# Append to the JavaScript file
with open('app_fixed.js', 'a', encoding='utf-8') as f:
    f.write(remaining_js)

print("Completed the fixed JavaScript file with enhanced Services section visibility and improved scroll navigation")