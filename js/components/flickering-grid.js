
class FlickeringGrid {
    constructor(containerSelector, options = {}) {
        this.container = document.querySelector(containerSelector);
        if (!this.container) return;

        this.options = {
            squareSize: options.squareSize || 4,
            gridGap: options.gridGap || 6,
            flickerChance: options.flickerChance || 0.3,
            color: options.color || '114, 255, 114', // Neon green in RGB
            maxOpacity: options.maxOpacity || 0.3,
            ...options
        };

        this.canvas = document.createElement('canvas');
        this.canvas.className = 'flickering-grid-canvas';
        this.ctx = this.canvas.getContext('2d');
        this.container.appendChild(this.canvas); // Append to container, ensure container is relative

        this.squares = [];
        this.resize();
        window.addEventListener('resize', () => this.resize());

        this.animate = this.animate.bind(this);
        requestAnimationFrame(this.animate);
    }

    resize() {
        this.width = this.container.offsetWidth;
        this.height = this.container.offsetHeight;
        this.canvas.width = this.width;
        this.canvas.height = this.height;
        this.initSquares();
    }

    initSquares() {
        this.squares = [];
        const { squareSize, gridGap } = this.options;
        const totalSize = squareSize + gridGap;

        const cols = Math.ceil(this.width / totalSize);
        const rows = Math.ceil(this.height / totalSize);

        for (let i = 0; i < cols; i++) {
            for (let j = 0; j < rows; j++) {
                this.squares.push({
                    x: i * totalSize,
                    y: j * totalSize,
                    opacity: Math.random() * this.options.maxOpacity,
                    targetOpacity: Math.random() * this.options.maxOpacity,
                    changeSpeed: Math.random() * 0.02 + 0.005
                });
            }
        }
    }

    update() {
        for (let square of this.squares) {
            // Randomly change target properly
            if (Math.random() < 0.005) { // Low probability to change target
                square.targetOpacity = Math.random() * this.options.maxOpacity;
            }

            // Smoothly transition opacity
            if (square.opacity < square.targetOpacity) {
                square.opacity += square.changeSpeed;
                if (square.opacity > square.targetOpacity) square.opacity = square.targetOpacity;
            } else {
                square.opacity -= square.changeSpeed;
                if (square.opacity < square.targetOpacity) square.opacity = square.targetOpacity;
            }
        }
    }

    draw() {
        this.ctx.clearRect(0, 0, this.width, this.height);
        const { squareSize, color } = this.options;

        for (let square of this.squares) {
            this.ctx.fillStyle = `rgba(${color}, ${square.opacity})`;
            this.ctx.fillRect(square.x, square.y, squareSize, squareSize);
        }
    }

    animate() {
        this.update();
        this.draw();
        requestAnimationFrame(this.animate);
    }
}
