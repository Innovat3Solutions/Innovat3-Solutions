/**
 * Animated Grid Pattern (Vanilla JS Port)
 * Based on Magic UI React Component
 */

class AnimatedGrid {
    constructor(containerId, options = {}) {
        this.container = document.getElementById(containerId);
        if (!this.container) return;

        this.options = {
            width: options.width || 40,
            height: options.height || 40,
            x: options.x || -1,
            y: options.y || -1,
            strokeDasharray: options.strokeDasharray || 0,
            numSquares: options.numSquares || 30, // Default 30 random squares
            maxOpacity: options.maxOpacity || 0.3,
            duration: options.duration || 3, // Seconds
            repeatDelay: options.repeatDelay || 1, // Seconds
            ...options
        };

        this.squares = [];
        this.svgNS = "http://www.w3.org/2000/svg";
        this.init();
    }

    init() {
        // Create SVG structure
        this.svg = document.createElementNS(this.svgNS, "svg");
        this.svg.setAttribute("aria-hidden", "true");
        this.svg.classList.add("animated-grid-pattern");
        this.svg.style.width = "100%";
        this.svg.style.height = "100%";

        // Define Defs for Pattern
        const defs = document.createElementNS(this.svgNS, "defs");
        const patternId = "grid-pattern-" + Math.random().toString(36).substr(2, 9);
        this.patternId = patternId;

        const pattern = document.createElementNS(this.svgNS, "pattern");
        pattern.setAttribute("id", patternId);
        pattern.setAttribute("width", this.options.width);
        pattern.setAttribute("height", this.options.height);
        pattern.setAttribute("patternUnits", "userSpaceOnUse");
        pattern.setAttribute("x", this.options.x);
        pattern.setAttribute("y", this.options.y);

        const path = document.createElementNS(this.svgNS, "path");
        path.setAttribute("d", `M.5 ${this.options.height}V.5H${this.options.width}`);
        path.setAttribute("fill", "none");
        path.setAttribute("stroke-dasharray", this.options.strokeDasharray);

        // Append elements
        pattern.appendChild(path);
        defs.appendChild(pattern);
        this.svg.appendChild(defs);

        // Background Rect (The Grid Lines)
        const bgRect = document.createElementNS(this.svgNS, "rect");
        bgRect.setAttribute("width", "100%");
        bgRect.setAttribute("height", "100%");
        bgRect.setAttribute("fill", `url(#${patternId})`);
        this.svg.appendChild(bgRect);

        // Squares Container
        this.squaresGroup = document.createElementNS(this.svgNS, "svg");
        this.squaresGroup.setAttribute("x", this.options.x);
        this.squaresGroup.setAttribute("y", this.options.y);
        this.squaresGroup.classList.add("overflow-visible");
        this.svg.appendChild(this.squaresGroup);

        this.container.appendChild(this.svg);

        // Initialize Squares
        this.updateDimensions();

        // Resize Observer
        const resizeObserver = new ResizeObserver(() => {
            this.updateDimensions();
        });
        resizeObserver.observe(this.container);

        // Start Animation Loop (Interval based to pick new squares)
        // Note: For Vanilla JS, CSS Animations are more performant for the fading,
        // we just need JS to move them around.

        // Actually, let's generate N static rects and animate them with CSS
        this.renderSquares();
    }

    updateDimensions() {
        const rect = this.container.getBoundingClientRect();
        this.width = rect.width;
        this.height = rect.height;
    }

    getPos() {
        return [
            Math.floor((Math.random() * this.width) / this.options.width),
            Math.floor((Math.random() * this.height) / this.options.height),
        ];
    }

    renderSquares() {
        // Clear existing
        this.squaresGroup.innerHTML = '';

        for (let i = 0; i < this.options.numSquares; i++) {
            this.addSquare(i);
        }
    }

    addSquare(index) {
        const [x, y] = this.getPos();
        const rect = document.createElementNS(this.svgNS, "rect");

        rect.setAttribute("width", this.options.width - 1);
        rect.setAttribute("height", this.options.height - 1);
        rect.setAttribute("x", x * this.options.width + 1);
        rect.setAttribute("y", y * this.options.height + 1);
        rect.setAttribute("fill", "currentColor");
        rect.setAttribute("stroke-width", "0");

        // Animation
        rect.style.opacity = "0";
        rect.classList.add("grid-square-anim");

        // Randomize delays slightly so they don't all pulse in sync
        const delay = Math.random() * 5;
        rect.style.animationDelay = `${delay}s`;

        // Random duration
        const duration = this.options.duration + Math.random() * 2;
        rect.style.animationDuration = `${duration}s`;

        // When animation iterates, we ideally want to move it.
        // Pure CSS can't move it easily. We can use 'animationiteration' event.
        rect.addEventListener('animationiteration', () => {
            const [newX, newY] = this.getPos();
            rect.setAttribute("x", newX * this.options.width + 1);
            rect.setAttribute("y", newY * this.options.height + 1);
        });

        this.squaresGroup.appendChild(rect);
    }
}

// Auto-init helper
function initAnimatedGrid(id, options) {
    new AnimatedGrid(id, options);
}
