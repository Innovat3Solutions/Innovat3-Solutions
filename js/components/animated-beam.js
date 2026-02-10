/**
 * Animated Beam Component
 * Connects elements with animated SVG paths.
 */

class AnimatedBeam {
    constructor(containerSelector, options = {}) {
        this.container = document.querySelector(containerSelector);
        if (!this.container) return;

        this.svg = this.container.querySelector('svg.beam-svg');
        if (!this.svg) {
            this.svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
            this.svg.classList.add('beam-svg');
            this.svg.style.position = 'absolute';
            this.svg.style.top = '0';
            this.svg.style.left = '0';
            this.svg.style.width = '100%';
            this.svg.style.height = '100%';
            this.svg.style.pointerEvents = 'none';
            this.svg.style.zIndex = '1';
            this.container.appendChild(this.svg);
        }

        this.centerNode = this.container.querySelector(options.centerSelector || '.beam-center');
        this.outerNodes = this.container.querySelectorAll(options.outerSelector || '.beam-node');

        this.options = {
            color: options.color || '#84CC16',
            duration: options.duration || 3,
            ...options
        };

        this.init();
        window.addEventListener('resize', () => this.updatePaths());
    }

    init() {
        this.paths = [];
        this.outerNodes.forEach((node, index) => {
            const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
            path.setAttribute("stroke", "rgba(0,0,0,0.1)");
            path.setAttribute("stroke-width", "2");
            path.setAttribute("fill", "none");
            this.svg.appendChild(path);

            // Beam path (the animated one)
            const beamPath = document.createElementNS("http://www.w3.org/2000/svg", "path");
            beamPath.setAttribute("stroke", this.options.color);
            beamPath.setAttribute("stroke-width", "2");
            beamPath.setAttribute("stroke-linecap", "round");
            beamPath.setAttribute("fill", "none");
            beamPath.style.opacity = "0"; // Start hidden
            this.svg.appendChild(beamPath);

            this.paths.push({ bg: path, beam: beamPath, node: node, index: index });
        });

        this.updatePaths();
        this.animate();
    }

    getCenter(element) {
        const rect = element.getBoundingClientRect();
        const containerRect = this.container.getBoundingClientRect();
        return {
            x: rect.left - containerRect.left + rect.width / 2,
            y: rect.top - containerRect.top + rect.height / 2
        };
    }

    updatePaths() {
        if (!this.centerNode) return;

        const centerPos = this.getCenter(this.centerNode);

        this.paths.forEach(item => {
            const nodePos = this.getCenter(item.node);

            // Calculate Control Points for a nice curve
            // Simple Quadratic Bezier logic: Midpoint with offset? 
            // Or simple variable curvature based on relative position.

            const dx = centerPos.x - nodePos.x;
            const dy = centerPos.y - nodePos.y;

            // Curvature control
            const controlX = nodePos.x + dx * 0.5;
            const controlY = nodePos.y; // Keep Y flat at start? 

            // Let's use a standard "connector" curve: Horizontal out, then Vertical
            // Path: M startX,startY C c1x,c1y c2x,c2y endX,endY

            const d = `M ${nodePos.x},${nodePos.y} 
                       C ${nodePos.x + dx * 0.5},${nodePos.y} 
                         ${centerPos.x - dx * 0.5},${centerPos.y} 
                         ${centerPos.x},${centerPos.y}`;

            item.bg.setAttribute("d", d);
            item.beam.setAttribute("d", d);
            item.length = item.beam.getTotalLength();

            // Set up dash array for animation
            item.beam.style.strokeDasharray = item.length;
            item.beam.style.strokeDashoffset = item.length;
        });
    }

    animate() {
        const flow = () => {
            this.paths.forEach((item, i) => {
                // Staggered animation
                const delay = i * 1000;

                // Keyframe-like animation using JS or CSS transitions is tedious.
                // Let's use a CSS Class triggering.

                // Actually, CSS animation with --dash-offset variable is best.
                // But we need dynamic length. 
                // Let's just create a style tag for specific keyframes or use Web Animations API.

                item.beam.animate([
                    { strokeDashoffset: item.length, opacity: 1 },
                    { strokeDashoffset: 0, opacity: 1 },
                    { strokeDashoffset: -item.length, opacity: 0 }
                ], {
                    duration: 3000,
                    delay: i * 500, // Stagger
                    iterations: Infinity,
                    easing: 'linear'
                });
            });
        };

        flow();
    }
}
