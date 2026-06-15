import os
import re

def matches_keywords(query, keywords):
    for kw in keywords:
        if kw == "motivat":
            pattern = r'\bmotivat'
        else:
            pattern = r'\b' + re.escape(kw) + r'\b'
        if re.search(pattern, query):
            return True
    return False

import random
import math
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='../static', static_url_path='')

# ════════════════════════════════════════════════════════════════
# OFFLINE AI COACH ENGINE
# ════════════════════════════════════════════════════════════════
def get_ai_reply(question):
    q = (question or "").lower().strip()
    if not q:
        return "💬 Ask me anything about workouts, diet, calories, fat loss, muscle gain, recovery, or any specific body part training!"

    if matches_keywords(q, ["hello", "hi", "hey", "sup", "what's up"]):
        return "Hey there! 💪🔥 I'm your FitPulse AI Coach — fully working offline! Ask me about chest, back, legs, shoulders, arms, diet, fat loss, calorie burn, or recovery. Let's crush it! 🚀"

    # Food items - Bananas, Oats, Carbs
    if matches_keywords(q, ["banana", "bananas", "oats", "oatmeal", "carb", "carbs"]):
        return """🍌 **CARBOHYDRATE GUIDE & FUEL**

⚡ **Pre-Workout Fuel (Bananas):**
• Bananas are rich in fast-digesting carbohydrates (fructose) and potassium.
• Eat 1-2 bananas 30-45 minutes before training to fuel workouts and prevent muscle cramps.

🌾 **Sustained Energy (Oats / Oatmeal):**
• Oats contain complex carbs and beta-glucan fiber, giving a slow, steady release of energy.
• Best consumed for breakfast or 2 hours before a heavy workout.

📊 **Target:** Aim for 3-5g of clean carbs per kg of bodyweight depending on your goal (bulking vs cutting)."""

    # Supplements
    if matches_keywords(q, ["creatine", "whey", "supplement", "supplements"]):
        return """💊 **EVIDENCE-BASED SUPPLEMENTS**

✅ **Tier 1 (Proven & Effective):**
• **Creatine Monohydrate** — 5g daily. Boosts ATP production, increases strength, and hydrates muscle cells. No loading phase needed!
• **Whey Protein** — 25-30g post-workout. Convenient, high-quality protein to hit daily targets.
• **Caffeine** — 150-300mg pre-workout. Enhances focus, power output, and pain tolerance.

✅ **Tier 2 (Health & Recovery Support):**
• Omega-3 Fish Oil (1-2g daily for joints & heart)
• Vitamin D3 (2000-4000 IU for hormone support)
• Magnesium (200-400mg before bed for muscle relaxation)

❌ **Skip:** BCAAs (useless if eating enough protein), mass gainers (just cheap sugar), and testosterone boosters."""

    # Food items - Protein, Chicken, Paneer, Egg
    if matches_keywords(q, ["chicken", "paneer", "egg", "eggs", "tofu", "fish", "meat", "protein", "shake"]):
        return """🍳 **PROTEIN SOURCES & GUIDELINES**

🍗 **Animal-Based Proteins:**
• Chicken Breast: ~31g protein per 100g (leanest source)
• Egg Whites: ~4g protein per egg white (zero fat)
• Fish (Salmon/Tuna): ~20-25g protein per 100g (healthy omega-3s)

🧀 **Vegetarian Proteins:**
• Paneer: ~18g protein per 100g (high casein, great before bed)
• Tofu / Tempeh: ~8-15g protein per 100g (complete plant protein)
• Lentils / Beans: Great fiber + moderate protein source

🥤 **Post-Workout (Whey):**
• Whey Protein Shake: 24-30g fast-digesting protein to kickstart muscle recovery.

📊 **Target:** Consume 1.6 - 2.2g of protein per kg of bodyweight daily to build and maintain muscle."""

    # Chest
    if matches_keywords(q, ["chest", "push", "bench", "pec"]):
        return """🏋️ **ULTIMATE CHEST WORKOUT (Hypertrophy Focus)**

💥 **Compound Movements:**
• Barbell Bench Press — 4 sets × 8-10 reps (heavy load)
• Incline Dumbbell Press — 4 sets × 10-12 reps (upper chest focus)
• Decline Hammer Press — 3 sets × 10 reps (lower chest focus)

💥 **Isolation & Finishers:**
• Cable Crossover Fly — 3 sets × 15 reps (constant tension)
• Dumbbell Flat Fly — 3 sets × 12 reps
• Bodyweight Dips (chest-focused) — 3 sets × 12 reps (lean forward)
• Push-ups (to failure) — 3 sets as a finisher

⚡ **Pro Tips:** Retract your shoulder blades, control the negative phase (3 seconds down), and squeeze your chest at the top of each rep."""

    # Back
    if matches_keywords(q, ["back", "pull", "lat", "row", "deadlift"]):
        return """💪 **COMPLETE BACK WORKOUT (Width & Thickness)**

🔥 **Width Builders:**
• Pull-ups (weighted if possible) — 4 sets × Max reps
• Wide-grip Lat Pulldown — 4 sets × 12 reps
• Straight Arm Lat Pulldowns — 3 sets × 15 reps (constant tension)

🔥 **Thickness Builders:**
• Barbell Bent-over Row — 4 sets × 8-10 reps (heavy)
• Seated Cable Row — 4 sets × 12 reps
• T-Bar Row — 3 sets × 10 reps
• Single Arm Dumbbell Row — 3 sets × 12 reps each arm

🔥 **Lower Back & Posture:**
• Conventional Deadlifts — 3 sets × 5 reps (pure strength)

⚡ **Pro Tips:** Pull with your elbows, retract your scapula before rowing, and feel the stretch at the top of pulldowns."""

    # Legs
    if matches_keywords(q, ["leg", "legs", "squat", "quad", "hamstring", "glute", "calf", "calves"]):
        return """🦵 **BEAST MODE LEG DAY**

🔥 **Quad Dominant:**
• Barbell Back Squat — 4 sets × 6-8 reps (heavy!)
• Leg Press — 4 sets × 12 reps (feet low & close for quads)
• Leg Extensions — 3 sets × 15 reps (squeeze for 1 sec at top)

🔥 **Hamstrings & Glutes:**
• Romanian Deadlift (RDL) — 4 sets × 10 reps (focus on hip hinge)
• Lying Leg Curl — 3 sets × 12 reps
• Bulgarian Split Squat — 3 sets × 10 reps each leg (quad/glute burner)
• Hip Thrusts — 4 sets × 12 reps (glute pump)

🔥 **Calves:**
• Standing Calf Raise — 4 sets × 20 reps
• Seated Calf Raise — 3 sets × 15 reps

⚡ **Pro Tips:** Sit deep (hips below parallel on squats), control the stretch on RDLs, and stretch calves at the bottom of raises."""

    # Shoulders
    if matches_keywords(q, ["shoulder", "shoulders", "delts", "delt", "ohp", "overhead"]):
        return """🔱 **3D SHOULDER WORKOUT**

💥 **Heavy Press:**
• Overhead Barbell Press (OHP) — 4 sets × 8 reps
• Seated Dumbbell Press — 4 sets × 10 reps
• Arnold Press — 3 sets × 12 reps

💥 **Lateral Delts (Width):**
• Dumbbell Lateral Raise — 4 sets × 15 reps (keep shoulders down)
• Behind-the-back Cable Lateral — 3 sets × 15 reps

💥 **Rear Delts (3D look):**
• Face Pulls (cable) — 4 sets × 15 reps (pull to forehead)
• Reverse Pec Deck — 3 sets × 15 reps

💥 **Traps:**
• Barbell Shrugs — 4 sets × 15 reps

⚡ **Pro Tips:** Keep lateral raises strict (don't swing). Rear delts respond extremely well to high volume and control."""

    # Arms
    if matches_keywords(q, ["arm", "arms", "bicep", "biceps", "tricep", "triceps", "curl"]):
        return """💪 **ULTIMATE ARMS WORKOUT (Superset Burner)**

🔥 **Superset 1 (Biceps + Triceps):**
• 1A. Barbell Bicep Curl — 4 sets × 10 reps
• 1B. Close-grip Bench Press — 4 sets × 10 reps

🔥 **Superset 2 (Width + Thickness):**
• 2A. Dumbbell Hammer Curl — 3 sets × 12 reps
• 2B. Overhead Dumbbell Extension — 3 sets × 12 reps

🔥 **Superset 3 (Detail & Pump):**
• 3A. Preacher Curl — 3 sets × 15 reps
• 3B. Cable Rope Pushdowns — 3 sets × 15 reps

⚡ **Pro Tips:** Do not swing your body on curls. Squeeze your triceps at the bottom of pushdowns and stretch fully at the top of overhead extensions."""

    # Core / Abs
    if matches_keywords(q, ["abs", "core", "six pack", "plank", "crunch"]):
        return """🔥 **SHREDDED CORE WORKOUT**

💥 **Upper Abs:** Crunches 3×20 | Cable Crunch 3×15 (high load)
💥 **Lower Abs:** Hanging Leg Raise 4×12 | Reverse Crunch 3×15
💥 **Obliques:** Russian Twist 3×20 | Woodchops 3×12 each side
💥 **Stability:** Plank 3×60s | Ab Wheel Rollout 3×10

⚡ **The Abs Truth:** Abs are revealed, not built! You must be at a low body fat percentage (<15% for men, <22% for women) to see them. Focus on a calorie deficit and high-intensity training."""

    # Cardio / HIIT
    if matches_keywords(q, ["cardio", "hiit", "running", "run", "cycling", "treadmill"]):
        return """🏃 **CARDIO & HIIT PROTOCOLS**

🌟 **HIIT (High-Intensity Interval Training) — 20 mins:**
• 30 seconds max sprint followed by 60 seconds walking recovery.
• Repeat 12-15 rounds. Incredible for fat oxidation and boosting metabolic rate (EPOC).

🚴 **LISS (Low-Intensity Steady State) — 45 mins:**
• Fast walking, steady cycling, or swimming at a conversational pace.
• Ideal for active recovery and burning fat without taxing the central nervous system.

🎯 **Rule:** Limit cardio to 3-4 sessions a week to protect muscle mass, and perform it *after* lifting weights."""

    # Diet general
    if matches_keywords(q, ["diet", "meal", "food", "eat", "nutrition"]):
        return """🥗 **DAILY METABOLIC MEAL RECOMMENDATIONS**

🌅 **Breakfast (7-8 AM) — 500 kcal:**
• Oats (75g) + banana + peanut butter + whey protein shake
• OR 4 egg whites + 2 whole eggs + whole wheat toast + avocado

☀️ **Lunch (12-1 PM) — 650 kcal:**
• Brown rice or quinoa + grilled chicken breast / paneer / tofu (200g)
• Large bowl of mixed green salad + 1 tsp olive oil

⚡ **Pre-Workout Fuel (4 PM) — 300 kcal:**
• Banana + black coffee + handful of almonds

🏋️ **Post-Workout Recovery (6 PM) — 400 kcal:**
• Whey protein shake + fast carbohydrates (banana or cream of rice)

🌙 **Dinner (8 PM) — 550 kcal:**
• Sweet potato or roti + grilled fish or tofu + steamed broccoli/spinach

📊 **Targets:** 2400 kcal | 160g protein | 250g carbs | 70g fats. Scale meals according to your bodyweight and goals."""

    # Fat loss
    if matches_keywords(q, ["fat", "loss", "cut", "weight loss", "reduce", "lean", "shred"]):
        return """🔥 **SCIENCE-BASED FAT LOSS PLAN**

📉 **1. Calorie Deficit:**
• Calculate your TDEE and consume 300-500 kcal below maintenance.
• Track calories accurately using MyFitnessPal.

🥗 **2. Nutrition Guidelines:**
• Keep protein HIGH: 2.0 - 2.4g per kg of bodyweight to preserve muscle.
• Drink 3-4 liters of water daily to maintain metabolic efficiency.
• Eliminate processed foods, sugary drinks, and late-night snacks.

🏋️ **3. Exercise Protocol:**
• Lift weights 4-5 times a week to keep your metabolism elevated.
• Walk 8k-10k steps daily (NEAT is the key to consistent fat loss!).
• Sleep 7-8 hours (high cortisol from sleep deprivation triggers belly fat storage)."""

    # Muscle gain
    if matches_keywords(q, ["muscle", "gain", "bulk", "bulking", "hypertrophy"]):
        return """💪 **HYPERTROPHY & MUSCLE GAIN BLUEPRINT**

📈 **1. Caloric Surplus:**
• Consume 300-500 kcal above maintenance (lean bulking).
• Focus on slow weight gain (0.5kg - 1kg per month) to minimize fat storage.

🏋️ **2. Progressive Overload:**
• You must increase the weight, reps, or sets on your exercises every single week.
• Focus on compound lifts in the 8-12 rep range.

🥗 **3. Macronutrient Targets:**
• Protein: 1.8 - 2.2g per kg of bodyweight.
• Carbs: High carbs to fuel workouts and restore glycogen.
• Fats: Healthy fats (avocados, nuts) for hormone health.

🛌 **4. Rest:**
• Muscle grows in bed, not in the gym! Take 1-2 full rest days per week."""

    # Calories
    if matches_keywords(q, ["calorie", "burn", "kcal", "how many", "calories burned"]):
        return """⚡ **CALORIE EXPENDITURE GUIDE**

🏋️ **Weight Training (1 hour):**
• Moderate: 350-500 kcal | Intense: 500-700 kcal

🏃 **Cardio & Sports (30 minutes):**
• Fast Walking: 150 kcal | Jogging: 300 kcal | Running: 400 kcal
• HIIT: 350 kcal | Cycling: 300 kcal | Jump Rope: 400 kcal

🔥 **EPOC Effect:** High intensity weight lifting and HIIT create an 'afterburn' effect, causing you to burn extra calories for up to 48 hours post-workout!"""

    # Recovery
    if matches_keywords(q, ["recovery", "sleep", "rest", "sore", "overtraining", "injury", "stretching"]):
        return """🛌 **OPTIMAL RECOVERY PROTOCOL**

😴 **Sleep:** 7-9 hours of quality sleep. This is when growth hormone peaks and muscle fibers repair.
💧 **Hydration:** 3-4 liters of water daily. Dehydrated muscles are weaker and more prone to injury.
🥩 **Nutrition:** Satiate your muscles with 30g of protein and fast carbs within 1 hour post-workout.
🧘 **Active Recovery:** 10 mins of light stretching, mobility drills, or foam rolling daily.
⚠️ **Signs of Overtraining:** Persistent muscle soreness, drop in strength, chronic fatigue, insomnia, or elevated resting heart rate."""

    # Beginner
    if matches_keywords(q, ["beginner", "start", "new", "first time", "newbie"]):
        return """✅ **COMPLETE BEGINNER'S BLUEPRINT**

📅 **Weeks 1-4 Workout Schedule (3 Days/Week):**

🌟 **Day A (Push Focus):**
• Push-ups (or DB Bench Press): 3 sets × 10-12 reps
• Seated DB Shoulder Press: 3 sets × 12 reps
• Bodyweight Dips / Bench Dips: 3 sets × 10 reps

🌟 **Day B (Pull Focus):**
• Lat Pulldown / Assisted Pull-ups: 3 sets × 12 reps
• Single Arm DB Row: 3 sets × 12 reps each arm
• Standing DB Bicep Curls: 3 sets × 12 reps

🌟 **Day C (Legs & Core Focus):**
• Goblet Squats: 3 sets × 15 reps
• Romanian Deadlifts: 3 sets × 12 reps
• Plank: 3 sets × 30-45 seconds

🎯 **Rule:** Learn proper form first. Increase weights slowly by 2.5kg. Focus on consistency!"""

    # General Workout query
    if matches_keywords(q, ["workout", "workouts", "exercise", "exercises", "training", "routine", "gym", "routine", "schedule"]):
        return """🏋️ **FITPULSE ROUTINE SELECTOR**

To get a detailed exercise layout, ask me specifically about:
• 🏋️ **Chest Workout** (bench press, incline DB, cable flies)
• 🧹 **Back Workout** (pullups, deadlifts, bent-over rows)
• 🦵 **Leg Workout** (squats, leg press, Romanian deadlifts)
• 🔱 **Shoulder Workout** (military press, lateral raises)
• 💪 **Arm Workout** (biceps curls, skull crushers, hammer curls)
• 🔥 **Core Workout** (hanging leg raises, planks, crunches)
• 🏃 **Cardio / HIIT** (sprints, interval cycling, steady-state)

💡 *Tip:* Navigate to the **Synth Lab** module in the sidebar to generate a complete, custom weekly workout schedule!"""

    # Motivation
    if matches_keywords(q, ["motivat", "lazy", "skip", "don't feel", "can't", "hard", "give up", "quit"]):
        return """🔥 **MOTIVATION RADAR BOOST!**

💪 *"The only bad workout is the one that didn't happen."*
💪 *"Success isn't always about greatness. It's about consistency."*
💪 *"You don't have to feel like it. You just have to do it."*

🎯 **Action Plan:**
1. Put your gym clothes on — that is 50% of the friction.
2. Commit to just 15 minutes of moving. If you still hate it, you can leave. (Spoiler: You won't leave!).
3. Remember why you started. Every rep is a deposit into your future self. Let's get to work! 🚀"""

    return f"""🤖 **FitPulse AI Response**

Great query! Here's my general fitness advice based on your question: *"{question}"*

📋 **Key Principles:**
1. **Progressive Overload** — increase weight/reps/sets every week to keep muscles growing.
2. **Protein Intake** — consume 1.6-2.2g per kg bodyweight daily.
3. **Sleep & Rest** — sleep 7-8 hours nightly for full recovery.
4. **Consistency** — train 3-5 days/week and track your caloric targets.

Ask me a specific question like 'chest workout' or 'diet plan' to get an immediate detailed blueprint! 💪🔥"""

# ════════════════════════════════════════════════════════════════
# FLASK ROUTES
# ════════════════════════════════════════════════════════════════

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.json or {}
    question = data.get('question', '')
    reply = get_ai_reply(question)
    return jsonify({
        "question": question,
        "reply": reply
    })

@app.route('/api/predict_calories', methods=['POST'])
def api_predict_calories():
    data = request.json or {}
    try:
        weight = float(data.get('weight', 72))
        duration = float(data.get('duration', 45))
        intensity = data.get('intensity', 'Medium')
    except (ValueError, TypeError):
        weight, duration, intensity = 72, 45, 'Medium'

    type_mult = {
        "Weight Training": 7.0, "HIIT": 12.0, "Running": 10.0, "Cycling": 8.0,
        "Swimming": 9.0, "Jump Rope": 11.0, "Walking": 4.0, "Yoga": 3.5,
        "CrossFit": 13.0, "Martial Arts": 11.0
    }
    
    # Map high/medium/low levels
    int_mult = {"Low": 0.7, "Medium": 1.0, "High": 1.3, "Extreme": 1.6}
    
    base = type_mult.get("Weight Training", 7.0) # default base
    intensity_f = int_mult.get(intensity, 1.0)
    
    calories_burned = int(duration * base * intensity_f * (weight / 70.0))
    
    return jsonify({
        "calories": calories_burned
    })

if __name__ == '__main__':
    print("FitPulse AI Premium Web Server launching on http://127.0.0.1:8510 ...")
    app.run(host='127.0.0.1', port=8510, debug=True)
