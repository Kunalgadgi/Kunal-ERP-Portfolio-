document.addEventListener('DOMContentLoaded', function () {
    // Dark/Light mode toggle
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const body = document.body;

    // Check for saved theme preference or default to light
    const savedTheme = localStorage.getItem('theme') || 'light';
    body.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

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

    // Navbar shadow on scroll
    const navbar = document.querySelector('.custom-navbar');
    window.addEventListener('scroll', function () {
        if (window.scrollY > 30) {
            navbar.style.boxShadow = '0 4px 20px rgba(0,0,0,0.25)';
        } else {
            navbar.style.boxShadow = 'none';
        }
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
