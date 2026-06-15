import os
import random
import math
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='static', static_url_path='')

# ════════════════════════════════════════════════════════════════
# OFFLINE AI COACH ENGINE
# ════════════════════════════════════════════════════════════════
def get_ai_reply(question):
    q = (question or "").lower().strip()
    if not q:
        return "💬 Ask me anything about workouts, diet, calories, fat loss, muscle gain, recovery, or any specific body part training!"

    if any(x in q for x in ["hello", "hi", "hey", "sup", "what's up"]):
        return "Hey there! 💪🔥 I'm your FitPulse AI Coach — fully working offline! Ask me about chest, back, legs, shoulders, arms, diet, fat loss, calorie burn, or recovery. Let's crush it! 🚀"

    # Chest
    if any(x in q for x in ["chest", "push", "bench", "pec"]):
        return """🏋️ **ULTIMATE CHEST WORKOUT**

💥 **Compound Movements:**
• Barbell Bench Press — 4×8-10 (heavy)
• Incline Dumbbell Press — 4×10-12
• Decline Bench Press — 3×10

💥 **Isolation & Finishers:**
• Cable Crossover Fly — 3×15
• Dumbbell Fly (flat) — 3×12
• Push-ups (to failure) — 3 sets
• Dips (chest-focused) — 3×12

⚡ **Pro Tips:** Control the negative (3 sec), squeeze at top, full range of motion. Rest 90-120 sec between heavy sets, 60 sec for isolation."""

    # Back
    if any(x in q for x in ["back", "pull", "lat", "row", "deadlift"]):
        return """💪 **COMPLETE BACK WORKOUT**

🔥 **Width Builders:**
• Pull-ups (weighted if possible) — 4 sets
• Wide-grip Lat Pulldown — 4×12
• Straight Arm Pulldown — 3×15

🔥 **Thickness Builders:**
• Barbell Bent-over Row — 4×8-10
• Seated Cable Row — 4×12
• T-Bar Row — 3×10
• Single Arm Dumbbell Row — 3×12 each

⚡ **Pro Tips:** Retract shoulder blades, drive elbows back, squeeze lats for 1 sec at contraction. Mind-muscle connection is everything!"""

    # Legs
    if any(x in q for x in ["leg", "legs", "squat", "quad", "hamstring", "glute"]):
        return """🦵 **BEAST MODE LEG DAY**

🔥 **Quad Dominant:**
• Barbell Back Squat — 4×6-8 (heavy!)
• Front Squat — 3×10
• Leg Press — 4×12
• Leg Extension — 3×15 (drop set last)

🔥 **Hamstring & Glutes:**
• Romanian Deadlift — 4×10
• Lying Leg Curl — 3×12
• Bulgarian Split Squat — 3×10 each
• Hip Thrust — 4×12

🔥 **Calves:**
• Standing Calf Raise — 4×20
• Seated Calf Raise — 3×15

⚡ **Pro Tips:** Go deep on squats (below parallel), squeeze glutes at top of hip thrusts, slow negative on RDLs!"""

    # Shoulders
    if any(x in q for x in ["shoulder", "delts", "delt", "ohp", "overhead"]):
        return """🔱 **3D SHOULDER WORKOUT**

💥 **Heavy Press:**
• Overhead Barbell Press — 4×8-10
• Seated Dumbbell Press — 4×10
• Arnold Press — 3×12

💥 **Lateral Development:**
• Lateral Raise (cable or dumbbell) — 4×15
• Behind-the-back Cable Lateral — 3×15

💥 **Rear Delts:**
• Face Pulls — 4×15
• Reverse Pec Deck — 3×15
• Bent-over Rear Delt Fly — 3×12

💥 **Traps:**
• Barbell Shrugs — 4×15

⚡ **Pro Tips:** Use lighter weight on laterals with strict form. Rear delts need MORE volume than you think!"""

    # Arms
    if any(x in q for x in ["arm", "bicep", "tricep", "curl", "arms"]):
        return """💪 **ULTIMATE ARMS WORKOUT**

🔥 **Biceps:**
• Barbell Curl — 4×10
• Incline Dumbbell Curl — 3×12
• Hammer Curl — 3×12
• Preacher Curl — 3×15 (squeeze!)
• Cable Curl (21s) — 2 sets

🔥 **Triceps:**
• Close-grip Bench Press — 4×10
• Skull Crushers — 3×12
• Overhead Cable Extension — 3×15
• Rope Pushdown — 3×15
• Diamond Push-ups — 2 sets to failure

⚡ **Pro Tips:** Superset biceps + triceps for insane pump. Control the weight, don't swing. Full stretch at bottom, full squeeze at top!"""

    # Core / Abs
    if any(x in q for x in ["abs", "core", "six pack", "plank", "crunch"]):
        return """🔥 **SHREDDED CORE WORKOUT**

💥 **Upper Abs:** Crunches 3×20, Cable Crunch 3×15
💥 **Lower Abs:** Hanging Leg Raise 4×12, Reverse Crunch 3×15, Flutter Kicks 3×30s
💥 **Obliques:** Russian Twist 3×20, Side Plank 3×30s each, Woodchops 3×12
💥 **Stability:** Plank 3×60s, Ab Wheel Rollout 3×10, Dead Bug 3×12 each

⚡ **Truth:** Abs are made in the kitchen! You need <15% body fat (men) to see them. Train abs 3-4x/week, but DIET is 80% of the equation."""

    # Diet
    if any(x in q for x in ["diet", "meal", "food", "eat", "nutrition", "protein", "gain", "bulk"]):
        return """🥗 **AI-OPTIMIZED DIET PLAN**

🌅 **Breakfast (7-8 AM) — 500 kcal:**
• Oats + banana + peanut butter + whey protein shake
• OR 4 egg whites + 2 whole eggs + toast + avocado

☀️ **Lunch (12-1 PM) — 650 kcal:**
• Brown rice/quinoa + grilled chicken/paneer (200g)
• Mixed salad + olive oil dressing
• 1 fruit (apple/orange)

⚡ **Pre-Workout (4 PM) — 300 kcal:**
• Banana + black coffee + handful of almonds

🏋️ **Post-Workout (6 PM) — 400 kcal:**
• Whey protein shake + fast carbs (banana/rice cakes)

🌙 **Dinner (8 PM) — 550 kcal:**
• Roti/sweet potato + tofu/fish/eggs + steamed veggies
• Greek yogurt before bed

📊 **Daily Targets:** 2400 kcal | 160g protein | 250g carbs | 70g fats
💡 **Adjust:** +300 kcal for bulking, -400 kcal for cutting"""

    # Fat loss
    if any(x in q for x in ["fat", "loss", "cut", "weight loss", "reduce", "lean", "shred"]):
        return """🔥 **SCIENCE-BASED FAT LOSS PLAN**

📉 **Calorie Deficit:**
• Calculate TDEE → eat 300-500 kcal below
• Track with MyFitnessPal for accuracy

🥗 **Nutrition Rules:**
• Protein HIGH: 2.0-2.4g per kg bodyweight
• Cut sugary drinks, fried foods, processed snacks
• Eat more fiber (veggies, fruits, oats)
• Drink 3-4L water daily

🏋️ **Training:**
• Strength train 4-5x/week (preserve muscle!)
• HIIT cardio 2-3x/week (20 min sessions)
• Walk 8,000-10,000 steps daily (NEAT is huge!)

😴 **Recovery:**
• Sleep 7-8 hours (cortisol = belly fat!)
• Manage stress (meditation, walking)

🎯 **Realistic Goal:** 0.5-1% bodyweight loss per week
⚠️ **Don't:** Crash diet, do excessive cardio, skip meals"""

    # Calories
    if any(x in q for x in ["calorie", "burn", "kcal", "how many", "calories burned"]):
        return """⚡ **CALORIE BURN GUIDE**

🏋️ **Weight Training (1 hour):**
• Light: 200-350 kcal
• Moderate: 350-500 kcal
• Intense: 500-700 kcal

🏃 **Cardio (30 minutes):**
• Walking: 120-180 kcal
• Jogging: 250-350 kcal
• Running (fast): 350-500 kcal
• HIIT: 300-450 kcal
• Cycling: 250-400 kcal
• Jump Rope: 300-450 kcal

🔥 **EPOC (Afterburn):** Intense workouts burn extra 50-200 kcal for 24-48 hours after!"""

    # Recovery
    if any(x in q for x in ["recovery", "sleep", "rest", "sore", "overtraining", "injury"]):
        return """🛌 **OPTIMAL RECOVERY PROTOCOL**

😴 **Sleep:** 7-9 hours (growth hormone peaks during deep sleep!)
💧 **Hydration:** 3-4 liters water daily
🥩 **Nutrition:** 30g protein within 1 hour post-workout
🧘 **Active Recovery:** Light stretching, yoga, foam rolling 10 min daily

📋 **Weekly Structure:**
• Train: 4-5 days
• Active recovery: 1-2 days (walking, stretching)
• Full rest: 1 day

⚠️ **Signs of Overtraining:** Constant fatigue, strength loss, insomnia, frequent illness, elevated resting heart rate"""

    # Beginner
    if any(x in q for x in ["beginner", "start", "new", "first time", "newbie"]):
        return """✅ **COMPLETE BEGINNER'S GUIDE**

📅 **Week 1-4 Plan (3 days/week):**

**Day A — Push:**
• Push-ups 3×10-15 | Dumbbell Shoulder Press 3×12
• Dumbbell Bench Press 3×12 | Tricep Dips 3×10

**Day B — Pull:**
• Assisted Pull-ups 3×8 | Dumbbell Row 3×12 each
• Lat Pulldown 3×12 | Bicep Curl 3×12

**Day C — Legs:**
• Bodyweight Squat 3×15 | Lunges 3×10 each
• Leg Press 3×12 | Plank 3×30s

🎯 **Rules:** Start light, learn proper form first, increase weight by 2.5kg every 1-2 weeks, eat enough protein, sleep 8 hours!"""

    # Supplement
    if any(x in q for x in ["supplement", "whey", "creatine", "bcaa", "pre workout", "pre-workout"]):
        return """💊 **EVIDENCE-BASED SUPPLEMENTS**

✅ **Tier 1 (Proven):**
• Whey Protein — 25-30g post-workout
• Creatine Monohydrate — 5g daily (most researched!)
• Caffeine — 150-300mg pre-workout

✅ **Tier 2 (Helpful):**
• Omega-3 Fish Oil — 2-3g daily
• Vitamin D3 — 2000-4000 IU daily
• Magnesium — 200-400mg before bed
• Multivitamin — as insurance

❌ **Skip:** BCAAs (waste if eating enough protein), fat burners, testosterone boosters"""

    # Motivation
    if any(x in q for x in ["motivat", "lazy", "skip", "don't feel", "can't", "hard", "give up", "quit"]):
        return """🔥 **MOTIVATION BOOST!**

💪 "The only bad workout is the one that didn't happen."
💪 "Your body can stand almost anything. It's your mind you have to convince."
💪 "Don't wish for it. Work for it."

🎯 **Action Plan:**
1. Just show up — even 20 minutes counts
2. Track progress — small wins compound
3. Remember WHY you started

⚡ You've got this! Every rep, every set, every day — you're building a better version of yourself! 🚀"""

    return f"""🤖 **FitPulse AI Response**

Great question! Here's my general advice based on your query: *"{question}"*

📋 **Key Principles:**
1. **Progressive Overload** — increase weight/reps/sets every week
2. **Protein Intake** — 1.6-2.2g per kg bodyweight daily
3. **Sleep** — 7-8 hours for optimal recovery & growth
4. **Consistency** — 4-5 training days/week minimum

I'm here to help you reach your fitness goals! 💪🔥"""

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
    print("FitPulse AI Premium Web Server launching on http://127.0.0.1:5000 ...")
    app.run(host='127.0.0.1', port=5000, debug=True)
