import os
import re

# Configuration
TEMPLATE_PATH = "templates/niche_template.html"
OUTPUT_DIR = "pages/niches"

# Theme Definitions
THEMES = {
    "blue": {"accent": "#0ea5e9", "light_bg": "#f0f9ff", "hero_bg": "#0f172a"},   # Water/Pools/Plumbing
    "green": {"accent": "#16a34a", "light_bg": "#f0fdf4", "hero_bg": "#064e3b"},  # Nature/Landscaping
    "red": {"accent": "#dc2626", "light_bg": "#fef2f2", "hero_bg": "#450a0a"},    # Urgent/HVAC/Restoration
    "orange": {"accent": "#ea580c", "light_bg": "#fff7ed", "hero_bg": "#431407"}, # Construction/Electric
    "teal": {"accent": "#0d9488", "light_bg": "#f0fdfa", "hero_bg": "#042f2e"},   # Medical/Health
    "indigo": {"accent": "#4f46e5", "light_bg": "#eef2ff", "hero_bg": "#1e1b4b"}, # Professional/Legal
    "pink": {"accent": "#db2777", "light_bg": "#fdf2f8", "hero_bg": "#500724"},   # Beauty
    "slate": {"accent": "#475569", "light_bg": "#f8fafc", "hero_bg": "#0f172a"},  # Tech/Auto
    "default": {"accent": "#84cc16", "light_bg": "#f8fafc", "hero_bg": "#0f172a"} # Default Lime
}

# Niche Data with Expanded Content
NICHES = [
    # --- Home Services (Voice AI & Lead Capture) ---
    {
        "name": "Pool Cleaners & Maintenance",
        "hero_headline": "Stop Missing Calls While Your Hands Are Wet",
        "slug": "pool-cleaners-and-maintenance",
        "image": "pool-cleaners-and-maintenance.png",
        "pain": "Technicians are in the field with wet hands, missing calls from new leads.",
        "stat": "30% Missed Calls",
        "opportunity": "A 'Missed Call Text Back' system captures that $1,200/year annual contract immediately.",
        "excerpt": "Stop missing revenue while you're cleaning pools. Our AI Voice Agents answer calls 24/7, qualify leads, and schedule maintenance routes without you lifting a finger.",
        "faqs": [
            {"q": "Can the AI really schedule appointments for me?", "a": "Yes. The AI connects directly to your calendar (Google, Outlook, etc.) and books appointments only during your available slots."},
            {"q": "Does it sound like a robot?", "a": "No. We use advanced voice synthesis that sounds natural and human-like. Most callers don't realized they are speaking to an AI."},
            {"q": "What happens if the AI doesn't know the answer?", "a": "The AI is trained on your specific business knowledge. If it encounters a complex issue, it can transfer the call to you or take a detailed message."}
        ]
    },
    {
        "name": "Pool Contractors & Construction",
        "hero_headline": "Capture Every High-Value Install Lead",
        "slug": "pool-contractors-and-construction",
        "image": "pool-contractors-and-construction.png",
        "pain": "Customers shopping for a $80k pool want instant answers.",
        "stat": "21x Conversion Drop",
        "opportunity": "Instant AI lead qualification to filter 'tire kickers' from serious buyers.",
        "excerpt": "Filter out the tire-kickers from the high-ticket buyers instantly. Our Lead Capture systems qualify prospects before you ever spend time on a site visit.",
        "faqs": [
            {"q": "How does it qualify leads?", "a": "We build custom forms and chat flows that ask about budget, timeline, and property type before allowing a booking."},
            {"q": "Can I see the conversation history?", "a": "Absolutely. All transcripts and chat logs are saved in your CRM for review."},
            {"q": "Does this work with my existing website?", "a": "Yes, we can embed our lead capture tools directly into your current site."}
        ]
    },
    {
        "name": "Landscaping & Lawn Care",
        "hero_headline": "Quote Jobs While You're Mowing",
        "slug": "landscaping-and-lawn-care",
        "image": "landscaping-and-lawn-care.png",
        "pain": "Managing recurring cuts vs. one-off projects leads to 48% admin time.",
        "stat": "$126k Lost Annually",
        "opportunity": "Automated booking and recurring invoicing workflows.",
        "excerpt": "Eliminate the scheduling chaos of recurring routes. We automate your invoicing and dispatch so you can focus on growing your crew.",
        "faqs": [
            {"q": "Can it handle recurring billing?", "a": "Yes, our systems can automatically generate and send invoices for recurring services."},
            {"q": "What about rain delays?", "a": "You can use the system to blast SMS updates to all customers on a specific route with one click."},
            {"q": "Is the app easy for my crew to use?", "a": "We build simple, mobile-first interfaces specifically for field teams."}
        ]
    },
    {
        "name": "HVAC Services",
        "hero_headline": "Prioritize Emergencies, Automate the Rest",
        "slug": "hvac-services",
        "image": "hvac-services.png",
        "pain": "During heatwaves, phones ring off the hook, and 62% of calls go unanswered.",
        "stat": "5.3% Avg Margin",
        "opportunity": "AI Voice Agents to handle dispatch and emergency booking overflow 24/7.",
        "excerpt": "Don't let a heatwave break your dispatch. Our AI agents handle overflow calls during peak times, prioritizing emergencies and booking routine maintenance efficiently.",
        "faqs": [
            {"q": "Can it distinguish between emergencies and routine calls?", "a": "Yes. The AI is trained to recognize keywords like 'emergency', 'leak', or 'no AC' and prioritize those calls."},
            {"q": "Does it work after hours?", "a": "Yes, 24/7/365. You never miss a call, even at 3 AM."},
            {"q": "Can it dispatch technicians?", "a": "It can notify on-call technicians via SMS or push notification immediately after booking."}
        ]
    },
    {
        "name": "General Contractors",
        "hero_headline": "Stop Chasing Leads, Start Building Projects",
        "slug": "general-contractors",
        "image": "general-contractors.png",
        "pain": "Leads from HomeAdvisor/Angi are sold to 5 people; speed is the only differentiator.",
        "stat": "78% to First Responder",
        "opportunity": "Speed-to-lead automation that texts the lead within 30 seconds.",
        "excerpt": "Speed is everything in contracting. Our automation texts new leads within 30 seconds, securing the job before your competitors even see the notification.",
        "faqs": [
            {"q": "How fast is the response?", "a": "typically under 30 seconds from the moment the lead is submitted."},
            {"q": "Can it handle follow-ups?", "a": "Yes, if they don't reply, the system can automatically follow up over the next few days."},
            {"q": "Does it integrate with HomeAdvisor/Angi?", "a": "Yes, we can parse email leads from these platforms and trigger the automation instantly."}
        ]
    },
    {
        "name": "Window Installers",
        "hero_headline": "Qualify Leads Before You Drive Out",
        "slug": "window-installers",
        "image": "window-installers.png",
        "pain": "Time spent driving to give free estimates that don't close.",
        "stat": "68% Leads Go Cold",
        "opportunity": "Automated pre-qualification forms to ensure appointments are with ready-to-buy homeowners.",
        "excerpt": "Stop driving across town for tire-kickers. Qualify homeowners automatically with virtual estimate tools and AI chatbots.",
        "faqs": [
            {"q": "Can customers upload photos?", "a": "Yes, our intake forms allow customers to upload photos of their windows for rough estimates."},
            {"q": "Does it integrate with my calendar?", "a": "Yes, qualified leads can book estimate slots directly on your calendar."},
            {"q": "Is the system secure?", "a": "Yes, all customer data is encrypted and secure."}
        ]
    },
    {
        "name": "Plumbers",
        "hero_headline": "Answer Emergency Calls at 2 AM (Without Waking Up)",
        "slug": "plumbers",
        "image": "plumbers.png",
        "pain": "A burst pipe customer won't wait; they call the next number on Google.",
        "stat": "80% Revenue Loss",
        "opportunity": "24/7 AI answering that dispatches emergency calls immediately.",
        "excerpt": "Be the first to answer, every time. Our AI Voice Agents ensure you capture every emergency call, even when your hands are under a sink.",
        "faqs": [
            {"q": "Does it understand plumbing terminology?", "a": "Yes, we train the model on specific plumbing terms and services."},
            {"q": "Can I change the script?", "a": "Absolutely. We customize the conversation flow to match your business processes."},
            {"q": "What is the cost compared to a call center?", "a": "Our AI solutions are typically 1/10th the cost of a human call center."}
        ]
    },
    {
        "name": "Painters",
        "hero_headline": "Schedule Estimates While You're on a Ladder",
        "slug": "painters",
        "image": "painters.png",
        "pain": "Homeowners often forget or ghost on estimate appointments.",
        "stat": "30% No-Show Rate",
        "opportunity": "Automated SMS reminders and confirmation workflows (e.g., 'Reply C to Confirm').",
        "excerpt": "Eliminate no-shows with automated SMS confirmations. We ensure your customers are ready and waiting when you arrive for the estimate.",
        "faqs": [
            {"q": "How do confirmations work?", "a": "The system sends a text/email 24 hours before. If they don't confirm, it alerts you."},
            {"q": "Can I send color charts?", "a": "Yes, you can include links to digital color charts in the confirmation messages."},
            {"q": "Does it work for exterior and interior jobs?", "a": "Yes, the system is flexible for all types of painting services."}
        ]
    },
    {
        "name": "Electricians",
        "hero_headline": "Dispatch Faster, Bill Sooner",
        "slug": "electricians",
        "image": "electricians.png",
        "pain": "Highly skilled labor wasted on scheduling $100 outlet fixes.",
        "stat": "40% Admin Time",
        "opportunity": "Online booking for small jobs; human dispatch for big projects.",
        "excerpt": "Focus your skilled labor on high-value projects. Automate the scheduling of small repairs and let AI handle the routine questions.",
        "faqs": [
            {"q": "Can I set different job types?", "a": "Yes, you can have 'Service Call', 'Estimate', and 'Emergency' as different booking options."},
            {"q": "Does it integrate with ServiceTitan?", "a": "We have integrations or workarounds for most major field service software."},
            {"q": "Is it mobile friendly?", "a": "Yes, the booking interface works perfectly on all mobile devices."}
        ]
    },
    {
        "name": "Property Management",
        "hero_headline": "Automate Tenant Requests & Lease Renewals",
        "slug": "property-management",
        "image": "property-management.png",
        "pain": "Phones ringing with 'my toilet is running' 24/7 or prospects asking for listings you don't have.",
        "stat": "60% Comm Time",
        "opportunity": "Branded Tenant App & AI Dispatch.",
        "excerpt": "Streamline your portfolio with a custom tenant portal app. Automate maintenance requests and let AI handle leasing inquiries 24/7.",
        "faqs": [
            {"q": "Can tenants pay rent through the app?", "a": "Yes, we can integrate payment gateways for seamless rent collection."},
            {"q": "How does maintenance dispatch work?", "a": "Tenants submit a request, and the system automatically notifies the assigned vendor based on the category."},
            {"q": "Does it handle multiple properties?", "a": "Yes, the system scales to handle hundreds or thousands of units."}
        ]
    },

    # --- Medical & Health (Private AI & HIPAA) ---
    {
        "name": "Dentists & Orthodontists",
        "hero_headline": "Fill Your Chair, Not Your Voicemail",
        "slug": "dentists-and-orthodontists",
        "image": "dentists-and-orthodontists.png",
        "pain": "Marketing for new teeth is expensive; keeping them is cheap.",
        "stat": "5-6x Cheaper Retention",
        "opportunity": "Automated 6-month recall campaigns (SMS/Email) to boost LTV.",
        "excerpt": "Maximize patient lifetime value with automated recall systems. Our AI ensures your chairs stay full by automatically rescheduling check-ups.",
        "faqs": [
            {"q": "Is this HIPAA compliant?", "a": "Yes, all our medical communication automation is fully HIPAA compliant."},
            {"q": "Can it write back into my PMS?", "a": "We integrate with many major Practice Management Systems to update appointment status."},
            {"q": "Will patients get annoyed?", "a": "No, we use smart frequency limits and personalized messaging to ensure a positive experience."}
        ]
    },
    {
        "name": "Family Practice Doctors",
        "hero_headline": "Reduce No-Shows with Smart Reminders",
        "slug": "family-practice-doctors",
        "image": "family-practice-doctors.png",
        "pain": "A 15-minute gap is revenue specifically lost forever.",
        "stat": "19% No-Show Rate",
        "opportunity": "Smart waitlist automation to fill last-minute cancellations.",
        "excerpt": "Never let a cancellation hurt your revenue. Our smart waitlist system automatically texts eligible patients to fill sudden openings instantly.",
        "faqs": [
            {"q": "How does the waitlist work?", "a": "When a slot opens, the system texts the next 5 people on the list. First to reply gets the spot."},
            {"q": "Is patient data secure?", "a": "Yes, we use Private AI infrastructure to ensure complete data sovereignty and security."},
            {"q": "Can it handle new patient intake?", "a": "Yes, we can automate the sending and collection of digital intake forms."}
        ]
    },
    {
        "name": "Veterinarians",
        "hero_headline": "Care for Pets, Let AI Handle the Phones",
        "slug": "veterinarians",
        "image": "veterinarians.png",
        "pain": "Front desk is overwhelmed checking in pets, ignoring the phone.",
        "stat": "30% Scheduling Calls",
        "opportunity": "AI Voice Agent to handle scheduling and FAQ while staff handles the animals.",
        "excerpt": "Let your staff focus on the animals, not the phones. AI Voice Agents handle scheduling, refills, and FAQs with zero hold times.",
        "faqs": [
            {"q": "Can it handle prescription refills?", "a": "Yes, it can take refill requests and route them to the pharmacy queue."},
            {"q": "Does it sound compassionate?", "a": "We tune the voice and tone to be warm and empathetic, suitable for pet owners."},
            {"q": "What languages does it speak?", "a": "Our agents can be configured to speak multiple languages, including Spanish."}
        ]
    },
    {
        "name": "Med Spas & Laser Facilities",
        "hero_headline": "Book High-Ticket Treatments Automatically",
        "slug": "med-spas-and-laser-facilities",
        "image": "med-spas-and-laser-facilities.png",
        "pain": "Clients impulse-buy beauty; if you don't answer, they go elsewhere.",
        "stat": "400% Conversion Boost",
        "opportunity": "Instant Instagram DM automation and SMS follow-up.",
        "excerpt": "Capture beauty leads instantly on Instagram and SMS. Automated booking workflows turn likes into consultations while you sleep.",
        "faqs": [
            {"q": "Does it work with Instagram DMs?", "a": "Yes, we automate responses to DMs and comments to capture leads instantly."},
            {"q": "Can it take deposits?", "a": "Yes, we can integrate payment links to secure booking deposits."},
            {"q": "Can it manage membership points?", "a": "We can integrate with loyalty systems to show clients their points balance."}
        ]
    },

    # --- Beauty & Personal Care (Booking & Reviews) ---
    {
        "name": "Hair Salons & Stylists",
        "hero_headline": "Fill Last-Minute Openings Instantly",
        "slug": "hair-salons-and-stylists",
        "image": "hair-salons-and-stylists.png",
        "pain": "Stylists can't answer phones while cutting hair.",
        "stat": "$15k Lost Annually",
        "opportunity": "'Text-to-Book' automation for missed calls.",
        "excerpt": "Keep your scissors moving and let AI handle the bookings. Missed call text-back ensures you never lose a client to voicemail.",
        "faqs": [
            {"q": "Can it handle specific stylists?", "a": "Yes, clients can book specific time slots with their preferred stylist."},
            {"q": "What about cancellations?", "a": "It automatically enforces your cancellation policy and can charge fees if configured."},
            {"q": "Is it hard to set up?", "a": "No, we handle the entire setup and integration for you."}
        ]
    },
    {
        "name": "Barbershops",
        "hero_headline": "Cut Hair, Not Phone Tag",
        "slug": "barbershops",
        "image": "barbershops.png",
        "pain": "Relying on walk-ins instead of predictable appointments.",
        "stat": "25% Revenue Boost",
        "opportunity": "Membership systems and automated recurring appointments.",
        "excerpt": "Transform walk-ins into loyal members. Automated recurring appointments and membership management stabilize your cash flow.",
        "faqs": [
            {"q": "How do memberships work?", "a": "We set up automated billing for monthly cuts, guaranteeing revenue."},
            {"q": "Can I blast out open slots?", "a": "Yes, send a text blast to your VIP list to fill a slow afternoon."},
            {"q": "Does it work on mobile?", "a": "Yes, clients can book from their phone in under 30 seconds."}
        ]
    },
    {
        "name": "Nail Salons",
        "hero_headline": "Book Appointments While You Work",
        "slug": "nail-salons",
        "image": "nail-salons.png",
        "pain": "High volume means bad reviews bury the good ones.",
        "stat": "94% Avoid Low Stars",
        "opportunity": "Automated 'Review Request' texts sent 1 hour after service.",
        "excerpt": "Dominate local search with automated reviews. We send smart requests to happy clients, boosting your 5-star rating automatically.",
        "faqs": [
            {"q": "Does it gate negative reviews?", "a": "We can route unhappy feedback to a private form so you can resolve it before it goes public."},
            {"q": "Which platforms does it support?", "a": "Google, Facebook, Yelp, and more."},
            {"q": "Is it automated?", "a": "Yes, it triggers automatically after the appointment is marked complete."}
        ]
    },
    {
        "name": "Pet Groomers",
        "hero_headline": "Groom More Dogs, Answer Fewer Phones",
        "slug": "pet-groomers",
        "image": "pet-groomers.png",
        "pain": "Manually texting owners 'Fluffy is ready.'",
        "stat": "2 hrs/day Admin",
        "opportunity": "Automated 'Ready for Pickup' SMS notifications.",
        "excerpt": "Save hours of phone time with automated updates. One click notifies owners that their pet is ready for pickup.",
        "faqs": [
            {"q": "Can I send photos?", "a": "Yes, send a cute photo of the finished groom to delight the owner."},
            {"q": "Does it remind them to rebook?", "a": "Yes, the system automatically reminds them when it's time for the next groom."},
            {"q": "Is it easy to use?", "a": "Very. It's designed for busy grooming environments."}
        ]
    },

    # --- Professional Services (Private AI & Consulting) ---
    {
        "name": "Attorneys & Law Firms",
        "hero_headline": "Capture Every Potential Case, Instantly",
        "slug": "attorneys-and-law-firms",
        "image": "attorneys-and-law-firms.png",
        "pain": "Every minute on admin is money burned.",
        "stat": "2.9 Billable Hours/Day",
        "opportunity": "Client intake automation to populate documents before the first meeting.",
        "excerpt": "Secure Private AI for the legal sector. Automate client intake and document drafting without compromising confidentiality or privilege.",
        "faqs": [
            {"q": "Is client data kept private?", "a": "Yes. We deploy Private AI models that do not train on your data and run in secure environments."},
            {"q": "Can it draft documents?", "a": "Yes, it can generate first drafts of common legal documents based on intake data."},
            {"q": "Does it integrate with Clio/MyCase?", "a": "We build custom integrations for major legal practice management software."}
        ]
    },
    {
        "name": "Accountants & CPAs",
        "hero_headline": "Automate Tax Season Inquiries",
        "slug": "accountants-and-cpas",
        "image": "accountants-and-cpas.png",
        "pain": "Chasing clients for documents manually.",
        "stat": "40% Revenue in Q1",
        "opportunity": "Automated document collection reminders and portals.",
        "excerpt": "End the tax season chase. Secure client portals and automated follow-ups collect documents faster, smoothing out your workflow.",
        "faqs": [
            {"q": "Is the portal secure?", "a": "Yes, bank-level encryption ensures financial data is safe."},
            {"q": "Does it automate reminders?", "a": "Yes, it gently nags clients for missing documents so you don't have to."},
            {"q": "Can it handle e-signatures?", "a": "Yes, we integrate with DocuSign and other providers for seamless signing."}
        ]
    },
    {
        "name": "Financial Managers & Advisors",
        "hero_headline": "Qualify Prospects Before the First Meeting",
        "slug": "financial-managers-and-advisors",
        "image": "financial-managers-and-advisors.png",
        "pain": "Losing clients because you didn't say 'Happy Birthday.'",
        "stat": "95% Profit Boost",
        "opportunity": "Automated relationship management (birthday texts, quarterly review reminders).",
        "excerpt": "Scale your personal touch. Automated relationship management ensures every client feels valued, increasing retention and referrals.",
        "faqs": [
            {"q": "Is it compliant with FINRA?", "a": "We build systems with compliance in mind, including archiving and approval workflows."},
            {"q": "Can it schedule annual reviews?", "a": "Yes, it automates the outreach and booking of periodic review meetings."},
            {"q": "Does it integrate with Redtail/Wealthbox?", "a": "Yes, we specialize in CRM integrations for wealth management."}
        ]
    },
    {
        "name": "Real Estate Brokers",
        "hero_headline": "Respond to Leads Before They Click Away",
        "slug": "real-estate-brokers",
        "image": "real-estate-brokers.png",
        "pain": "Leads come from Zillow and sit in an email inbox for 4 hours.",
        "stat": "48% Ignored Leads",
        "opportunity": "AI Voice Receptionist & Lead Capture.",
        "excerpt": "Never miss a buyer call again. AI Voice Agents screen leads, answer property questions, and schedule viewings 24/7.",
        "faqs": [
            {"q": "Can it answer questions about specific listings?", "a": "Yes, the AI has access to your MLS data or listing feed to answer specific questions."},
            {"q": "Does it transfer hot leads?", "a": "Yes, if a buyer is ready to make an offer, the call is patched to you instantly."},
            {"q": "Does it work with IDX websites?", "a": "We can integrate the capture forms seamlessly with your IDX site."}
        ]
    },

    # --- Retail & Auto (Custom Apps & Upsells) ---
    {
        "name": "Auto Mechanics & Repair Shops",
        "hero_headline": "Approve Repairs via Text, Not Tag",
        "slug": "auto-mechanics-and-repair-shops",
        "image": "auto-mechanics-and-repair-shops.png",
        "pain": "Advisors are explaining a transmission fix and ignoring 3 new calls.",
        "stat": "$108k Lost Revenue",
        "opportunity": "AI call overflow to capture appointment requests.",
        "excerpt": "Keep your bays full and your phone lines open. AI handles the appointment schedulings so your advisors can focus on selling service.",
        "faqs": [
            {"q": "Can it give price estimates?", "a": "It can provide general pricing for standard services, or take info for a custom quote."},
            {"q": "Does it remind customers of service intervals?", "a": "Yes, automated retention marketing brings customers back for oil changes and tires."},
            {"q": "Is it integrated with shop management software?", "a": "We work with many shop systems to sync appointments."}
        ]
    },
    {
        "name": "Window Tinting & Auto Detail",
        "hero_headline": "Quote & Book Details Hands-Free",
        "slug": "window-tinting-and-auto-detail",
        "image": "window-tinting-and-auto-detail.png",
        "pain": "Selling just the wash, not the wax/ceramic.",
        "stat": "30% Higher Ticket",
        "opportunity": "Automated upsell emails/texts sent upon booking confirmation.",
        "excerpt": "Maximize every ticket with automated upsells. Suggest ceramic coatings or tint packages automatically when a customer books a detail.",
        "faqs": [
            {"q": "How do upsells work?", "a": "After booking, the customer creates a confirmation with 'One-click add-on' options."},
            {"q": "Can I take deposits?", "a": "Yes, secure revenue and reduce no-shows with upfront deposits."},
            {"q": "Does it assist with reviews?", "a": "Yes, it automatically requests a review once the job is marked complete."}
        ]
    },
    {
        "name": "Restaurants",
        "hero_headline": "Take Back Your Margins from Delivery Apps",
        "slug": "restaurants",
        "image": "restaurants.png",
        "pain": "Relying on 3rd party apps that hide customer data and charge huge fees.",
        "stat": "$4,500/mo Lost",
        "opportunity": "A custom app to capture orders commission-free and own the data.",
        "excerpt": "Take back your margins. Launch a branded ordering app to bypass 3rd party commissions and own your customer data.",
        "faqs": [
            {"q": "Do I own the customer data?", "a": "100%. Unlike DoorDash, you get the email and phone number for every customer."},
            {"q": "Does it integrate with my Kitchen Display System?", "a": "We integrate with many modern POS and KDS systems."},
            {"q": "Can I send push notifications?", "a": "Yes, send offers directly to your customers' phones to drive slow-day traffic."}
        ]
    }
]

# Services Data (8 Cards)
SERVICES = [
    {
        "name": "Voice AI Agents",
        "icon": "mic",
        "desc_template": "Automate 24/7 appointment booking and customer service for your {niche_name} business.",
        "link": "../services/voice-ai.html"
    },
    {
        "name": "Custom Apps",
        "icon": "smartphone",
        "desc_template": "Branded mobile apps for {niche_name} customers to book, order, and manage their profile.",
        "link": "../services/custom-apps.html"
    },
    {
        "name": "Review Management",
        "icon": "star",
        "desc_template": "Automate 5-star review requests to boost your local {niche_name} SEO ranking.",
        "link": "../services/review-automation.html"
    },
    {
        "name": "Private AI",
        "icon": "shield",
        "desc_template": "Secure, private AI models trained on your specific {niche_name} data and documents.",
        "link": "../services/private-ai-infra.html"
    },
    {
        "name": "Lead Capture",
        "icon": "magnet",
        "desc_template": "Instant speed-to-lead automation to convert new {niche_name} inquiries into bookings.",
        "link": "../services/lead-database.html"
    },
    {
        "name": "Data Intelligence",
        "icon": "bar-chart",
        "desc_template": "Unified dashboards to track every {niche_name} KPI and revenue metric in real-time.",
        "link": "../services/data-intelligence.html"
    },
    {
        "name": "Workflow Automation",
        "icon": "zap",
        "desc_template": "Eliminate repetitive {niche_name} admin tasks and reclaim your time.",
        "link": "../services/workflow-automation.html"
    },
    {
        "name": "Growth Consulting",
        "icon": "trending-up",
        "desc_template": "Strategic guidance and implementation support to scale your {niche_name} operations.",
        "link": "../services/consulting.html"
    }
]
# Case Studies Data
CASE_STUDIES = [
    # Voice AI Success
    {
        "id": "voice-retail",
        "category": "Retail",
        "title": "Major Retailer Saves $20k/Mo",
        "stat": "20% Increase in Conversions",
        "desc": "How AI voice agents eliminated missed calls and converted 20% more inquiries into bookings.",
        "icon": "phone-call",
        "link": "#"
    },
    {
        "id": "voice-law",
        "category": "Legal",
        "title": "Law Firm 11x ROI",
        "stat": "$85k Added Monthly Revenue",
        "desc": "A regional firm used AI intake to capture leads instantly, resulting in 180% more qualified cases.",
        "icon": "scale",
        "link": "#"
    },
    {
        "id": "voice-medical",
        "category": "Healthcare",
        "title": "Clinic Reduces Admin by 53%",
        "stat": "41% Decrease in No-Shows",
        "desc": "Automated appointment reminders and intelligent scheduling filled calendars and reduced staff workload.",
        "icon": "stethoscope",
        "link": "#"
    },
    # Review Management
    {
        "id": "reviews-dental",
        "category": "Healthcare",
        "title": "Dental Practice Adds $127k",
        "stat": "4.3 to 4.7 Star Rating",
        "desc": "Automated review requests boosted local SEO, driving 18% more new patient inquiries.",
        "icon": "star",
        "link": "#"
    },
    {
        "id": "reviews-dining",
        "category": "Hospitality",
        "title": "Restaurant Reservations Up 10%",
        "stat": "174% ARR Increase",
        "desc": "Active daily review management on Google and social media directly correlated to increased table bookings.",
        "icon": "utensils",
        "link": "#"
    },
    # Custom Apps & Automation
    {
        "id": "app-coffee",
        "category": "Food & Bev",
        "title": "Coffee Chain Loyalty Growth",
        "stat": "34M+ Active Users",
        "desc": "Mobile ordering app transformed the customer experience, driving massive loyalty and repeat purchases.",
        "icon": "smartphone",
        "link": "#"
    },
    {
        "id": "lead-contractor",
        "category": "Home Services",
        "title": "Contractor Doubles Leads",
        "stat": "280% ROI in Year 1",
        "desc": "Automated lead response systems allowed a general contractor to secure jobs before competitors responded.",
        "icon": "hard-hat",
        "link": "#"
    },
    {
        "id": "auto-repair",
        "category": "Automotive",
        "title": "Shop Automates Bookings",
        "stat": "70% Faster Ordering",
        "desc": "AI chat interactions handled appointment scheduling, freeing up service advisors to upsell.",
        "icon": "wrench",
        "link": "#"
    }
]

# Map Nitches to Case Studies
NICHE_CASE_STUDY_MAP = {
    # Home Services
    "pool-cleaners-and-maintenance": ["voice-retail", "lead-contractor", "reviews-dental"],
    "pool-contractors-and-construction": ["lead-contractor", "voice-retail", "app-coffee"],
    "landscaping-and-lawn-care": ["lead-contractor", "voice-retail", "reviews-dental"],
    "hvac-services": ["voice-retail", "lead-contractor", "reviews-dental"],
    "general-contractors": ["lead-contractor", "voice-retail", "app-coffee"],
    "window-installers": ["lead-contractor", "voice-retail", "reviews-dental"],
    "plumbers": ["voice-retail", "lead-contractor", "reviews-dining"],
    "painters": ["lead-contractor", "reviews-dental", "voice-retail"],
    "electricians": ["voice-retail", "lead-contractor", "reviews-dental"],
    "property-management": ["voice-retail", "lead-contractor", "app-coffee"],
    
    # Medical
    "dentists-and-orthodontists": ["reviews-dental", "voice-medical", "app-coffee"],
    "family-practice-doctors": ["voice-medical", "reviews-dental", "app-coffee"],
    "veterinarians": ["voice-medical", "reviews-dental", "lead-contractor"],
    "med-spas-and-laser-facilities": ["voice-retail", "reviews-dental", "app-coffee"],
    
    # Beauty
    "hair-salons-and-stylists": ["voice-retail", "reviews-dining", "app-coffee"],
    "barbershops": ["app-coffee", "voice-retail", "reviews-dining"],
    "nail-salons": ["reviews-dining", "voice-retail", "app-coffee"],
    "pet-groomers": ["lead-contractor", "reviews-dining", "voice-retail"],
    
    # Prof Services
    "attorneys-and-law-firms": ["voice-law", "reviews-dental", "lead-contractor"],
    "accountants-and-cpas": ["voice-law", "lead-contractor", "reviews-dental"],
    "financial-managers-and-advisors": ["voice-law", "app-coffee", "lead-contractor"],
    "real-estate-brokers": ["lead-contractor", "voice-retail", "reviews-dining"],
    
    # Auto & Retail
    "auto-mechanics-and-repair-shops": ["auto-repair", "reviews-dental", "voice-retail"],
    "window-tinting-and-auto-detail": ["auto-repair", "reviews-dining", "app-coffee"],
    "restaurants": ["reviews-dining", "app-coffee", "voice-retail"]
}


# Common FAQs for all niches
GLOBAL_FAQS = [
    {
        "q": "How long does the setup process take?",
        "a": "Most agencies are live within 7-14 days. We handle all the technical setup, training, and integration with your CRM and existing tools."
    },
    {
        "q": "Is there a long-term contract?",
        "a": "We offer flexible month-to-month options as well as discounted annual plans. We believe our results should keep you, not a standardized contract."
    }
]



# Hero Templates
HERO_TEMPLATES = {
    # 1. BEYOND UI STYLE (Minimal, Split, Pill Badge)
    "beyond": """
    <header class="niche-hero hero-beyond" style="background: white; padding-top: 140px;">
        <div class="container niche-hero-content">
            <div class="hero-text">
                <div class="badge-pill accent">
                    <span class="badge-tag">NEW</span>
                    <span>AI Model v2.0 Live</span>
                </div>
                <h1 class="hero-h1-beyond">
                    {{HERO_HEADLINE}}
                </h1>
                <p class="sub-headline" style="font-size: 1.125rem; color: #64748b; line-height: 1.6; margin-bottom: 2.5rem; max-width: 500px;">
                    {{SERVICE_EXCERPT}}
                </p>
                <div class="cta-group" style="display: flex; gap: 1rem;">
                    <a href="#contact" class="btn btn-primary shiny-button">Get Started</a>
                    <a href="#process" class="btn btn-lg btn-outline" style="display: flex; align-items: center; gap: 0.5rem; padding: 14px 24px; border-radius: 8px;">
                        <i data-lucide="play-circle" size="20"></i> Watch Demo
                    </a>
                </div>
                <div style="margin-top: 3rem; display: flex; gap: 2rem; opacity: 0.6; filter: grayscale(1);">
                     <!-- Mini Logo Strip -->
                     <img src="../../images/logos/logo1.svg" style="height: 24px;" onerror="this.style.display='none'">
                     <img src="../../images/logos/logo2.svg" style="height: 24px;" onerror="this.style.display='none'">
                     <img src="../../images/logos/logo3.svg" style="height: 24px;" onerror="this.style.display='none'">
                </div>
            </div>
            <div class="hero-image-wrapper visual-proof-container" style="background: var(--niche-light-bg); border-radius: 24px; overflow: hidden; position: relative;">
                 <!-- Main Image -->
                 <img src="../../images/niche_graphics/{{IMAGE_PATH}}" alt="{{NICHE_NAME}}" style="width: 85%; border-radius: 12px; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25); transform: rotate(-2deg) translateY(20px);">
                 
                 <!-- Float Card 1 -->
                 <div class="float-card" style="top: 20%; right: 5%;">
                    <div class="float-stat">
                        <span class="float-label">Revenue</span>
                        <span class="float-value">$14k</span>
                    </div>
                 </div>
                 
                 <!-- Float Card 2 -->
                 <div class="float-card delayed" style="bottom: 20%; left: 5%;">
                    <div class="float-stat">
                        <span class="float-label">Leads</span>
                        <span class="float-value">800+</span>
                    </div>
                 </div>
            </div>
        </div>
    </header>
    """,

    # 2. MARKETIVE STYLE (Bold, Bento-ish, Playful)
    "marketive": """
    <header class="niche-hero hero-marketive" style="background: linear-gradient(180deg, white 0%, var(--niche-light-bg) 100%); padding-top: 140px;">
        <div class="container niche-hero-content">
            <div class="hero-text">
                <div style="display: inline-block; padding: 8px 16px; background: white; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); margin-bottom: 1.5rem; font-weight: 700; color: #ef4444; font-size: 0.8rem; letter-spacing: 0.05em; text-transform: uppercase;">
                    #1 {{NICHE_NAME}} Solution
                </div>
                <h1 class="hero-h1-marketive">
                    {{HERO_HEADLINE}}
                </h1>
                <p class="sub-headline" style="font-size: 1.25rem; color: #475569; margin: 2rem 0;">
                    {{SERVICE_EXCERPT}} From automated campaigns to real-time insights.
                </p>
                <div class="cta-group" style="display: flex; gap: 1rem; align-items: center;">
                    <a href="#contact" class="btn btn-primary shiny-button" style="background: #ef4444; color: white; border: none; box-shadow: 0 10px 15px -3px rgba(239, 68, 68, 0.3);">Get Started</a>
                    <a href="#contact" style="font-weight: 600; color: #0f172a; display: flex; align-items: center; gap: 4px;">Book a Demo <i data-lucide="arrow-right"></i></a>
                </div>
                
                <div style="margin-top: 3rem; display: flex; align-items: center; gap: 1rem;">
                    <div style="display: flex; margin-left: 10px;">
                        <!-- Avatar Stack Placeholder -->
                        <div style="width: 40px; height: 40px; border-radius: 50%; background: #cbd5e1; border: 2px solid white; margin-left: -10px;"></div>
                        <div style="width: 40px; height: 40px; border-radius: 50%; background: #94a3b8; border: 2px solid white; margin-left: -10px;"></div>
                        <div style="width: 40px; height: 40px; border-radius: 50%; background: #64748b; border: 2px solid white; margin-left: -10px;"></div>
                    </div>
                    <div>
                        <div style="font-weight: 700; color: #0f172a;">4.9 (150k)</div>
                        <div style="font-size: 0.8rem; color: #64748b;">Trusted by leaders</div>
                    </div>
                </div>
            </div>
            
            <div class="hero-image-wrapper" style="position: relative;">
                <!-- Central Laptop/Screen -->
                <div style="position: relative; z-index: 2;">
                     <img src="../../images/niche_graphics/{{IMAGE_PATH}}" alt="{{NICHE_NAME}}" style="width: 100%; border-radius: 16px; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);">
                </div>
                
                <!-- Floating Elements (Marketive Style) -->
                <div class="float-card" style="top: -20px; right: -20px; z-index: 3; padding: 10px;">
                     <div style="color: #ef4444; font-weight: 700;">Synced</div>
                </div>
                <div class="float-card delayed" style="bottom: 20px; left: -30px; z-index: 3; padding: 16px;">
                     <div style="font-size: 2rem; font-weight: 800; color: #0f172a;">125k+</div>
                     <div style="font-size: 0.8rem; color: #64748b;">Leads Captured</div>
                </div>
            </div>
        </div>
    </header>
    """,

    # 3. ALVA STYLE (Fintech, Clean, Dashboards)
    "alva": """
    <header class="niche-hero hero-alva" style="background: #fafafa; padding-top: 140px;">
        <div class="container niche-hero-content">
            <div class="hero-text">
                <div class="badge-pill" style="background: #18181b; color: white; border: none;">
                    <span style="background: white; color: black; border-radius: 4px; padding: 2px 6px; font-size: 0.7rem; font-weight: 700; margin-right: 8px;">NEW</span>
                    Multi-channel automation
                </div>
                <h1 class="hero-h1-alva">
                    {{HERO_HEADLINE}}
                </h1>
                <p class="sub-headline" style="font-size: 1.1rem; color: #52525b; margin-bottom: 2rem; max-width: 480px;">
                     {{SERVICE_EXCERPT}} Keep your business needs safely organized under one roof.
                </p>
                <div class="cta-group" style="display: flex; gap: 1rem;">
                    <a href="#contact" class="btn btn-primary shiny-button" style="background: #18181b; color: white; border-radius: 99px; padding: 14px 28px;">Try for Free</a>
                    <a href="#process" class="btn btn-outline" style="border-radius: 99px; padding: 14px 28px; display: flex; align-items: center; gap: 8px;">
                        See Preview <i data-lucide="play-circle" size="16"></i>
                    </a>
                </div>
                
                <div style="margin-top: 3rem; opacity: 0.4; filter: grayscale(1);">
                     <div style="font-size: 0.8rem; font-weight: 600; margin-bottom: 1rem;">TRUSTED BY TEAMS AT</div>
                     <div style="display: flex; gap: 2rem; align-items: center;">
                         <!-- Logo Placeholders -->
                        <div style="font-weight: 800; letter-spacing: -1px; font-size: 1.2rem;">slack</div>
                        <div style="font-weight: 800; letter-spacing: -1px; font-size: 1.2rem;">zoom</div>
                        <div style="font-weight: 800; letter-spacing: -1px; font-size: 1.2rem;">airbnb</div>
                     </div>
                </div>
            </div>
            
            <div class="hero-image-wrapper" style="background: #f4f4f5; padding: 2rem; border-radius: 24px;">
                 <img src="../../images/niche_graphics/{{IMAGE_PATH}}" alt="{{NICHE_NAME}}" style="width: 100%; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
                 
                 <!-- Stat Overlay -->
                 <div style="background: white; padding: 1.5rem; border-radius: 12px; margin-top: -40px; margin-left: 20px; position: relative; z-index: 2; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); width: 80%;">
                      <div style="font-size: 0.9rem; color: #71717a;">Total Revenue</div>
                      <div style="font-size: 2.5rem; font-weight: 700; letter-spacing: -0.05em; margin: 4px 0;">$48,403</div>
                      <div style="display: flex; gap: 1rem; align-items: flex-end; height: 40px;">
                          <div style="background: #e4e4e7; width: 20%; height: 60%; border-radius: 4px;"></div>
                          <div style="background: #e4e4e7; width: 20%; height: 80%; border-radius: 4px;"></div>
                          <div style="background: #18181b; width: 20%; height: 100%; border-radius: 4px; position: relative;">
                               <div style="position: absolute; top: -30px; left: 50%; transform: translateX(-50%); background: #18181b; color: white; padding: 4px 8px; border-radius: 4px; font-size: 0.7rem;">$30k</div>
                          </div>
                      </div>
                 </div>
            </div>
        </div>
    </header>
    """,

    # 4. MONOTREE STYLE (New Standard)
    "monotree": """
    <header class="niche-hero">
        <div class="container niche-hero-content">
            <div class="hero-text">
                <h1 class="font-primary">
                    {{HERO_HEADLINE}}
                    <!-- SVG Scribble Underline -->
                    <svg style="position: absolute; width: 250px; height: 12px; bottom: -12px; left: 0; color: var(--niche-accent); opacity: 0.6;" viewBox="0 0 100 10" preserveAspectRatio="none">
                        <path d="M0 5 Q 50 10 100 5" stroke="currentColor" stroke-width="3" fill="none" />
                    </svg>
                </h1>
                <p class="sub-headline">
                    {{SERVICE_EXCERPT}} Stop losing revenue to missed calls and manual admin.
                </p>
                
                <div class="hero-cta-group">
                    <input type="email" placeholder="Enter work email" class="hero-input">
                    <button class="hero-btn">Book a demo</button>
                </div>
                
                <!-- Trust / Stats Row -->
                <div style="display: flex; align-items: center; gap: 3rem; border-top: 1px solid #e2e8f0; padding-top: 2rem; margin-top: 2rem;">
                    <div>
                        <div style="font-size: 2rem; font-weight: 700; color: #0f172a; line-height: 1;">{{STAT_TEXT}}</div>
                        <div style="font-size: 0.875rem; color: #64748b; font-weight: 500; margin-top: 4px;">{{PAIN_POINT}} (Solved)</div>
                    </div>
                    <!-- Star Rating -->
                    <div style="display: flex; flex-direction: column; gap: 4px;">
                        <div style="display: flex; gap: 2px;">
                            <i data-lucide="star" style="fill: #0f172a; color: #0f172a; width: 16px;"></i>
                            <i data-lucide="star" style="fill: #0f172a; color: #0f172a; width: 16px;"></i>
                            <i data-lucide="star" style="fill: #0f172a; color: #0f172a; width: 16px;"></i>
                            <i data-lucide="star" style="fill: #0f172a; color: #0f172a; width: 16px;"></i>
                            <i data-lucide="star" style="fill: #0f172a; color: #0f172a; width: 16px;"></i>
                        </div>
                        <span style="font-size: 0.875rem; font-weight: 600; color: #0f172a;">4.9/5 Average Rating</span>
                    </div>
                </div>
            </div>
            
            <div class="hero-image-wrapper">
                 <img src="../../images/niche_graphics/{{IMAGE_PATH}}" alt="{{NICHE_NAME}}">
            </div>
        </div>
    </header>
    """,

    # 5. IMMERSIVE STYLE (Dark, Centered, Premium)
    "immersive": """
    <header class="niche-hero hero-immersive" style="background: var(--niche-hero-bg); color: white; padding-top: 160px; text-align: center; position: relative; overflow: hidden;">
        <!-- Background Glow -->
        <div style="position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 100%; height: 100%; pointer-events: none; background: radial-gradient(circle at 50% 10%, rgba(255,255,255,0.05), transparent 70%);"></div>
        
        <div class="container niche-hero-content" style="grid-template-columns: 1fr; max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">
             <!-- Badge -->
             <div class="badge-pill" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.15); color: #e2e8f0; margin: 0 auto 1.5rem; backdrop-filter: blur(4px);">
                <span style="width: 8px; height: 8px; background: var(--niche-accent); border-radius: 50%; display: inline-block; margin-right: 8px;"></span>
                {{NICHE_NAME}} Growth Engine
             </div>
             <h1 class="hero-h1-immersive" style="font-size: 4rem; letter-spacing: -0.03em; line-height: 1.1; margin-bottom: 1.5rem; font-weight: 800;">
                {{HERO_HEADLINE}}
             </h1>
             <p class="sub-headline" style="color: #94a3b8; font-size: 1.25rem; max-width: 650px; margin: 0 auto 2.5rem; line-height: 1.6;">
                {{SERVICE_EXCERPT}}
             </p>
             <div class="cta-group" style="justify-content: center; gap: 1rem;">
                 <a href="#contact" class="btn btn-primary shiny-button" style="background: var(--niche-accent); color: black; border: none; font-weight: 700; padding: 16px 32px; font-size: 1.1rem;">Start Growing</a>
                 <a href="#process" class="btn btn-outline" style="border-color: rgba(255,255,255,0.2); color: white; backdrop-filter: blur(4px);">View Strategy</a>
             </div>
             
             <!-- Visual Element -->
             <div class="hero-image-wrapper" style="margin-top: 4rem; width: 100%; border-radius: 20px; box-shadow: 0 -20px 40px -10px rgba(var(--niche-accent-rgb), 0.1), 0 0 0 1px rgba(255,255,255,0.1); background: rgba(255,255,255,0.05); padding: 12px;">
                <img src="../../images/niche_graphics/{{IMAGE_PATH}}" alt="{{NICHE_NAME}}" style="border-radius: 12px; width: 100%; display: block;">
             </div>
        </div>
    </header>
    """
}

# Hero Variant Assignments
NICHE_VARIANTS = {
    # Home Services -> Mix of Monotree (Clean) and Beyond (Bold)
    "pool-cleaners-and-maintenance": "monotree",
    "pool-contractors-and-construction": "immersive", # Premium
    "landscaping-and-lawn-care": "monotree",
    "hvac-services": "beyond", # Urgent/Bold
    "general-contractors": "monotree",
    "window-installers": "marketive", # Visual
    "plumbers": "beyond", # Urgent
    "painters": "marketive", # Visual
    "electricians": "monotree",
    "property-management": "alva", # Organized/Fintechy

    # Medical -> Clean/Trust (Alva or Monotree) or High End (Immersive)
    "dentists-and-orthodontists": "alva",
    "family-practice-doctors": "monotree",
    "veterinarians": "monotree",
    "med-spas-and-laser-facilities": "immersive", # High end beauty

    # Beauty -> Visual (Marketive) or Stylish
    "hair-salons-and-stylists": "marketive",
    "barbershops": "beyond", # Bold/Masculine
    "nail-salons": "monotree",
    "pet-groomers": "monotree",

    # Professional -> Trust (Alva/Monotree)
    "attorneys-and-law-firms": "alva",
    "accountants-and-cpas": "alva",
    "financial-managers-and-advisors": "alva",
    "real-estate-brokers": "immersive", # Luxury Real Estate vibe

    # Auto & Retail -> Tech/Action
    "auto-mechanics-and-repair-shops": "beyond",
    "window-tinting-and-auto-detail": "marketive",
    "restaurants": "immersive",
}

def generate_pages():
    # Read template
    with open(TEMPLATE_PATH, "r") as f:
        template = f.read()

    # Ensure output dir exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for niche in NICHES:
        slug = niche.get("slug")
        theme_key = niche.get("theme", "default")
        theme = THEMES.get(theme_key, THEMES["default"])
        
        filename = f"{slug}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Generate FAQ HTML (Carousel Structure)
        all_faqs = niche.get("faqs", []) + GLOBAL_FAQS
        
        cards_html = ""
        for faq in all_faqs:
            cards_html += f'''
                <div class="faq-card">
                    <h3 class="faq-question">{faq['q']}</h3>
                    <div class="faq-answer">
                        <p>{faq['a']}</p>
                    </div>
                </div>'''

        faq_html = f'''
    <section class="faq-carousel-section">
        <div class="faq-header-container">
            <div>
                <span class="subtitle" style="text-transform: uppercase; letter-spacing: 1px; font-size: 0.8rem; margin-bottom: 0.5rem; display: block; opacity: 0.7;">Support</span>
                <h2 style="font-weight: 300; font-size: 2.5rem; line-height: 1.2;">Frequently<br><span class="serif-title" style="font-style: italic;">Asked Questions</span></h2>
            </div>
            
            <div class="faq-nav-group">
                <button class="faq-nav-btn prev" aria-label="Previous">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="M12 19l-7-7 7-7"/></svg>
                </button>
                <button class="faq-nav-btn next" aria-label="Next">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
                </button>
            </div>
        </div>

        <div class="faq-carousel-wrapper">
            <div class="faq-track">
{cards_html}
            </div>
        </div>
    </section>'''


        # Replace placeholders using Regex to handle potential whitespace (formatted lines)
        content = template
        content = re.sub(r'\{\{\s*NICHE_NAME\s*\}\}', niche["name"], content)
        content = re.sub(r'\{\{\s*PAIN_POINT\s*\}\}', niche["pain"], content)
        content = re.sub(r'\{\{\s*STAT_TEXT\s*\}\}', niche["stat"], content)
        content = re.sub(r'\{\{\s*OPPORTUNITY\s*\}\}', niche["opportunity"], content)
        content = re.sub(r'\{\{\s*IMAGE_PATH\s*\}\}', niche["image"], content)
        content = re.sub(r'\{\{\s*SERVICE_EXCERPT\s*\}\}', niche.get("excerpt", ""), content)
        content = re.sub(r'\{\{\s*FAQ_SECTION\s*\}\}', faq_html, content)
        
        # Theme Color Replacements
        content = re.sub(r'\{\{\s*ACCENT_COLOR\s*\}\}', theme["accent"], content)
        content = re.sub(r'\{\{\s*LIGHT_BG_COLOR\s*\}\}', theme["light_bg"], content)
        content = re.sub(r'\{\{\s*HERO_BG_COLOR\s*\}\}', theme["hero_bg"], content)
        
        # Hero Background
        hero_bg = f"../../images/niche_backgrounds/bg_{slug}.png"
        content = re.sub(r'\{\{\s*HERO_BG_IMAGE\s*\}\}', hero_bg, content)
        
        # --- Dynamic Hero Selection ---
        variant_key = NICHE_VARIANTS.get(slug, "monotree") # Default to monotree
        hero_html = HERO_TEMPLATES.get(variant_key, HERO_TEMPLATES["monotree"])
        
        # Populate Hero-Specific Placeholders
        # Use provided hero_headline or fallback to generic "Put [Niche] First" style
        default_headline = f"Put {niche['name']} First"
        headline = niche.get("hero_headline", default_headline)
        
        hero_html = hero_html.replace("{{HERO_HEADLINE}}", headline)
        hero_html = hero_html.replace("{{NICHE_NAME}}", niche["name"])
        hero_html = hero_html.replace("{{SERVICE_EXCERPT}}", niche.get("excerpt", ""))
        hero_html = hero_html.replace("{{OPPORTUNITY}}", niche["opportunity"])
        hero_html = hero_html.replace("{{IMAGE_PATH}}", niche["image"])
        hero_html = hero_html.replace("{{STAT_TEXT}}", niche["stat"])
        hero_html = hero_html.replace("{{PAIN_POINT}}", niche["pain"])
        
        # Inject into Main Content
        content = content.replace("{{HERO_SECTION}}", hero_html)
        # ------------------------------
        
        # Generate Services Section
        services_html = ""
        for service in SERVICES:
            # Contextualize description
            desc = service["desc_template"].format(niche_name=niche["name"])
            
            services_html += f'''
            <div class="service-card shine-border">
                <div class="card-content-layer">
                    <div class="service-icon-wrapper"><i data-lucide="{service['icon']}"></i></div>
                    <h3 class="service-title">{service['name']}</h3>
                    <p class="service-desc">{desc}</p>
                    <a href="{service['link']}" class="service-link">
                        Learn More <i data-lucide="arrow-right" size="16"></i>
                    </a>
                </div>
            </div>
            '''
        
        content = content.replace("{{SERVICES_SECTION}}", services_html)

        # Generate Case Studies Section
        case_studies_html = ""
        # Default to first 3 if mapping missing, else use map
        cs_ids = NICHE_CASE_STUDY_MAP.get(slug, ["voice-retail", "reviews-dental", "lead-contractor"])
        
        for cs_id in cs_ids:
            # excessive lookups are fine for this scale
            cs = next((item for item in CASE_STUDIES if item["id"] == cs_id), None)
            if cs:
                case_studies_html += f'''
                <div class="case-card">
                    <div class="case-img" style="background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.6)), url('../../images/stock/stock_business.jpg');">
                         <!-- Fallback icon if no image -->
                         <i data-lucide="{cs['icon']}" size="48" style="opacity: 0.8;"></i>
                         <div class="case-tag">{cs['category']}</div>
                    </div>
                    <div class="case-content">
                        <div class="case-meta">
                            <i data-lucide="calendar" size="14"></i> 2025 Study
                        </div>
                        <h4 style="font-weight: 700; font-size: 1.1rem; margin-bottom: 0.25rem;">{cs['title']}</h4>
                        <div style="font-weight: 800; color: #84cc16; font-size: 0.9rem; margin-bottom: 0.5rem;">{cs['stat']}</div>
                        <p style="font-size: 0.95rem; color: #64748b; margin-top: auto; line-height: 1.5;">{cs['desc']}</p>
                        <a href="#" class="case-link" style="margin-top: 1rem;">Read Analysis <i data-lucide="arrow-right" size="16"></i></a>
                    </div>
                </div>
                '''

        content = content.replace("{{CASE_STUDIES}}", case_studies_html)

        # Write file
        with open(filepath, "w") as f:
            f.write(content)
        
        print(f"Generated: {filename}")

if __name__ == "__main__":
    generate_pages()
