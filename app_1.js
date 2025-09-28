// Dashboard JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Code Quality Trends Chart
    initializeQualityChart();

    // Initialize animations
    initializeAnimations();

    // Add interactive functionality
    initializeInteractivity();
});

// Initialize the Code Quality Trends Chart using Chart.js
function initializeQualityChart() {
    const ctx = document.getElementById('qualityChart');
    if (!ctx) return;

    // Data from the provided JSON
    const qualityData = {
        'v2.6': 80,
        'v2.5': 75,
        'v2.4': 72,
        'v2.3': 68,
        'v2.2': 65,
        'v2.1': 58
    };

    const labels = Object.keys(qualityData);
    const data = Object.values(qualityData);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Quality Score (%)',
                data: data,
                backgroundColor: ['#1FB8CD', '#FFC185', '#B4413C', '#ECEBD5', '#5D878F', '#DB4545'],
                borderColor: ['#1FB8CD', '#FFC185', '#B4413C', '#ECEBD5', '#5D878F', '#DB4545'],
                borderWidth: 2,
                borderRadius: 4,
                borderSkipped: false,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    borderColor: '#1FB8CD',
                    borderWidth: 1,
                    callbacks: {
                        label: function(context) {
                            return `Quality Score: ${context.parsed.y}%`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        color: '#a7a9a9',
                        font: {
                            size: 11
                        },
                        callback: function(value) {
                            return value + '%';
                        }
                    },
                    grid: {
                        color: 'rgba(167, 169, 169, 0.1)',
                        drawBorder: false
                    }
                },
                x: {
                    ticks: {
                        color: '#a7a9a9',
                        font: {
                            size: 11
                        }
                    },
                    grid: {
                        display: false
                    }
                }
            },
            animation: {
                duration: 1500,
                easing: 'easeOutQuart'
            }
        }
    });
}

// Initialize animations for progress bars and other elements
function initializeAnimations() {
    // Animate progress bars on load
    const progressFills = document.querySelectorAll('.progress-fill, .coverage-fill, .score-fill');

    // Set initial width to 0 and animate to target width
    progressFills.forEach(fill => {
        const targetWidth = fill.style.width;
        fill.style.width = '0%';
        fill.style.transition = 'width 1.5s ease-out';

        setTimeout(() => {
            fill.style.width = targetWidth;
        }, 200);
    });

    // Animate metric values counting up (only once)
    animateCountersOnce();

    // Add staggered animations for dashboard cards
    animateCards();
}

// Animate counter values only once to prevent value changes
function animateCountersOnce() {
    const counters = document.querySelectorAll('.metric-value .value, .vuln-count, .score-value');

    counters.forEach(counter => {
        // Skip if already animated
        if (counter.dataset.animated === 'true') return;

        const originalText = counter.textContent;
        const number = parseFloat(originalText.replace(/[^\d.]/g, ''));

        if (!isNaN(number) && number > 0) {
            let current = 0;
            const increment = number / 60; // Animate over ~1 second (60 frames)
            const suffix = originalText.replace(number.toString(), '');

            counter.textContent = '0' + suffix;

            const timer = setInterval(() => {
                current += increment;
                if (current >= number) {
                    counter.textContent = originalText; // Restore original value
                    counter.dataset.animated = 'true'; // Mark as animated
                    clearInterval(timer);
                } else {
                    const displayValue = Math.floor(current);
                    counter.textContent = displayValue + suffix;
                }
            }, 16); // ~60fps
        } else {
            counter.dataset.animated = 'true'; // Mark as processed
        }
    });
}

// Animate dashboard cards with staggered entrance
function animateCards() {
    const cards = document.querySelectorAll('.dashboard-card');

    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';

        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100); // Stagger by 100ms
    });
}

// Initialize interactive functionality
function initializeInteractivity() {
    // Add hover effects and tooltips
    initializeTooltips();

    // Add click handlers for expandable sections
    initializeExpandableSections();

    // Add action item checkbox functionality
    initializeActionItems();

    // Add metric card click handlers
    initializeMetricCards();
}

// Initialize tooltips for additional context
function initializeTooltips() {
    const tooltipElements = [
        { selector: '.metric-item', content: 'Performance metric - click for details' },
        { selector: '.hotspot-item', content: 'Technical debt hotspot requiring attention' },
        { selector: '.scan-tool', content: 'Security scan tool results' },
        { selector: '.vuln-stat', content: 'Vulnerability count by severity level' },
        { selector: '.gate-item', content: 'Quality gate status indicator' },
        { selector: '.goal-item', content: 'Quality improvement target and timeline' }
    ];

    tooltipElements.forEach(({ selector, content }) => {
        const elements = document.querySelectorAll(selector);
        elements.forEach(element => {
            element.setAttribute('title', content);

            // Add enhanced hover effect
            element.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-2px)';
                this.style.boxShadow = '0 8px 25px rgba(0, 0, 0, 0.15)';
                this.style.transition = 'all 0.3s ease-out';
            });

            element.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
                this.style.boxShadow = '';
            });
        });
    });
}

// Initialize expandable sections
function initializeExpandableSections() {
    const expandableCards = document.querySelectorAll('.dashboard-card');

    expandableCards.forEach(card => {
        const header = card.querySelector('.card-header');
        if (header) {
            header.style.cursor = 'pointer';
            header.addEventListener('click', function() {
                const body = card.querySelector('.card-body');
                const isExpanded = card.classList.contains('expanded');

                if (isExpanded) {
                    card.classList.remove('expanded');
                    body.style.maxHeight = 'none';
                    header.style.borderBottomLeftRadius = '';
                    header.style.borderBottomRightRadius = '';
                } else {
                    card.classList.add('expanded');
                    body.style.maxHeight = body.scrollHeight + 'px';
                    header.style.borderBottomLeftRadius = '0';
                    header.style.borderBottomRightRadius = '0';
                }
            });
        }
    });
}

// Initialize action items functionality
function initializeActionItems() {
    const actionCheckboxes = document.querySelectorAll('.action-item input[type="checkbox"]');

    actionCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const label = this.nextElementSibling;
            const actionItem = this.parentElement;

            if (this.checked) {
                label.style.textDecoration = 'line-through';
                label.style.opacity = '0.6';
                actionItem.style.backgroundColor = 'rgba(33, 128, 141, 0.1)';
                actionItem.style.borderColor = 'rgba(33, 128, 141, 0.3)';

                // Add completion animation
                actionItem.style.transform = 'scale(1.02)';
                setTimeout(() => {
                    actionItem.style.transform = 'scale(1)';
                }, 200);
            } else {
                label.style.textDecoration = 'none';
                label.style.opacity = '1';
                actionItem.style.backgroundColor = '';
                actionItem.style.borderColor = '';
            }
        });
    });
}

// Initialize metric cards with click functionality
function initializeMetricCards() {
    const metricItems = document.querySelectorAll('.metric-item');

    metricItems.forEach(item => {
        item.addEventListener('click', function() {
            // Add a temporary highlight effect
            this.style.backgroundColor = 'rgba(33, 128, 141, 0.2)';
            this.style.transform = 'scale(1.05)';
            this.style.borderColor = 'rgba(33, 128, 141, 0.5)';

            setTimeout(() => {
                this.style.backgroundColor = '';
                this.style.transform = 'scale(1)';
                this.style.borderColor = '';
            }, 300);

            // Show metric details in console (could be expanded to modal)
            const metricName = this.querySelector('.metric-label').textContent;
            const metricValue = this.querySelector('.metric-value .value').textContent;
            console.log(`${metricName}: ${metricValue} - Detailed metrics would appear here`);
        });
    });

    // Add click handlers for other interactive elements
    const clickableElements = document.querySelectorAll('.hotspot-item, .scan-tool, .sonar-metric');
    clickableElements.forEach(element => {
        element.style.cursor = 'pointer';
        element.addEventListener('click', function() {
            this.style.backgroundColor = 'rgba(33, 128, 141, 0.1)';
            setTimeout(() => {
                this.style.backgroundColor = '';
            }, 300);
        });
    });
}

// Add keyboard navigation support
document.addEventListener('keydown', function(e) {
    if (e.key === 'Tab') {
        // Ensure good keyboard navigation
        const focusableElements = document.querySelectorAll(
            'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"]), .metric-item, .dashboard-card .card-header'
        );

        focusableElements.forEach(element => {
            element.addEventListener('focus', function() {
                this.style.outline = '2px solid #1FB8CD';
                this.style.outlineOffset = '2px';
            });

            element.addEventListener('blur', function() {
                this.style.outline = '';
                this.style.outlineOffset = '';
            });
        });
    }
});

// Performance monitoring
function trackPerformance() {
    if (window.performance && window.performance.mark) {
        window.performance.mark('dashboard-loaded');

        window.addEventListener('load', () => {
            setTimeout(() => {
                const loadTime = performance.now();
                console.log(`Dashboard loaded in ${loadTime.toFixed(2)}ms`);
            }, 0);
        });
    }
}

// Initialize performance tracking
trackPerformance();

// Prevent any unintended data updates by ensuring animations only run once
let animationsInitialized = false;

// Override the initialization to prevent multiple calls
const originalInitializeAnimations = initializeAnimations;
initializeAnimations = function() {
    if (!animationsInitialized) {
        originalInitializeAnimations();
        animationsInitialized = true;
    }
};