// Fixed Adarsh M - AI & Development Specialist - Enhanced Dark Theme with Fixed Navigation

// Global WhatsApp functions - defined immediately
window.openWhatsApp = function(serviceType = 'general') {
    let message = 'Hi Adarsh, ';
    
    switch(serviceType) {
        case 'web-apps':
            message += "I'm interested in Web Applications services";
            break;
        case 'mobile-apps':
            message += "I'm interested in Mobile Applications services";
            break;
        case 'ai-calling':
            message += "I'm interested in AI Calling Solutions services";
            break;
        case 'chatbot':
            message += "I'm interested in Chatbot Development services";
            break;
        case 'saas':
            message += "I'm interested in SaaS Solutions services";
            break;
        case 'ai-automation':
            message += "I'm interested in AI Automation services";
            break;
        case 'ai-development':
            message += "I'm interested in AI Development services";
            break;
        default:
            message += "I'm interested in your AI & Development services";
    }

    message += ". Let's discuss how you can help transform my business with your cutting-edge solutions!";

    const whatsappUrl = `https://wa.me/918197098847?text=${encodeURIComponent(message)}`;
    window.open(whatsappUrl, '_blank');
};

window.sendWhatsAppMessage = function() {
    const name = document.getElementById('user-name').value.trim();
    const email = document.getElementById('user-email').value.trim();
    const company = document.getElementById('user-company').value.trim();
    const service = document.getElementById('service-select').value;
    const description = document.getElementById('project-description').value.trim();

    // Enhanced validation with visual feedback
    if (!name || !email) {
        showNotification('Please fill in your name and email to get started', 'error');
        return;
    }

    if (!service) {
        showNotification('Please select a service you are interested in', 'error');
        return;
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        showNotification('Please enter a valid email address', 'error');
        return;
    }

    // Construct enhanced WhatsApp message
    let message = `🚀 Hi Adarsh, I'm ${name}`;
    if (company) {
        message += ` from ${company}`;
    }
    message += `!\n\n`;
    message += `📧 Email: ${email}\n`;
    message += `🔧 Service Interest: ${service}\n`;
    if (description) {
        message += `📝 Project Details: ${description}\n`;
    }
    message += `\nI'm excited about ${service} and would love to discuss how your AI & Development expertise can transform my business. Your portfolio looks incredible!\n\nWhen would be a good time to connect for a consultation?`;

    const whatsappUrl = `https://wa.me/918197098847?text=${encodeURIComponent(message)}`;
    window.open(whatsappUrl, '_blank');

    // Clear form and show success with enhanced animation
    document.getElementById('user-name').value = '';
    document.getElementById('user-email').value = '';
    document.getElementById('user-company').value = '';
    document.getElementById('service-select').value = '';
    document.getElementById('project-description').value = '';

    showNotification('🎉 Message sent via WhatsApp! Adarsh will respond shortly with personalized recommendations.', 'success');
};

// FIXED: Enhanced smooth scroll functions for hero buttons
window.scrollToServices = function() {
    console.log('🎯 Explore Services button clicked');
    const servicesSection = document.querySelector('#services');
    if (servicesSection) {
        const offset = 100; // Proper offset for header clearance
        const targetPosition = servicesSection.offsetTop - offset;
        
        // Smooth scroll to services section
        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
        
        // Add visual feedback after scroll completes
        setTimeout(() => {
            servicesSection.style.animation = 'highlightSection 2s ease-out';
            console.log('✅ Successfully scrolled to services section');
        }, 800);
    } else {
        console.error('❌ Services section not found');
    }
};

window.scrollToPortfolio = function() {
    console.log('🎯 View Portfolio button clicked');
    const portfolioSection = document.querySelector('#portfolio');
    if (portfolioSection) {
        const offset = 100; // Consistent offset
        const targetPosition = portfolioSection.offsetTop - offset;
        
        // Smooth scroll to portfolio section
        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
        
        // Add visual feedback
        setTimeout(() => {
            portfolioSection.style.animation = 'highlightSection 2s ease-out';
            console.log('✅ Successfully scrolled to portfolio section');
        }, 800);
    } else {
        console.error('❌ Portfolio section not found');
    }
};

// Enhanced global notification function with better styling
function showNotification(message, type = 'info', duration = 6000) {
    // Remove any existing notifications
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notification => notification.remove());

    const notification = document.createElement('div');
    notification.className = 'notification';
    
    let bgColor, textColor, icon, borderColor;
    switch(type) {
        case 'success':
            bgColor = 'linear-gradient(135deg, rgba(0, 255, 255, 0.9), rgba(0, 200, 200, 0.9))';
            textColor = '#0a0a0a';
            borderColor = '#00ffff';
            icon = '✅';
            break;
        case 'error':
            bgColor = 'linear-gradient(135deg, rgba(255, 0, 100, 0.9), rgba(200, 0, 80, 0.9))';
            textColor = '#ffffff';
            borderColor = '#ff0064';
            icon = '❌';
            break;
        default:
            bgColor = 'linear-gradient(135deg, rgba(255, 0, 255, 0.9), rgba(200, 0, 200, 0.9))';
            textColor = '#ffffff';
            borderColor = '#ff00ff';
            icon = 'ℹ️';
    }

    notification.style.cssText = `
        position: fixed;
        top: 120px;
        right: 20px;
        background: ${bgColor};
        color: ${textColor};
        padding: 20px 28px;
        border-radius: 15px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3), 0 0 20px ${borderColor}33;
        z-index: 10000;
        animation: slideInRight 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        max-width: 400px;
        display: flex;
        align-items: center;
        gap: 16px;
        backdrop-filter: blur(20px);
        border: 2px solid ${borderColor}66;
        font-family: var(--font-family-base);
        font-weight: 600;
        font-size: 15px;
        line-height: 1.4;
    `;
    notification.innerHTML = `
        <span style="font-size: 22px; filter: drop-shadow(0 0 5px currentColor);">${icon}</span>
        <span>${message}</span>
    `;

    document.body.appendChild(notification);

    // Enhanced exit animation
    setTimeout(() => {
        if (notification.parentElement) {
            notification.style.animation = 'slideOutRight 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
            setTimeout(() => {
                if (notification.parentElement) {
                    notification.remove();
                }
            }, 400);
        }
    }, duration);
}

// Enhanced smooth scroll utility with easing
function smoothScrollTo(targetPosition, duration = 1000) {
    const startPosition = window.pageYOffset;
    const distance = targetPosition - startPosition;
    let startTime = null;

    function animation(currentTime) {
        if (startTime === null) startTime = currentTime;
        const timeElapsed = currentTime - startTime;
        const run = easeInOutCubic(timeElapsed, startPosition, distance, duration);
        window.scrollTo(0, run);
        if (timeElapsed < duration) requestAnimationFrame(animation);
    }

    // Enhanced easing function
    function easeInOutCubic(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t * t + b;
        t -= 2;
        return c / 2 * (t * t * t + 2) + b;
    }

    requestAnimationFrame(animation);
}

class AdarshMLandingPage {
    constructor() {
        this.whatsappNumber = '+91 8197098847';
        this.email = 'adarshm.boostmysites@gmail.com';
        this.portfolioUrl = 'https://services.boostmysites.in/adarshm/ai-development';
        this.isServicesVisible = false;
        this.init();
    }

    init() {
        this.setupHeroButtons(); // FIXED: Add this first to ensure buttons work
        this.setupNavigation();
        this.setupTestimonialCarousel();
        this.setupScrollAnimations();
        this.setupScrollEffects();
        this.setupMobileMenu();
        this.setupContactForm();
        this.setupParallaxEffects();
        this.setupServicesVisibility();
        this.setupAdvancedAnimations();
        this.setupPerformanceOptimizations();
        
        console.log('🚀 Adarsh M Portfolio - Enhanced Dark Theme Loaded Successfully');
        console.log('✅ Services Section Fixed and Fully Visible');
        console.log('✅ Header Spacing Optimized');
        console.log('✅ Original "Adarsh M" Branding Preserved');
        console.log('✅ Hero Button Navigation Fixed');
    }

    // FIXED: Setup hero buttons with proper event listeners
    setupHeroButtons() {
        // Fix Explore Services button
        const exploreBtn = document.querySelector('.cta-primary');
        if (exploreBtn) {
            // Remove existing onclick and add proper event listener
            exploreBtn.removeAttribute('onclick');
            exploreBtn.addEventListener('click', (e) => {
                e.preventDefault();
                console.log('🎯 Explore Services button clicked via event listener');
                window.scrollToServices();
            });
            console.log('✅ Explore Services button event listener attached');
        }

        // Fix View Portfolio button
        const portfolioBtn = document.querySelector('.cta-secondary');
        if (portfolioBtn) {
            // Remove existing onclick and add proper event listener
            portfolioBtn.removeAttribute('onclick');
            portfolioBtn.addEventListener('click', (e) => {
                e.preventDefault();
                console.log('🎯 View Portfolio button clicked via event listener');
                window.scrollToPortfolio();
            });
            console.log('✅ View Portfolio button event listener attached');
        }
    }

    // Enhanced Services Visibility Setup
    setupServicesVisibility() {
        const servicesSection = document.getElementById('services');
        const serviceCards = document.querySelectorAll('.service-card');
        
        if (servicesSection) {
            // Ensure services section is always visible
            servicesSection.style.display = 'block';
            servicesSection.style.visibility = 'visible';
            servicesSection.style.opacity = '1';
            
            // Add enhanced interaction for service cards
            serviceCards.forEach((card, index) => {
                // Ensure each card is visible
                card.style.display = 'flex';
                card.style.visibility = 'visible';
                
                // Add enhanced hover effects
                card.addEventListener('mouseenter', () => {
                    this.enhanceServiceCard(card, true);
                });
                
                card.addEventListener('mouseleave', () => {
                    this.enhanceServiceCard(card, false);
                });

                // FIXED: Add click tracking for Learn More buttons
                const learnMoreBtn = card.querySelector('.service-btn');
                if (learnMoreBtn) {
                    learnMoreBtn.addEventListener('click', (e) => {
                        const serviceTitle = card.querySelector('.service-title')?.textContent;
                        console.log(`🔗 Service clicked: ${serviceTitle}`);
                        
                        // Add click animation
                        card.style.transform = 'translateY(-12px) scale(0.98)';
                        setTimeout(() => {
                            card.style.transform = '';
                        }, 200);

                        // Show feedback notification
                        showNotification(`🚀 Opening ${serviceTitle} details...`, 'info', 3000);
                    });
                }
            });

            console.log(`✅ Services section initialized with ${serviceCards.length} cards`);
        }
    }

    enhanceServiceCard(card, isHovering) {
        const icon = card.querySelector('.service-icon');
        const title = card.querySelector('.service-title');
        const description = card.querySelector('.service-description');
        const btn = card.querySelector('.service-btn');

        if (isHovering) {
            if (icon) {
                icon.style.transform = 'scale(1.15) rotate(5deg)';
                icon.style.filter = 'drop-shadow(0 8px 16px rgba(0, 255, 255, 0.6))';
            }
            if (title) {
                title.style.textShadow = '0 0 15px rgba(255, 255, 255, 0.6)';
            }
            if (description) {
                description.style.color = 'rgba(255, 255, 255, 0.95)';
            }
            if (btn) {
                btn.style.boxShadow = '0 8px 25px rgba(0, 255, 255, 0.5)';
            }
        } else {
            if (icon) {
                icon.style.transform = '';
                icon.style.filter = '';
            }
            if (title) {
                title.style.textShadow = '';
            }
            if (description) {
                description.style.color = '';
            }
            if (btn) {
                btn.style.boxShadow = '';
            }
        }
    }

    // Enhanced parallax effects with performance optimization
    setupParallaxEffects() {
        let ticking = false;
        let lastScrollY = window.pageYOffset;

        const handleParallax = () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    const scrolled = window.pageYOffset;
                    const scrollDelta = scrolled - lastScrollY;

                    // Only update if significant scroll change
                    if (Math.abs(scrollDelta) > 2) {
                        // Enhanced floating shapes parallax
                        const shapes = document.querySelectorAll('.floating-shape');
                        shapes.forEach((shape, index) => {
                            const speed = 0.3 + (index * 0.1);
                            const yPos = -(scrolled * speed);
                            const rotation = scrolled * 0.05 + (index * 45);
                            const scale = 1 + (scrolled * 0.0001);
                            shape.style.transform = `translateY(${yPos}px) rotate(${rotation}deg) scale(${scale})`;
                        });

                        // Enhanced gradient orbs parallax
                        const orbs = document.querySelectorAll('.gradient-orb');
                        orbs.forEach((orb, index) => {
                            const speed = 0.2 + (index * 0.05);
                            const yPos = -(scrolled * speed);
                            const scale = 1 + (scrolled * 0.00005);
                            const opacity = 0.2 - (scrolled * 0.0001);
                            orb.style.transform = `translateY(${yPos}px) scale(${scale})`;
                            orb.style.opacity = Math.max(0.05, opacity);
                        });

                        lastScrollY = scrolled;
                    }

                    ticking = false;
                });
                ticking = true;
            }
        };

        window.addEventListener('scroll', handleParallax, { passive: true });
    }

    // Enhanced Contact Form Setup with advanced validation
    setupContactForm() {
        const inputs = document.querySelectorAll('#user-name, #user-email, #service-select');
        inputs.forEach(input => {
            // Real-time validation
            input.addEventListener('blur', () => {
                this.validateField(input);
            });

            input.addEventListener('input', () => {
                this.clearFieldError(input);
                this.updateFieldStatus(input);
            });

            // Enhanced focus effects with neon glow
            input.addEventListener('focus', () => {
                input.parentElement.classList.add('focused');
                input.style.boxShadow = '0 0 20px rgba(0, 255, 255, 0.4)';
                input.style.borderColor = '#00ffff';
            });

            input.addEventListener('blur', () => {
                input.parentElement.classList.remove('focused');
                if (!input.classList.contains('error')) {
                    input.style.boxShadow = '';
                    input.style.borderColor = '';
                }
            });
        });

        // Enhanced textarea with character counter
        const textarea = document.getElementById('project-description');
        if (textarea) {
            this.addCharacterCounter(textarea);
            
            // Add auto-resize functionality
            textarea.addEventListener('input', () => {
                this.autoResizeTextarea(textarea);
            });
        }

        // FIXED: Add form submission tracking
        const submitBtn = document.querySelector('button[onclick="sendWhatsAppMessage()"]');
        if (submitBtn) {
            submitBtn.addEventListener('click', () => {
                console.log('📊 Form submission attempted');
            });
        }
    }

    updateFieldStatus(field) {
        const value = field.value.trim();
        if (value && !field.classList.contains('error')) {
            field.style.borderColor = '#00ff88';
            field.style.boxShadow = '0 0 10px rgba(0, 255, 136, 0.3)';
        }
    }

    autoResizeTextarea(textarea) {
        textarea.style.height = 'auto';
        textarea.style.height = textarea.scrollHeight + 'px';
    }

    addCharacterCounter(textarea) {
        const maxLength = 500;
        const counter = document.createElement('div');
        counter.className = 'character-counter';
        counter.style.cssText = `
            font-size: var(--font-size-sm);
            color: rgba(255, 255, 255, 0.6);
            text-align: right;
            margin-top: var(--space-4);
            transition: color 0.3s ease;
        `;
        
        textarea.parentElement.appendChild(counter);

        const updateCounter = () => {
            const remaining = maxLength - textarea.value.length;
            counter.textContent = `${remaining} characters remaining`;
            
            if (remaining < 50) {
                counter.style.color = '#ffaa00';
                counter.style.textShadow = '0 0 5px rgba(255, 170, 0, 0.5)';
            } else if (remaining < 0) {
                counter.style.color = '#ff0064';
                counter.style.textShadow = '0 0 5px rgba(255, 0, 100, 0.5)';
            } else {
                counter.style.color = 'rgba(255, 255, 255, 0.6)';
                counter.style.textShadow = '';
            }
        };

        textarea.addEventListener('input', updateCounter);
        textarea.setAttribute('maxlength', maxLength);
        updateCounter();
    }

    validateField(field) {
        const value = field.value.trim();
        let isValid = true;
        let errorMessage = '';

        this.clearFieldError(field);

        if (field.hasAttribute('required') && !value) {
            isValid = false;
            errorMessage = 'This field is required';
        }

        if (field.type === 'email' && value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value)) {
                isValid = false;
                errorMessage = 'Please enter a valid email address';
            }
        }

        if (field.id === 'user-name' && value) {
            if (value.length < 2) {
                isValid = false;
                errorMessage = 'Name must be at least 2 characters long';
            } else if (!/^[a-zA-Z\s]+$/.test(value)) {
                isValid = false;
                errorMessage = 'Name should only contain letters and spaces';
            }
        }

        if (!isValid) {
            this.showFieldError(field, errorMessage);
        } else if (value) {
            this.showFieldSuccess(field);
        }

        return isValid;
    }

    showFieldError(field, message) {
        field.classList.add('error');
        field.style.borderColor = '#ff0064';
        field.style.boxShadow = '0 0 15px rgba(255, 0, 100, 0.4)';
        
        const errorElement = document.createElement('div');
        errorElement.className = 'field-error';
        errorElement.textContent = message;
        errorElement.style.cssText = `
            color: #ff0064;
            font-size: var(--font-size-sm);
            margin-top: var(--space-4);
            animation: shake 0.4s ease-in-out;
            text-shadow: 0 0 5px rgba(255, 0, 100, 0.3);
            font-weight: 500;
        `;
        
        field.parentElement.appendChild(errorElement);
    }

    showFieldSuccess(field) {
        field.classList.remove('error');
        field.style.borderColor = '#00ff88';
        field.style.boxShadow = '0 0 10px rgba(0, 255, 136, 0.3)';
    }

    clearFieldError(field) {
        field.classList.remove('error');
        field.style.borderColor = '';
        field.style.boxShadow = '';
        
        const existingError = field.parentElement.querySelector('.field-error');
        if (existingError) {
            existingError.remove();
        }
    }

    // Enhanced Navigation functionality
    setupNavigation() {
        const navLinks = document.querySelectorAll('.nav-link');
        const sections = document.querySelectorAll('section[id]');

        navLinks.forEach(link => {
            const href = link.getAttribute('href');
            
            if (href && href.startsWith('#')) {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    const targetId = href;
                    const targetSection = document.querySelector(targetId);
                    
                    if (targetSection) {
                        const offset = 100; // Enhanced offset for better header clearance
                        const targetPosition = targetSection.offsetTop - offset;
                        
                        // Use native smooth scrolling
                        window.scrollTo({
                            top: targetPosition,
                            behavior: 'smooth'
                        });

                        // Add visual feedback
                        this.highlightNavLink(link);
                        
                        // Special handling for services section
                        if (targetId === '#services') {
                            setTimeout(() => {
                                this.animateServicesEntrance();
                            }, 800);
                        }
                    }

                    this.closeMobileMenu();
                });
            }
        });

        // Enhanced active navigation on scroll
        window.addEventListener('scroll', debounce(() => {
            this.updateActiveNavigation(sections, navLinks);
        }, 100), { passive: true });
    }

    highlightNavLink(activeLink) {
        const allLinks = document.querySelectorAll('.nav-link');
        allLinks.forEach(link => {
            link.style.transform = '';
            link.style.textShadow = '';
        });
        
        activeLink.style.transform = 'scale(1.1)';
        activeLink.style.textShadow = '0 0 15px rgba(0, 255, 255, 0.8)';
        
        setTimeout(() => {
            activeLink.style.transform = '';
        }, 300);
    }

    animateServicesEntrance() {
        const serviceCards = document.querySelectorAll('.service-card');
        serviceCards.forEach((card, index) => {
            setTimeout(() => {
                card.style.animation = 'serviceCardEntrance 0.8s cubic-bezier(0.16, 1, 0.3, 1)';
            }, index * 150);
        });
    }

    updateActiveNavigation(sections, navLinks) {
        const scrollPosition = window.scrollY + 200; // Adjusted for better header clearance

        sections.forEach((section) => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                        
                        // Add enhanced active state
                        link.style.textShadow = '0 0 12px rgba(0, 255, 255, 0.8)';
                    } else {
                        link.style.textShadow = '';
                    }
                });
            }
        });
    }

    // Enhanced Mobile menu functionality
    setupMobileMenu() {
        const hamburger = document.getElementById('hamburger');
        const navMenu = document.getElementById('nav-menu');

        if (hamburger && navMenu) {
            hamburger.addEventListener('click', (e) => {
                e.stopPropagation();
                this.toggleMobileMenu();
            });

            document.addEventListener('click', (e) => {
                if (!hamburger.contains(e.target) && !navMenu.contains(e.target)) {
                    this.closeMobileMenu();
                }
            });

            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') {
                    this.closeMobileMenu();
                }
            });

            window.addEventListener('resize', debounce(() => {
                if (window.innerWidth > 768) {
                    this.closeMobileMenu();
                }
            }, 250));
        }
    }

    toggleMobileMenu() {
        const hamburger = document.getElementById('hamburger');
        const navMenu = document.getElementById('nav-menu');
        
        if (hamburger && navMenu) {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
            
            // Enhanced mobile menu effects
            if (navMenu.classList.contains('active')) {
                document.body.style.overflow = 'hidden';
                navMenu.style.animation = 'mobileMenuSlideIn 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
            } else {
                document.body.style.overflow = '';
                navMenu.style.animation = 'mobileMenuSlideOut 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
            }
        }
    }

    closeMobileMenu() {
        const hamburger = document.getElementById('hamburger');
        const navMenu = document.getElementById('nav-menu');
        
        if (hamburger && navMenu) {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
            document.body.style.overflow = '';
            navMenu.style.animation = '';
        }
    }

    // Enhanced Testimonial carousel with advanced features
    setupTestimonialCarousel() {
        const testimonialCards = document.querySelectorAll('.testimonial-card');
        const dots = document.querySelectorAll('.dot');
        let currentSlide = 0;
        let autoSlideInterval;
        let isUserInteracting = false;

        if (testimonialCards.length === 0 || dots.length === 0) return;

        // Enhanced dot navigation
        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                this.showTestimonial(index, testimonialCards, dots);
                currentSlide = index;
                isUserInteracting = true;
                this.restartAutoSlide();
                
                // Add dot click animation
                dot.style.transform = 'scale(1.5)';
                setTimeout(() => {
                    dot.style.transform = '';
                }, 200);
                
                setTimeout(() => { isUserInteracting = false; }, 12000);
            });
        });

        const startAutoSlide = () => {
            autoSlideInterval = setInterval(() => {
                if (!isUserInteracting) {
                    currentSlide = (currentSlide + 1) % testimonialCards.length;
                    this.showTestimonial(currentSlide, testimonialCards, dots);
                }
            }, 7000); // Slightly longer interval
        };

        this.restartAutoSlide = () => {
            clearInterval(autoSlideInterval);
            startAutoSlide();
        };

        // Enhanced touch/swipe support
        let startX = 0, endX = 0, startTime = 0;
        const testimonialContainer = document.querySelector('.testimonials-container');
        
        if (testimonialContainer) {
            testimonialContainer.addEventListener('touchstart', (e) => {
                startX = e.touches[0].clientX;
                startTime = Date.now();
                isUserInteracting = true;
            }, { passive: true });

            testimonialContainer.addEventListener('touchend', (e) => {
                endX = e.changedTouches[0].clientX;
                const timeDiff = Date.now() - startTime;
                
                if (timeDiff < 600) {
                    const newSlide = this.handleSwipe(startX, endX, currentSlide, testimonialCards.length);
                    if (newSlide !== currentSlide) {
                        currentSlide = newSlide;
                        this.showTestimonial(currentSlide, testimonialCards, dots);
                        this.restartAutoSlide();
                    }
                }
                
                setTimeout(() => { isUserInteracting = false; }, 8000);
            }, { passive: true });
        }

        // Enhanced keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (e.target.closest('.testimonials-container')) {
                if (e.key === 'ArrowLeft') {
                    currentSlide = currentSlide === 0 ? testimonialCards.length - 1 : currentSlide - 1;
                    this.showTestimonial(currentSlide, testimonialCards, dots);
                    isUserInteracting = true;
                    this.restartAutoSlide();
                } else if (e.key === 'ArrowRight') {
                    currentSlide = (currentSlide + 1) % testimonialCards.length;
                    this.showTestimonial(currentSlide, testimonialCards, dots);
                    isUserInteracting = true;
                    this.restartAutoSlide();
                }
            }
        });

        startAutoSlide();
    }

    showTestimonial(index, cards, dots) {
        // Enhanced card transitions
        cards.forEach((card, i) => {
            card.classList.remove('active');
            if (i === index) {
                card.style.opacity = '0';
                card.style.transform = 'translateY(30px) scale(0.95)';
            }
        });
        
        dots.forEach((dot, i) => {
            dot.classList.remove('active');
            if (i === index) {
                dot.style.boxShadow = '0 0 15px rgba(0, 255, 255, 0.8)';
            } else {
                dot.style.boxShadow = '';
            }
        });

        setTimeout(() => {
            if (cards[index] && dots[index]) {
                cards[index].classList.add('active');
                cards[index].style.opacity = '1';
                cards[index].style.transform = 'translateY(0) scale(1)';
                dots[index].classList.add('active');
            }
        }, 200);
    }

    handleSwipe(startX, endX, currentSlide, totalSlides) {
        const threshold = 80;
        const diff = startX - endX;

        if (Math.abs(diff) > threshold) {
            if (diff > 0) {
                return (currentSlide + 1) % totalSlides;
            } else {
                return currentSlide === 0 ? totalSlides - 1 : currentSlide - 1;
            }
        }
        return currentSlide;
    }

    // Advanced scroll animations with Intersection Observer
    setupScrollAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.animateElement(entry.target);
                    
                    // Enhanced stagger effect
                    if (entry.target.parentElement && 
                        (entry.target.parentElement.classList.contains('services-grid') ||
                         entry.target.parentElement.classList.contains('portfolio-grid'))) {
                        const siblings = Array.from(entry.target.parentElement.children);
                        const index = siblings.indexOf(entry.target);
                        entry.target.style.transitionDelay = `${index * 200}ms`;
                        entry.target.style.animation = `elementEntrance 1s cubic-bezier(0.16, 1, 0.3, 1) ${index * 100}ms both`;
                    }
                }
            });
        }, observerOptions);

        // Observe all animated elements
        const animatedElements = document.querySelectorAll('.service-card, .portfolio-item, .stat-card');
        animatedElements.forEach(element => {
            this.prepareForAnimation(element);
            observer.observe(element);
        });

        this.setupCounterAnimation();
    }

    prepareForAnimation(element) {
        element.style.opacity = '0';
        element.style.transform = 'translateY(50px) scale(0.9)';
        element.style.transition = 'all 1s cubic-bezier(0.16, 1, 0.3, 1)';
    }

    animateElement(element) {
        element.style.opacity = '1';
        element.style.transform = 'translateY(0) scale(1)';
    }

    setupCounterAnimation() {
        const statNumbers = document.querySelectorAll('.stat-number');
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.animateCounter(entry.target);
                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.8 });

        statNumbers.forEach(number => {
            counterObserver.observe(number);
        });
    }

    animateCounter(element) {
        const text = element.textContent;
        const hasPlus = text.includes('+');
        const hasPercent = text.includes('%');
        const isTime = text.includes('/');
        
        if (isTime) return;

        const finalValue = parseInt(text.replace(/[^\d]/g, ''));
        if (isNaN(finalValue)) return;

        const duration = 3000;
        const steps = 100;
        const stepValue = finalValue / steps;
        const stepDuration = duration / steps;

        let currentValue = 0;
        const timer = setInterval(() => {
            currentValue += stepValue;
            if (currentValue >= finalValue) {
                currentValue = finalValue;
                clearInterval(timer);
            }
            
            let displayValue = Math.floor(currentValue);
            if (hasPlus) displayValue += '+';
            if (hasPercent) displayValue += '%';
            
            element.textContent = displayValue;
            
            // Add pulsing effect during animation
            element.style.textShadow = `0 0 ${10 + Math.sin(currentValue / 10) * 5}px rgba(0, 255, 255, 0.8)`;
        }, stepDuration);
    }

    // Enhanced scroll effects with performance optimization
    setupScrollEffects() {
        let lastScrollY = window.scrollY;
        let ticking = false;
        
        const handleScroll = () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    const navbar = document.getElementById('navbar');
                    const currentScrollY = window.scrollY;

                    if (navbar) {
                        // Enhanced navbar hide/show with animation
                        if (currentScrollY > lastScrollY && currentScrollY > 200) {
                            navbar.style.transform = 'translateY(-100%)';
                            navbar.style.boxShadow = '0 10px 40px rgba(0, 0, 0, 0.2)';
                        } else {
                            navbar.style.transform = 'translateY(0)';
                            navbar.style.boxShadow = '0 8px 32px rgba(0, 255, 255, 0.1)';
                        }

                        // Enhanced background blur effect
                        if (currentScrollY > 80) {
                            navbar.classList.add('scrolled');
                            navbar.style.background = 'rgba(10, 10, 10, 0.95)';
                            navbar.style.borderBottomColor = 'rgba(0, 255, 255, 0.3)';
                        } else {
                            navbar.classList.remove('scrolled');
                            navbar.style.background = '';
                            navbar.style.borderBottomColor = '';
                        }
                    }

                    lastScrollY = currentScrollY;
                    ticking = false;
                });
                ticking = true;
            }
        };

        window.addEventListener('scroll', handleScroll, { passive: true });
    }

    // Advanced animations setup
    setupAdvancedAnimations() {
        // Add CSS animations dynamically
        const animationStyles = document.createElement('style');
        animationStyles.textContent = `
            @keyframes highlightSection {
                0% { transform: scale(1); }
                50% { transform: scale(1.02); }
                100% { transform: scale(1); }
            }
            
            @keyframes serviceCardEntrance {
                0% { 
                    opacity: 0; 
                    transform: translateY(30px) scale(0.9); 
                }
                100% { 
                    opacity: 1; 
                    transform: translateY(0) scale(1); 
                }
            }
            
            @keyframes elementEntrance {
                0% { 
                    opacity: 0; 
                    transform: translateY(40px) scale(0.95); 
                }
                100% { 
                    opacity: 1; 
                    transform: translateY(0) scale(1); 
                }
            }
            
            @keyframes mobileMenuSlideIn {
                0% { 
                    transform: translateX(-100%); 
                    opacity: 0; 
                }
                100% { 
                    transform: translateX(0); 
                    opacity: 1; 
                }
            }
            
            @keyframes mobileMenuSlideOut {
                0% { 
                    transform: translateX(0); 
                    opacity: 1; 
                }
                100% { 
                    transform: translateX(-100%); 
                    opacity: 0; 
                }
            }
        `;
        document.head.appendChild(animationStyles);
    }

    // Performance optimizations
    setupPerformanceOptimizations() {
        // Lazy load images if any are added later
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src;
                        img.classList.remove('lazy');
                        imageObserver.unobserve(img);
                    }
                });
            });

            document.querySelectorAll('img[data-src]').forEach(img => {
                imageObserver.observe(img);
            });
        }

        // Optimize scroll events
        let scrollTimeout;
        window.addEventListener('scroll', () => {
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(() => {
                // Scroll end actions
                console.log('📊 Scroll performance optimized');
            }, 150);
        }, { passive: true });
    }
}

// Utility functions
function debounce(func, wait) {
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

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new AdarshMLandingPage();
});

// Fallback initialization for immediate execution
if (document.readyState === 'complete') {
    new AdarshMLandingPage();
}

// Enhanced CSS animations and styles dynamically
const enhancedStyles = document.createElement('style');
enhancedStyles.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }

    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-10px); }
        75% { transform: translateX(10px); }
    }

    @keyframes glow {
        0%, 100% { 
            text-shadow: 0 0 5px currentColor; 
        }
        50% { 
            text-shadow: 0 0 20px currentColor, 0 0 30px currentColor; 
        }
    }

    /* Enhanced navbar transitions */
    .navbar {
        transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), 
                    background-color 0.4s ease,
                    box-shadow 0.4s ease,
                    border-bottom-color 0.4s ease !important;
    }

    .navbar.scrolled {
        background: rgba(10, 10, 10, 0.98) !important;
        backdrop-filter: blur(30px);
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.4);
    }

    /* Enhanced field animations */
    .field-error {
        animation: shake 0.5s ease-in-out;
    }

    .form-control:focus {
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Service card enhancements */
    .service-card:hover .service-icon {
        animation: glow 2s ease-in-out infinite;
    }

    .service-card:hover .service-title {
        animation: glow 2s ease-in-out infinite;
    }

    /* Portfolio item enhancements */
    .portfolio-item:hover .portfolio-content {
        transform: translateY(-8px);
        transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Stat card hover effects */
    .stat-card:hover {
        transform: translateY(-6px) scale(1.05);
        box-shadow: 0 20px 50px rgba(0, 255, 255, 0.2);
        border-color: rgba(0, 255, 255, 0.4);
    }

    .stat-card:hover .stat-number {
        animation: glow 1s ease-in-out;
    }

    /* Enhanced notification styles */
    .notification {
        font-family: var(--font-family-base);
        font-size: 15px;
        font-weight: 600;
        backdrop-filter: blur(25px);
    }

    /* Form group focus effects */
    .form-group.focused .form-control {
        border-color: #00ffff !important;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.4) !important;
        background: rgba(255, 255, 255, 0.08) !important;
    }

    /* Character counter enhancements */
    .character-counter {
        transition: color 0.3s ease, text-shadow 0.3s ease;
    }

    /* Enhanced button hover effects */
    .btn--primary:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(0, 255, 255, 0.5);
        filter: brightness(1.1);
    }

    .btn--outline:hover {
        transform: translateY(-2px);
        background: rgba(0, 255, 255, 0.15) !important;
    }

    /* Loading states */
    .btn:disabled {
        opacity: 0.7;
        cursor: not-allowed;
        transform: none !important;
        filter: grayscale(0.5);
    }

    .btn.loading::after {
        content: '';
        position: absolute;
        width: 18px;
        height: 18px;
        margin: auto;
        border: 2px solid currentColor;
        border-right-color: transparent;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }

    @keyframes spin {
        to { transform: rotate(360deg); }
    }

    /* Enhanced testimonial transitions */
    .testimonial-card {
        transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .testimonial-card.active {
        transform: translateY(0) scale(1);
        opacity: 1;
    }

    /* Enhanced scroll behavior */
    html {
        scroll-behavior: smooth;
    }

    /* Enhanced focus states */
    .btn:focus-visible,
    .nav-link:focus-visible,
    .form-control:focus {
        outline: 3px solid rgba(0, 255, 255, 0.6);
        outline-offset: 3px;
    }

    /* Mobile menu overlay enhancement */
    @media (max-width: 768px) {
        .nav-menu.active::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.8);
            z-index: -1;
            backdrop-filter: blur(10px);
        }
    }
`;

document.head.appendChild(enhancedStyles);

// Performance optimization: Preload critical resources
const preloadResources = () => {
    const importantLinks = [
        'https://services.boostmysites.in/adarshm/web-apps',
        'https://services.boostmysites.in/adarshm/mobile-apps',
        'https://services.boostmysites.in/adarshm/ai-calling',
        'https://services.boostmysites.in/adarshm/chatbot-development',
        'https://services.boostmysites.in/adarshm/saas',
        'https://services.boostmysites.in/adarshm/ai-automation',
        'https://services.boostmysites.in/adarshm/ai-development'
    ];

    importantLinks.forEach(href => {
        const link = document.createElement('link');
        link.rel = 'prefetch';
        link.href = href;
        document.head.appendChild(link);
    });

    console.log('🚀 Resource preloading completed');
};

// Enhanced error handling
window.addEventListener('error', (e) => {
    console.error('🚨 Application error:', e.error);
});

window.addEventListener('unhandledrejection', (e) => {
    console.error('🚨 Unhandled promise rejection:', e.reason);
});

// Preload resources after page load
window.addEventListener('load', () => {
    preloadResources();
    console.log('✅ Adarsh M Landing Page fully loaded and optimized');
    console.log('✅ Hero button navigation fixed');
});