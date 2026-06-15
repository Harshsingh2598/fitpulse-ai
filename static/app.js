// ═══════════════════ STATE ═══════════════════
let activeTab = 'dashboard';
let chatHistoryDash = [
    { sender: 'ai', text: "Hey Harsh 👋 I'm your FitPulse AI Coach. Ask me about chest workout, diet plan, fat loss tips, recovery, legs, or back." }
];
let chatHistoryDedicated = [
    { sender: 'ai', text: "Hey Harsh 👋 I'm your FitPulse AI Coach. How can I help you with your fitness goals today?" }
];

// ═══════════════════ INIT ═══════════════════
document.addEventListener('DOMContentLoaded', () => {

    // Landing page GSAP intro
    if (typeof gsap !== 'undefined') {
        gsap.from('.landing-nav', { duration: 0.6, y: -40, opacity: 0, ease: 'power3.out' });
        gsap.from('.hero-badge', { duration: 0.7, y: -20, opacity: 0, delay: 0.2, ease: 'back.out(1.7)' });
        gsap.from('.hero-title', { duration: 0.9, scale: 0.96, opacity: 0, delay: 0.35, ease: 'power3.out' });
        gsap.from('.hero-sub', { duration: 0.8, y: 20, opacity: 0, delay: 0.5, ease: 'power3.out' });
        gsap.from('.hero-actions > *', { duration: 0.7, y: 15, opacity: 0, delay: 0.65, stagger: 0.12, ease: 'back.out(1.4)' });
        gsap.from('.stat-pill', { duration: 0.6, y: 10, opacity: 0, delay: 0.85, stagger: 0.08, ease: 'power2.out' });
        gsap.from('.feat-card', { duration: 0.7, y: 40, opacity: 0, delay: 1.0, stagger: 0.1, ease: 'power2.out' });
    }

    // Enter app buttons
    const enterBtns = ['btn-enter-app', 'btn-enter-app-2', 'btn-enter-app-3'];
    enterBtns.forEach(id => {
        const btn = document.getElementById(id);
        if (btn) btn.addEventListener('click', enterWorkspace);
    });

    // Report date
    const reportDate = document.getElementById('report-date-display');
    if (reportDate) {
        const d = new Date();
        reportDate.textContent = `${String(d.getDate()).padStart(2,'0')}-${String(d.getMonth()+1).padStart(2,'0')}-${d.getFullYear()}`;
    }

    // Nav clicks
    document.querySelectorAll('.nav-list .nav-item').forEach(item => {
        item.addEventListener('click', e => {
            e.preventDefault();
            switchTab(item.getAttribute('data-target'));
        });
    });

    // Sliders
    bindSlider('diet-weight', 'diet-weight-val', ' kg');
    bindSlider('predictor-weight', 'predictor-weight-val', ' kg');
    bindSlider('predictor-duration', 'predictor-duration-val', ' min');

    // Chat buttons
    document.getElementById('btn-dash-chat-send').addEventListener('click', sendDashMsg);
    document.getElementById('dash-chat-input').addEventListener('keypress', e => { if (e.key === 'Enter') sendDashMsg(); });

    document.getElementById('btn-dedicated-chat-send').addEventListener('click', sendDedicatedMsg);
    document.getElementById('dedicated-chat-input').addEventListener('keypress', e => { if (e.key === 'Enter') sendDedicatedMsg(); });

    document.getElementById('btn-clear-chat-dedicated').addEventListener('click', () => {
        chatHistoryDedicated = [{ sender: 'ai', text: "Chat cleared ✅ Ask your next fitness question." }];
        renderChat('dedicated');
    });

    // Action buttons
    document.getElementById('btn-predict-calories').addEventListener('click', () => predictCalories(true));
    document.getElementById('btn-calculate-diet').addEventListener('click', () => calculateDiet(true));
    document.getElementById('btn-generate-workout').addEventListener('click', generateWorkout);

    // Real-time slider recalculations (instant UI feedback)
    const dietWeight = document.getElementById('diet-weight');
    if (dietWeight) {
        dietWeight.addEventListener('input', () => {
            calculateDiet(false);
        });
    }
    const dietGoal = document.getElementById('diet-goal');
    if (dietGoal) {
        dietGoal.addEventListener('change', () => {
            calculateDiet(true);
        });
    }

    const predWeight = document.getElementById('predictor-weight');
    const predDuration = document.getElementById('predictor-duration');
    const predIntensity = document.getElementById('predictor-intensity');

    const runPredictRealtime = () => {
        predictCalories(false);
    };

    if (predWeight) predWeight.addEventListener('input', runPredictRealtime);
    if (predDuration) predDuration.addEventListener('input', runPredictRealtime);
    if (predIntensity) predIntensity.addEventListener('change', runPredictRealtime);

    // Premium dynamic FX initialization
    if (typeof gsap !== 'undefined') {
        const navList = document.querySelector('.nav-list');
        if (navList) navList.classList.add('has-gsap');
        init3DTilt();
        initMouseGlow();
        initButtonBounce();
    }
    initVoiceCore();
});

// ═══════════════════ ENTER WORKSPACE ═══════════════════
function enterWorkspace() {
    const landing = document.getElementById('landing-page');
    const workspace = document.getElementById('app-workspace');

    if (typeof gsap !== 'undefined') {
        gsap.to(landing, {
            duration: 0.5, opacity: 0, y: -25, ease: 'power2.in',
            onComplete: () => {
                landing.style.display = 'none';
                workspace.style.display = 'flex';
                gsap.fromTo(workspace, { opacity: 0 }, { duration: 0.6, opacity: 1, ease: 'power2.out' });
                gsap.from('.sidebar', { duration: 0.7, x: -270, ease: 'power3.out' });
                gsap.from('.sidebar-brand, .nav-item, .sidebar-user', {
                    duration: 0.5, x: -15, opacity: 0, delay: 0.15, stagger: 0.04, ease: 'power2.out'
                });
                initCharts();
                renderChat('dashboard');
                startCyberTelemetry();
                initTopologyCanvas();
                animatePage('dashboard');
                setTimeout(() => updateNavIndicator('dashboard'), 200);
            }
        });
    } else {
        landing.style.display = 'none';
        workspace.style.display = 'flex';
        initCharts();
        renderChat('dashboard');
        startCyberTelemetry();
        initTopologyCanvas();
    }
}

// ═══════════════════ NAVIGATION ═══════════════════
function switchTab(target) {
    if (activeTab === target) return;
    activeTab = target;
    
    if (typeof gsap !== 'undefined') {
        updateNavIndicator(target);
    }

    document.querySelectorAll('.nav-list .nav-item').forEach(item => {
        item.classList.toggle('active', item.getAttribute('data-target') === target);
    });

    document.querySelectorAll('.page').forEach(p => {
        p.classList.remove('active');
        p.style.display = 'none';
    });

    if (target === 'coach') {
        renderChat('dedicated');
        setTimeout(initTopologyCanvas, 50);
    }
    if (target === 'dashboard') {
        renderChat('dashboard');
        setTimeout(initTopologyCanvas, 50);
    }
    if (target === 'vocal') {
        setTimeout(initVocalOrbCanvas, 50);
    }
    if (target === 'tracker') {
        setTimeout(initHeatmapCanvas, 50);
    }

    animatePage(target);
}

function animatePage(target) {
    const section = document.getElementById(`section-${target}`);
    if (!section) return;

    if (typeof gsap !== 'undefined') {
        section.style.display = 'block';
        gsap.fromTo(section,
            { opacity: 0, y: 15 },
            { duration: 0.5, opacity: 1, y: 0, ease: 'power3.out' }
        );
        const cards = section.querySelectorAll('.card, .metric-card, .chart-box, .three-col-diagnostics > div');
        if (cards.length > 0) {
            gsap.from(cards, {
                duration: 0.45, y: 18, opacity: 0, delay: 0.08,
                stagger: 0.06, ease: 'power2.out'
            });
        }
    } else {
        section.style.display = 'block';
        section.classList.add('active');
        section.style.opacity = '1';
        section.style.transform = 'none';
    }

    if (target === 'dashboard') animateCounters();
}

function animateCounters() {
    if (typeof gsap === 'undefined') return;
    const counters = [
        { id: 'm-calories', end: 2350, fmt: v => Math.round(v).toLocaleString() },
        { id: 'm-workouts', end: 16, fmt: v => Math.round(v) },
        { id: 'm-muscle', end: 88, fmt: v => Math.round(v) + '%' },
        { id: 'm-protein', end: 150, fmt: v => Math.round(v) + 'g' }
    ];
    counters.forEach(c => {
        const el = document.getElementById(c.id);
        if (!el) return;
        let obj = { val: 0 };
        gsap.to(obj, {
            val: c.end, duration: 1.3, ease: 'power3.out',
            onUpdate: () => { el.textContent = c.fmt(obj.val); }
        });
    });
}

// ═══════════════════ SLIDER ═══════════════════
function bindSlider(sliderId, valId, suffix) {
    const s = document.getElementById(sliderId);
    const v = document.getElementById(valId);
    if (s && v) {
        s.addEventListener('input', () => { v.textContent = s.value + suffix; });
    }
}

// ═══════════════════ CHAT ═══════════════════
function appendChatBubble(containerId, msg, animate = true) {
    const container = document.getElementById(containerId);
    if (!container) return;

    // Remove typing dots if present before adding bubble
    removeTyping();

    const bubble = document.createElement('div');
    bubble.className = `chat-bubble ${msg.sender}`;

    const sender = document.createElement('span');
    sender.className = 'chat-sender';
    sender.textContent = msg.sender === 'ai' ? '🤖 Coach' : '🧑 You';

    const text = document.createElement('div');
    text.textContent = msg.text;

    bubble.appendChild(sender);
    bubble.appendChild(text);
    container.appendChild(bubble);

    container.scrollTop = container.scrollHeight;

    if (animate && typeof gsap !== 'undefined') {
        gsap.fromTo(bubble,
            { scale: 0.7, y: 30, opacity: 0, transformOrigin: msg.sender === 'ai' ? 'left bottom' : 'right bottom' },
            { duration: 0.45, scale: 1, y: 0, opacity: 1, ease: 'back.out(1.4)' }
        );
    }
}

function renderChat(key) {
    const cId = key === 'dashboard' ? 'dash-chat-history' : 'dedicated-chat-history';
    const history = key === 'dashboard' ? chatHistoryDash : chatHistoryDedicated;
    const container = document.getElementById(cId);
    if (!container) return;

    container.innerHTML = '';
    history.forEach(msg => {
        appendChatBubble(cId, msg, false); // no entry animation for history
    });
}

function showTyping(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return null;
    
    // Clear any duplicate typing dots
    removeTyping();

    const indicator = document.createElement('div');
    indicator.className = 'typing-indicator';
    indicator.id = 'typing-dots';
    indicator.innerHTML = '<div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>';
    container.appendChild(indicator);
    container.scrollTop = container.scrollHeight;
    
    // Animate typing dots with a quick bounce
    if (typeof gsap !== 'undefined') {
        gsap.fromTo('.typing-dot',
            { y: 0 },
            { y: -6, duration: 0.4, repeat: -1, yoyo: true, stagger: 0.15, ease: 'power1.inOut' }
        );
    }
    return indicator;
}

function removeTyping() {
    const dots = document.getElementById('typing-dots');
    if (dots) dots.remove();
}

async function queryCoach(message) {
    try {
        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question: message })
        });
        if (res.ok) {
            const data = await res.json();
            return data.reply;
        }
        throw new Error('HTTP error');
    } catch (e) {
        return getOfflineReply(message);
    }
}

function getOfflineReply(q) {
    q = (q || '').toLowerCase().trim();
    if (!q) return "Ask me anything about workouts, diet, calories, fat loss, muscle gain, recovery, or specific food items!";
    
    // Exact word boundary regular expressions to prevent substring collisions (e.g. "chicken" matching "hi", "whey" matching "hey")
    if (/\b(hello|hi|hey|sup|what's up)\b/.test(q)) {
        return "Hey Harsh 👋 I'm your FitPulse AI Coach. Ask me any fitness query! You can ask about chest, back, legs, arms, shoulders, core, cardio, diet plans, fat loss, muscle gain, recovery, or supplements.";
    }
    
    // Food items / Diet specific queries
    if (/\b(banana|bananas|oats|oatmeal|carb|carbs)\b/.test(q)) {
        return "🍌 Oats and bananas are premium carbohydrate sources. Bananas provide quick-acting fructose and potassium (perfect 30 mins pre-workout). Oats are complex, slow-digesting carbs that provide sustained energy. Keep carbs around 3-5g per kg of bodyweight.";
    }
    
    // Supplements (checked before general protein to prioritize supplements like whey/creatine)
    if (/\b(creatine|whey|supplement|supplements)\b/.test(q)) {
        return "💊 Supplement recommendations: 1. Creatine Monohydrate (5g daily) for strength & cellular hydration. 2. Whey Protein (25-30g post-workout) for convenience. 3. Caffeine (150-300mg) for energy. Skip overpriced fat burners or BCAAs.";
    }
    
    if (/\b(chicken|paneer|egg|eggs|tofu|fish|meat|protein|shake)\b/.test(q)) {
        return "🍳 High protein foods are vital for muscle protein synthesis. Chicken breast (31g protein/100g), Paneer (18g protein/100g), Egg whites (4g protein/egg), and Whey protein are clean sources. Target 1.6 to 2.2g of protein per kg of bodyweight daily.";
    }
    
    if (/\b(diet|meal|food|eat|nutrition)\b/.test(q)) {
        return "🥗 Optimal diet layout: Breakfast: Oats, eggs, or paneer. Lunch: Rice/quinoa + chicken/paneer/tofu + green salad. Pre-workout: Banana + black coffee. Post-workout: Whey protein shake. Dinner: Sweet potato/roti + fish/tempeh + broccoli. Adjust calories based on your gain/loss goal.";
    }
    if (/\b(fat|loss|cut|weight loss|reduce|lean|shred)\b/.test(q)) {
        return "🔥 Fat loss protocol: Maintain a 300-500 kcal deficit below TDEE. Keep protein high (2.0-2.4g/kg) to protect muscle. Walk 8,000-10,000 steps daily. Incorporate strength training 4x/week and high-intensity cardio 2x/week. Sleep 8 hours.";
    }
    if (/\b(muscle|gain|bulk|bulking|hypertrophy)\b/.test(q)) {
        return "💪 Muscle gain protocol: Maintain a small caloric surplus (+300 kcal). Prioritize progressive overload (increase weight/reps weekly). Focus on compound lifts (squats, bench, pull-ups) in the 8-12 rep range. Consume 1.8-2.2g protein/kg.";
    }
    
    // Workouts / Exercise specific queries
    if (/\b(chest|push|bench|pec)\b/.test(q)) {
        return "🏋️ Chest Hypertrophy: Flat Barbell Bench Press (4x8), Incline Dumbbell Press (4x10), Decline Hammer Strength Press (3x10), Cable Crossover Fly (3x15). Focus on a 3-second negative phase and full contraction.";
    }
    if (/\b(back|pull|lat|row|deadlift)\b/.test(q)) {
        return "💪 Back Thickness & Width: Pull-ups (4 sets to failure), Wide-grip Lat Pulldowns (4x12), Barbell Bent-over Rows (4x10), Seated Cable Rows (3x12), and Deadlifts (3x5). Drive with your elbows to maximize lat activation.";
    }
    if (/\b(leg|legs|squat|quad|hamstring|glute|calf|calves)\b/.test(q)) {
        return "🦵 Complete Leg Day: Barbell Back Squats (4x8), Leg Press (4x12), Romanian Deadlifts (4x10 for hamstrings), Bulgarian Split Squats (3x10 each leg), and Standing Calf Raises (4x20). Focus on full range of motion.";
    }
    if (/\b(shoulder|shoulders|delt|delts|ohp)\b/.test(q)) {
        return "🔱 3D Shoulder Protocol: Overhead Barbell Press (4x8), Seated Dumbbell Press (4x10), Dumbbell Lateral Raises (4x15 for side delts), Face Pulls (4x15 for rear delts), and Barbell Shrugs (3x12 for traps). Keep side lateral raises strict.";
    }
    if (/\b(arm|arms|bicep|biceps|tricep|triceps|curl)\b/.test(q)) {
        return "💪 Arms Pump supersets: Alternate Biceps Curl (4x12) with Close-Grip Bench Press (4x10). Superset Hammer Curls (3x12) with Cable Rope Pushdowns (3x15). Finish with Preacher Curls (3x12) and Skull Crushers (3x12).";
    }
    if (/\b(abs|core|plank|crunch|six pack)\b/.test(q)) {
        return "🔥 Core Stability & Definition: Hanging Leg Raises (4x12), Cable Crunches (3x15), Russian Twists (3x20), and Planks (3x60 seconds). Note: Visible abs require a low body fat percentage (<14% for men, <22% for women).";
    }
    if (/\b(cardio|hiit|running|run|cycling|treadmill)\b/.test(q)) {
        return "🏃 Cardio & HIIT protocols: For active recovery, do 30-45 mins of LISS (Low-Intensity Steady State) like fast walking or cycling. For calorie conditioning, do HIIT: 15 seconds sprint followed by 45 seconds walk, repeat 15 times.";
    }
    
    // Recovery / Support queries
    if (/\b(recovery|sleep|rest|sore|injury|stretching)\b/.test(q)) {
        return "🛌 Muscle Recovery: Sleep 7-9 hours (growth hormone peaks during deep sleep), stay hydrated (3L+ water), consume 30g protein post-workout, and do active recovery stretching/foam rolling. Take 1-2 full rest days weekly.";
    }
    if (/\b(beginner|start|new|first)\b/.test(q)) {
        return "✅ Beginner Fitness Blueprint: Start with a 3-day Full Body workout schedule (Squats, Push-ups, Lat Pulldowns, Overhead Press, Planks). Train with light weights, master form first, and progressively overload.";
    }
    if (/\b(workout|workouts|exercise|exercises|training|routine|gym|schedule)\b/.test(q)) {
        return "🏋️ FitPulse Routine Selector: You can get specific workouts by asking for Chest workout, Back workout, Leg workout, Shoulder workout, Arm workout, or Core workout. You can also generate a custom program in the Synth Lab tab!";
    }
    if (/motivat|\b(lazy|skip|don't feel|can't|hard|give up|quit)\b/.test(q)) {
        return "🔥 Motivation Radar: Commit to just 15 minutes of training. Get dressed, walk in the gym, and start. Action breeds motivation! Track your progress and remember your 'why'. Let's go! 🚀";
    }
    
    return `🤖 FitPulse AI Coach: For "${q}", remember the golden pillars: 1. Progressive overload (increase intensity weekly), 2. High protein intake (1.6-2.2g/kg), 3. Caloric control (deficit for fat loss, surplus for muscle), 4. Sleep 8 hours. Ask me about specific exercises or meals!`;
}

async function sendDashMsg() {
    const input = document.getElementById('dash-chat-input');
    const msg = input.value.trim();
    if (!msg) return;

    const userMsg = { sender: 'user', text: msg };
    chatHistoryDash.push(userMsg);
    input.value = '';

    appendChatBubble('dash-chat-history', userMsg, true);
    showTyping('dash-chat-history');

    const reply = await queryCoach(msg);
    const aiMsg = { sender: 'ai', text: reply };
    chatHistoryDash.push(aiMsg);

    appendChatBubble('dash-chat-history', aiMsg, true);
}

async function sendDedicatedMsg() {
    const input = document.getElementById('dedicated-chat-input');
    const msg = input.value.trim();
    if (!msg) return;

    const userMsg = { sender: 'user', text: msg };
    chatHistoryDedicated.push(userMsg);
    input.value = '';

    appendChatBubble('dedicated-chat-history', userMsg, true);
    showTyping('dedicated-chat-history');

    const reply = await queryCoach(msg);
    const aiMsg = { sender: 'ai', text: reply };
    chatHistoryDedicated.push(aiMsg);

    appendChatBubble('dedicated-chat-history', aiMsg, true);
}

function quickQuery(text) {
    const input = document.getElementById('dash-chat-input');
    if (input) { input.value = text; sendDashMsg(); }
}
function quickQueryDedicated(text) {
    const input = document.getElementById('dedicated-chat-input');
    if (input) { input.value = text; sendDedicatedMsg(); }
}

// ═══════════════════ CALORIE PREDICTOR ═══════════════════
async function predictCalories(animate = true) {
    const weight = parseInt(document.getElementById('predictor-weight').value);
    const duration = parseInt(document.getElementById('predictor-duration').value);
    const intensity = document.getElementById('predictor-intensity').value;
    const card = document.getElementById('predict-card');
    const valEl = document.getElementById('cal-prediction-value');
    const msgEl = document.getElementById('cal-prediction-message');

    let calories;
    const factor = { Low: 5, Medium: 8, High: 12 }[intensity] || 8;
    calories = Math.round(duration * factor * weight / 70);

    card.classList.add('active');

    if (animate) {
        valEl.textContent = '...';
        try {
            const res = await fetch('/api/predict_calories', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ weight, duration, intensity })
            });
            if (res.ok) {
                const data = await res.json();
                calories = data.calories;
            }
        } catch (e) {}

        if (typeof gsap !== 'undefined') {
            let obj = { val: 0 };
            gsap.to(obj, {
                val: calories, duration: 1.2, ease: 'power3.out',
                onUpdate: () => { valEl.textContent = Math.round(obj.val); }
            });
        } else {
            valEl.textContent = calories;
        }
    } else {
        if (typeof gsap !== 'undefined') {
            gsap.to(valEl, {
                duration: 0.15,
                innerText: calories,
                snap: { innerText: 1 },
                ease: 'power1.out',
                overwrite: 'auto'
            });
        } else {
            valEl.textContent = calories;
        }
    }
    msgEl.textContent = `Energy burned at ${intensity.toLowerCase()} intensity for ${duration} minutes at ${weight}kg.`;
}

// ═══════════════════ DIET PLANNER ═══════════════════
function calculateDiet(animate = true) {
    const weight = parseInt(document.getElementById('diet-weight').value);
    const goal = document.getElementById('diet-goal').value;

    const calEl = document.getElementById('diet-display-calories');
    const proEl = document.getElementById('diet-display-protein');
    const carbEl = document.getElementById('diet-display-carbs');
    const fatEl = document.getElementById('diet-display-fats');
    const output = document.getElementById('diet-output');
    const container = document.getElementById('diet-meals-container');

    const protein = Math.round(weight * 1.8);
    let calories;
    if (goal === 'Muscle Gain') calories = Math.round(weight * 30) + 400;
    else if (goal === 'Fat Loss') calories = Math.round(weight * 30) - 500;
    else calories = Math.round(weight * 30);
    calories = Math.max(1200, Math.min(4500, calories));

    const fats = Math.round(calories * 0.25 / 9);
    const carbs = Math.round((calories - protein * 4 - fats * 9) / 4);

    calEl.textContent = `${calories.toLocaleString()} kcal`;
    proEl.textContent = `${protein}g`;
    carbEl.textContent = `${Math.max(0, carbs)}g`;
    fatEl.textContent = `${fats}g`;

    let meals = [];
    if (goal === 'Muscle Gain') {
        meals = [
            { name: "🍳 Breakfast (High Cal)", items: [
                { n: "Rolled Oats & Milk", q: `${Math.round(weight*1.3)}g oats + 300ml milk` },
                { n: "Whole Eggs & Whites", q: "3 Whole + 2 Whites" },
                { n: "Almonds & Honey", q: "1.5 handfuls + 1 Tbsp" }
            ]},
            { name: "🍲 Lunch (Anabolic)", items: [
                { n: "Rice / Pasta", q: `${Math.round(weight*3.5)}g cooked` },
                { n: "Chicken / Paneer", q: `${Math.round(weight*2.5)}g raw` },
                { n: "Veggies & Olive Oil", q: "1 Large Bowl + 1 Tbsp" }
            ]},
            { name: "🍌 Mid-day Snack", items: [
                { n: "Banana & PB", q: "2 Bananas + 2 Tbsp PB" },
                { n: "Whey Protein", q: "1.5 Scoops" }
            ]},
            { name: "🥗 Dinner (Recovery)", items: [
                { n: "Quinoa / Sweet Potato", q: `${Math.round(weight*2.5)}g cooked` },
                { n: "Salmon / Tofu", q: `${Math.round(weight*2.2)}g raw` },
                { n: "Steamed Broccoli", q: "200g with lemon" }
            ]}
        ];
    } else if (goal === 'Fat Loss') {
        meals = [
            { name: "🍳 Breakfast (High Protein)", items: [
                { n: "Oats & Skim Milk", q: `${Math.round(weight*0.7)}g oats + 200ml` },
                { n: "Egg Whites / Paneer", q: "5 Whites / 100g Paneer" },
                { n: "Chia / Almonds", q: "1 Tbsp / 10 pieces" }
            ]},
            { name: "🍲 Lunch (Lean)", items: [
                { n: "Rice / Roti", q: `${Math.round(weight*1.2)}g / 1 Roti` },
                { n: "Grilled Chicken / Tofu", q: `${Math.round(weight*2.2)}g raw` },
                { n: "Green Salad", q: "1 Large Bowl + lemon" }
            ]},
            { name: "🍎 Snack", items: [
                { n: "Apple / Orange", q: "1 Medium Fruit" },
                { n: "Greek Yogurt", q: "150g" }
            ]},
            { name: "🥗 Dinner (Low Carb)", items: [
                { n: "Cauliflower Rice", q: `${Math.round(weight*0.8)}g cooked` },
                { n: "Baked Fish / Tempeh", q: `${Math.round(weight*2.0)}g raw` },
                { n: "Broccoli & Spinach", q: "250g steamed" }
            ]}
        ];
    } else {
        meals = [
            { name: "🍳 Breakfast", items: [
                { n: "Oats & Low-Fat Milk", q: `${Math.round(weight*1.0)}g + 250ml` },
                { n: "Eggs", q: "2 Whole + 2 Whites" },
                { n: "Nuts & Berries", q: "1 Handful (20g)" }
            ]},
            { name: "🍲 Lunch", items: [
                { n: "Rice / Roti", q: `${Math.round(weight*2.2)}g / 2 Rotis` },
                { n: "Chicken / Paneer", q: `${Math.round(weight*2.2)}g raw` },
                { n: "Mixed Salad", q: "1 Bowl + 1 Tsp Oil" }
            ]},
            { name: "🍌 Snack", items: [
                { n: "Banana & Almonds", q: "1 Banana + 15 Almonds" },
                { n: "Whey / Soya", q: "1 Scoop / 45g" }
            ]},
            { name: "🥗 Dinner", items: [
                { n: "Quinoa / Brown Rice", q: `${Math.round(weight*1.5)}g cooked` },
                { n: "Salmon / Tofu", q: `${Math.round(weight*2.0)}g raw` },
                { n: "Steamed Veggies", q: "200g" }
            ]}
        ];
    }

    container.innerHTML = '';
    meals.forEach((m, i) => {
        const card = document.createElement('div');
        card.className = 'day-card';
        const hdr = document.createElement('div');
        hdr.className = 'day-name';
        hdr.textContent = m.name;
        card.appendChild(hdr);

        m.items.forEach(item => {
            const row = document.createElement('div');
            row.className = 'exercise-row';
            const nameSpan = document.createElement('span');
            nameSpan.textContent = item.n;
            const qtySpan = document.createElement('span');
            qtySpan.className = 'exercise-reps';
            qtySpan.textContent = item.q;
            row.appendChild(nameSpan);
            row.appendChild(qtySpan);
            card.appendChild(row);
        });

        container.appendChild(card);

        if (animate && typeof gsap !== 'undefined') {
            gsap.from(card, { duration: 0.4, y: 20, opacity: 0, delay: i * 0.1, ease: 'power2.out' });
        }
    });

    output.style.display = 'block';
    output.classList.remove('hidden-section');
    if (animate) {
        setTimeout(() => { output.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); }, 80);
    }
}

// ═══════════════════ WORKOUT GENERATOR ═══════════════════
function generateWorkout() {
    const goal = document.getElementById('workout-goal').value;
    const level = document.getElementById('workout-level').value;
    const output = document.getElementById('workout-output');
    const title = document.getElementById('workout-title');
    const container = document.getElementById('routine-days-container');

    title.textContent = `${goal} Routine — ${level} Level`;

    let routine = [];
    if (goal === 'Muscle Gain') {
        routine = [
            { day: "🏋️ Day 1: Chest & Triceps", ex: ["Bench Press|4x10", "Incline DB Press|4x12", "Cable Fly|3x15", "Skullcrushers|3x12", "Tricep Pushdowns|4x12"] },
            { day: "💪 Day 2: Back & Biceps", ex: ["Pullups|4xMax", "Lat Pulldown|4x12", "Barbell Rows|3x10", "Hammer Curls|3x15", "Cable Bicep Curls|4x12"] },
            { day: "🦵 Day 3: Legs & Abs", ex: ["Barbell Squats|4x8", "Leg Press|4x12", "Leg Curls|3x15", "Calf Raises|4x20", "Hanging Leg Raises|3x15"] },
            { day: "🔥 Day 4: Shoulders & Arms", ex: ["Overhead Press|4x10", "Lateral Raises|4x15", "Face Pulls|3x15", "DB Shrugs|4x12", "Close-Grip Bench|3x10"] }
        ];
    } else if (goal === 'Fat Loss') {
        routine = [
            { day: "🏃 Day 1: HIIT & Core", ex: ["Treadmill Sprints|10 intervals", "KB Swings|4x20", "Mountain Climbers|4x30s", "Russian Twists|3x20", "Plank|3x60s"] },
            { day: "🏋️ Day 2: Upper Circuit", ex: ["Pushups|4x15", "DB Rows|4x12", "DB Thrusters|3x12", "Dips|3x12", "Curl to Press|3x15"] },
            { day: "🦵 Day 3: Lower Burn", ex: ["Goblet Squats|4x15", "Walking Lunges|3x20", "Glute Bridges|3x20", "Jump Squats|3x15", "Calf Raises|3x25"] },
            { day: "🚲 Day 4: LISS & Abs", ex: ["Stationary Bike|45 min", "Hanging Knee Raises|3x15", "Ab Wheel|3x12", "Side Planks|3x30s each"] }
        ];
    } else if (goal === 'Strength') {
        routine = [
            { day: "🏋️ Day 1: Squat Focus", ex: ["Barbell Squats|5x5", "Leg Press|3x8", "Romanian DL|3x8", "Ab Rollouts|3x10", "Planks|3x60s"] },
            { day: "💪 Day 2: Bench Focus", ex: ["Bench Press|5x5", "Close-Grip Bench|3x8", "Incline DB Bench|3x8", "Weighted Pullups|4x6", "Barbell Curls|3x8"] },
            { day: "🏋️ Day 3: Deadlift Focus", ex: ["Deadlifts|5x5", "Barbell Shrugs|3x8", "Deficit DL|3x5", "DB Row|3x8", "Farmer Walks|3x50m"] },
            { day: "🔥 Day 4: Press Focus", ex: ["Military Press|5x5", "Dips|3x8", "Lateral Raises|3x12", "Face Pulls|4x12", "Chin-ups|3xMax"] }
        ];
    } else {
        routine = [
            { day: "🟢 Day 1: Full Body A", ex: ["Goblet Squats|3x10", "Pushups|3xMax", "DB Rows|3x10", "DB Shoulder Press|3x10", "Plank|3x30s"] },
            { day: "💤 Day 2: Recovery", ex: ["Light Walking|30 mins", "Full Body Stretch|15 mins", "Mobility Drills|10 mins"] },
            { day: "🟢 Day 3: Full Body B", ex: ["Leg Press|3x10", "Lat Pulldown|3x10", "DB Bench|3x10", "Hamstring Curl|3x12", "Bird-Dogs|3x10"] }
        ];
    }

    container.innerHTML = '';
    routine.forEach((day, i) => {
        const card = document.createElement('div');
        card.className = 'day-card';
        const hdr = document.createElement('div');
        hdr.className = 'day-name';
        hdr.textContent = day.day;
        card.appendChild(hdr);

        day.ex.forEach(e => {
            const parts = e.split('|');
            const row = document.createElement('div');
            row.className = 'exercise-row';
            const name = document.createElement('span');
            name.textContent = parts[0];
            const reps = document.createElement('span');
            reps.className = 'exercise-reps';
            reps.textContent = parts[1] || '';
            row.appendChild(name);
            row.appendChild(reps);
            card.appendChild(row);
        });

        container.appendChild(card);
        if (typeof gsap !== 'undefined') {
            gsap.from(card, { duration: 0.4, y: 20, opacity: 0, delay: i * 0.1, ease: 'power2.out' });
        }
    });

    output.style.display = 'block';
    output.classList.remove('hidden-section');
    setTimeout(() => { output.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); }, 80);
}

// ═══════════════════ CHARTS ═══════════════════
let calChart = null;
let proChart = null;

function initCharts() {
    const calCtx = document.getElementById('chart-calories');
    const proCtx = document.getElementById('chart-protein');
    if (!calCtx || !proCtx) return;

    if (calChart) calChart.destroy();
    if (proChart) proChart.destroy();

    Chart.defaults.color = '#94a3b8';
    Chart.defaults.font.family = "'Inter', sans-serif";

    calChart = new Chart(calCtx.getContext('2d'), {
        type: 'line',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [{
                label: 'Calories Burned',
                data: [400, 520, 650, 700, 620, 800, 900],
                borderColor: '#00f5ff',
                backgroundColor: 'rgba(0,245,255,0.08)',
                borderWidth: 3,
                tension: 0.4,
                fill: true,
                pointBackgroundColor: '#00f5ff',
                pointBorderColor: '#fff',
                pointRadius: 5,
                pointHoverRadius: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                y: { grid: { color: 'rgba(255,255,255,0.04)' }, ticks: { callback: v => v + ' kcal' } },
                x: { grid: { display: false } }
            }
        }
    });

    const ctx2d = proCtx.getContext('2d');
    const gradient = ctx2d.createLinearGradient(0, 0, 0, 300);
    gradient.addColorStop(0, '#ff2bd6');
    gradient.addColorStop(1, '#8a2bff');

    proChart = new Chart(ctx2d, {
        type: 'bar',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [{
                label: 'Protein (g)',
                data: [100, 120, 130, 125, 140, 145, 150],
                backgroundColor: gradient,
                borderColor: '#ff2bd6',
                borderWidth: 1,
                borderRadius: 8,
                hoverBackgroundColor: '#ff2bd6'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                y: { grid: { color: 'rgba(255,255,255,0.04)' }, ticks: { callback: v => v + 'g' } },
                x: { grid: { display: false } }
            }
        }
    });
}

// ═══════════════════ CYBER CANVAS & TELEMETRY ═══════════════════
let anomalyInterval = null;
let fluxInterval = null;
let topologyAnimId = null;
let vocalAnimId = null;
let heatmapAnimId = null;

function startCyberTelemetry() {
    const dashLog = document.getElementById('dashboard-anomaly-log');
    const vocalLog = document.getElementById('vocal-logic-log');
    
    const logsList = [
        "FITPULSE_SYNC :: Caloric offset detected in Sector 7-G. Adjusting macro distribution...",
        "ALERT :: Predictive model 0.98 accuracy confirmed for anomaly cluster ALPHA. Initiating counter-measures.",
        "SYS :: Entropy levels within normal parameters (0.0831%). Global sync verified.",
        "WARNING :: Memory fragmentation detected in Neural Core 01. Garbage collection starting...",
        "CRON :: Hydration sync active. Synaptic latency at 0.04ms.",
        "LOG :: User Harsh Singh completed core authentication block. Session token refreshed.",
        "RAG :: Fragment_7B correlation confirmed for high-frequency trading indices. Match rate 98.2%.",
        "BIOMETRIC :: Heart rate spike detected (Zone 4 transition). Auto-logging HIIT session.",
        "DIET_PLANNER :: Macro optimization complete. Protein ratio calibrated to 2.2g/kg.",
        "ACHIEVEMENT :: Streaks validation complete. Level 24 XP refreshed (+500 XP)."
    ];
    
    if (anomalyInterval) clearInterval(anomalyInterval);
    anomalyInterval = setInterval(() => {
        const time = new Date().toLocaleTimeString();
        const randLog = logsList[Math.floor(Math.random() * logsList.length)];
        const color = randLog.includes("ALERT") ? "#ff3366" : randLog.includes("WARNING") ? "#ffb800" : randLog.includes("RESOLVED") || randLog.includes("complete") ? "#39ff14" : "#a5b4fc";
        
        const logLine = `<div style="color: ${color};"><span style="color: #6366f1;">[${time}]</span> ${randLog}</div>`;
        
        if (dashLog) {
            dashLog.innerHTML += logLine;
            dashLog.scrollTop = dashLog.scrollHeight;
            if (dashLog.children.length > 50) dashLog.children[0].remove();
        }
        if (vocalLog) {
            vocalLog.innerHTML += logLine;
            vocalLog.scrollTop = vocalLog.scrollHeight;
            if (vocalLog.children.length > 50) vocalLog.children[0].remove();
        }
    }, 4000);
    
    const dashFlux = document.getElementById('dashboard-flux-stream');
    const vocalFlux = document.getElementById('vocal-flux-stream');
    
    if (fluxInterval) clearInterval(fluxInterval);
    fluxInterval = setInterval(() => {
        const hexAddr = "0x" + Math.floor(Math.random()*1000).toString(16).toUpperCase();
        let hexBytes = [];
        for (let i = 0; i < 8; i++) {
            hexBytes.push(Math.floor(Math.random()*256).toString(16).toUpperCase().padStart(2, '0'));
        }
        const fluxLine = `<div>${hexAddr.padEnd(6, ' ')} ${hexBytes.join(' ')}</div>`;
        
        if (dashFlux) {
            dashFlux.innerHTML += fluxLine;
            dashFlux.scrollTop = dashFlux.scrollHeight;
            if (dashFlux.children.length > 30) dashFlux.children[0].remove();
        }
        if (vocalFlux) {
            vocalFlux.innerHTML += fluxLine;
            vocalFlux.scrollTop = vocalFlux.scrollHeight;
            if (vocalFlux.children.length > 30) vocalFlux.children[0].remove();
        }
    }, 1200);

    // Initial fill
    for (let i = 0; i < 10; i++) {
        const hexAddr = "0x" + Math.floor(Math.random()*1000).toString(16).toUpperCase();
        let hexBytes = [];
        for (let j = 0; j < 8; j++) {
            hexBytes.push(Math.floor(Math.random()*256).toString(16).toUpperCase().padStart(2, '0'));
        }
        const fluxLine = `<div>${hexAddr.padEnd(6, ' ')} ${hexBytes.join(' ')}</div>`;
        if (dashFlux) dashFlux.innerHTML += fluxLine;
        if (vocalFlux) vocalFlux.innerHTML += fluxLine;
    }
}

// Node Topology Canvas rendering
function initTopologyCanvas() {
    const canvas = document.getElementById('canvas-topology');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    let angle = 0;
    const nodes = [
        { x: 0, y: -40, color: '#00f5ff', r: 5 },  // top
        { x: -38, y: 12, color: '#39ff14', r: 5 }, // left
        { x: 38, y: 12, color: '#ff7a18', r: 5 },  // right
        { x: 0, y: 40, color: '#8a2bff', r: 5 },   // bottom
        { x: 0, y: 0, color: '#ff2bd6', r: 7 }     // center
    ];
    
    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        const cx = canvas.width / 2;
        const cy = canvas.height / 2;
        
        ctx.beginPath();
        ctx.arc(cx, cy, 40, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(0, 245, 255, 0.08)';
        ctx.lineWidth = 1;
        ctx.stroke();
        
        ctx.beginPath();
        ctx.arc(cx, cy, 20, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(0, 245, 255, 0.04)';
        ctx.stroke();
        
        angle += 0.015;
        
        const rotatedNodes = nodes.map((node, i) => {
            if (i === 4) return { x: cx, y: cy, color: node.color, r: node.r };
            const cos = Math.cos(angle);
            const sin = Math.sin(angle);
            const rx = node.x * cos - node.y * sin;
            const ry = node.x * sin + node.y * cos;
            return { x: cx + rx, y: cy + ry, color: node.color, r: node.r };
        });
        
        ctx.lineWidth = 1;
        for (let i = 0; i < 4; i++) {
            ctx.beginPath();
            ctx.moveTo(rotatedNodes[4].x, rotatedNodes[4].y);
            ctx.lineTo(rotatedNodes[i].x, rotatedNodes[i].y);
            ctx.strokeStyle = `rgba(0, 245, 255, 0.25)`;
            ctx.stroke();
            
            const nextIdx = (i + 1) % 4;
            ctx.beginPath();
            ctx.moveTo(rotatedNodes[i].x, rotatedNodes[i].y);
            ctx.lineTo(rotatedNodes[nextIdx].x, rotatedNodes[nextIdx].y);
            ctx.strokeStyle = `rgba(255, 43, 214, 0.2)`;
            ctx.stroke();
        }
        
        rotatedNodes.forEach(node => {
            ctx.beginPath();
            ctx.arc(node.x, node.y, node.r, 0, Math.PI * 2);
            ctx.fillStyle = node.color;
            ctx.shadowBlur = 10;
            ctx.shadowColor = node.color;
            ctx.fill();
            ctx.shadowBlur = 0;
        });
        
        topologyAnimId = requestAnimationFrame(draw);
    }
    
    if (topologyAnimId) cancelAnimationFrame(topologyAnimId);
    draw();
}

// Pulsing Vocal Orb Ring Visualizer
let vocalPulsing = false;
function initVocalOrbCanvas() {
    const canvas = document.getElementById('canvas-vocal-orb');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    let time = 0;
    
    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        const cx = canvas.width / 2;
        const cy = canvas.height / 2;
        
        time += 0.05;
        
        const baseRadius = 90;
        const numRings = 3;
        
        for (let r = 0; r < numRings; r++) {
            const radFactor = baseRadius + r * 30 + (vocalPulsing ? Math.sin(time + r) * 15 : Math.sin(time * 0.5 + r) * 4);
            const opacity = 0.25 - r * 0.08 + (vocalPulsing ? Math.abs(Math.sin(time)) * 0.1 : 0);
            
            ctx.beginPath();
            ctx.arc(cx, cy, radFactor, 0, Math.PI * 2);
            ctx.strokeStyle = `rgba(0, 245, 255, ${opacity})`;
            ctx.lineWidth = 2 - r * 0.5;
            ctx.stroke();
            
            ctx.beginPath();
            ctx.arc(cx, cy, radFactor + 6, time * 0.1 * (r + 1), time * 0.1 * (r + 1) + 0.4);
            ctx.strokeStyle = `rgba(255, 43, 214, ${opacity * 1.5})`;
            ctx.lineWidth = 3;
            ctx.stroke();
        }
        
        const numPoints = 12;
        const points = [];
        for (let i = 0; i < numPoints; i++) {
            const angle = (i / numPoints) * Math.PI * 2 + time * 0.02;
            const amp = vocalPulsing ? 25 + Math.sin(time * 2 + i) * 18 : 10 + Math.sin(time * 0.5 + i) * 3;
            const radius = 68 + amp;
            points.push({
                x: cx + Math.cos(angle) * radius,
                y: cy + Math.sin(angle) * radius
            });
        }
        
        ctx.beginPath();
        ctx.moveTo(points[0].x, points[0].y);
        for (let i = 1; i < numPoints; i++) {
            ctx.lineTo(points[i].x, points[i].y);
        }
        ctx.closePath();
        ctx.strokeStyle = 'rgba(0, 245, 255, 0.4)';
        ctx.lineWidth = 1.5;
        ctx.stroke();
        
        ctx.strokeStyle = 'rgba(138, 43, 226, 0.15)';
        ctx.lineWidth = 1;
        for (let i = 0; i < numPoints; i++) {
            const next = (i + 4) % numPoints;
            ctx.beginPath();
            ctx.moveTo(points[i].x, points[i].y);
            ctx.lineTo(points[next].x, points[next].y);
            ctx.stroke();
        }
        
        vocalAnimId = requestAnimationFrame(draw);
    }
    
    if (vocalAnimId) cancelAnimationFrame(vocalAnimId);
    draw();
}

// Synaptic Density Heatmap
function initHeatmapCanvas() {
    const canvas = document.getElementById('canvas-heatmap');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    const blobs = [];
    const numBlobs = 6;
    
    for (let i = 0; i < numBlobs; i++) {
        blobs.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            vx: (Math.random() - 0.5) * 1.5,
            vy: (Math.random() - 0.5) * 1.5,
            r: 50 + Math.random() * 40,
            color: i % 3 === 0 ? 'rgba(0, 245, 255, 0.25)' : i % 3 === 1 ? 'rgba(255, 43, 214, 0.22)' : 'rgba(57, 255, 20, 0.18)'
        });
    }
    
    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        ctx.fillStyle = 'rgba(3, 7, 18, 0.3)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        ctx.globalCompositeOperation = 'screen';
        
        blobs.forEach(b => {
            b.x += b.vx;
            b.y += b.vy;
            
            if (b.x - b.r < 0 || b.x + b.r > canvas.width) b.vx *= -1;
            if (b.y - b.r < 0 || b.y + b.r > canvas.height) b.vy *= -1;
            
            const grad = ctx.createRadialGradient(b.x, b.y, 0, b.x, b.y, b.r);
            grad.addColorStop(0, b.color);
            grad.addColorStop(1, 'rgba(0,0,0,0)');
            
            ctx.beginPath();
            ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
            ctx.fillStyle = grad;
            ctx.fill();
        });
        
        ctx.globalCompositeOperation = 'source-over';
        
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.02)';
        ctx.lineWidth = 1;
        const gridSize = 20;
        for (let x = 0; x < canvas.width; x += gridSize) {
            ctx.beginPath();
            ctx.moveTo(x, 0);
            ctx.lineTo(x, canvas.height);
            ctx.stroke();
        }
        for (let y = 0; y < canvas.height; y += gridSize) {
            ctx.beginPath();
            ctx.moveTo(0, y);
            ctx.lineTo(canvas.width, y);
            ctx.stroke();
        }
        
        heatmapAnimId = requestAnimationFrame(draw);
    }
    
    if (heatmapAnimId) cancelAnimationFrame(heatmapAnimId);
    draw();
}

// Simulated Voice AI assistant coaching phrases (for fallback)
const voicePhrases = [
    { u: "Recommend a high-intensity chest exercise routine.", a: "Analyzing hypertrophy profiles... Matching chest workouts. Incline dumbbell press 4x10, flat bench press 4x8, cable crossover fly 3x15 recommended. Focus on retraction & tempo." },
    { u: "Check my calorie burn for a 30-minute HIIT run.", a: "Predicting energy burn... Running at High intensity for 30 minutes at 72kg burns approximately 342 kilocalories. EPOC afterburn active (+51 kcal)." },
    { u: "What is my current muscle score status?", a: "Accessing biometrics... Muscle Score at 88% (+1.2% growth). Consistency is high. Recommended recovery index: 7.5 hours sleep tonight." },
    { u: "Establish a fat loss macro layout.", a: "Compiling diet matrix... Calculated caloric deficit target is 1,950 kcal daily. Macro partition: 144g protein, 210g carbs, 55g fats." }
];

let recognition = null;
let isSpeaking = false;
let autoRestartSpeech = false;
let simTimeoutId = null;

// Initialize Vocal Core elements and click handlers
function initVoiceCore() {
    const micBtn = document.getElementById('btn-vocal-mic-trigger');
    const authModal = document.getElementById('vocal-nexus-modal');
    const authAccept = document.getElementById('btn-modal-init-confirm');
    const authDeny = document.getElementById('btn-modal-init-close');

    if (!micBtn) return;

    // Mic click starts authorization/neural link sync
    micBtn.addEventListener('click', () => {
        if (micBtn.classList.contains('active')) {
            stopVocalSystem();
        } else {
            if (authModal) {
                authModal.classList.add('active');
                if (typeof gsap !== 'undefined') {
                    gsap.fromTo(authModal.querySelector('.nexus-modal-card'),
                        { scale: 0.8, opacity: 0 },
                        { duration: 0.45, scale: 1, opacity: 1, ease: 'back.out(1.4)' }
                    );
                }
            }
        }
    });

    if (authAccept) {
        authAccept.addEventListener('click', () => {
            if (authModal) authModal.classList.remove('active');
            startVocalSystem();
        });
    }

    if (authDeny) {
        authDeny.addEventListener('click', () => {
            if (authModal) authModal.classList.remove('active');
        });
    }

    // Keyboard Override / Manual text override queries
    const vocalTextInput = document.getElementById('vocal-text-input');
    const vocalTextBtn = document.getElementById('btn-vocal-text-send');

    if (vocalTextBtn && vocalTextInput) {
        vocalTextBtn.addEventListener('click', () => {
            processVocalTextQuery();
        });
        vocalTextInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                processVocalTextQuery();
            }
        });
    }

    // Suggestions click binding
    document.querySelectorAll('.vocal-chip').forEach(chip => {
        chip.addEventListener('click', () => {
            const query = chip.getAttribute('data-query');
            if (vocalTextInput) vocalTextInput.value = query;
            processVocalTextQuery(query);
        });
    });
}

// Process Keyboard/Chip Override query in Vocal Tab
async function processVocalTextQuery(overrideQuery) {
    const input = document.getElementById('vocal-text-input');
    const query = (overrideQuery || (input ? input.value : '')).trim();
    if (!query) return;

    if (input) input.value = '';

    // Cancel simulation loop since user interacted manually
    if (simTimeoutId) {
        clearTimeout(simTimeoutId);
        simTimeoutId = null;
    }

    const transcript = document.getElementById('vocal-transcription-output');
    vocalPulsing = true; // Start wave visualizer

    writeVocalLog("USER", `"${query}"`, "#ffffff");
    if (transcript) transcript.innerHTML = `🗣️ User: "${query}"`;

    writeVocalLog("SYS", "Processing query...", "#ffb800");
    const reply = await queryCoach(query);

    writeVocalLog("AI", reply, "#39ff14");
    if (transcript) transcript.innerHTML = `🤖 Coach: "${reply}"`;

    speakOutLoud(reply);
}

// Start Vocal Stream & Web Speech Recognition
function startVocalSystem() {
    const micBtn = document.getElementById('btn-vocal-mic-trigger');
    const transcript = document.getElementById('vocal-transcription-output');

    if (micBtn) micBtn.classList.add('active');
    vocalPulsing = true;
    autoRestartSpeech = true;

    // Reset simulation timer if active
    if (simTimeoutId) {
        clearTimeout(simTimeoutId);
        simTimeoutId = null;
    }

    writeVocalLog("SYSTEM", "Synchronizing neural voice link...", "#00f5ff");
    if (transcript) transcript.innerHTML = "🎙️ Neural link established. Listening for voice command...";

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (SpeechRecognition) {
        if (!recognition) {
            recognition = new SpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = 'en-US';

            recognition.onstart = () => {
                writeVocalLog("MIC", "Stream initialized. Listening...", "#a855f7");
            };

            recognition.onerror = (e) => {
                if (e.error !== 'no-speech') {
                    writeVocalLog("ERR", `Stream error: ${e.error}`, "#ff3366");
                }
                if (e.error === 'not-allowed') {
                    autoRestartSpeech = false;
                    stopVocalSystem();
                    if (transcript) transcript.innerHTML = "❌ Microphone access denied. Check system permissions.";
                }
            };

            recognition.onend = () => {
                if (autoRestartSpeech) {
                    try { recognition.start(); } catch (err) {}
                }
            };

            recognition.onresult = async (event) => {
                const speechResult = event.results[0][0].transcript;
                writeVocalLog("USER", `"${speechResult}"`, "#ffffff");
                if (transcript) transcript.innerHTML = `🗣️ User: "${speechResult}"`;

                writeVocalLog("SYS", "Processing neural query...", "#ffb800");
                const reply = await queryCoach(speechResult);

                writeVocalLog("AI", reply, "#39ff14");
                if (transcript) transcript.innerHTML = `🤖 Coach: "${reply}"`;

                speakOutLoud(reply);
            };
        }

        try {
            recognition.start();
        } catch (e) {
            // Speech recognition already running
        }
    } else {
        writeVocalLog("WARN", "SpeechRecognition API not supported. Starting simulated neural stream.", "#ff7a18");
        simulateVoiceInput();
    }
}

// Stop Vocal Stream & Voice Output
function stopVocalSystem() {
    const micBtn = document.getElementById('btn-vocal-mic-trigger');
    const transcript = document.getElementById('vocal-transcription-output');

    if (micBtn) micBtn.classList.remove('active');
    vocalPulsing = false;
    autoRestartSpeech = false;

    if (simTimeoutId) {
        clearTimeout(simTimeoutId);
        simTimeoutId = null;
    }

    if (recognition) {
        try { recognition.stop(); } catch (e) {}
    }

    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    isSpeaking = false;

    writeVocalLog("SYSTEM", "Neural speech link terminated. Core offline.", "#ff3366");
    if (transcript) transcript.innerHTML = "Neural link established. Awaiting vocal command sequence...";
}

// Speaks responses out loud using TTS
function speakOutLoud(text) {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel(); // Stop any currently playing audio
        
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.pitch = 1.0;
        utterance.rate = 1.05;

        utterance.onstart = () => {
            isSpeaking = true;
            // Stop speech recognition while speaking to prevent echo loopback
            if (recognition && autoRestartSpeech) {
                autoRestartSpeech = false;
                try { recognition.stop(); } catch (e) {}
            }
        };

        utterance.onend = () => {
            isSpeaking = false;
            // Resume speech recognition after voice output finishes, if active
            const micBtn = document.getElementById('btn-vocal-mic-trigger');
            if (micBtn && micBtn.classList.contains('active')) {
                autoRestartSpeech = true;
                if (recognition) {
                    try { recognition.start(); } catch (e) {}
                }
            }
        };

        window.speechSynthesis.speak(utterance);
    }
}

// Writes time-stamped activity reports to terminal logs
function writeVocalLog(prefix, text, color) {
    const logEl = document.getElementById('vocal-logic-log');
    const fluxEl = document.getElementById('vocal-flux-stream');
    const time = new Date().toLocaleTimeString();

    const logMsg = `<div style="margin-bottom:6px;"><span style="color:#64748b;">[${time}]</span> <span style="color:${color};font-weight:700;">${prefix}:</span> ${text}</div>`;

    if (logEl) {
        logEl.innerHTML += logMsg;
        logEl.scrollTop = logEl.scrollHeight;
        if (logEl.children.length > 50) logEl.children[0].remove();
    }

    if (fluxEl && prefix !== 'SYSTEM' && prefix !== 'WARN' && prefix !== 'ERR' && prefix !== 'MIC') {
        const fluxMsg = `<div style="margin-bottom:4px;font-family:monospace;font-size:12px;"><span style="color:var(--cyan);">></span> ${prefix}: ${text.substring(0, 45)}...</div>`;
        fluxEl.innerHTML += fluxMsg;
        fluxEl.scrollTop = fluxEl.scrollHeight;
        if (fluxEl.children.length > 30) fluxEl.children[0].remove();
    }
}

// Fallback voice simulation loops if mic not supported/authorized
function simulateVoiceInput() {
    if (!vocalPulsing || recognition) return;

    const phrase = voicePhrases[Math.floor(Math.random() * voicePhrases.length)];
    const transcript = document.getElementById('vocal-transcription-output');

    writeVocalLog("USER", `"${phrase.u}"`, "#ffffff");
    if (transcript) transcript.innerHTML = `🗣️ User: "${phrase.u}"`;

    if (simTimeoutId) clearTimeout(simTimeoutId);
    simTimeoutId = setTimeout(() => {
        if (!vocalPulsing) return;
        writeVocalLog("AI", phrase.a, "#39ff14");
        if (transcript) transcript.innerHTML = `🤖 Coach: "${phrase.a}"`;
        speakOutLoud(phrase.a);

        simTimeoutId = setTimeout(simulateVoiceInput, 10000);
    }, 3000);
}

// ═══════════════════ PREMIUM INTERACTION EFFECTS ═══════════════════

// Elastic Navigation Highlight Indicator
function updateNavIndicator(targetTab) {
    const indicator = document.querySelector('.nav-indicator');
    const activeItem = document.querySelector(`.nav-item[data-target="${targetTab}"]`);
    if (indicator && activeItem) {
        gsap.to(indicator, {
            y: activeItem.offsetTop,
            height: activeItem.offsetHeight,
            duration: 0.55,
            ease: "elastic.out(1, 0.75)",
            overwrite: 'auto'
        });
    }
}

// 3D Card Hover Perspective Tilt (Framer Motion spring emulation)
function init3DTilt() {
    const cards = document.querySelectorAll('.card, .metric-card, .feat-card, .day-card');
    cards.forEach(card => {
        card.style.transformStyle = 'preserve-3d';
        
        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const w = rect.width;
            const h = rect.height;
            
            // Calculate cursor offset angles (max 12 deg tilt)
            const rx = -((y - h / 2) / h) * 12;
            const ry = ((x - w / 2) / w) * 12;
            
            gsap.to(card, {
                duration: 0.25,
                rotateX: rx,
                rotateY: ry,
                transformPerspective: 800,
                ease: 'power2.out',
                overwrite: 'auto'
            });
        });
        
        card.addEventListener('mouseleave', () => {
            gsap.to(card, {
                duration: 0.65,
                rotateX: 0,
                rotateY: 0,
                transformPerspective: 800,
                ease: 'elastic.out(1.1, 0.75)',
                overwrite: 'auto'
            });
        });
    });
}

// Cursor Tracking Ambient Glow
function initMouseGlow() {
    let glow = document.getElementById('mouse-glow');
    if (!glow) {
        glow = document.createElement('div');
        glow.id = 'mouse-glow';
        document.body.appendChild(glow);
    }
    
    window.addEventListener('mousemove', e => {
        glow.style.opacity = '1';
        gsap.to(glow, {
            x: e.clientX,
            y: e.clientY,
            duration: 0.45,
            ease: 'power2.out',
            overwrite: 'auto'
        });
    });
    
    document.addEventListener('mouseleave', () => {
        glow.style.opacity = '0';
    });
}

// Micro-interactions: Button Spring Click Feedback
function initButtonBounce() {
    const btns = document.querySelectorAll('.btn-glow, .btn-outline, .btn-sm, .suggestion-chip, .quick-suggestion');
    btns.forEach(btn => {
        btn.addEventListener('mouseenter', () => {
            gsap.to(btn, { scale: 1.04, duration: 0.2, ease: 'power1.out', overwrite: 'auto' });
        });
        btn.addEventListener('mouseleave', () => {
            gsap.to(btn, { scale: 1.0, duration: 0.25, ease: 'power1.out', overwrite: 'auto' });
        });
        btn.addEventListener('mousedown', () => {
            gsap.to(btn, { scale: 0.94, duration: 0.08, ease: 'power1.out', overwrite: 'auto' });
        });
        btn.addEventListener('mouseup', () => {
            gsap.to(btn, { scale: 1.04, duration: 0.12, ease: 'power1.out', overwrite: 'auto' });
        });
    });
}


