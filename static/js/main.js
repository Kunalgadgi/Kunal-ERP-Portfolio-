document.addEventListener('DOMContentLoaded', function () {
    // Dark/Light mode toggle
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const body = document.body;

    // Check for saved theme preference, otherwise detect system theme
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const initialTheme = savedTheme || (systemPrefersDark ? 'dark' : 'light');
    
    body.setAttribute('data-theme', initialTheme);
    updateThemeIcon(initialTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            const currentTheme = body.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            
            body.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
    }

    function updateThemeIcon(theme) {
        if (themeIcon) {
            themeIcon.className = theme === 'light' ? 'bi bi-moon' : 'bi bi-sun';
        }
    }

    // Smooth scroll for in-page anchors
    document.querySelectorAll('a[href*="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            const hash = this.getAttribute('href').split('#')[1];
            if (hash && document.getElementById(hash) && window.location.pathname === this.pathname.replace(window.location.origin, '') || (hash && document.getElementById(hash) && this.getAttribute('href').startsWith('#'))) {
                const target = document.getElementById(hash);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth' });
                    const navMenu = document.getElementById('navMenu');
                    if (navMenu && navMenu.classList.contains('show')) {
                        new bootstrap.Collapse(navMenu).hide();
                    }
                }
            }
        });
    });

    // Navbar auto-hide on scroll
    const navbar = document.querySelector('.custom-navbar');
    let lastScrollTop = 0;
    let scrollTimeout;

    window.addEventListener('scroll', function () {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Clear previous timeout
        clearTimeout(scrollTimeout);
        
        // Hide navbar when scrolling down, show when scrolling up
        if (scrollTop > lastScrollTop && scrollTop > 100) {
            // Scrolling down
            navbar.classList.add('nav-hidden');
            navbar.classList.remove('nav-visible');
        } else {
            // Scrolling up or at top
            navbar.classList.remove('nav-hidden');
            navbar.classList.add('nav-visible');
        }
        
        // Add shadow when scrolled
        if (scrollTop > 30) {
            navbar.style.boxShadow = '0 4px 20px rgba(0,0,0,0.25)';
        } else {
            navbar.style.boxShadow = 'none';
        }
        
        lastScrollTop = scrollTop;
        
        // Reset to visible after scrolling stops
        scrollTimeout = setTimeout(() => {
            if (scrollTop > 0) {
                navbar.classList.remove('nav-hidden');
                navbar.classList.add('nav-visible');
            }
        }, 1500);
    });

    // Animate skill progress bars when visible
    const bars = document.querySelectorAll('.progress-bar[data-width]');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const bar = entry.target;
                bar.style.width = bar.getAttribute('data-width') + '%';
                observer.unobserve(bar);
            }
        });
    }, { threshold: 0.3 });
    bars.forEach(bar => observer.observe(bar));
});
