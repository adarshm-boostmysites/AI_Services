# Continue with the rest of the dark theme styles
remaining_dark_theme = """
.service-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, transparent, rgba(0, 255, 255, 0.05), transparent);
  opacity: 0;
  transition: all var(--transition-normal);
}

.service-card:hover::before {
  opacity: 1;
}

.service-card:hover {
  transform: translateY(-10px);
  border-color: rgba(0, 255, 255, 0.5);
  box-shadow: 0 20px 40px rgba(0, 255, 255, 0.1), 0 0 30px rgba(0, 255, 255, 0.2);
}

.service-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, var(--neon-cyan), var(--neon-magenta));
  opacity: 0;
  transition: opacity var(--transition-normal);
  border-radius: var(--radius-lg);
  filter: blur(20px);
  z-index: -1;
}

.service-card:hover .service-glow {
  opacity: 0.1;
}

.service-content {
  position: relative;
  z-index: 2;
}

.service-icon {
  font-size: 3rem;
  margin-bottom: var(--space-lg);
  filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.3));
  transition: all var(--transition-normal);
}

.service-card:hover .service-icon {
  transform: scale(1.1);
  filter: drop-shadow(0 0 20px var(--neon-cyan));
}

.service-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-white);
  margin-bottom: var(--space-md);
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
}

.service-description {
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: var(--space-lg);
}

.service-btn {
  margin-top: auto;
}

/* Portfolio Section - Fixed scroll positioning */
.portfolio {
  padding: var(--space-2xl) 0;
  background: linear-gradient(135deg, var(--bg-primary), var(--bg-secondary));
  /* ADDED: Scroll margin for better navigation */
  scroll-margin-top: 120px;
}

.portfolio-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--space-lg);
}

.portfolio-item {
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-lg);
  padding: var(--space-xl);
  transition: all var(--transition-normal);
  position: relative;
  overflow: hidden;
}

.portfolio-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(255, 0, 255, 0.05), rgba(255, 255, 0, 0.05));
  opacity: 0;
  transition: opacity var(--transition-normal);
}

.portfolio-item:hover::before {
  opacity: 1;
}

.portfolio-item:hover {
  transform: translateY(-5px);
  border-color: rgba(255, 0, 255, 0.3);
  box-shadow: 0 15px 30px rgba(255, 0, 255, 0.1);
}

.portfolio-content {
  position: relative;
  z-index: 2;
}

.portfolio-category {
  display: inline-block;
  padding: var(--space-xs) var(--space-sm);
  background: rgba(0, 255, 255, 0.2);
  color: var(--neon-cyan);
  border: 1px solid var(--neon-cyan);
  border-radius: var(--radius-sm);
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  margin-bottom: var(--space-md);
  letter-spacing: 1px;
}

.portfolio-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--text-white);
  margin-bottom: var(--space-sm);
  line-height: 1.3;
}

.portfolio-description {
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: var(--space-md);
}

.portfolio-meta {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-xs);
  margin-bottom: var(--space-lg);
}

.portfolio-tech {
  padding: var(--space-xs) var(--space-sm);
  background: rgba(255, 255, 255, 0.1);
  color: var(--text-white);
  border-radius: var(--radius-sm);
  font-size: 0.8rem;
  font-weight: 500;
}

/* Stats Section - Fixed scroll positioning */
.stats {
  padding: var(--space-2xl) 0;
  background: linear-gradient(135deg, var(--bg-secondary), var(--bg-tertiary));
  scroll-margin-top: 120px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-lg);
}

.stat-card {
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-lg);
  padding: var(--space-xl);
  text-align: center;
  transition: all var(--transition-normal);
}

.stat-card:hover {
  transform: translateY(-5px);
  border-color: rgba(255, 255, 0, 0.3);
  box-shadow: 0 15px 30px rgba(255, 255, 0, 0.1);
}

.stat-card .stat-number {
  font-size: 3rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--neon-yellow), var(--neon-cyan));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  display: block;
  margin-bottom: var(--space-sm);
}

.stat-card .stat-label {
  color: var(--text-secondary);
  font-weight: 500;
  font-size: 1rem;
}

/* Testimonials - Fixed scroll positioning */
.testimonials {
  padding: var(--space-2xl) 0;
  background: var(--bg-primary);
  scroll-margin-top: 120px;
}

.testimonials-container {
  max-width: 800px;
  margin: 0 auto;
  position: relative;
}

.testimonial-card {
  display: none;
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-lg);
  padding: var(--space-xl);
  text-align: center;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.testimonial-card.active {
  display: block;
  animation: fadeInUp 0.6s ease;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.stars {
  font-size: 1.5rem;
  margin-bottom: var(--space-lg);
  filter: drop-shadow(0 0 10px var(--neon-yellow));
}

.testimonial-text {
  font-size: 1.2rem;
  color: var(--text-white);
  line-height: 1.7;
  margin-bottom: var(--space-lg);
  font-style: italic;
  font-weight: 500;
}

.testimonial-results {
  background: rgba(0, 255, 255, 0.1);
  border: 1px solid rgba(0, 255, 255, 0.3);
  padding: var(--space-md);
  border-radius: var(--radius-md);
  color: var(--neon-cyan);
  font-weight: 600;
  margin-bottom: var(--space-lg);
}

.author-name {
  font-weight: 700;
  color: var(--text-white);
  font-size: 1.1rem;
  display: block;
  margin-bottom: var(--space-xs);
}

.author-company {
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.testimonial-dots {
  display: flex;
  justify-content: center;
  gap: var(--space-sm);
  margin-top: var(--space-lg);
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  border: none;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.dot.active,
.dot:hover {
  background: var(--neon-cyan);
  box-shadow: 0 0 10px var(--neon-cyan);
  transform: scale(1.2);
}

/* Contact Section - Fixed scroll positioning */
.contact {
  padding: var(--space-2xl) 0;
  background: linear-gradient(135deg, var(--bg-tertiary), var(--bg-accent));
  scroll-margin-top: 120px;
}

.contact-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-2xl);
  align-items: start;
}

.contact-info .section-title {
  text-align: left;
  margin-bottom: var(--space-md);
}

.contact-info .section-subtitle {
  text-align: left;
  margin-bottom: var(--space-xl);
}

.contact-details {
  display: flex;
  flex-direction: column;
  gap: var(--space-lg);
}

.contact-item {
  display: flex;
  align-items: center;
  gap: var(--space-md);
  padding: var(--space-md);
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-md);
  transition: all var(--transition-normal);
}

.contact-item:hover {
  border-color: rgba(0, 255, 255, 0.3);
  transform: translateX(10px);
  box-shadow: 0 5px 15px rgba(0, 255, 255, 0.1);
}

.contact-icon {
  font-size: 1.5rem;
  filter: drop-shadow(0 0 10px var(--neon-cyan));
}

.contact-link {
  color: var(--text-white);
  text-decoration: none;
  transition: all var(--transition-fast);
}

.contact-link:hover {
  color: var(--neon-cyan);
  text-shadow: 0 0 10px var(--neon-cyan);
}

.whatsapp-link {
  cursor: pointer;
}

.contact-form-wrapper {
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-lg);
  padding: var(--space-xl);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

.form-title {
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--text-white);
  text-align: center;
  margin-bottom: var(--space-sm);
}

.form-subtitle {
  color: var(--text-secondary);
  text-align: center;
  margin-bottom: var(--space-xl);
}

.form-group {
  margin-bottom: var(--space-lg);
}

.form-control {
  width: 100%;
  padding: var(--space-md);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-md);
  color: var(--text-white);
  font-family: var(--font-primary);
  font-size: 1rem;
  transition: all var(--transition-fast);
}

.form-control:focus {
  outline: none;
  border-color: var(--neon-cyan);
  box-shadow: 0 0 0 3px rgba(0, 255, 255, 0.2);
  background: rgba(255, 255, 255, 0.08);
}

.form-control::placeholder {
  color: var(--text-muted);
}

/* Footer */
.footer {
  background: var(--bg-primary);
  padding: var(--space-2xl) 0 var(--space-lg) 0;
  border-top: 1px solid var(--glass-border);
}

.footer-content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: var(--space-2xl);
  margin-bottom: var(--space-xl);
}

.footer-brand .brand {
  display: flex;
  align-items: center;
  gap: var(--space-md);
  margin-bottom: var(--space-md);
}

.footer-description {
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: var(--space-lg);
}

.social-links {
  display: flex;
  gap: var(--space-md);
}

.social-link {
  width: 40px;
  height: 40px;
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-white);
  text-decoration: none;
  transition: all var(--transition-normal);
  cursor: pointer;
}

.social-link:hover {
  border-color: var(--neon-cyan);
  background: rgba(0, 255, 255, 0.1);
  box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
  transform: translateY(-2px);
}

.footer-links {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-xl);
}

.footer-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-white);
  margin-bottom: var(--space-md);
}

.footer-list {
  list-style: none;
}

.footer-list li {
  margin-bottom: var(--space-sm);
}

.footer-link {
  color: var(--text-secondary);
  text-decoration: none;
  transition: all var(--transition-fast);
  cursor: pointer;
}

.footer-link:hover {
  color: var(--neon-cyan);
  text-shadow: 0 0 5px var(--neon-cyan);
}

.footer-bottom {
  text-align: center;
  padding-top: var(--space-lg);
  border-top: 1px solid var(--glass-border);
  color: var(--text-muted);
}

/* FIXED Responsive Design - Updated for better mobile experience */
@media (max-width: 768px) {
  .navbar {
    /* FIXED: Better mobile navbar positioning */
    top: var(--space-sm);
    left: var(--space-sm);
    right: var(--space-sm);
    transform: none;
    border-radius: var(--radius-lg);
  }

  .nav-container {
    padding: var(--space-sm);
  }

  .brand-text {
    display: none;
  }

  .nav-menu {
    position: fixed;
    top: 80px;
    left: -100%;
    width: 100%;
    height: calc(100vh - 80px);
    background: rgba(10, 10, 10, 0.95);
    backdrop-filter: blur(20px);
    flex-direction: column;
    justify-content: start;
    align-items: center;
    padding: var(--space-xl);
    transition: left var(--transition-normal);
    z-index: 999;
  }

  .nav-menu.active {
    left: 0;
  }

  .hamburger {
    display: flex;
  }

  .hamburger.active span:nth-child(1) {
    transform: rotate(45deg) translate(5px, 5px);
  }

  .hamburger.active span:nth-child(2) {
    opacity: 0;
  }

  .hamburger.active span:nth-child(3) {
    transform: rotate(-45deg) translate(7px, -6px);
  }

  .hero {
    min-height: 80vh;
    padding: var(--space-xl) 0;
    /* FIXED: Reduced mobile padding */
    padding-top: calc(var(--space-xl) + 60px);
  }

  .hero-cta {
    flex-direction: column;
    align-items: center;
  }

  .hero-stats {
    grid-template-columns: repeat(2, 1fr);
  }

  .services-grid {
    grid-template-columns: 1fr;
  }

  /* FIXED: Ensure services section is visible on mobile */
  .services {
    scroll-margin-top: 80px;
    padding-top: calc(var(--space-xl) + 20px);
  }

  .contact-content {
    grid-template-columns: 1fr;
  }

  .footer-content {
    grid-template-columns: 1fr;
  }

  .footer-links {
    grid-template-columns: 1fr;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .hero-stats {
    grid-template-columns: 1fr;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .services-grid {
    grid-template-columns: 1fr;
  }

  .service-card {
    padding: var(--space-lg);
  }

  .container {
    padding: 0 var(--space-md);
  }
}

/* Accessibility */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

:focus-visible {
  outline: 2px solid var(--neon-cyan);
  outline-offset: 2px;
}

/* Scrollbar Styling */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: var(--bg-primary);
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, var(--neon-cyan), var(--neon-magenta));
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, var(--neon-magenta), var(--neon-yellow));
}

/* ADDITIONAL FIXES FOR SERVICES VISIBILITY */

/* Ensure all sections have proper scroll positioning */
section[id] {
  scroll-margin-top: 120px;
}

@media (max-width: 768px) {
  section[id] {
    scroll-margin-top: 80px;
  }
}

/* Force services section to be visible */
#services {
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
}

#services .services-grid {
  display: grid !important;
  visibility: visible !important;
}

#services .service-card {
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
}
"""

# Append the remaining dark theme styles
with open('style_fixed.css', 'a', encoding='utf-8') as f:
    f.write(remaining_dark_theme)

print("Completed the CSS file with all fixes for Services section visibility and improved header gap")