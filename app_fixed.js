// Adarsh M - AI & Development Specialist - FIXED Dark Theme Interactive Features

// Global WhatsApp functions - defined immediately for single-click functionality
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

    message += ". Let's discuss how you can help transform my business!";

    const whatsappUrl = `https://wa.me/918197098847?text=${encodeURIComponent(message)}`;
    window.open(whatsappUrl, '_blank');
};

window.sendWhatsAppMessage = function() {
    const name = document.getElementById('user-name').value.trim();
    const email = document.getElementById('user-email').value.trim();
    const company = document.getElementById('user-company').value.trim();
    const service = document.getElementById('service-select').value;
    const description = document.getElementById('project-description').value.trim();

    // Enhanced validation with dark theme notifications
    if (!name || !email) {
        showDarkNotification('Please fill in your name and email', 'error');
        return;
    }

    if (!service) {
        showDarkNotification('Please select a service', 'error');
        return;
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        showDarkNotification('Please enter a valid email address', 'error');
        return;
    }

    // Construct WhatsApp message
    let message = `Hi Adarsh, I'm ${name}`;
    if (company) {
        message += ` from ${company}`;
    }
    message += `.\n\n`;
    message += `📧 Email: ${email}\n`;
    message += `🔧 Service Interest: ${service}\n`;
    if (description) {
        message += `📝 Project Details: ${description}\n`;
    }
    message += `\nI'm interested in ${service} services and would love to discuss how your AI & Development expertise can help transform my business. When would be a good time to connect?`;

    const whatsappUrl = `https://wa.me/918197098847?text=${encodeURIComponent(message)}`;
    window.open(whatsappUrl, '_blank');

    // Clear form and show success with dark theme styling
    document.getElementById('user-name').value = '';
    document.getElementById('user-email').value = '';
    document.getElementById('user-company').value = '';
    document.getElementById('service-select').value = '';
    document.getElementById('project-description').value = '';

    showDarkNotification('Message sent via WhatsApp! Adarsh will respond shortly.', 'success');
};

// Dark theme notification system
function showDarkNotification(message, type = 'info') {
    const existingNotification = document.querySelector('.dark-notification');
    if (existingNotification) {
        existingNotification.remove();
    }

    const notification = document.createElement('div');
    notification.className = 'dark-notification';

    let bgGradient, icon, glowColor;
    switch(type) {
        case 'success':
            bgGradient = 'linear-gradient(135deg, #00ffff, #ff00ff)';
            glowColor = '#00ffff';
            icon = '✅';
            break;
        case 'error':
            bgGradient = 'linear-gradient(135deg, #ff00ff, #ffff00)';
            glowColor = '#ff00ff';
            icon = '❌';
            break;
        default:
            bgGradient = 'linear-gradient(135deg, #ffff00, #00ffff)';
            glowColor = '#ffff00';
            icon = 'ℹ️';
    }

    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
        padding: 20px 24px;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3), 0 0 30px ${glowColor}33;
        z-index: 10000;
        animation: slideInNeon 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        max-width: 350px;
        display: flex;
        align-items: center;
        gap: 16px;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 14px;
        border-left: 4px solid ${glowColor};
    `;

    notification.innerHTML = `
        <span style="font-size: 20px; filter: drop-shadow(0 0 10px ${glowColor});">${icon}</span>
        <span style="text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);">${message}</span>
    `;

    document.body.appendChild(notification);

    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentElement) {
            notification.style.animation = 'slideOutNeon 0.5s cubic-bezier(0.16, 1, 0.3, 1)';
            setTimeout(() => {
                if (notification.parentElement) {
                    notification.remove();
                }
            }, 500);
        }
    }, 5000);
}

// FIXED Main Dark Theme Landing Page Class
class DarkThemeAILanding {
    constructor() {
        this.whatsappNumber = '+91 8197098847';
        this.email = 'adarshm.boostmysites@gmail.com';
        this.portfolioUrl = 'https://services.boostmysites.in/adarshm/ai-development';
        this.currentTestimonial = 0;
        this.testimonialInterval = null;
        this.init();
    }

    init() {
        this.setupDarkNavigation();
        this.setupDarkServiceCards();
        this.setupDarkTestimonials();
        this.setupDarkScrollEffects();
        this.setupDarkMobileMenu();
        this.setupDarkHeroButtons();
        this.setupDarkFormValidation();
        this.setupDarkAnimations();
        this.setupDarkParallax();
        this.setupDarkCounters();
        this.addDarkThemeStyles();

        // ADDED: Force Services section visibility
        this.ensureServicesVisibility();
    }

    // ADDED: Ensure Services section is always visible
    ensureServicesVisibility() {
        const servicesSection = document.getElementById('services');
        const servicesGrid = document.querySelector('.services-grid');
        const serviceCards = document.querySelectorAll('.service-card');

        if (servicesSection) {
            servicesSection.style.display = 'block';
            servicesSection.style.visibility = 'visible';
            servicesSection.style.opacity = '1';
        }

        if (servicesGrid) {
            servicesGrid.style.display = 'grid';
            servicesGrid.style.visibility = 'visible';
        }

        serviceCards.forEach(card => {
            card.style.display = 'block';
            card.style.visibility = 'visible';
            card.style.opacity = '1';
        });

        console.log('Services section visibility ensured');
    }

    // FIXED Enhanced dark theme navigation with improved smooth scrolling
    setupDarkNavigation() {
        const navLinks = document.querySelectorAll('.nav-link');
        const sections = document.querySelectorAll('section[id]');

        // Enhanced smooth scroll with FIXED dark theme effects
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('href');
                const targetSection = document.querySelector(targetId);

                if (targetSection) {
                    // IMPROVED: Calculate proper offset accounting for fixed navbar with increased gap
                    const navbar = document.querySelector('.navbar');
                    const navbarHeight = navbar ? navbar.offsetHeight : 80;
                    const offset = navbarHeight + 60; // Increased offset for better visibility
                    const targetPosition = targetSection.offsetTop - offset;

                    // Enhanced smooth scroll
                    this.smoothDarkScroll(targetPosition);

                    // Add neon glow effect to clicked nav item
                    this.addNavGlow(link);

                    // Update active state immediately for better UX
                    navLinks.forEach(navLink => navLink.classList.remove('active'));
                    link.classList.add('active');

                    // ADDED: Special handling for services section
                    if (targetId === '#services') {
                        setTimeout(() => {
                            this.ensureServicesVisibility();
                        }, 500);
                    }
                }

                this.closeDarkMobileMenu();
            });
        });

        // Update active navigation with neon effects
        window.addEventListener('scroll', this.debounce(() => {
            this.updateDarkActiveNav(sections, navLinks);
        }, 50), { passive: true });
    }

    addNavGlow(link) {
        link.style.textShadow = '0 0 20px #00ffff, 0 0 30px #00ffff';
        setTimeout(() => {
            link.style.textShadow = '';
        }, 1000);
    }

    // IMPROVED smooth scrolling function
    smoothDarkScroll(targetPosition, duration = 1000) {
        const startPosition = window.pageYOffset;
        const distance = targetPosition - startPosition;
        let startTime = null;

        function darkAnimation(currentTime) {
            if (startTime === null) startTime = currentTime;
            const timeElapsed = currentTime - startTime;
            const run = easeInOutCubic(timeElapsed, startPosition, distance, duration);
            window.scrollTo(0, run);
            if (timeElapsed < duration) requestAnimationFrame(darkAnimation);
        }

        function easeInOutCubic(t, b, c, d) {
            t /= d / 2;
            if (t < 1) return c / 2 * t * t * t + b;
            t -= 2;
            return c / 2 * (t * t * t + 2) + b;
        }

        requestAnimationFrame(darkAnimation);
    }

    // IMPROVED navigation active state detection
    updateDarkActiveNav(sections, navLinks) {
        const scrollPosition = window.scrollY + 150; // Adjusted for better accuracy

        sections.forEach((section) => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }

    // Enhanced dark service cards with single-click navigation
    setupDarkServiceCards() {
        const serviceCards = document.querySelectorAll('.service-card');

        // ADDED: Ensure cards are visible first
        serviceCards.forEach(card => {
            card.style.display = 'block';
            card.style.visibility = 'visible';
            card.style.opacity = '1';
        });

        serviceCards.forEach((card, index) => {
            // Single-click WhatsApp integration (no double opening)
            let clickTimeout = null;

            card.addEventListener('click', (e) => {
                // Don't interfere with button clicks
                if (e.target.closest('.service-btn')) {
                    return;
                }

                // Prevent multiple rapid clicks
                if (clickTimeout) return;

                clickTimeout = setTimeout(() => {
                    clickTimeout = null;
                }, 1000);

                const serviceType = card.dataset.service;
                if (serviceType) {
                    this.addServiceClickEffect(card);
                    setTimeout(() => {
                        openWhatsApp(serviceType);
                    }, 200);
                }
            });

            // Enhanced hover effects with neon glow
            card.addEventListener('mouseenter', () => {
                this.addServiceHoverEffect(card, index);
            });

            card.addEventListener('mouseleave', () => {
                this.removeServiceHoverEffect(card);
            });

            // Add floating animation to service icons
            const icon = card.querySelector('.service-icon');
            if (icon) {
                icon.style.animation = `floating ${8 + index}s ease-in-out infinite`;
                icon.style.animationDelay = `${index * 0.5}s`;
            }
        });
    }

    addServiceClickEffect(card) {
        card.style.transform = 'translateY(-5px) scale(0.98)';
        card.style.boxShadow = '0 25px 50px rgba(0, 255, 255, 0.3), 0 0 40px rgba(0, 255, 255, 0.2)';

        setTimeout(() => {
            card.style.transform = '';
            card.style.boxShadow = '';
        }, 300);
    }

    addServiceHoverEffect(card, index) {
        const colors = ['#00ffff', '#ff00ff', '#ffff00'];
        const color = colors[index % 3];

        card.style.borderColor = `${color}80`;
        card.style.boxShadow = `0 20px 40px ${color}20, 0 0 30px ${color}30`;

        const serviceGlow = card.querySelector('.service-glow');
        if (serviceGlow) {
            serviceGlow.style.background = `linear-gradient(135deg, ${color}20, transparent)`;
            serviceGlow.style.opacity = '1';
        }
    }

    removeServiceHoverEffect(card) {
        card.style.borderColor = '';
        card.style.boxShadow = '';

        const serviceGlow = card.querySelector('.service-glow');
        if (serviceGlow) {
            serviceGlow.style.opacity = '0';
        }
    }
