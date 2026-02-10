
# Hero Templates
HERO_TEMPLATES = {
    "classic": """
    <header class="niche-hero hero-classic">
        <div class="container niche-hero-content">
            <div class="hero-text">
                <div class="badge" style="background: rgba(255,255,255,0.1); color: white; border: 1px solid rgba(255,255,255,0.2);">
                    {{NICHE_NAME}} Strategy
                </div>
                <h1>Digital Growth & AI for {{NICHE_NAME}}</h1>
                <p class="service-excerpt" style="font-size: 1.25rem; color: #cbd5e1; margin-bottom: 1.5rem; border-left: 3px solid var(--niche-accent); padding-left: 1rem;">
                    {{SERVICE_EXCERPT}}
                </p>
                <p class="sub-headline">{{OPPORTUNITY}}</p>
                <div class="cta-group">
                    <a href="#contact" class="btn btn-primary shiny-button" style="background: var(--niche-accent); color: black; border: none;">Book Strategy Call</a>
                </div>
                <div style="margin-top: 2rem; display: flex; align-items: center; gap: 1rem; opacity: 0.8;">
                    <div style="font-size: 0.875rem;">Trusted by top leaders in your industry</div>
                </div>
            </div>
            <div class="hero-image-wrapper">
                <img src="../../images/niche_graphics/{{IMAGE_PATH}}" alt="{{NICHE_NAME}} Dashboard" onerror="this.src='../../images/niche_graphics/graphic_general_business.png'">
            </div>
        </div>
    </header>
    """,
    "immersive": """
    <header class="niche-hero hero-immersive">
        <div class="container niche-hero-content">
            <div class="hero-text">
                <div class="badge" style="background: rgba(255,255,255,0.1); color: white; border: 1px solid rgba(255,255,255,0.2);">
                    {{NICHE_NAME}} Strategy
                </div>
                <h1>{{NICHE_NAME}} Growth Engine</h1>
                <p class="sub-headline" style="font-size: 1.5rem; color: #e2e8f0; max-width: 700px;">{{SERVICE_EXCERPT}}</p>
                <div class="cta-group" style="margin-top: 2rem;">
                    <a href="#contact" class="btn btn-primary shiny-button" style="background: var(--niche-accent); color: black; border: none; padding: 1.25rem 2.5rem; font-size: 1.1rem;">Start Your Transformation</a>
                </div>
            </div>
            <!-- Image hidden in CSS, background serves as visual -->
        </div>
    </header>
    """,
    "offset": """
    <header class="niche-hero hero-offset">
        <div class="container niche-hero-content">
            <div class="hero-text">
                <h1>{{NICHE_NAME}} <span style="color: var(--niche-accent);">Redefined</span></h1>
                <p class="service-excerpt" style="font-size: 1.1rem; color: #cbd5e1; margin-bottom: 1.5rem;">
                    {{SERVICE_EXCERPT}}
                </p>
                <div class="cta-group">
                    <a href="#contact" class="btn btn-primary shiny-button" style="background: var(--niche-accent); color: black; border: none;">Get a Proposal</a>
                </div>
            </div>
            <div class="hero-image-wrapper">
                <img src="../../images/niche_graphics/{{IMAGE_PATH}}" alt="{{NICHE_NAME}} Dashboard" style="border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;" onerror="this.src='../../images/niche_graphics/graphic_general_business.png'">
            </div>
        </div>
    </header>
    """,
    "card_stack": """
    <header class="niche-hero hero-card-stack">
        <div class="container">
            <div class="glass-card">
                <div class="hero-text">
                    <div class="badge" style="background: rgba(255,255,255,0.1); color: white; border: 1px solid rgba(255,255,255,0.2);">
                        Professional {{NICHE_NAME}} Systems
                    </div>
                    <h1>Secure AI for {{NICHE_NAME}}</h1>
                    <p class="service-excerpt" style="font-size: 1.1rem; color: #cbd5e1; margin-bottom: 2rem;">
                        {{SERVICE_EXCERPT}}
                    </p>
                    <a href="#contact" class="btn btn-primary shiny-button" style="background: var(--niche-accent); color: black; border: none;">Request Access</a>
                </div>
                <div class="hero-image-wrapper">
                    <img src="../../images/niche_graphics/{{IMAGE_PATH}}" alt="{{NICHE_NAME}} Dashboard" onerror="this.src='../../images/niche_graphics/graphic_general_business.png'">
                </div>
            </div>
        </div>
    </header>
    """,
    "bold": """
    <header class="niche-hero hero-bold" style="background-image: none; background-color: var(--niche-hero-bg);">
        <div class="container niche-hero-content">
            <div class="hero-text">
                <h1>DOMINATE<br><span style="color: var(--niche-accent); -webkit-text-stroke: 1px white;">{{NICHE_NAME}}</span></h1>
                <p class="sub-headline" style="font-size: 1.5rem; font-weight: 300; letter-spacing: 1px; color: #e2e8f0; margin-top: 2rem; border-top: 1px solid #334155; padding-top: 2rem;">
                    {{SERVICE_EXCERPT}}
                </p>
                <div class="cta-group">
                    <a href="#contact" class="btn btn-primary shiny-button" style="background: white; color: black; border: none;">Book Now</a>
                </div>
            </div>
            <div class="hero-image-wrapper">
                 <img src="../../images/niche_graphics/{{IMAGE_PATH}}" alt="{{NICHE_NAME}} Dashboard" onerror="this.src='../../images/niche_graphics/graphic_general_business.png'">
            </div>
        </div>
    </header>
    """
}

# Hero Variant Assignments
NICHE_VARIANTS = {
    # Immersive (Visual)
    "restaurants": "immersive",
    "hair-salons-and-stylists": "immersive",
    "med-spas-and-laser-facilities": "immersive",
    "window-tinting-and-auto-detail": "immersive",

    # Card Stack (Trust/Pro)
    "attorneys-and-law-firms": "card_stack",
    "accountants-and-cpas": "card_stack",
    "financial-managers-and-advisors": "card_stack",
    "dentists-and-orthodontists": "card_stack",
    "family-practice-doctors": "card_stack",

    # Bold (Trades)
    "general-contractors": "bold",
    "pool-contractors-and-construction": "bold",
    "hvac-services": "bold",
    "plumbers": "bold",
    "window-installers": "bold",

    # Offset (Creative/Modern)
    "real-estate-brokers": "offset",
    "property-management": "offset",

    # Classic (Default/Balanced)
    "pool-cleaners-and-maintenance": "classic",
    "landscaping-and-lawn-care": "classic",
    "painters": "classic",
    "electricians": "classic",
    "veterinarians": "classic",
    "auto-mechanics-and-repair-shops": "classic",
    "barbershops": "classic",
    "pet-groomers": "classic",
    "nail-salons": "classic"
}
