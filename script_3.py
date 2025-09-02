# Add the dark theme specific styles with FIXES for Services section visibility and header gap
dark_theme_fixes = """
/* Dark Theme AI Portfolio Landing Page - FIXED VERSION */

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Root Variables - Exact Dark Theme Colors */
:root {
  /* Primary Dark Background */
  --bg-primary: #0a0a0a;
  --bg-secondary: #1a1a2e;
  --bg-tertiary: #16213e;
  --bg-accent: #0f0f23;
  
  /* Neon Accent Colors */
  --neon-cyan: #00ffff;
  --neon-magenta: #ff00ff;
  --neon-yellow: #ffff00;
  
  /* Glass Morphism */
  --glass-bg: rgba(255, 255, 255, 0.05);
  --glass-border: rgba(255, 255, 255, 0.1);
  --glass-blur: blur(20px);
  
  /* Typography */
  --font-primary: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --text-white: #ffffff;
  --text-secondary: rgba(255, 255, 255, 0.7);
  --text-muted: rgba(255, 255, 255, 0.5);
  
  /* Spacing */
  --space-xs: 8px;
  --space-sm: 16px;
  --space-md: 24px;
  --space-lg: 32px;
  --space-xl: 48px;
  --space-2xl: 64px;
  
  /* Border Radius */
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --radius-xl: 32px;
  
  /* Transitions */
  --transition-fast: 0.2s ease;
  --transition-normal: 0.4s ease;
  --transition-slow: 0.6s ease;
}

/* Base Styles */
html {
  font-size: 16px;
  font-family: var(--font-primary);
  scroll-behavior: smooth;
}

body {
  background: var(--bg-primary);
  color: var(--text-white);
  font-family: var(--font-primary);
  line-height: 1.6;
  overflow-x: hidden;
}

/* Animated Background Gradient */
@keyframes gradientShift {
  0% {
    background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 25%, var(--bg-tertiary) 50%, var(--bg-accent) 100%);
  }
  25% {
    background: linear-gradient(135deg, var(--bg-secondary) 0%, var(--bg-tertiary) 25%, var(--bg-accent) 50%, var(--bg-primary) 100%);
  }
  50% {
    background: linear-gradient(135deg, var(--bg-tertiary) 0%, var(--bg-accent) 25%, var(--bg-primary) 50%, var(--bg-secondary) 100%);
  }
  75% {
    background: linear-gradient(135deg, var(--bg-accent) 0%, var(--bg-primary) 25%, var(--bg-secondary) 50%, var(--bg-tertiary) 100%);
  }
  100% {
    background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 25%, var(--bg-tertiary) 50%, var(--bg-accent) 100%);
  }
}

/* Gradient Text Animation */
@keyframes gradientText {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

.gradient-text {
  background: linear-gradient(135deg, var(--neon-cyan), var(--neon-magenta), var(--neon-yellow), var(--neon-cyan));
  background-size: 300% 300%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gradientText 3s ease infinite;
  font-weight: 700;
}

/* Floating Animation */
@keyframes floating {
  0%, 100% {
    transform: translateY(0px) rotate(0deg);
  }
  33% {
    transform: translateY(-20px) rotate(120deg);
  }
  66% {
    transform: translateY(10px) rotate(240deg);
  }
}

/* FIXED Navigation - Glass Morphism with better header gap */
.navbar {
  position: fixed;
  top: var(--space-lg); /* CHANGED: from var(--space-sm) to var(--space-lg) for better gap */
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-xl);
  padding: var(--space-sm) var(--space-lg);
  transition: all var(--transition-normal);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.navbar.scrolled {
  background: rgba(10, 10, 10, 0.8);
  backdrop-filter: blur(25px);
  border-color: rgba(0, 255, 255, 0.2);
  box-shadow: 0 8px 32px rgba(0, 255, 255, 0.1);
}

.nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1200px;
  margin: 0 auto;
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: var(--space-sm);
}

.brand-logo {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, var(--neon-cyan), var(--neon-magenta));
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--bg-primary);
  transition: all var(--transition-normal);
}

.brand-logo:hover {
  transform: scale(1.1);
  box-shadow: 0 0 20px var(--neon-cyan);
}

.brand-text {
  display: flex;
  flex-direction: column;
}

/* PRESERVED - "Adarsh M" branding as in dark theme */
.brand-name {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-white);
  /* Maintain the original dark theme styling */
  text-shadow: 0 0 5px rgba(255, 255, 255, 0.3);
}

.brand-tagline {
  font-size: 12px;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.nav-menu {
  display: flex;
  list-style: none;
  gap: var(--space-lg);
}

.nav-link {
  color: var(--text-secondary);
  text-decoration: none;
  font-weight: 500;
  transition: all var(--transition-fast);
  position: relative;
  padding: var(--space-xs) 0;
}

.nav-link:hover,
.nav-link.active {
  color: var(--neon-cyan);
  text-shadow: 0 0 10px var(--neon-cyan);
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--neon-cyan);
  transition: width var(--transition-fast);
  box-shadow: 0 0 10px var(--neon-cyan);
}

.nav-link:hover::after,
.nav-link.active::after {
  width: 100%;
}

.hamburger {
  display: none;
  flex-direction: column;
  cursor: pointer;
  gap: 4px;
}

.hamburger span {
  width: 24px;
  height: 2px;
  background: var(--text-white);
  transition: all var(--transition-fast);
  border-radius: 1px;
}

/* Hero Section - Dark Theme with Animation */
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  position: relative;
  padding: var(--space-2xl) 0;
  /* ADDED: Extra padding top to account for fixed navbar with increased gap */
  padding-top: calc(var(--space-2xl) + 100px);
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  animation: gradientShift 15s ease infinite;
  z-index: 1;
}

.animated-bg {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 25%, var(--bg-tertiary) 50%, var(--bg-accent) 100%);
  background-size: 400% 400%;
  animation: gradientShift 15s ease infinite;
}

.floating-shape {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--neon-cyan), var(--neon-magenta));
  opacity: 0.1;
  animation: floating 20s ease-in-out infinite;
}

.shape-1 {
  width: 300px;
  height: 300px;
  top: 10%;
  right: 10%;
  animation-delay: -5s;
}

.shape-2 {
  width: 200px;
  height: 200px;
  bottom: 20%;
  left: 5%;
  animation-delay: -10s;
}

.shape-3 {
  width: 150px;
  height: 150px;
  top: 60%;
  right: 30%;
  animation-delay: -15s;
}

.neon-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(40px);
  opacity: 0.3;
  animation: floating 25s ease-in-out infinite;
}

.orb-1 {
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, var(--neon-cyan), transparent);
  top: -200px;
  right: -200px;
  animation-delay: -8s;
}

.orb-2 {
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, var(--neon-magenta), transparent);
  bottom: -150px;
  left: -150px;
  animation-delay: -12s;
}

.orb-3 {
  width: 250px;
  height: 250px;
  background: radial-gradient(circle, var(--neon-yellow), transparent);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  animation-delay: -18s;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--space-lg);
  position: relative;
  z-index: 2;
}

.hero-content {
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
}

.hero-title {
  font-size: clamp(2.5rem, 6vw, 5rem);
  line-height: 1.2;
  margin-bottom: var(--space-lg);
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
}

.hero-subtitle-text {
  font-size: clamp(1.5rem, 4vw, 2.5rem);
  color: var(--text-white);
  font-weight: 600;
  text-shadow: 0 0 20px rgba(255, 255, 255, 0.5);
}

.hero-subtitle {
  font-size: clamp(1.1rem, 2vw, 1.3rem);
  color: var(--text-secondary);
  margin-bottom: var(--space-xl);
  line-height: 1.7;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.hero-cta {
  display: flex;
  gap: var(--space-lg);
  justify-content: center;
  margin-bottom: var(--space-2xl);
  flex-wrap: wrap;
}

.hero-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: var(--space-lg);
  max-width: 600px;
  margin: 0 auto;
}

.stat-item {
  text-align: center;
  padding: var(--space-md);
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-lg);
  transition: all var(--transition-normal);
}

.stat-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 255, 255, 0.2);
  border-color: rgba(0, 255, 255, 0.3);
}

.stat-number {
  display: block;
  font-size: 2.5rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--neon-cyan), var(--neon-magenta));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: var(--space-xs);
}

.stat-label {
  font-size: 0.9rem;
  color: var(--text-secondary);
  font-weight: 500;
}

/* Button Styles - Neon Theme */
.btn {
  padding: var(--space-sm) var(--space-lg);
  border-radius: var(--radius-md);
  font-family: var(--font-primary);
  font-weight: 600;
  font-size: 1rem;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: var(--space-xs);
  cursor: pointer;
  transition: all var(--transition-normal);
  border: none;
  position: relative;
  overflow: hidden;
}

.btn--primary {
  background: linear-gradient(135deg, var(--neon-cyan), var(--neon-magenta));
  color: var(--bg-primary);
  box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
}

.btn--primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 0 30px rgba(0, 255, 255, 0.5), 0 10px 20px rgba(0, 0, 0, 0.3);
}

.btn--outline {
  background: transparent;
  color: var(--text-white);
  border: 2px solid var(--glass-border);
  backdrop-filter: var(--glass-blur);
}

.btn--outline:hover {
  border-color: var(--neon-cyan);
  color: var(--neon-cyan);
  box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
  text-shadow: 0 0 10px var(--neon-cyan);
}

.btn--neon {
  background: transparent;
  color: var(--neon-cyan);
  border: 1px solid var(--neon-cyan);
  box-shadow: 0 0 10px rgba(0, 255, 255, 0.2);
}

.btn--neon:hover {
  background: var(--neon-cyan);
  color: var(--bg-primary);
  box-shadow: 0 0 20px var(--neon-cyan);
  text-shadow: none;
}

.btn--lg {
  padding: var(--space-md) var(--space-xl);
  font-size: 1.1rem;
}

.btn--sm {
  padding: var(--space-xs) var(--space-sm);
  font-size: 0.9rem;
}

.btn--full-width {
  width: 100%;
  justify-content: center;
}

.btn-icon {
  font-size: 1.2em;
}

/* FIXED Services Section - Glass Morphism Cards with proper visibility */
.services {
  padding: var(--space-2xl) 0;
  position: relative;
  /* ADDED: Scroll margin to account for fixed navbar */
  scroll-margin-top: 120px;
  /* ADDED: Extra top padding for better visibility when scrolled to */
  padding-top: calc(var(--space-2xl) + 40px);
}

/* Ensure services section is visible */
.services::before {
  content: '';
  display: block;
  height: 120px;
  margin-top: -120px;
  visibility: hidden;
  pointer-events: none;
}

.section-header {
  text-align: center;
  margin-bottom: var(--space-2xl);
}

.section-title {
  font-size: clamp(2rem, 5vw, 3rem);
  margin-bottom: var(--space-md);
  font-weight: 700;
}

.section-subtitle {
  font-size: 1.2rem;
  color: var(--text-secondary);
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: var(--space-lg);
  /* ADDED: Make sure grid is visible */
  position: relative;
  z-index: 1;
}

.service-card {
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-lg);
  padding: var(--space-xl);
  text-align: center;
  transition: all var(--transition-normal);
  position: relative;
  overflow: hidden;
  cursor: pointer;
  /* ADDED: Ensure visibility */
  opacity: 1;
  visibility: visible;
}
"""

# Append the fixed dark theme styles to the CSS file
with open('style_fixed.css', 'a', encoding='utf-8') as f:
    f.write(dark_theme_fixes)

print("Added fixed dark theme styles with Services section visibility and header gap improvements")