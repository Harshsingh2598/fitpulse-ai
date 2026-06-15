# ⚡ FitPulse AI — Premium Gym Trainer & Fitness Assistant

An ultra-premium, offline-compatible fitness assistant built with modern design aesthetics, real-time calculations, and a fully interactive voice coach (Vocal Nexus AI).

---

## 🚀 Key Features

1. **🤖 Neural RAG Chat Console**: Direct access to fitness intelligence and RAG search correlation lists.
2. **🎙️ Vocal Nexus AI Assistant**: 
   - Real-time biometric voice synchronization coach.
   - **Keyboard & Chip Override**: Manual inputs and suggestion chips if microphone access is denied or unavailable.
   - **Echo/Loopback Prevention**: Automatically pauses speech recognition while the synthetic coach voice is speaking to prevent audio feedback.
3. **🏋️ Synth Lab (Workout Generator)**: Compile structured routines scaled to user level and goal.
4. **🥗 Diet Matrix (Diet Planner)**: Dynamically calculates macros (protein, carbs, fats) based on your weight and outputs daily meal schedules.
5. **🔥 Predictor Engine (Calorie Burn)**: Real-time slider calculations estimating caloric expenditure by intensity level.
6. **📊 Entropy Map & Diagnostics**: Beautiful telemetry metrics, node topologies, and custom canvas-based visualizations.
7. **📄 Singularity Report**: Exportable and printable weekly fitness performance summaries.

---

## 🛠️ Technology Stack
- **Frontend**: Vanilla HTML5, Custom CSS3, Javascript, GSAP (GreenSock Animation Platform) for spring physics transitions, and Chart.js.
- **Backend**: Python 3, Flask.
- **Deployment**: Configured for Vercel Serverless Functions (`@vercel/python`).

---

## 💻 Running Locally

Simply run one of the included batch startup files in the project root:
- Double-click **`RUN_APP_FIXED.bat`** (Automatically installs dependencies and launches the app on `http://127.0.0.1:8510`).

Or start the server manually in your terminal:
```bash
pip install -r requirements.txt
python api/index.py
```

---

## ☁️ Vercel Serverless Deployment

This repository is pre-configured for **Vercel zero-config deployments**:
- **`vercel.json`**: Rewrites all browser requests directly to the serverless function.
- **`api/index.py`**: The serverless entry point that exports the Flask application handle.
- **`.gitignore`**: Excludes unnecessary caches, environments, and local telemetry files.

### Deploying in 2 Steps:
1. **Push to GitHub**:
   ```bash
   git add README.md
   git commit -m "docs: add premium README.md"
   git push origin main
   ```
2. **Import to Vercel**: Connect your GitHub repository to Vercel and it will deploy automatically.
