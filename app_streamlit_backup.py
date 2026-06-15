import streamlit as st
import pandas as pd
import time
import random
import math
from datetime import datetime, timedelta

st.set_page_config(
    page_title="FitPulse AI — Ultimate Animated Fitness Platform",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ════════════════════════════════════════════════════════════════
# DYNAMIC THEME SYSTEM
# ════════════════════════════════════════════════════════════════
if 'water_ml' not in st.session_state:
    st.session_state.water_ml = 0

theme_colors = {
    "Cyberpunk (Pink/Cyan)": {
        "cyan": "#00F5FF", "pink": "#FF2BD6", "green": "#39FF14", "orange": "#FFB800",
        "purple": "#A855F7", "blue": "#3B82F6", "red": "#FF3366", "yellow": "#FAFF00", "lime": "#BFFF00",
        "gradient": "linear-gradient(90deg, #FAFF00, #39FF14, #00F5FF, #A855F7, #FF2BD6, #FF3366, #FFB800, #FAFF00)"
    },
    "Emerald Pulse (Green/Blue)": {
        "cyan": "#39FF14", "pink": "#00F5FF", "green": "#00FF77", "orange": "#BFFF00",
        "purple": "#0070FF", "blue": "#00D2FF", "red": "#00FFD2", "yellow": "#FFD700", "lime": "#ADFF2F",
        "gradient": "linear-gradient(90deg, #00FF77, #39FF14, #00F5FF, #0070FF, #00D2FF, #00FFD2, #BFFF00, #00FF77)"
    },
    "Solar Flare (Orange/Red)": {
        "cyan": "#FFB800", "pink": "#FF3366", "green": "#FF8800", "orange": "#FFAA00",
        "purple": "#E60067", "blue": "#FF5500", "red": "#FF0033", "yellow": "#FFFF00", "lime": "#E0E000",
        "gradient": "linear-gradient(90deg, #FFAA00, #FFB800, #FF8800, #FF5500, #FF3366, #E60067, #FF0033, #FFAA00)"
    },
    "Electric Ice (Cyan/Blue)": {
        "cyan": "#00F5FF", "pink": "#3B82F6", "green": "#00A8FF", "orange": "#0070FF",
        "purple": "#002BFF", "blue": "#00E1FF", "red": "#0059FF", "yellow": "#E0FFFF", "lime": "#7DF9FF",
        "gradient": "linear-gradient(90deg, #00E1FF, #00F5FF, #00A8FF, #0070FF, #3B82F6, #002BFF, #0059FF, #00E1FF)"
    },
    "Acid Lime (Lime/Yellow)": {
        "cyan": "#BFFF00", "pink": "#FFB800", "green": "#8FFF00", "orange": "#FFD700",
        "purple": "#D4FF00", "blue": "#AAFF00", "red": "#FF9900", "yellow": "#FAFF00", "lime": "#7FFF00",
        "gradient": "linear-gradient(90deg, #D4FF00, #BFFF00, #8FFF00, #AAFF00, #FFB800, #FFD700, #FF9900, #D4FF00)"
    }
}

theme_name = st.sidebar.selectbox("🎨 UI Theme", list(theme_colors.keys()), index=0, key="theme_selector")
colors = theme_colors[theme_name]

# ════════════════════════════════════════════════════════════════
# MEGA CSS — ULTRA ANIMATED, BRIGHT, NEON, GLASSMORPHISM
# ════════════════════════════════════════════════════════════════
st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700;800&family=Orbitron:wght@400;500;600;700;800;900&display=swap');

:root {
    --neon-cyan: #00F5FF;
    --neon-pink: #FF2BD6;
    --neon-green: #39FF14;
    --neon-orange: #FFB800;
    --neon-purple: #A855F7;
    --neon-blue: #3B82F6;
    --neon-red: #FF3366;
    --neon-yellow: #FAFF00;
    --neon-lime: #BFFF00;
    --dark-bg: #030712;
    --card-bg: rgba(8, 12, 40, 0.78);
    --card-bg-hover: rgba(15, 20, 60, 0.85);
    --border-glow: rgba(0, 245, 255, 0.25);
    --text-bright: #FFFFFF;
    --text-secondary: #C8D6FF;
    --text-muted: #8892B0;
    --glass: rgba(255, 255, 255, 0.04);
}

/* ═══ GLOBAL ═══ */
*, *::before, *::after { box-sizing: border-box; }

.stApp {
    background:
        radial-gradient(ellipse at 10% 15%, rgba(0,245,255,0.12), transparent 35%),
        radial-gradient(ellipse at 90% 10%, rgba(255,43,214,0.10), transparent 30%),
        radial-gradient(ellipse at 50% 90%, rgba(57,255,20,0.08), transparent 30%),
        radial-gradient(ellipse at 70% 50%, rgba(168,85,247,0.06), transparent 25%),
        radial-gradient(ellipse at 30% 60%, rgba(255,184,0,0.05), transparent 25%),
        linear-gradient(160deg, #020617 0%, #0a0f2e 30%, #150025 60%, #0a1628 100%);
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
}

.block-container {
    padding-top: 0.5rem !important;
    max-width: 1500px;
}

#MainMenu, footer, .stDeployButton, header { visibility: hidden; display: none; }
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: #030712; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, var(--neon-cyan), var(--neon-pink), var(--neon-green));
    border-radius: 20px;
}

h1, h2, h3, h4, h5, h6, p, div, span, label, li {
    color: var(--text-bright) !important;
}

/* ═══ KEYFRAME ANIMATIONS ═══ */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(40px) scale(0.96); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}
@keyframes fadeDown {
    from { opacity: 0; transform: translateY(-30px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes fadeLeft {
    from { opacity: 0; transform: translateX(-40px); }
    to { opacity: 1; transform: translateX(0); }
}
@keyframes fadeRight {
    from { opacity: 0; transform: translateX(40px); }
    to { opacity: 1; transform: translateX(0); }
}
@keyframes scaleIn {
    from { opacity: 0; transform: scale(0.7); }
    to { opacity: 1; transform: scale(1); }
}
@keyframes float {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    25% { transform: translateY(-14px) rotate(2deg); }
    50% { transform: translateY(-8px) rotate(-1deg); }
    75% { transform: translateY(-16px) rotate(1deg); }
}
@keyframes floatSlow {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
}
@keyframes glow {
    0%, 100% { box-shadow: 0 0 20px rgba(0,245,255,0.3), 0 0 40px rgba(0,245,255,0.1); }
    33% { box-shadow: 0 0 30px rgba(255,43,214,0.4), 0 0 60px rgba(255,43,214,0.15); }
    66% { box-shadow: 0 0 25px rgba(57,255,20,0.35), 0 0 50px rgba(57,255,20,0.12); }
}
@keyframes textGlow {
    0%, 100% { text-shadow: 0 0 20px rgba(0,245,255,0.5), 0 0 40px rgba(0,245,255,0.2); }
    50% { text-shadow: 0 0 30px rgba(255,43,214,0.6), 0 0 60px rgba(255,43,214,0.3); }
}
@keyframes shimmer {
    0% { background-position: -300% center; }
    100% { background-position: 300% center; }
}
@keyframes shimmerFast {
    0% { background-position: -200% center; }
    100% { background-position: 200% center; }
}
@keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.08); opacity: 0.9; }
}
@keyframes pulseSoft {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.03); }
}
@keyframes borderMove {
    0%, 100% { border-color: rgba(0,245,255,0.35); }
    25% { border-color: rgba(255,43,214,0.50); }
    50% { border-color: rgba(57,255,20,0.45); }
    75% { border-color: rgba(255,184,0,0.40); }
}
@keyframes borderRotate {
    0% { border-image-source: linear-gradient(0deg, var(--neon-cyan), var(--neon-pink)); }
    25% { border-image-source: linear-gradient(90deg, var(--neon-pink), var(--neon-green)); }
    50% { border-image-source: linear-gradient(180deg, var(--neon-green), var(--neon-orange)); }
    75% { border-image-source: linear-gradient(270deg, var(--neon-orange), var(--neon-cyan)); }
    100% { border-image-source: linear-gradient(360deg, var(--neon-cyan), var(--neon-pink)); }
}
@keyframes scan {
    0% { left: -120%; }
    100% { left: 120%; }
}
@keyframes scanFast {
    0% { left: -80%; }
    100% { left: 180%; }
}
@keyframes rotate360 {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
@keyframes morphBlob {
    0%, 100% { border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; }
    25% { border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%; }
    50% { border-radius: 40% 60% 30% 70% / 40% 70% 60% 30%; }
    75% { border-radius: 60% 30% 60% 40% / 70% 40% 50% 60%; }
}
@keyframes colorShift {
    0%, 100% { filter: hue-rotate(0deg); }
    50% { filter: hue-rotate(30deg); }
}
@keyframes neonFlicker {
    0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% { opacity: 1; }
    20%, 24%, 55% { opacity: 0.6; }
}
@keyframes ripple {
    0% { transform: scale(0.8); opacity: 1; }
    100% { transform: scale(2.5); opacity: 0; }
}
@keyframes slideIn {
    from { transform: translateX(-100%); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}
@keyframes bounceIn {
    0% { transform: scale(0.3); opacity: 0; }
    50% { transform: scale(1.05); }
    70% { transform: scale(0.95); }
    100% { transform: scale(1); opacity: 1; }
}
@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    14% { transform: scale(1.15); }
    28% { transform: scale(1); }
    42% { transform: scale(1.15); }
    70% { transform: scale(1); }
}
@keyframes particleRise {
    0% { transform: translateY(0) scale(1); opacity: 0.8; }
    100% { transform: translateY(-120vh) scale(0.3); opacity: 0; }
}
@keyframes dashMove {
    to { stroke-dashoffset: 0; }
}
@keyframes typewriter {
    from { width: 0; }
    to { width: 100%; }
}
@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}
@keyframes rainbowBorder {
    0% { border-color: #FF0000; }
    14% { border-color: #FF7700; }
    28% { border-color: #FFFF00; }
    42% { border-color: #00FF00; }
    57% { border-color: #0000FF; }
    71% { border-color: #8B00FF; }
    85% { border-color: #FF00FF; }
    100% { border-color: #FF0000; }
}
@keyframes energyWave {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ═══ BACKGROUND ELEMENTS ═══ */
.grid-bg {
    position: fixed; inset: 0; z-index: -3; pointer-events: none;
    background-image:
        linear-gradient(rgba(0,245,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,245,255,0.03) 1px, transparent 1px);
    background-size: 48px 48px;
    animation: pulseSoft 8s infinite;
}
.hex-bg {
    position: fixed; inset: 0; z-index: -4; pointer-events: none; opacity: 0.015;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='28' height='49' viewBox='0 0 28 49'%3E%3Cg fill-rule='evenodd'%3E%3Cg fill='%2300f5ff' fill-opacity='1'%3E%3Cpath d='M13.99 9.25l13 7.5v15l-13 7.5L1 31.75v-15l12.99-7.5zM3 17.9v12.7l10.99 6.34 11-6.35V17.9l-11-6.34L3 17.9zM0 15l12.98-7.5V0h-2v6.35L0 12.69v2.3zm0 18.5L12.98 41v8h-2v-6.85L0 35.81v-2.3zM15 0v7.5L27.99 15H28v-2.31h-.01L17 6.35V0h-2zm0 49v-8l12.99-7.5H28v2.31h-.01L17 42.15V49h-2z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}

/* Floating orbs */
.orb { position: fixed; border-radius: 50%; pointer-events: none; z-index: -2; }
.orb-cyan {
    width: 350px; height: 350px;
    background: radial-gradient(circle, rgba(0,245,255,0.25), transparent 70%);
    top: 5%; left: 3%;
    animation: float 9s infinite ease-in-out, morphBlob 20s infinite ease-in-out;
    filter: blur(50px);
}
.orb-pink {
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(255,43,214,0.20), transparent 70%);
    top: 40%; right: 5%;
    animation: float 11s 2s infinite ease-in-out, morphBlob 18s 3s infinite ease-in-out;
    filter: blur(55px);
}
.orb-green {
    width: 280px; height: 280px;
    background: radial-gradient(circle, rgba(57,255,20,0.18), transparent 70%);
    bottom: 8%; left: 25%;
    animation: float 13s 4s infinite ease-in-out, morphBlob 22s 5s infinite ease-in-out;
    filter: blur(60px);
}
.orb-purple {
    width: 250px; height: 250px;
    background: radial-gradient(circle, rgba(168,85,247,0.15), transparent 70%);
    top: 65%; left: 60%;
    animation: floatSlow 15s 1s infinite ease-in-out, morphBlob 25s infinite ease-in-out;
    filter: blur(65px);
}
.orb-orange {
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(255,184,0,0.12), transparent 70%);
    top: 20%; right: 30%;
    animation: floatSlow 10s 3s infinite ease-in-out, morphBlob 16s 2s infinite ease-in-out;
    filter: blur(45px);
}

/* Particles */
.particles-container { position: fixed; inset: 0; z-index: -1; pointer-events: none; overflow: hidden; }
.particle {
    position: absolute;
    border-radius: 50%;
    animation: particleRise linear infinite;
}

/* ═══ SIDEBAR ═══ */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020818 0%, #0a1535 40%, #150020 70%, #080e28 100%) !important;
    border-right: 1px solid var(--border-glow) !important;
    box-shadow: 4px 0 30px rgba(0,245,255,0.08);
}
[data-testid="stSidebar"] .stRadio label {
    font-weight: 700 !important;
    font-size: 15px !important;
    transition: all 0.3s !important;
    padding: 4px 8px !important;
    border-radius: 10px !important;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(0,245,255,0.08) !important;
    transform: translateX(6px);
}

/* ═══ HERO ═══ */
.hero-main {
    border-radius: 32px;
    padding: 52px 48px;
    background:
        linear-gradient(135deg,
            rgba(0,245,255,0.12) 0%,
            rgba(168,85,247,0.14) 30%,
            rgba(255,43,214,0.12) 60%,
            rgba(57,255,20,0.08) 100%);
    border: 1px solid var(--border-glow);
    position: relative;
    overflow: hidden;
    animation: fadeUp 0.9s ease-out, borderMove 5s infinite ease-in-out, glow 6s infinite;
}
.hero-main::before {
    content: "";
    position: absolute;
    top: 0; left: -120%;
    width: 80%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), rgba(0,245,255,0.06), transparent);
    animation: scan 5s infinite ease-in-out;
}
.hero-main::after {
    content: "";
    position: absolute;
    bottom: 0; right: -120%;
    width: 60%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,43,214,0.05), transparent);
    animation: scan 7s 2s infinite ease-in-out;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 10px 22px;
    border-radius: 999px;
    background: linear-gradient(135deg, rgba(0,245,255,0.12), rgba(57,255,20,0.08));
    border: 1px solid rgba(0,245,255,0.4);
    font-weight: 900;
    font-size: 14px;
    color: var(--neon-cyan) !important;
    margin-bottom: 20px;
    animation: fadeDown 0.6s ease-out, borderMove 3s infinite;
    backdrop-filter: blur(10px);
}
.live-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    background: var(--neon-green);
    display: inline-block;
    animation: pulse 1.4s infinite;
    box-shadow: 0 0 12px rgba(57,255,20,0.6);
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 62px;
    font-weight: 900;
    line-height: 1.05;
    margin: 0 0 16px 0;
    animation: fadeUp 1s ease-out 0.2s both, textGlow 4s infinite;
}

.grad-main {
    background: linear-gradient(90deg,
        #FAFF00, #39FF14, #00F5FF, #A855F7, #FF2BD6, #FF3366, #FFB800, #FAFF00);
    background-size: 400% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 4s linear infinite;
}
.grad-cyan-pink {
    background: linear-gradient(90deg, #00F5FF, #A855F7, #FF2BD6);
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 3s linear infinite;
}
.grad-green-cyan {
    background: linear-gradient(90deg, #39FF14, #00F5FF, #3B82F6);
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 3.5s linear infinite;
}
.grad-fire {
    background: linear-gradient(90deg, #FFB800, #FF3366, #FF2BD6, #FFB800);
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 3s linear infinite;
}
.grad-rainbow {
    background: linear-gradient(90deg, #FF0000, #FF7700, #FFFF00, #00FF00, #0000FF, #8B00FF, #FF00FF, #FF0000);
    background-size: 500% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 6s linear infinite;
}

.hero-sub {
    font-size: 20px;
    font-weight: 700;
    color: var(--text-secondary) !important;
    max-width: 850px;
    line-height: 1.55;
    animation: fadeUp 1s ease-out 0.4s both;
}

/* ═══ GLASS CARD ═══ */
.glass {
    border-radius: 28px;
    padding: 28px;
    background: var(--card-bg);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid var(--border-glow);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.04);
    transition: all 0.45s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
    animation: fadeUp 0.7s ease-out both;
    margin-bottom: 16px;
}
.glass::before {
    content: "";
    position: absolute;
    top: 0; left: -120%;
    width: 80%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.06), transparent);
    transition: left 0.7s;
}
.glass:hover::before { left: 120%; }
.glass:hover {
    transform: translateY(-8px) scale(1.012);
    border-color: rgba(255,43,214,0.5);
    box-shadow:
        0 20px 60px rgba(0,245,255,0.12),
        0 8px 32px rgba(255,43,214,0.10),
        inset 0 1px 0 rgba(255,255,255,0.06);
}

/* Card delays */
.d1 { animation-delay: 0.05s !important; }
.d2 { animation-delay: 0.12s !important; }
.d3 { animation-delay: 0.19s !important; }
.d4 { animation-delay: 0.26s !important; }
.d5 { animation-delay: 0.33s !important; }
.d6 { animation-delay: 0.40s !important; }
.d7 { animation-delay: 0.47s !important; }
.d8 { animation-delay: 0.54s !important; }

/* ═══ METRIC CARD ═══ */
.metric-box {
    text-align: center;
    min-height: 175px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.metric-icon {
    font-size: 46px;
    display: block;
    margin-bottom: 10px;
    animation: float 3.5s infinite ease-in-out;
    filter: drop-shadow(0 0 15px rgba(0,245,255,0.4));
}
.metric-val {
    font-family: 'Orbitron', sans-serif;
    font-size: 42px;
    font-weight: 900;
    letter-spacing: 1px;
    line-height: 1.1;
}
.metric-label {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--text-muted) !important;
    font-weight: 800;
    margin-top: 6px;
}
.metric-change {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 800;
    margin-top: 8px;
}
.change-up { background: rgba(57,255,20,0.12); color: var(--neon-green) !important; }
.change-down { background: rgba(255,51,102,0.12); color: var(--neon-red) !important; }

/* ═══ FEATURE CARD ═══ */
.feat-card {
    min-height: 220px;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.feat-card::after {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--neon-cyan), var(--neon-pink), var(--neon-green));
    background-size: 200% auto;
    animation: shimmer 3s linear infinite;
    transform: scaleX(0);
    transition: transform 0.4s;
    border-radius: 28px 28px 0 0;
}
.feat-card:hover::after { transform: scaleX(1); }
.feat-icon-wrap {
    width: 68px; height: 68px;
    border-radius: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    margin-bottom: 16px;
    transition: transform 0.4s, box-shadow 0.4s;
    position: relative;
    overflow: hidden;
}
.feat-icon-wrap::before {
    content: "";
    position: absolute; inset: 0;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(0,245,255,0.15), rgba(255,43,214,0.10));
    z-index: -1;
}
.feat-card:hover .feat-icon-wrap {
    transform: scale(1.12) rotate(8deg);
    box-shadow: 0 8px 25px rgba(0,245,255,0.3);
}
.feat-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 8px;
}
.feat-desc {
    color: var(--text-secondary) !important;
    font-size: 15px;
    font-weight: 600;
    line-height: 1.55;
}

/* ═══ IMAGE CARD ═══ */
.img-card {
    height: 240px;
    border-radius: 28px;
    background-size: cover;
    background-position: center;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow:
        inset 0 -90px 100px rgba(0,0,0,0.80),
        0 8px 32px rgba(0,0,0,0.4),
        0 0 30px rgba(0,245,255,0.10);
    display: flex;
    align-items: flex-end;
    padding: 22px;
    position: relative;
    overflow: hidden;
    transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    animation: fadeUp 0.7s ease-out both;
}
.img-card::before {
    content: "";
    position: absolute;
    top: 0; left: -120%;
    width: 60%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.10), transparent);
    transition: left 0.6s;
}
.img-card:hover::before { left: 120%; }
.img-card:hover {
    transform: translateY(-10px) scale(1.03);
    box-shadow:
        inset 0 -90px 100px rgba(0,0,0,0.80),
        0 20px 60px rgba(0,245,255,0.15),
        0 0 50px rgba(255,43,214,0.12);
    border-color: rgba(0,245,255,0.4);
}
.img-card-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 26px;
    font-weight: 900;
    text-shadow: 0 2px 12px rgba(0,0,0,0.8), 0 0 20px rgba(0,245,255,0.3);
    z-index: 2;
}
.img-card-badge {
    position: absolute;
    top: 16px; right: 16px;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 900;
    backdrop-filter: blur(8px);
    z-index: 2;
    animation: pulse 2s infinite;
}

/* ═══ CHAT ═══ */
.chat-container {
    border-radius: 28px;
    padding: 24px;
    background: var(--card-bg);
    border: 1px solid var(--border-glow);
    max-height: 520px;
    overflow-y: auto;
    animation: fadeUp 0.6s ease-out;
}
.chat-ai-msg {
    border-radius: 22px 22px 22px 6px;
    padding: 18px 22px;
    margin: 12px 0;
    font-size: 16px;
    font-weight: 700;
    line-height: 1.6;
    background: linear-gradient(135deg, rgba(0,245,255,0.12), rgba(168,85,247,0.10));
    border: 1px solid rgba(0,245,255,0.30);
    animation: fadeLeft 0.5s ease-out;
    max-width: 85%;
}
.chat-user-msg {
    border-radius: 22px 22px 6px 22px;
    padding: 18px 22px;
    margin: 12px 0;
    font-size: 16px;
    font-weight: 700;
    line-height: 1.6;
    background: linear-gradient(135deg, #FF2BD6, #8A2BFF);
    animation: fadeRight 0.5s ease-out;
    max-width: 80%;
    margin-left: auto;
    box-shadow: 0 4px 20px rgba(255,43,214,0.25);
}
.chat-avatar {
    display: inline-flex;
    width: 36px; height: 36px;
    border-radius: 12px;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    margin-right: 10px;
    animation: glow 3s infinite;
}
.chat-avatar-ai { background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple)); }
.chat-avatar-user { background: linear-gradient(135deg, var(--neon-pink), var(--neon-orange)); }

/* ═══ PROGRESS BAR ═══ */
.progress-wrap {
    height: 14px;
    background: rgba(255,255,255,0.06);
    border-radius: 14px;
    overflow: hidden;
    margin: 10px 0;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.3);
}
.progress-fill {
    height: 100%;
    border-radius: 14px;
    background: linear-gradient(90deg, var(--neon-green), var(--neon-cyan), var(--neon-pink), var(--neon-orange));
    background-size: 300% auto;
    animation: shimmer 2.5s linear infinite;
    transition: width 1.5s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 0 15px rgba(0,245,255,0.3);
}

/* ═══ SECTION TITLES ═══ */
.sec-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 34px;
    font-weight: 900;
    margin: 30px 0 6px;
    animation: fadeUp 0.6s ease-out;
}
.sec-sub {
    color: var(--text-secondary) !important;
    font-weight: 700;
    font-size: 16px;
    margin-bottom: 22px;
    animation: fadeUp 0.6s ease-out 0.15s both;
}

/* ═══ STATUS BADGE ═══ */
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    border-radius: 999px;
    font-weight: 900;
    font-size: 13px;
    backdrop-filter: blur(8px);
}
.status-online {
    background: rgba(57,255,20,0.10);
    border: 1px solid rgba(57,255,20,0.35);
    color: var(--neon-green) !important;
}

/* ═══ TAG ═══ */
.tag {
    display: inline-flex;
    padding: 5px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 0.5px;
}
.tag-cyan { background: rgba(0,245,255,0.12); color: var(--neon-cyan) !important; border: 1px solid rgba(0,245,255,0.3); }
.tag-pink { background: rgba(255,43,214,0.12); color: var(--neon-pink) !important; border: 1px solid rgba(255,43,214,0.3); }
.tag-green { background: rgba(57,255,20,0.12); color: var(--neon-green) !important; border: 1px solid rgba(57,255,20,0.3); }
.tag-orange { background: rgba(255,184,0,0.12); color: var(--neon-orange) !important; border: 1px solid rgba(255,184,0,0.3); }
.tag-purple { background: rgba(168,85,247,0.12); color: var(--neon-purple) !important; border: 1px solid rgba(168,85,247,0.3); }
.tag-red { background: rgba(255,51,102,0.12); color: var(--neon-red) !important; border: 1px solid rgba(255,51,102,0.3); }

/* ═══ TIMELINE ═══ */
.timeline-item {
    display: flex;
    gap: 18px;
    padding: 18px 0 18px 28px;
    border-left: 2px solid var(--border-glow);
    position: relative;
    animation: fadeLeft 0.5s ease-out both;
}
.timeline-item::before {
    content: "";
    position: absolute;
    left: -7px; top: 22px;
    width: 12px; height: 12px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--neon-cyan), var(--neon-pink));
    box-shadow: 0 0 12px rgba(0,245,255,0.5);
    animation: pulse 2s infinite;
}
.timeline-time {
    font-size: 13px;
    color: var(--text-muted) !important;
    font-weight: 700;
    min-width: 80px;
}
.timeline-text {
    color: var(--text-secondary) !important;
    font-size: 15px;
    font-weight: 600;
    line-height: 1.5;
}

/* ═══ NOTIFICATION CARD ═══ */
.notif {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 16px 20px;
    background: rgba(255,255,255,0.02);
    border-radius: 18px;
    margin-bottom: 12px;
    border: 1px solid transparent;
    transition: all 0.35s;
    animation: fadeUp 0.5s ease-out both;
}
.notif:hover {
    background: rgba(0,245,255,0.04);
    border-color: var(--border-glow);
    transform: translateX(6px);
}
.notif-icon {
    width: 48px; height: 48px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    flex-shrink: 0;
}
.notif-title { font-size: 15px; font-weight: 800; }
.notif-desc { font-size: 13px; color: var(--text-muted) !important; font-weight: 600; }

/* ═══ CHART BARS ═══ */
.bars-container {
    display: flex;
    align-items: flex-end;
    gap: 8px;
    height: 200px;
    padding: 16px 0;
}
.bar-item {
    flex: 1;
    border-radius: 10px 10px 0 0;
    position: relative;
    min-width: 28px;
    cursor: pointer;
    transition: all 0.35s;
    animation: fadeUp 0.5s ease-out both;
}
.bar-item:hover {
    filter: brightness(1.4);
    transform: scaleY(1.06);
    transform-origin: bottom;
}
.bar-label {
    position: absolute;
    bottom: -26px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 11px;
    color: var(--text-muted) !important;
    font-weight: 700;
    white-space: nowrap;
}
.bar-value {
    position: absolute;
    top: -24px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 12px;
    font-weight: 800;
    color: var(--neon-cyan) !important;
    opacity: 0;
    transition: opacity 0.3s;
}
.bar-item:hover .bar-value { opacity: 1; }

/* ═══ WORKOUT SPLIT CARD ═══ */
.split-card {
    border-radius: 22px;
    padding: 22px;
    background: linear-gradient(135deg, rgba(0,245,255,0.06), rgba(255,43,214,0.04));
    border: 1px solid var(--border-glow);
    margin-bottom: 14px;
    transition: all 0.35s;
    animation: fadeUp 0.5s ease-out both;
}
.split-card:hover {
    transform: translateX(8px);
    border-color: rgba(255,43,214,0.4);
    background: linear-gradient(135deg, rgba(0,245,255,0.10), rgba(255,43,214,0.08));
}
.split-day {
    font-family: 'Orbitron', sans-serif;
    font-size: 14px;
    font-weight: 900;
    color: var(--neon-cyan) !important;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.split-muscle {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 20px;
    font-weight: 800;
    margin: 4px 0;
}
.split-exercises {
    font-size: 14px;
    color: var(--text-secondary) !important;
    font-weight: 600;
    line-height: 1.6;
}

/* ═══ MEAL CARD ═══ */
.meal-card {
    border-radius: 24px;
    padding: 28px;
    text-align: center;
    min-height: 200px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}
.meal-card::after {
    content: "";
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    animation: shimmer 3s linear infinite;
}
.meal-icon { font-size: 52px; margin-bottom: 14px; animation: float 3s infinite ease-in-out; }
.meal-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 6px;
}
.meal-desc {
    font-size: 14px;
    color: var(--text-secondary) !important;
    font-weight: 600;
    line-height: 1.5;
}
.meal-kcal {
    display: inline-flex;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 900;
    margin-top: 10px;
}

/* ═══ CALORIE RESULT ═══ */
.cal-result {
    text-align: center;
    padding: 48px;
    border-radius: 32px;
    background:
        radial-gradient(circle at 30% 40%, rgba(255,184,0,0.12), transparent 50%),
        radial-gradient(circle at 70% 60%, rgba(255,51,102,0.10), transparent 50%),
        var(--card-bg);
    border: 1px solid rgba(255,184,0,0.3);
    animation: scaleIn 0.7s ease-out, glow 4s infinite;
}
.cal-number {
    font-family: 'Orbitron', sans-serif;
    font-size: 72px;
    font-weight: 900;
    line-height: 1;
    margin: 16px 0;
}
.cal-label {
    font-size: 18px;
    color: var(--text-secondary) !important;
    font-weight: 700;
}

/* ═══ BUTTONS ═══ */
.stButton > button {
    background: linear-gradient(90deg, #00F5FF, #A855F7, #FF2BD6, #FFB800) !important;
    background-size: 300% auto !important;
    animation: shimmer 4s linear infinite !important;
    color: white !important;
    border: 0 !important;
    border-radius: 18px !important;
    font-weight: 900 !important;
    font-size: 15px !important;
    padding: 14px 28px !important;
    box-shadow: 0 6px 24px rgba(0,245,255,0.20), 0 2px 8px rgba(255,43,214,0.15) !important;
    transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    letter-spacing: 0.5px !important;
}
.stButton > button:hover {
    transform: translateY(-4px) scale(1.02) !important;
    box-shadow: 0 12px 40px rgba(0,245,255,0.30), 0 4px 16px rgba(255,43,214,0.25) !important;
}
.stButton > button:active {
    transform: translateY(-1px) scale(0.98) !important;
}

/* ═══ INPUTS ═══ */
.stTextInput input, .stNumberInput input, .stTextArea textarea {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid var(--border-glow) !important;
    border-radius: 16px !important;
    color: white !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    padding: 14px 18px !important;
    transition: all 0.3s !important;
}
.stTextInput input:focus, .stNumberInput input:focus, .stTextArea textarea:focus {
    border-color: var(--neon-cyan) !important;
    box-shadow: 0 0 0 3px rgba(0,245,255,0.12) !important;
}
.stSelectbox > div > div {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid var(--border-glow) !important;
    border-radius: 16px !important;
    color: white !important;
    font-weight: 700 !important;
}

/* ═══ TABS ═══ */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.02);
    border-radius: 18px;
    padding: 5px;
    gap: 5px;
    border: 1px solid var(--border-glow);
}
.stTabs [data-baseweb="tab"] {
    border-radius: 14px;
    color: var(--text-secondary) !important;
    font-weight: 700;
    padding: 12px 22px;
    transition: all 0.3s;
}
.stTabs [data-baseweb="tab"]:hover {
    color: white !important;
    background: rgba(0,245,255,0.08);
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple)) !important;
    color: white !important;
}
.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"] { display: none; }

/* ═══ DIVIDER ═══ */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border-glow), rgba(255,43,214,0.2), var(--border-glow), transparent);
    margin: 36px 0;
}

/* ═══ RING PROGRESS ═══ */
.ring-container { text-align: center; position: relative; display: inline-block; }
.ring-text {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    font-family: 'Orbitron', sans-serif;
    font-size: 28px;
    font-weight: 900;
}

/* ═══ SLIDER ═══ */
.stSlider > div > div > div { background: var(--neon-cyan) !important; }

/* ═══ RESPONSIVE ═══ */
@media (max-width: 768px) {
    .hero-title { font-size: 36px !important; }
    .metric-val { font-size: 28px !important; }
    .sec-title { font-size: 24px !important; }
    .cal-number { font-size: 48px !important; }
}
</style>

<!-- Background Elements -->
<div class="grid-bg"></div>
<div class="hex-bg"></div>
<div class="orb orb-cyan"></div>
<div class="orb orb-pink"></div>
<div class="orb orb-green"></div>
<div class="orb orb-purple"></div>
<div class="orb orb-orange"></div>

<!-- Particles -->
<div class="particles-container">
''' + ''.join([
    f'<div class="particle" style="left:{random.randint(0,100)}%;bottom:-10px;width:{random.randint(2,5)}px;height:{random.randint(2,5)}px;background:{colors["cyan"] if i%3==0 else colors["pink"] if i%3==1 else colors["green"]};animation-duration:{random.randint(8,20)}s;animation-delay:{random.uniform(0,10):.1f}s;opacity:{random.uniform(0.2,0.6):.1f};"></div>'
    for i in range(30)
]) + '''
</div>
''', unsafe_allow_html=True)

# Theme Overrides CSS Block
st.markdown(f'''
<style>
:root {{
    --neon-cyan: {colors['cyan']};
    --neon-pink: {colors['pink']};
    --neon-green: {colors['green']};
    --neon-orange: {colors['orange']};
    --neon-purple: {colors['purple']};
    --neon-blue: {colors['blue']};
    --neon-red: {colors['red']};
    --neon-yellow: {colors['yellow']};
    --neon-lime: {colors['lime']};
    --border-glow: {colors['cyan']}40;
}}
.orb-cyan {{
    background: radial-gradient(circle, {colors['cyan']}40, transparent 70%) !important;
}}
.orb-pink {{
    background: radial-gradient(circle, {colors['pink']}33, transparent 70%) !important;
}}
.orb-green {{
    background: radial-gradient(circle, {colors['green']}30, transparent 70%) !important;
}}
.orb-purple {{
    background: radial-gradient(circle, {colors['purple']}26, transparent 70%) !important;
}}
.orb-orange {{
    background: radial-gradient(circle, {colors['orange']}20, transparent 70%) !important;
}}
.grad-main {{
    background: {colors['gradient']} !important;
    background-size: 400% auto !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}}
.grad-cyan-pink {{
    background: linear-gradient(90deg, {colors['cyan']}, {colors['pink']}) !important;
    background-size: 300% auto !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}}
.grad-green-cyan {{
    background: linear-gradient(90deg, {colors['green']}, {colors['cyan']}, {colors['blue']}) !important;
    background-size: 300% auto !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}}
.grad-fire {{
    background: linear-gradient(90deg, {colors['orange']}, {colors['red']}, {colors['pink']}) !important;
    background-size: 300% auto !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}}
.grad-rainbow {{
    background: {colors['gradient']} !important;
    background-size: 500% auto !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}}
/* Streamlit widget glassmorphism overrides */
.stButton > button {{
    background: {colors['gradient']} !important;
    background-size: 300% auto !important;
    animation: shimmer 4s linear infinite !important;
    color: white !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 18px !important;
    font-weight: 900 !important;
    font-size: 15px !important;
    padding: 12px 28px !important;
    box-shadow: 0 6px 24px {colors['cyan']}33, 0 2px 8px {colors['pink']}26 !important;
    transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
}}
.stButton > button:hover {{
    transform: translateY(-4px) scale(1.02) !important;
    box-shadow: 0 12px 40px {colors['cyan']}4D, 0 4px 16px {colors['pink']}4D !important;
}}
.stTextInput input, .stNumberInput input, .stTextArea textarea, .stSelectbox > div > div {{
    background: rgba(8, 12, 40, 0.6) !important;
    border: 1px solid {colors['cyan']}40 !important;
    border-radius: 16px !important;
    color: white !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    padding: 12px 18px !important;
    transition: all 0.3s !important;
    backdrop-filter: blur(10px) !important;
}}
.stTextInput input:focus, .stNumberInput input:focus, .stTextArea textarea:focus, .stSelectbox > div > div:focus-within {{
    border-color: {colors['cyan']} !important;
    box-shadow: 0 0 15px {colors['cyan']}4D !important;
    background: rgba(15, 20, 60, 0.85) !important;
}}
/* Sidebar overrides */
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #020818 0%, #0a1535 50%, #080e28 100%) !important;
    border-right: 1px solid {colors['cyan']}40 !important;
}}
[data-testid="stSidebar"] .stRadio label {{
    font-weight: 700 !important;
    font-size: 15px !important;
    transition: all 0.3s !important;
    padding: 6px 12px !important;
    border-radius: 10px !important;
}}
[data-testid="stSidebar"] .stRadio label:hover {{
    background: {colors['cyan']}1A !important;
    transform: translateX(6px);
    color: {colors['cyan']} !important;
}}
[data-testid="stSidebar"] div[role="radiogroup"] label[data-selected="true"] {{
    background: linear-gradient(135deg, {colors['cyan']}40, {colors['purple']}20) !important;
    border-left: 4px solid {colors['cyan']} !important;
    color: white !important;
}}
</style>
''', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# SESSION STATE
# ════════════════════════════════════════════════════════════════
if 'chat_msgs' not in st.session_state:
    st.session_state.chat_msgs = []
if 'total_queries' not in st.session_state:
    st.session_state.total_queries = 0
if 'workouts_done' not in st.session_state:
    st.session_state.workouts_done = 0

# ════════════════════════════════════════════════════════════════
# AI ENGINE — OFFLINE, NO API NEEDED
# ════════════════════════════════════════════════════════════════
def ai_reply(question: str) -> str:
    q = (question or "").lower().strip()
    if not q:
        return "💬 Ask me anything about workouts, diet, calories, fat loss, muscle gain, recovery, or any specific body part training!"

    # Greetings
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

🔥 **EPOC (Afterburn):** Intense workouts burn extra 50-200 kcal for 24-48 hours after!

📱 Use the Calorie Predictor page for personalized estimates!"""

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

⚠️ **Signs of Overtraining:** Constant fatigue, strength loss, insomnia, frequent illness, elevated resting heart rate

💊 **Supplements:** Creatine 5g/day, Omega-3, Vitamin D, Magnesium"""

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

❌ **Skip:** BCAAs (waste if eating enough protein), fat burners, testosterone boosters

💡 **Remember:** Supplements are 5% of results. Training + diet + sleep = 95%!"""

    # Stretching / Flexibility
    if any(x in q for x in ["stretch", "flexibility", "warm up", "cool down", "mobility"]):
        return """🧘 **MOBILITY & STRETCHING ROUTINE**

🔥 **Pre-Workout (Dynamic — 5 min):**
• Arm circles, leg swings, hip circles
• Bodyweight squats, lunges, high knees
• Cat-cow, world's greatest stretch

🧊 **Post-Workout (Static — 10 min):**
• Chest doorway stretch — 30s each
• Lat stretch — 30s each
• Hip flexor stretch — 30s each
• Hamstring stretch — 30s each
• Quad stretch — 30s each
• Shoulder cross-body stretch — 30s each

💡 **Hold each static stretch 20-30 seconds, never bounce. Breathe deeply!**"""

    # Motivation
    if any(x in q for x in ["motivat", "lazy", "skip", "don't feel", "can't", "hard", "give up", "quit"]):
        return """🔥 **MOTIVATION BOOST!**

💪 "The only bad workout is the one that didn't happen."
💪 "Your body can stand almost anything. It's your mind you have to convince."
💪 "Don't wish for it. Work for it."

🎯 **Action Plan:**
1. Just show up — even 20 minutes counts
2. Track progress — small wins compound
3. Find a workout buddy
4. Set specific goals (not "lose weight" → "lose 5kg in 8 weeks")
5. Remember WHY you started

⚡ You've got this! Every rep, every set, every day — you're building a better version of yourself! 🚀"""

    # Thank you
    if any(x in q for x in ["thank", "thanks", "thx", "appreciate"]):
        return "You're welcome! 😊💪 Keep pushing hard and stay consistent. Remember — progressive overload + proper nutrition + good sleep = guaranteed results! Ask me anything else anytime! 🔥"

    # Default
    return f"""🤖 **FitPulse AI Response**

Great question! Here's my general advice based on your query: *"{question}"*

📋 **Key Principles:**
1. **Progressive Overload** — increase weight/reps/sets every week
2. **Protein Intake** — 1.6-2.2g per kg bodyweight daily
3. **Sleep** — 7-8 hours for optimal recovery & growth
4. **Consistency** — 4-5 training days/week minimum
5. **Track Everything** — what gets measured gets managed

💡 **Try asking me specifically:**
• "chest workout" or "back workout"
• "diet plan" or "fat loss tips"
• "calorie burn" or "beginner plan"
• "supplements" or "recovery tips"
• "shoulder workout" or "arm workout"

I'm here to help you reach your fitness goals! 💪🔥"""

# ════════════════════════════════════════════════════════════════
# CHAT RENDERER
# ════════════════════════════════════════════════════════════════
def render_chat(key="main"):
    if f"msgs_{key}" not in st.session_state:
        st.session_state[f"msgs_{key}"] = [
            ("AI", "Hey! 💪🔥 I'm your FitPulse AI Coach — fully working offline, no API needed! Ask me about **chest, back, legs, shoulders, arms, diet, fat loss, calories, recovery, supplements** or anything fitness! Let's go! 🚀")
        ]

    # Chat header
    st.markdown('''
    <div class="glass" style="padding: 18px 24px; margin-bottom: 16px;">
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <div style="display: flex; align-items: center; gap: 14px;">
                <div class="chat-avatar chat-avatar-ai" style="width: 48px; height: 48px; font-size: 24px;">🤖</div>
                <div>
                    <div style="font-family: Space Grotesk, sans-serif; font-size: 22px; font-weight: 900;">FitPulse AI Coach</div>
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span class="status-badge status-online"><span class="live-dot"></span> Online & Working</span>
                        <span class="tag tag-cyan">Offline Mode</span>
                    </div>
                </div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 13px; color: var(--text-muted) !important; font-weight: 700;">No API needed</div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Quick action buttons
    bc1, bc2, bc3, bc4, bc5, bc6 = st.columns(6)
    quick = [
        (bc1, "🏋️ Chest", "chest workout"),
        (bc2, "💪 Back", "back workout"),
        (bc3, "🦵 Legs", "legs workout"),
        (bc4, "🥗 Diet", "diet plan"),
        (bc5, "🔥 Fat Loss", "fat loss tips"),
        (bc6, "🛌 Recovery", "recovery tips"),
    ]
    for col, label, prompt in quick:
        if col.button(label, key=f"q_{key}_{label}", use_container_width=True):
            st.session_state[f"msgs_{key}"].append(("You", prompt))
            st.session_state[f"msgs_{key}"].append(("AI", ai_reply(prompt)))
            st.session_state.total_queries += 1
            st.rerun()

    # Display messages
    msgs_html = ""
    for who, msg in st.session_state[f"msgs_{key}"][-12:]:
        if who == "You":
            msgs_html += f'<div class="chat-user-msg"><span class="chat-avatar chat-avatar-user">🧑</span> {msg}</div>'
        else:
            formatted = msg.replace('\n', '<br>')
            msgs_html += f'<div class="chat-ai-msg"><span class="chat-avatar chat-avatar-ai">🤖</span> {formatted}</div>'

    chat_main_col, chat_sidebar_col = st.columns([9, 4])

    with chat_main_col:
        st.markdown(f'<div class="chat-container">{msgs_html}</div>', unsafe_allow_html=True)
        
        if len(st.session_state[f"msgs_{key}"]) > 1:
            last_user_query = ""
            for who, msg in reversed(st.session_state[f"msgs_{key}"]):
                if who == "You":
                    last_user_query = msg.split()[-1].upper() if msg else "CORE"
                    break
            if not last_user_query:
                last_user_query = "FRAGMENT_7B"
            # Limit length of display query
            last_user_query = last_user_query[:16]
            st.markdown(f'''
            <div style="background: rgba(8,12,40,0.5); border: 1px dashed var(--border-glow); border-radius: 12px; padding: 10px; margin-top: 10px; text-align: center;">
                <span class="grad-main" style="font-family: Orbitron, sans-serif; font-weight: 800; font-size: 11px; letter-spacing: 2px;">
                    ••• RAG PROCESSING: MATCHING KNOWLEDGE FOR {last_user_query}
                </span>
            </div>
            ''', unsafe_allow_html=True)

        # Input
        st.markdown("<br>", unsafe_allow_html=True)
        with st.form(f"chat_form_{key}", clear_on_submit=True):
            ic1, ic2 = st.columns([5, 1])
            with ic1:
                question = st.text_input(
                    "Ask your fitness question",
                    placeholder="e.g. 'give me shoulder workout' or 'how to lose belly fat'...",
                    label_visibility="collapsed"
                )
            with ic2:
                send = st.form_submit_button("🚀 Send", use_container_width=True)

    with chat_sidebar_col:
        st.markdown('''
        <div class="glass" style="min-height: 200px; padding: 18px; margin-bottom: 16px;">
            <div style="font-family: Space Grotesk, sans-serif; font-weight: 800; font-size: 14px; margin-bottom: 12px; color: var(--neon-pink) !important; letter-spacing: 1px;">📚 KNOWLEDGE FRAGMENTS</div>
            <div class="notif" style="padding: 10px; margin-bottom: 8px;">
                <div style="width:100%;">
                    <div style="font-size: 12px; font-weight: 800; color: var(--neon-cyan) !important;">FRAGMENT_7B <span style="float:right; color:var(--neon-green) !important;">98.2% MATCH</span></div>
                    <div style="font-size: 11px; color: var(--text-muted) !important; margin-top: 4px; line-height: 1.3;">Hypertrophy and protein synthesis correlation database.</div>
                </div>
            </div>
            <div class="notif" style="padding: 10px; margin-bottom: 8px;">
                <div style="width:100%;">
                    <div style="font-size: 12px; font-weight: 800; color: var(--neon-purple) !important;">DELTA_SIGNAL <span style="float:right; color:var(--neon-cyan) !important;">45.0% MATCH</span></div>
                    <div style="font-size: 11px; color: var(--text-muted) !important; margin-top: 4px; line-height: 1.3;">Electrolyte balance data telemetry from active metabolic sensors.</div>
                </div>
            </div>
            <div class="notif" style="padding: 10px; margin-bottom: 0;">
                <div style="width:100%;">
                    <div style="font-size: 12px; font-weight: 800; color: var(--neon-orange) !important;">OMEGA_REF <span style="float:right; color:var(--neon-orange) !important;">22.1% MATCH</span></div>
                    <div style="font-size: 11px; color: var(--text-muted) !important; margin-top: 4px; line-height: 1.3;">Anaerobic conditioning indices & EPOC thresholds.</div>
                </div>
            </div>
        </div>
        <div class="glass" style="min-height: 200px; padding: 18px;">
            <div style="font-family: Space Grotesk, sans-serif; font-weight: 800; font-size: 14px; margin-bottom: 12px; color: var(--neon-cyan) !important; letter-spacing: 1px;">🕸 NEURAL NODE TOPOLOGY</div>
            <div style="text-align: center; position: relative;">
                <svg width="100%" height="130" viewBox="0 0 160 120">
                    <circle cx="80" cy="60" r="40" fill="none" stroke="rgba(0, 245, 255, 0.08)" stroke-width="1" stroke-dasharray="2,2"/>
                    <circle cx="80" cy="60" r="20" fill="none" stroke="rgba(0, 245, 255, 0.05)" stroke-width="1"/>
                    <line x1="80" y1="20" x2="40" y2="60" stroke="rgba(0, 245, 255, 0.25)" stroke-width="1"/>
                    <line x1="80" y1="20" x2="120" y2="60" stroke="rgba(255, 43, 214, 0.25)" stroke-width="1"/>
                    <line x1="40" y1="60" x2="80" y2="100" stroke="rgba(57, 255, 20, 0.2)" stroke-width="1"/>
                    <line x1="120" y1="60" x2="80" y2="100" stroke="rgba(0, 245, 255, 0.2)" stroke-width="1"/>
                    <line x1="80" y1="20" x2="80" y2="100" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1" stroke-dasharray="1,1"/>
                    <line x1="40" y1="60" x2="120" y2="60" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1" stroke-dasharray="1,1"/>
                    <circle cx="80" cy="60" r="6" fill="var(--neon-pink)" style="filter: drop-shadow(0 0 4px var(--neon-pink));"/>
                    <circle cx="80" cy="20" r="4" fill="var(--neon-cyan)" style="filter: drop-shadow(0 0 3px var(--neon-cyan));"/>
                    <circle cx="40" cy="60" r="4" fill="var(--neon-green)" style="filter: drop-shadow(0 0 3px var(--neon-green));"/>
                    <circle cx="120" cy="60" r="4" fill="var(--neon-orange)" style="filter: drop-shadow(0 0 3px var(--neon-orange));"/>
                    <circle cx="80" cy="100" r="4" fill="var(--neon-purple)" style="filter: drop-shadow(0 0 3px var(--neon-purple));"/>
                </svg>
                <div style="font-family: Orbitron, sans-serif; font-size: 10px; font-weight: 900; color: var(--neon-green) !important; margin-top: 4px; animation: pulse 2s infinite;">LIVE STREAM ACTIVE</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

    if send and question.strip():
        st.session_state[f"msgs_{key}"].append(("You", question.strip()))
        st.session_state[f"msgs_{key}"].append(("AI", ai_reply(question.strip())))
        st.session_state.total_queries += 1
        st.rerun()

    # Clear chat
    if st.button("🧹 Clear Chat", key=f"clear_{key}"):
        st.session_state[f"msgs_{key}"] = [("AI", "Chat cleared ✅ Ask your next fitness question!")]
        st.rerun()

# ════════════════════════════════════════════════════════════════
# SIDEBAR
# ════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown('''
    <div style="text-align: center; padding: 24px 0;">
        <div style="font-size: 56px; animation: float 3s infinite ease-in-out; filter: drop-shadow(0 0 20px rgba(0,245,255,0.4));">💪</div>
        <div style="font-family: Orbitron, sans-serif; font-size: 28px; font-weight: 900; margin-top: 8px;">
            <span class="grad-main">FitPulse AI</span>
        </div>
        <div style="color: var(--text-secondary) !important; font-weight: 700; font-size: 13px; margin-top: 6px; letter-spacing: 1px;">
            ULTIMATE FITNESS PLATFORM
        </div>
        <div style="margin-top: 14px;">
            <span class="status-badge status-online">
                <span class="live-dot"></span> AI Coach Online
            </span>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    page = st.radio(
        "🧭 Navigation",
        [
            "🚀 Dashboard",
            "🤖 AI Coach",
            "🏋️ Workout Generator",
            "🥗 Diet Planner",
            "🔥 Calorie Predictor",
            "❤️ Heart Rate Zones",
            "📊 Progress Tracker",
            "🏆 Achievements",
            "📄 Weekly Report"
        ],
        label_visibility="collapsed"
    )

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown(f'''
    <div class="glass" style="padding: 18px;">
        <div style="font-family: Space Grotesk, sans-serif; font-weight: 800; font-size: 16px; margin-bottom: 12px;">⚡ Session Stats</div>
        <div class="notif">
            <div class="notif-icon" style="background: rgba(0,245,255,0.12);">🤖</div>
            <div>
                <div class="notif-title">AI Queries</div>
                <div class="notif-desc">{st.session_state.total_queries} processed</div>
            </div>
        </div>
        <div class="notif">
            <div class="notif-icon" style="background: rgba(57,255,20,0.12);">💬</div>
            <div>
                <div class="notif-title">Chat Messages</div>
                <div class="notif-desc">{sum(len(st.session_state.get(k, [])) for k in st.session_state if k.startswith('msgs_'))} total</div>
            </div>
        </div>
        <div class="notif">
            <div class="notif-icon" style="background: rgba(255,43,214,0.12);">🏋️</div>
            <div>
                <div class="notif-title">Workouts</div>
                <div class="notif-desc">{st.session_state.workouts_done} generated</div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('''
    <div style="text-align: center; padding: 20px 0; margin-top: 16px;">
        <div style="color: var(--text-muted) !important; font-size: 11px; font-weight: 700; letter-spacing: 1px;">
            BUILT WITH ❤️ + AI<br>
            © 2024 FITPULSE PLATFORM
        </div>
    </div>
    ''', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
# PAGE: DASHBOARD
# ════════════════════════════════════════════════════════════════
if page == "🚀 Dashboard":

    st.markdown('''
    <div class="glass" style="padding: 12px 24px; margin-bottom: 20px; border-radius: 16px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
            <div style="display: flex; gap: 20px; font-family: Orbitron, sans-serif; font-size: 13px; font-weight: 700;">
                <div><span style="color: var(--text-muted) !important;">Protocol:</span> <span class="grad-cyan-pink">Singularity</span></div>
                <div><span style="color: var(--text-muted) !important;">RAG Stream:</span> <span class="grad-green-cyan">4.2</span></div>
            </div>
            <div style="display: flex; gap: 20px; font-family: Orbitron, sans-serif; font-size: 13px; font-weight: 700;">
                <div><span style="color: var(--text-muted) !important;">Auth:</span> <span style="color: var(--neon-cyan) !important;">ADMIN_01</span></div>
                <div><span class="status-badge status-online" style="padding: 3px 10px; font-size: 10px; height: auto;"><span class="live-dot" style="width:6px; height:6px;"></span> CORE ONLINE</span></div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Hero
    st.markdown('''
    <div class="hero-main">
        <div class="hero-badge"><span class="live-dot"></span> AI-Powered Fitness Intelligence</div>
        <div class="hero-title">Build Muscle. Burn Fat.<br><span class="grad-main">Train Smarter with AI.</span></div>
        <p class="hero-sub">
            The ultimate animated fitness platform with AI coach, workout generator, smart diet planner,
            calorie predictor, progress analytics, and achievement system — all working offline, no API needed.
        </p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Metric cards
    m1, m2, m3, m4, m5 = st.columns(5)
    metrics = [
        ("🔥", "2,450", "Daily Calories", "+12%", True, "grad-fire"),
        ("🏋️", "18", "Workouts/Month", "+3", True, "grad-cyan-pink"),
        ("💪", "92%", "Muscle Score", "+5%", True, "grad-green-cyan"),
        ("🥗", "165g", "Protein/Day", "+15g", True, "grad-main"),
        ("😴", "7.5h", "Avg Sleep", "+0.5h", True, "grad-cyan-pink"),
    ]
    for i, (col, (icon, val, label, change, is_up, grad)) in enumerate(zip([m1,m2,m3,m4,m5], metrics)):
        with col:
            st.markdown(f'''
            <div class="glass metric-box d{i+1}">
                <span class="metric-icon">{icon}</span>
                <div class="metric-val {grad}">{val}</div>
                <div class="metric-label">{label}</div>
                <span class="metric-change {'change-up' if is_up else 'change-down'}">
                    {'↑' if is_up else '↓'} {change}
                </span>
            </div>
            ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════
    # SINGULARITY DIAGNOSTICS SECTION
    # ════════════════════════════════════════════════════════════════
    st.markdown('<div class="sec-title">🔱 <span class="grad-rainbow">Singularity Neural Core Diagnostics</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Real-time synaptic mapping of global intelligence & fitness clusters</div>', unsafe_allow_html=True)
    
    diag_col1, diag_col2, diag_col3 = st.columns([4, 5, 4])
    
    with diag_col1:
        st.markdown('''
        <div class="glass" style="min-height: 250px; padding: 22px;">
            <div style="font-family: Space Grotesk, sans-serif; font-weight: 800; font-size: 16px; margin-bottom: 14px; color: var(--neon-cyan) !important;">⚡ SYSTEM LOAD GAUGES</div>
            <div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="text-align: center; width: 45%;">
                    <svg width="60" height="60" style="transform: rotate(-90deg);">
                        <circle cx="30" cy="30" r="24" fill="none" stroke="rgba(255,255,255,0.04)" stroke-width="4"/>
                        <circle cx="30" cy="30" r="24" fill="none" stroke="var(--neon-green)" stroke-width="4"
                                stroke-dasharray="150" stroke-dashoffset="30"
                                style="filter: drop-shadow(0 0 6px var(--neon-green));"/>
                    </svg>
                    <div style="font-family: Orbitron, sans-serif; font-size: 12px; font-weight: 900; margin-top: -42px; margin-bottom: 28px; color: #FFFFFF !important;">80%</div>
                    <div style="font-size: 9px; color: var(--text-muted) !important; font-weight: 800; text-transform: uppercase;">CPU LOAD</div>
                </div>
                <div style="text-align: center; width: 45%;">
                    <svg width="60" height="60" style="transform: rotate(-90deg);">
                        <circle cx="30" cy="30" r="24" fill="none" stroke="rgba(255,255,255,0.04)" stroke-width="4"/>
                        <circle cx="30" cy="30" r="24" fill="none" stroke="var(--neon-cyan)" stroke-width="4"
                                stroke-dasharray="150" stroke-dashoffset="84"
                                style="filter: drop-shadow(0 0 6px var(--neon-cyan));"/>
                    </svg>
                    <div style="font-family: Orbitron, sans-serif; font-size: 12px; font-weight: 900; margin-top: -42px; margin-bottom: 28px; color: #FFFFFF !important;">44%</div>
                    <div style="font-size: 9px; color: var(--text-muted) !important; font-weight: 800; text-transform: uppercase;">GPU LOAD</div>
                </div>
                <div style="text-align: center; width: 45%; margin-top: 10px;">
                    <svg width="60" height="60" style="transform: rotate(-90deg);">
                        <circle cx="30" cy="30" r="24" fill="none" stroke="rgba(255,255,255,0.04)" stroke-width="4"/>
                        <circle cx="30" cy="30" r="24" fill="none" stroke="var(--neon-pink)" stroke-width="4"
                                stroke-dasharray="150" stroke-dashoffset="12"
                                style="filter: drop-shadow(0 0 6px var(--neon-pink));"/>
                    </svg>
                    <div style="font-family: Orbitron, sans-serif; font-size: 12px; font-weight: 900; margin-top: -42px; margin-bottom: 28px; color: #FFFFFF !important;">92%</div>
                    <div style="font-size: 9px; color: var(--text-muted) !important; font-weight: 800; text-transform: uppercase;">SYNAP MEM</div>
                </div>
                <div style="text-align: center; width: 45%; margin-top: 10px;">
                    <svg width="60" height="60" style="transform: rotate(-90deg);">
                        <circle cx="30" cy="30" r="24" fill="none" stroke="rgba(255,255,255,0.04)" stroke-width="4"/>
                        <circle cx="30" cy="30" r="24" fill="none" stroke="var(--neon-orange)" stroke-width="4"
                                stroke-dasharray="150" stroke-dashoffset="108"
                                style="filter: drop-shadow(0 0 6px var(--neon-orange));"/>
                    </svg>
                    <div style="font-family: Orbitron, sans-serif; font-size: 12px; font-weight: 900; margin-top: -42px; margin-bottom: 28px; color: #FFFFFF !important;">28%</div>
                    <div style="font-size: 9px; color: var(--text-muted) !important; font-weight: 800; text-transform: uppercase;">RCQL RATE</div>
                </div>
            </div>
            <div style="margin-top: 15px; font-size: 11px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-weight: 700; color: var(--text-secondary) !important;">SYNAPTIC COHERENCE</span>
                    <span style="font-weight: 900; color: var(--neon-cyan) !important;">93.2%</span>
                </div>
                <div class="progress-wrap" style="height: 6px; margin: 0 0 10px 0;">
                    <div class="progress-fill" style="width: 93.2%; background: var(--neon-cyan);"></div>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-weight: 700; color: var(--text-secondary) !important;">TEMPORAL ALIGNMENT</span>
                    <span style="font-weight: 900; color: var(--neon-green) !important;">100%</span>
                </div>
                <div class="progress-wrap" style="height: 6px; margin: 0;">
                    <div class="progress-fill" style="width: 100%; background: var(--neon-green);"></div>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
    with diag_col2:
        st.markdown('''
        <div class="glass" style="min-height: 250px; padding: 22px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
                <div style="font-family: Space Grotesk, sans-serif; font-weight: 800; font-size: 16px; color: var(--neon-pink) !important;">⚠️ PREDICTIVE ANOMALY LOG</div>
                <span class="tag tag-pink" style="animation: pulse 1.5s infinite; font-size: 10px; height: auto;">MONITORING</span>
            </div>
            <div style="background: rgba(3,7,18,0.7); border: 1px solid var(--border-glow); border-radius: 16px; padding: 14px; height: 196px; overflow-y: auto; font-family: monospace; font-size: 11px; line-height: 1.5; color: #a5b4fc !important;">
                <div style="color: #a5b4fc;"><span style="color: #6366f1;">[14:22:01]</span> <strong style="color:#00F5FF;">NEXUS_SYNC ::</strong> Packet loss detected in Sector 7-G. Self-healing protocols engaged... <span style="color: #39FF14;">[RESOLVED]</span></div>
                <div style="color: #ff3366;"><span style="color: #ff3366;">[14:22:03]</span> <strong>ALERT ::</strong> Predictive model 0.98 accuracy confirmed for anomaly cluster ALPHA. Initiating counter-measures.</div>
                <div style="color: #3b82f6;"><span style="color: #3b82f6;">[14:22:35]</span> <strong>SYS ::</strong> Entropy levels within normal parameters (0.0831%). Global sync verified.</div>
                <div style="color: #ffb800;"><span style="color: #ffb800;">[14:22:45]</span> <strong>WARNING ::</strong> Memory fragmentation detected in Neural Core 01. Garbage collection starting...</div>
                <div style="color: #39ff14;"><span style="color: #39ff14;">[14:23:10]</span> <strong>CRON ::</strong> Hydration sync active. Synaptic latency at 0.04ms.</div>
                <div style="color: #e2e8f0;"><span style="color: #94a3b8;">[14:23:42]</span> <strong>LOG ::</strong> User Harsh Singh completed core authentication block. Session token refreshed.</div>
                <div style="color: #a855f7;"><span style="color: #a855f7;">[14:24:18]</span> <strong>RAG ::</strong> Fragment_7B correlation confirmed for high-frequency trading indices. Match rate 98.2%.</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
    with diag_col3:
        st.markdown('''
        <div class="glass" style="min-height: 250px; padding: 22px;">
            <div style="font-family: Space Grotesk, sans-serif; font-weight: 800; font-size: 16px; margin-bottom: 14px; color: var(--neon-green) !important;">💬 SYNAPTIC FLUX STREAM</div>
            <div style="background: rgba(3,7,18,0.7); border: 1px solid var(--border-glow); border-radius: 16px; padding: 14px; height: 196px; overflow-y: auto; font-family: monospace; font-size: 11px; line-height: 1.5; color: var(--neon-cyan) !important; text-shadow: 0 0 4px rgba(0,245,255,0.2);">
                <div>0xC7&nbsp;&nbsp;62 64 AB 22 A1 F8 1F 6F</div>
                <div>0x98&nbsp;&nbsp;97 3C 9E 94 F3 A6 27 0C</div>
                <div>0x188&nbsp;E2 FA ED 7E 8C 83 E4 A0</div>
                <div>0x356&nbsp;81 18 34 A9 B4 FF 1D D6</div>
                <div>0x14A&nbsp;E7 70 1A 39 7A 52 C1 D3</div>
                <div>0x297&nbsp;6D 58 5D 86 FC 39 42 77</div>
                <div>0x31A&nbsp;7F 6F A4 BD 50 C8 CB F9</div>
                <div>0x10F&nbsp;2B 36 64 15 E2 9D 5D 32</div>
                <div>0x5D&nbsp;&nbsp;8E E2 D6 1C 7C C6 47 D6</div>
                <div>0x9C&nbsp;&nbsp;CD 64 98 97 0F 13 D9 F9</div>
                <div>0xF2&nbsp;&nbsp;15 B6 82 03 14 81 03 36</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)

    # Feature grid
    st.markdown('<div class="sec-title">🚀 <span class="grad-main">AI Fitness Features</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Every feature is separated, animated, and portfolio-ready</div>', unsafe_allow_html=True)

    fc1, fc2, fc3 = st.columns(3)
    features = [
        ("🤖", "AI Coach Chat", "Ask any fitness question and get detailed, intelligent answers instantly. Works 100% offline!", "linear-gradient(135deg, rgba(0,245,255,0.15), rgba(168,85,247,0.10))", "d1"),
        ("🏋️", "Workout Generator", "AI creates personalized workout plans based on your goal, experience, and target muscles.", "linear-gradient(135deg, rgba(255,43,214,0.15), rgba(255,51,102,0.10))", "d2"),
        ("🥗", "Smart Diet Planner", "Complete meal plans with macro calculations, calories, and meal timing.", "linear-gradient(135deg, rgba(57,255,20,0.15), rgba(0,245,255,0.10))", "d3"),
        ("🔥", "Calorie Predictor", "ML-based calorie burn estimation using weight, duration, and intensity.", "linear-gradient(135deg, rgba(255,184,0,0.15), rgba(255,51,102,0.10))", "d4"),
        ("📊", "Progress Analytics", "Beautiful animated charts tracking calories, protein, weight, and performance.", "linear-gradient(135deg, rgba(168,85,247,0.15), rgba(0,245,255,0.10))", "d5"),
        ("🏆", "Achievements", "Gamified fitness with badges, streaks, and milestone rewards.", "linear-gradient(135deg, rgba(255,184,0,0.15), rgba(255,43,214,0.10))", "d6"),
    ]
    for i, (icon, title, desc, bg, delay) in enumerate(features):
        col = [fc1, fc2, fc3][i % 3]
        with col:
            st.markdown(f'''
            <div class="glass feat-card {delay}">
                <div class="feat-icon-wrap" style="background: {bg};">{icon}</div>
                <div class="feat-title">{title}</div>
                <div class="feat-desc">{desc}</div>
            </div>
            ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Image cards
    st.markdown('<div class="sec-title">🏋️ <span class="grad-cyan-pink">Training Zones</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Visual workout categories with stunning imagery</div>', unsafe_allow_html=True)

    ic1, ic2, ic3, ic4 = st.columns(4)
    images = [
        ("💥 Chest & Push", "https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=800&q=80",
         "background: rgba(0,245,255,0.15); color: #00F5FF !important; border: 1px solid rgba(0,245,255,0.4);"),
        ("🔱 Back & Pull", "https://images.unsplash.com/photo-1605296867304-46d5465a13f1?w=800&q=80",
         "background: rgba(168,85,247,0.15); color: #A855F7 !important; border: 1px solid rgba(168,85,247,0.4);"),
        ("🦵 Legs & Power", "https://images.unsplash.com/photo-1534368959876-26bf04f2c947?w=800&q=80",
         "background: rgba(255,43,214,0.15); color: #FF2BD6 !important; border: 1px solid rgba(255,43,214,0.4);"),
        ("⚡ HIIT & Cardio", "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=800&q=80",
         "background: rgba(57,255,20,0.15); color: #39FF14 !important; border: 1px solid rgba(57,255,20,0.4);"),
    ]
    for i, (col, (title, img, badge_style)) in enumerate(zip([ic1,ic2,ic3,ic4], images)):
        with col:
            st.markdown(f'''
            <div class="img-card d{i+1}" style="background-image: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.75) 100%), url('{img}');">
                <div class="img-card-badge" style="{badge_style}">Explore →</div>
                <div class="img-card-title">{title}</div>
            </div>
            ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Performance chart + Water Tracker + AI Insights
    chart_col, tracker_col, insight_col = st.columns([3, 2, 2])

    with chart_col:
        st.markdown('<div class="sec-title" style="font-size: 24px;">📈 <span class="grad-green-cyan">Weekly Performance</span></div>', unsafe_allow_html=True)

        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        vals = [45, 72, 88, 65, 92, 78, 95]
        colors_list = [colors['cyan'], colors['green'], colors['purple'], colors['orange'], colors['pink'], colors['red'], colors['cyan']]

        bars_html = ""
        for i, (d, v, c) in enumerate(zip(days, vals, colors_list)):
            bars_html += f'''
            <div class="bar-item d{i+1}" style="height:{v}%; background: linear-gradient(180deg, {c}, {c}44);">
                <span class="bar-value">{v}%</span>
                <span class="bar-label">{d}</span>
            </div>'''

        st.markdown(f'''
        <div class="glass">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <div>
                    <div style="font-weight: 800; font-size: 16px;">Workout Intensity</div>
                    <div style="color: var(--text-muted) !important; font-size: 13px;">Last 7 days</div>
                </div>
                <span class="tag tag-green">+18% ↑</span>
            </div>
            <div class="bars-container">{bars_html}</div>
        </div>
        ''', unsafe_allow_html=True)

    with tracker_col:
        st.markdown('<div class="sec-title" style="font-size: 24px;">💧 <span class="grad-main">Hydration</span></div>', unsafe_allow_html=True)
        
        water_ml = st.session_state.water_ml
        water_pct = min(100, int((water_ml / 3000) * 100))
        
        water_html = f'''
        <div class="glass" style="height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <div>
                    <div style="font-weight: 800; font-size: 16px;">Water Log</div>
                    <div style="color: var(--text-muted) !important; font-size: 13px;">Goal: 3.0L</div>
                </div>
                <span class="tag tag-cyan">{water_pct}%</span>
            </div>
            
            <div style="display: flex; align-items: center; justify-content: center; margin: 8px 0; position: relative; height: 110px;">
                <div style="width: 75px; height: 100px; border: 3px solid var(--neon-cyan); border-top: none; border-radius: 0 0 16px 16px; position: relative; overflow: hidden; background: rgba(255,255,255,0.03); box-shadow: 0 0 15px rgba(0,245,255,0.15);">
                    <div style="position: absolute; bottom: 0; left: 0; right: 0; height: {water_pct}%; background: linear-gradient(180deg, var(--neon-cyan), var(--neon-blue)); transition: height 0.6s ease-in-out; border-radius: 0 0 12px 12px; box-shadow: inset 0 2px 8px rgba(255,255,255,0.4);">
                        <div style="position: absolute; top: -5px; left: 0; width: 200%; height: 10px; background: rgba(255,255,255,0.15); border-radius: 50%; transform: translateX(-25%); animation: float 3s infinite ease-in-out;"></div>
                    </div>
                </div>
                <div style="position: absolute; font-family: 'Orbitron', sans-serif; font-size: 14px; font-weight: 900; color: #ffffff; text-shadow: 0 2px 4px rgba(0,0,0,0.8); z-index: 2;">
                    {water_ml} ml
                </div>
            </div>
            
            <div style="text-align: center; font-size: 11px; color: var(--text-muted) !important; font-weight: 700; margin-bottom: 4px;">
                Quick Add Intake:
            </div>
        </div>
        '''
        st.markdown(water_html, unsafe_allow_html=True)
        
        wc1, wc2 = st.columns(2)
        with wc1:
            if st.button("➕ 250ml", key="add_water_ml", use_container_width=True):
                st.session_state.water_ml = min(5000, st.session_state.water_ml + 250)
                st.rerun()
        with wc2:
            if st.button("➖ 250ml", key="sub_water_ml", use_container_width=True):
                st.session_state.water_ml = max(0, st.session_state.water_ml - 250)
                st.rerun()

    with insight_col:
        st.markdown('<div class="sec-title" style="font-size: 24px;">🧠 <span class="grad-fire">AI Insights</span></div>', unsafe_allow_html=True)

        insights = [
            ("🔥", "Peak Performance", "Thursday had highest intensity — keep progressive overload going!"),
            ("📈", "Volume Trend", "Weekly volume up 18% — great consistency this month!"),
            ("💡", "Recovery Alert", "Consider a deload week next week to prevent overtraining."),
            ("🎯", "Protein Goal", "You're 15g short of daily protein target — add a shake!"),
        ]
        for i, (icon, title, desc) in enumerate(insights):
            st.markdown(f'''
            <div class="notif d{i+1}">
                <div class="notif-icon" style="background: rgba(0,245,255,0.08); font-size: 26px;">{icon}</div>
                <div>
                    <div class="notif-title">{title}</div>
                    <div class="notif-desc">{desc}</div>
                </div>
            </div>
            ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Activity Timeline
    st.markdown('<div class="sec-title">🕐 <span class="grad-cyan-pink">Recent Activity</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Your latest fitness events and milestones</div>', unsafe_allow_html=True)

    tc1, tc2 = st.columns(2)
    activities = [
        ("2 min ago", "🏋️ <strong>Chest Workout</strong> completed — 45 min, 520 kcal burned", "d1"),
        ("1 hr ago", "🥗 <strong>Meal Logged</strong> — Lunch: 650 kcal, 45g protein", "d2"),
        ("3 hrs ago", "🔥 <strong>HIIT Session</strong> — 20 min, 380 kcal burned", "d3"),
        ("6 hrs ago", "🤖 <strong>AI Coach</strong> — Generated leg day workout plan", "d4"),
        ("Yesterday", "📊 <strong>Progress Update</strong> — Body weight: 72.5 kg (-0.3)", "d5"),
        ("2 days ago", "🏆 <strong>Achievement</strong> — 30-day streak unlocked!", "d6"),
    ]
    for i, (time_str, text, delay) in enumerate(activities):
        col = tc1 if i < 3 else tc2
        with col:
            st.markdown(f'''
            <div class="timeline-item {delay}">
                <div>
                    <div class="timeline-time">{time_str}</div>
                    <div class="timeline-text">{text}</div>
                </div>
            </div>
            ''', unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Dashboard AI Chat
    st.markdown('<div class="sec-title">🤖 <span class="grad-main">Quick AI Coach</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Ask anything right from the dashboard</div>', unsafe_allow_html=True)
    render_chat("dashboard")


# ════════════════════════════════════════════════════════════════
# PAGE: AI COACH
# ════════════════════════════════════════════════════════════════
elif page == "🤖 AI Coach":
    st.markdown('''
    <div class="hero-main" style="padding: 36px 42px;">
        <div class="hero-title" style="font-size: 48px;">Your Personal <span class="grad-main">AI Fitness Coach</span></div>
        <p class="hero-sub">Ask about chest, back, legs, shoulders, arms, abs, diet, fat loss, calories, supplements, recovery, stretching — I know it all! 💪</p>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Extra quick buttons row
    st.markdown('<div class="sec-title" style="font-size: 22px;">⚡ Quick Topics</div>', unsafe_allow_html=True)
    r1, r2, r3, r4 = st.columns(4)
    extra_quick = [
        (r1, "🔱 Shoulders", "shoulder workout"),
        (r2, "💪 Arms", "arm workout bicep tricep"),
        (r3, "🔥 Abs/Core", "abs core workout"),
        (r4, "💊 Supplements", "supplement guide"),
    ]
    for col, label, prompt in extra_quick:
        if col.button(label, key=f"eq_{label}", use_container_width=True):
            if "msgs_coach" not in st.session_state:
                st.session_state.msgs_coach = [("AI", "Ready to help!")]
            st.session_state.msgs_coach.append(("You", prompt))
            st.session_state.msgs_coach.append(("AI", ai_reply(prompt)))
            st.session_state.total_queries += 1
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    render_chat("coach")


# ════════════════════════════════════════════════════════════════
# PAGE: WORKOUT GENERATOR
# ════════════════════════════════════════════════════════════════
elif page == "🏋️ Workout Generator":
    st.markdown('''
    <div class="hero-main" style="padding: 36px 42px;">
        <div class="hero-title" style="font-size: 48px;">🏋️ <span class="grad-cyan-pink">AI Workout Generator</span></div>
        <p class="hero-sub">Select your goal, experience level, and target — AI creates your perfect training plan!</p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Image cards
    ic1, ic2, ic3 = st.columns(3)
    workout_imgs = [
        ("🏋️ Strength Zone", "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=800&q=80", "d1"),
        ("💪 Hypertrophy Lab", "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?w=800&q=80", "d2"),
        ("🔥 HIIT Arena", "https://images.unsplash.com/photo-1549060279-7e168fcee0c2?w=800&q=80", "d3"),
    ]
    for col, (title, img, delay) in zip([ic1,ic2,ic3], workout_imgs):
        with col:
            st.markdown(f'''
            <div class="img-card {delay}" style="background-image: linear-gradient(180deg, rgba(0,0,0,0.05), rgba(0,0,0,0.78)), url('{img}');">
                <div class="img-card-title">{title}</div>
            </div>
            ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Config
    cfg1, cfg2, cfg3 = st.columns(3)
    with cfg1:
        goal = st.selectbox("🎯 Goal", ["Muscle Gain", "Fat Loss", "Strength", "Athletic Performance", "Beginner Fitness"])
    with cfg2:
        level = st.selectbox("📊 Level", ["Beginner", "Intermediate", "Advanced", "Elite"])
    with cfg3:
        days = st.selectbox("📅 Training Days", ["3 Days/Week", "4 Days/Week", "5 Days/Week", "6 Days/Week"])

    focus = st.multiselect("🎯 Focus Areas", ["Chest", "Back", "Legs", "Shoulders", "Arms", "Core", "Full Body"], default=["Full Body"])

    if st.button("🚀 Generate AI Workout Plan", use_container_width=True):
        st.session_state.workouts_done += 1

        # Loading animation
        progress_ph = st.empty()
        steps = ["🔍 Analyzing your profile...", "🧠 AI designing split...", "💪 Selecting exercises...", "⚡ Optimizing volume...", "✨ Finalizing plan..."]
        for i, step in enumerate(steps):
            progress_ph.markdown(f'''
            <div class="glass" style="text-align: center; padding: 20px;">
                <div style="color: var(--neon-cyan) !important; font-weight: 800; animation: pulse 1s infinite;">{step}</div>
                <div class="progress-wrap" style="margin-top: 12px;">
                    <div class="progress-fill" style="width: {(i+1)*20}%;"></div>
                </div>
            </div>
            ''', unsafe_allow_html=True)
            time.sleep(0.3)
        progress_ph.empty()

        # Result
        st.markdown(f'''
        <div class="glass" style="animation: scaleIn 0.6s ease-out;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
                <div>
                    <div style="font-family: Space Grotesk, sans-serif; font-size: 28px; font-weight: 900;">
                        <span class="grad-main">{goal} Program — {level}</span>
                    </div>
                    <div style="color: var(--text-secondary) !important; font-weight: 700;">{days} • Focus: {", ".join(focus)}</div>
                </div>
                <span class="tag tag-green" style="font-size: 14px; padding: 8px 18px;">AI Generated ✅</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)

        # Determine the routines dynamically
        workout_plan = []
        num_days = int(days.split()[0])
        
        # Build split days based on frequency
        if num_days == 3:
            split_days = [
                ("DAY 1", "🟢 Full Body A", ["Squats|4×8", "Bench Press|4×10", "Lat Pulldowns|3×12", "OHP|3×10", "Bicep Curls|3×12", "Plank|3×60s"]),
                ("DAY 2", "🟢 Full Body B", ["Deadlift|3×5", "Incline DB Press|4×10", "Barbell Rows|4×8", "Lateral Raises|3×15", "Tricep Pushdowns|3×12", "Leg Raises|3×15"]),
                ("DAY 3", "🟢 Full Body C", ["Leg Press|4×12", "Pull-ups|4×Max", "Cable Flyes|3×12", "Rear Delt Flyes|3×15", "Hammer Curls|3×12", "Russian Twists|3×20"])
            ]
        elif num_days == 4:
            split_days = [
                ("DAY 1", "💪 Upper Body A", ["Bench Press|4×8", "Barbell Rows|4×10", "Dumbbell Press|3×12", "Skullcrushers|3×12", "Hammer Curls|3×12"]),
                ("DAY 2", "🦵 Lower Body A", ["Squats|4×8", "RDLs|4×10", "Leg Extensions|3×15", "Lying Leg Curls|3×12", "Calf Raises|4×20"]),
                ("DAY 3", "💪 Upper Body B", ["Incline DB Press|4×10", "Pull-ups|4×Max", "Lateral Raises|4×15", "Face Pulls|3×15", "Cable Curls|3×15"]),
                ("DAY 4", "🦵 Lower Body B & Core", ["Deadlifts|3×5", "Leg Press|4×12", "Lunges|3×10", "Plank|3×60s", "Hanging Knee Raises|3×15"])
            ]
        elif num_days == 5:
            split_days = [
                ("DAY 1", "💥 Chest Day", ["Bench Press|4×8", "Incline DB Press|4×10", "Decline Bench Press|3×10", "Cable Flyes|3×15", "Pushups|3×Max"]),
                ("DAY 2", "🔱 Back Day", ["Pull-ups|4×Max", "Barbell Rows|4×8", "Lat Pulldowns|4×12", "Seated Cable Rows|3×12", "Straight Arm Pulldowns|3×15"]),
                ("DAY 3", "🦵 Leg Day", ["Squats|4×8", "Leg Press|4×12", "Romanian Deadlift|4×10", "Leg Curls|3×15", "Standing Calf Raises|4×20"]),
                ("DAY 4", "🔱 Shoulder Day", ["OHP|4×8", "Arnold Press|3×12", "Lateral Raises|4×15", "Face Pulls|3×15", "Rear Delt Flyes|3×15"]),
                ("DAY 5", "💪 Arms & Core", ["Close-Grip Bench|4×10", "Barbell Curls|4×10", "Skullcrushers|3×12", "Hammer Curls|3×12", "Plank|3×60s"])
            ]
        else: # 6 days
            split_days = [
                ("DAY 1", "🔥 Push A", ["Bench Press|4×8", "Overhead Press|4×10", "Incline Flyes|3×12", "Skullcrushers|3×12", "Tricep Pushdowns|3×15"]),
                ("DAY 2", "🔱 Pull A", ["Barbell Rows|4×8", "Pull-ups|4×Max", "Face Pulls|3×15", "Barbell Curls|3×10", "Hammer Curls|3×12"]),
                ("DAY 3", "🦵 Legs A", ["Squats|4×8", "RDLs|4×10", "Leg Extensions|3×15", "Calf Raises|4×20"]),
                ("DAY 4", "🔥 Push B", ["Incline DB Press|4×10", "Arnold Press|3×12", "Cable Crossovers|3×15", "Dips|3×12", "Overhead Tricep Extensions|3×15"]),
                ("DAY 5", "🔱 Pull B", ["Deadlifts|3×5", "Wide Lat Pulldowns|4×12", "Seated Row|3×12", "Preacher Curls|3×12", "Russian Twists|3×20"]),
                ("DAY 6", "🦵 Legs B & Core", ["Leg Press|4×12", "Lunges|3×10", "Leg Curls|3×15", "Plank|3×60s", "Hanging Leg Raises|3×15"])
            ]

        # Adjust sets based on level
        sets_mod = 0
        if level == "Beginner":
            sets_mod = -1
        elif level in ["Advanced", "Elite"]:
            sets_mod = 1
            
        # Customize plans based on Goal and Focus Areas
        for d_id, split_name, exercises in split_days:
            formatted_split_name = split_name
            if goal == "Fat Loss":
                formatted_split_name = split_name.replace("Day", "Fat Burn").replace("Body", "HIIT").replace("Push", "Circuit Push").replace("Pull", "Circuit Pull").replace("Legs", "Leg Burnout")
            elif goal == "Strength":
                formatted_split_name = split_name.replace("Body", "Power").replace("Chest", "Bench Focus").replace("Leg", "Squat Focus").replace("Back", "Deadlift Focus").replace("Push", "Bench/OHP Focus")
            elif goal == "Athletic Performance":
                formatted_split_name = split_name.replace("Day", "Conditioning").replace("Body", "Explosive").replace("Arms", "Speed & Power")
            
            formatted_exercises = []
            for ex in exercises:
                name, sets_reps = ex.split('|')
                sets, reps = sets_reps.split('×')
                
                num_sets = max(2, min(5, int(sets) + sets_mod))
                
                if goal == "Fat Loss":
                    if reps.isdigit():
                        reps = str(int(int(reps) * 1.25))
                    formatted_exercises.append(f"{name} {num_sets}×{reps} (HIIT Pace)")
                elif goal == "Strength":
                    if reps.isdigit():
                        reps = str(max(3, int(int(reps) * 0.6)))
                    formatted_exercises.append(f"{name} {num_sets}×{reps} (Heavy - 3m rest)")
                elif goal == "Athletic Performance":
                    formatted_exercises.append(f"{name} {num_sets}×{reps} (Explosive)")
                else:
                    formatted_exercises.append(f"{name} {num_sets}×{reps}")
            
            # Filter by Focus Areas if "Full Body" is not selected
            if "Full Body" not in focus:
                filtered_exercises = []
                for ex_str in formatted_exercises:
                    matched = False
                    for f_muscle in focus:
                        f_lower = f_muscle.lower()
                        if f_lower == "chest" and any(x in ex_str.lower() for x in ["bench", "press", "fly", "pushup", "dip"]): matched = True
                        elif f_lower == "back" and any(x in ex_str.lower() for x in ["row", "pull", "deadlift", "chin"]): matched = True
                        elif f_lower == "legs" and any(x in ex_str.lower() for x in ["squat", "press", "rdl", "curl", "extension", "lunge", "calf"]): matched = True
                        elif f_lower == "shoulders" and any(x in ex_str.lower() for x in ["ohp", "press", "lateral", "raise", "delt", "shrug", "arnold"]): matched = True
                        elif f_lower == "arms" and any(x in ex_str.lower() for x in ["curl", "skullcrusher", "pushdown", "dip", "extension"]): matched = True
                        elif f_lower == "core" and any(x in ex_str.lower() for x in ["plank", "raise", "crunch", "rollout", "twist"]): matched = True
                    
                    if matched or any(x in ex_str.lower() for x in ["bench press", "barbell squat", "deadlift", "overhead press"]):
                        filtered_exercises.append(ex_str)
                if not filtered_exercises:
                    filtered_exercises = formatted_exercises
                workout_plan.append((d_id, formatted_split_name, " • ".join(filtered_exercises)))
            else:
                workout_plan.append((d_id, formatted_split_name, " • ".join(formatted_exercises)))

        for i, (day, muscle, exercises) in enumerate(workout_plan):
            st.markdown(f'''
            <div class="split-card d{i+1}">
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <div>
                        <div class="split-day">{day}</div>
                        <div class="split-muscle">{muscle}</div>
                        <div class="split-exercises">{exercises}</div>
                    </div>
                    <div style="font-size: 36px; animation: float 3s infinite ease-in-out;">{muscle.split()[0]}</div>
                </div>
            </div>
            ''', unsafe_allow_html=True)

        # Intensity score
        intensity = random.randint(82, 97)
        st.markdown(f'''
        <div class="glass" style="text-align: center; padding: 24px; margin-top: 16px;">
            <div style="font-family: Space Grotesk, sans-serif; font-size: 18px; font-weight: 800; margin-bottom: 8px;">
                AI Intensity Score
            </div>
            <div class="progress-wrap" style="max-width: 500px; margin: 0 auto;">
                <div class="progress-fill" style="width: {intensity}%;"></div>
            </div>
            <div style="font-family: Orbitron, sans-serif; font-size: 32px; font-weight: 900; margin-top: 12px;">
                <span class="grad-fire">{intensity}%</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
# PAGE: DIET PLANNER
# ════════════════════════════════════════════════════════════════
elif page == "🥗 Diet Planner":
    st.markdown('''
    <div class="hero-main" style="padding: 36px 42px;">
        <div class="hero-title" style="font-size: 48px;">🥗 <span class="grad-green-cyan">Smart Diet Planner</span></div>
        <p class="hero-sub">AI-calculated meal plans with precise macros, calories, and meal timing for your goals</p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    d1, d2, d3 = st.columns(3)
    with d1:
        weight = st.number_input("⚖️ Weight (kg)", 40, 150, 72)
    with d2:
        height = st.number_input("📏 Height (cm)", 140, 220, 175)
    with d3:
        diet_goal = st.selectbox("🎯 Goal", ["Muscle Gain (+300 kcal)", "Fat Loss (-400 kcal)", "Maintenance", "Lean Bulk (+200 kcal)"])

    activity = st.selectbox("🏃 Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Athlete"])

    # Calculate macros
    bmr = int(10 * weight + 6.25 * height - 5 * 25 + 5)
    activity_mult = {"Sedentary": 1.2, "Lightly Active": 1.375, "Moderately Active": 1.55, "Very Active": 1.725, "Athlete": 1.9}
    tdee = int(bmr * activity_mult.get(activity, 1.55))

    if "Gain" in diet_goal:
        calories = tdee + 300
    elif "Loss" in diet_goal:
        calories = tdee - 400
    elif "Lean" in diet_goal:
        calories = tdee + 200
    else:
        calories = tdee

    protein = int(weight * 2.0)
    fats = int(weight * 0.9)
    carbs = int((calories - protein * 4 - fats * 9) / 4)

    if st.button("🧠 Generate AI Diet Plan", use_container_width=True):
        with st.spinner(""):
            time.sleep(0.5)

        # Macro summary
        st.markdown(f'''
        <div class="glass" style="animation: scaleIn 0.6s ease-out;">
            <div style="text-align: center; margin-bottom: 24px;">
                <div style="font-family: Space Grotesk, sans-serif; font-size: 32px; font-weight: 900;">
                    Your <span class="grad-main">AI Diet Plan</span>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

        mc1, mc2, mc3, mc4 = st.columns(4)
        macro_data = [
            ("🔥", str(calories), "Total Calories", "grad-fire", "d1"),
            ("🥩", f"{protein}g", "Protein", "grad-green-cyan", "d2"),
            ("🍚", f"{carbs}g", "Carbs", "grad-cyan-pink", "d3"),
            ("🥑", f"{fats}g", "Healthy Fats", "grad-main", "d4"),
        ]
        for col, (icon, val, label, grad, delay) in zip([mc1,mc2,mc3,mc4], macro_data):
            with col:
                st.markdown(f'''
                <div class="glass metric-box {delay}">
                    <span class="metric-icon">{icon}</span>
                    <div class="metric-val {grad}">{val}</div>
                    <div class="metric-label">{label}</div>
                </div>
                ''', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Meal cards
        st.markdown('<div class="sec-title" style="font-size: 24px;">🍽️ <span class="grad-green-cyan">Daily Meal Plan</span></div>', unsafe_allow_html=True)

        # Scale meal portion quantities dynamically based on weight and goal
        w_factor = weight / 70.0
        
        if "Gain" in diet_goal or "Bulk" in diet_goal:
            meals = [
                ("🌅", "Breakfast", f"Oats: {int(100 * w_factor)}g + 300ml whole milk\nWhole Eggs: 3 large + 2 egg whites\nPeanut Butter: 2 tbsp\n1 large banana", f"{int(550 * w_factor)} kcal",
                 "linear-gradient(135deg, rgba(255,184,0,0.12), rgba(255,51,102,0.08))",
                 "background: rgba(255,184,0,0.15); color: #FFB800 !important;", "d1"),
                ("☀️", "Lunch", f"Brown Rice: {int(200 * w_factor)}g (cooked)\nGrilled Chicken: {int(180 * w_factor)}g\nMixed salad with 1 tbsp olive oil\nGreek Yogurt: 150g", f"{int(720 * w_factor)} kcal",
                 "linear-gradient(135deg, rgba(0,245,255,0.12), rgba(57,255,20,0.08))",
                 "background: rgba(57,255,20,0.15); color: #39FF14 !important;", "d2"),
                ("⚡", "Pre/Post WO", f"Whey Protein: 1.5 scoops\nAlmonds: {int(30 * w_factor)}g\nCream of Rice: {int(50 * w_factor)}g (pre-workout)\n1 medium apple", f"{int(450 * w_factor)} kcal",
                 "linear-gradient(135deg, rgba(168,85,247,0.12), rgba(255,43,214,0.08))",
                 "background: rgba(168,85,247,0.15); color: #A855F7 !important;", "d3"),
                ("🌙", "Dinner", f"Sweet Potato: {int(220 * w_factor)}g\nGrilled Salmon / Tofu: {int(180 * w_factor)}g\nSteamed Broccoli / Asparagus: 150g\nOlive oil: 1 tsp", f"{int(680 * w_factor)} kcal",
                 "linear-gradient(135deg, rgba(255,43,214,0.12), rgba(0,245,255,0.08))",
                 "background: rgba(255,43,214,0.15); color: #FF2BD6 !important;", "d4"),
            ]
        elif "Loss" in diet_goal:
            meals = [
                ("🌅", "Breakfast", f"Oats: {int(60 * w_factor)}g + water/skim milk\nEgg Whites: 5 large + 1 whole egg\nSpinach & mushrooms scramble\n1 handful of berries", f"{int(380 * w_factor)} kcal",
                 "linear-gradient(135deg, rgba(255,184,0,0.12), rgba(255,51,102,0.08))",
                 "background: rgba(255,184,0,0.15); color: #FFB800 !important;", "d1"),
                ("☀️", "Lunch", f"Quinoa / Roti: {int(100 * w_factor)}g\nLean Chicken / Tofu: {int(200 * w_factor)}g\nLarge green salad with lemon dressing\nCucumber slices", f"{int(520 * w_factor)} kcal",
                 "linear-gradient(135deg, rgba(0,245,255,0.12), rgba(57,255,20,0.08))",
                 "background: rgba(57,255,20,0.15); color: #39FF14 !important;", "d2"),
                ("⚡", "Pre/Post WO", f"Whey Protein: 1 scoop\nGreek Yogurt (0% fat): 150g\nAlmonds: 10 pieces\n1 cup black coffee", f"{int(280 * w_factor)} kcal",
                 "linear-gradient(135deg, rgba(168,85,247,0.12), rgba(255,43,214,0.08))",
                 "background: rgba(168,85,247,0.15); color: #A855F7 !important;", "d3"),
                ("🌙", "Dinner", f"Cauliflower Rice: 200g\nBaked Fish / Tempeh: {int(200 * w_factor)}g\nSteamed Asparagus & zucchini: 200g\nFlaxseeds: 1 tbsp", f"{int(480 * w_factor)} kcal",
                 "linear-gradient(135deg, rgba(255,43,214,0.12), rgba(0,245,255,0.08))",
                 "background: rgba(255,43,214,0.15); color: #FF2BD6 !important;", "d4"),
            ]
        else:
            meals = [
                ("🌅", "Breakfast", f"Oats: {int(80 * w_factor)}g + 200ml low-fat milk\nWhole Eggs: 2 large + 2 egg whites\nHandful of mixed nuts (15g)\n1 banana", f"{int(460 * w_factor)} kcal",
                 "linear-gradient(135deg, rgba(255,184,0,0.12), rgba(255,51,102,0.08))",
                 "background: rgba(255,184,0,0.15); color: #FFB800 !important;", "d1"),
                ("☀️", "Lunch", f"Brown Rice: {int(150 * w_factor)}g\nChicken / Paneer: {int(160 * w_factor)}g\nGreen salad with olive oil (1 tsp)\n1 medium fruit", f"{int(620 * w_factor)} kcal",
                 "linear-gradient(135deg, rgba(0,245,255,0.12), rgba(57,255,20,0.08))",
                 "background: rgba(57,255,20,0.15); color: #39FF14 !important;", "d2"),
                ("⚡", "Pre/Post WO", f"Whey Protein: 1 scoop\nRice Cakes: 2 with 1 tbsp peanut butter\nAlmonds: 12 pieces", f"{int(350 * w_factor)} kcal",
                 "linear-gradient(135deg, rgba(168,85,247,0.12), rgba(255,43,214,0.08))",
                 "background: rgba(168,85,247,0.15); color: #A855F7 !important;", "d3"),
                ("🌙", "Dinner", f"Sweet Potato: {int(150 * w_factor)}g\nWhite Fish / Tofu: {int(180 * w_factor)}g\nSteamed broccoli & green beans: 150g\nOlive oil: 1 tsp", f"{int(560 * w_factor)} kcal",
                 "linear-gradient(135deg, rgba(255,43,214,0.12), rgba(0,245,255,0.08))",
                 "background: rgba(255,43,214,0.15); color: #FF2BD6 !important;", "d4"),
            ]


        for col, (icon, name, foods, kcal, bg, badge_style, delay) in zip([ml1,ml2,ml3,ml4], meals):
            with col:
                formatted_foods = foods.replace('\n', '<br>')
                st.markdown(f'''
                <div class="glass meal-card {delay}" style="background: {bg};">
                    <div class="meal-icon">{icon}</div>
                    <div class="meal-name">{name}</div>
                    <div class="meal-desc">{formatted_foods}</div>
                    <span class="meal-kcal" style="{badge_style}">{kcal}</span>
                </div>
                ''', unsafe_allow_html=True)

        # Macro progress bars
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f'''
        <div class="glass" style="animation: fadeUp 0.6s ease-out 0.3s both;">
            <div style="font-family: Space Grotesk, sans-serif; font-size: 20px; font-weight: 800; margin-bottom: 16px;">
                📊 Daily Macro Targets
            </div>
            <div style="margin-bottom: 14px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-weight: 800; color: #39FF14 !important;">🥩 Protein</span>
                    <span style="font-weight: 800; color: var(--text-secondary) !important;">{protein}g / {protein}g</span>
                </div>
                <div class="progress-wrap">
                    <div class="progress-fill" style="width: 100%; background: linear-gradient(90deg, #39FF14, #00F5FF);"></div>
                </div>
            </div>
            <div style="margin-bottom: 14px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-weight: 800; color: #00F5FF !important;">🍚 Carbs</span>
                    <span style="font-weight: 800; color: var(--text-secondary) !important;">{carbs}g / {carbs}g</span>
                </div>
                <div class="progress-wrap">
                    <div class="progress-fill" style="width: 85%; background: linear-gradient(90deg, #00F5FF, #A855F7);"></div>
                </div>
            </div>
            <div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-weight: 800; color: #FFB800 !important;">🥑 Fats</span>
                    <span style="font-weight: 800; color: var(--text-secondary) !important;">{fats}g / {fats}g</span>
                </div>
                <div class="progress-wrap">
                    <div class="progress-fill" style="width: 92%; background: linear-gradient(90deg, #FFB800, #FF3366);"></div>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
# PAGE: CALORIE PREDICTOR
# ════════════════════════════════════════════════════════════════
elif page == "🔥 Calorie Predictor":
    st.markdown('''
    <div class="hero-main" style="padding: 36px 42px;">
        <div class="hero-title" style="font-size: 48px;">🔥 <span class="grad-fire">Calorie Burn Predictor</span></div>
        <p class="hero-sub">AI estimates your calorie expenditure based on weight, workout duration, type, and intensity</p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    p1, p2 = st.columns(2)
    with p1:
        cal_weight = st.number_input("⚖️ Your Weight (kg)", 40, 150, 72, key="cal_w")
        cal_minutes = st.slider("⏱️ Workout Duration (minutes)", 10, 180, 45)
    with p2:
        cal_type = st.selectbox("🏋️ Workout Type", [
            "Weight Training", "HIIT", "Running", "Cycling", "Swimming",
            "Jump Rope", "Walking", "Yoga", "CrossFit", "Martial Arts"
        ])
        cal_intensity = st.selectbox("⚡ Intensity Level", ["Low (easy)", "Medium (moderate)", "High (intense)", "Extreme (max effort)"])

    heart_rate = st.slider("❤️ Avg Heart Rate (bpm, optional)", 60, 200, 130)

    if st.button("🔥 Predict Calorie Burn", use_container_width=True):
        # Calculation
        type_mult = {
            "Weight Training": 7, "HIIT": 12, "Running": 10, "Cycling": 8,
            "Swimming": 9, "Jump Rope": 11, "Walking": 4, "Yoga": 3.5,
            "CrossFit": 13, "Martial Arts": 11
        }
        int_mult = {"Low (easy)": 0.7, "Medium (moderate)": 1.0, "High (intense)": 1.3, "Extreme (max effort)": 1.6}

        base = type_mult.get(cal_type, 7)
        intensity_f = int_mult.get(cal_intensity, 1.0)
        hr_bonus = max(0, (heart_rate - 100) * 0.15)
        calories_burned = int(cal_minutes * base * intensity_f * (cal_weight / 70) + hr_bonus * cal_minutes * 0.05)
        fat_grams = round(calories_burned / 7.7, 1)
        afterburn = int(calories_burned * 0.15) if cal_intensity in ["High (intense)", "Extreme (max effort)"] else int(calories_burned * 0.05)

        # Animated result
        progress_ph = st.empty()
        for i in range(0, calories_burned + 1, max(1, calories_burned // 30)):
            progress_ph.markdown(f'''
            <div class="cal-result">
                <div style="font-size: 20px; font-weight: 800; color: var(--text-secondary) !important;">Estimated Calorie Burn</div>
                <div class="cal-number grad-fire">🔥 {i}</div>
                <div class="cal-label">kilocalories</div>
            </div>
            ''', unsafe_allow_html=True)
            time.sleep(0.02)

        progress_ph.markdown(f'''
        <div class="cal-result">
            <div style="font-size: 20px; font-weight: 800; color: var(--text-secondary) !important;">Estimated Calorie Burn</div>
            <div class="cal-number grad-fire">🔥 {calories_burned}</div>
            <div class="cal-label">{cal_minutes} min {cal_type} • {cal_intensity.split("(")[0].strip()} Intensity</div>
            <div class="progress-wrap" style="max-width: 400px; margin: 16px auto;">
                <div class="progress-fill" style="width: {min(100, calories_burned / 10)}%;"></div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Breakdown
        b1, b2, b3 = st.columns(3)
        breakdown = [
            ("🔥", str(calories_burned), "Active Burn", "grad-fire", "d1"),
            ("⚡", str(afterburn), "EPOC Afterburn", "grad-cyan-pink", "d2"),
            ("💧", f"{fat_grams}g", "Fat Equivalent", "grad-green-cyan", "d3"),
        ]
        for col, (icon, val, label, grad, delay) in zip([b1,b2,b3], breakdown):
            with col:
                st.markdown(f'''
                <div class="glass metric-box {delay}">
                    <span class="metric-icon">{icon}</span>
                    <div class="metric-val {grad}">{val}</div>
                    <div class="metric-label">{label}</div>
                </div>
                ''', unsafe_allow_html=True)

        # Food equivalents
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="sec-title" style="font-size: 22px;">🍔 <span class="grad-main">That\'s Equivalent To Burning Off...</span></div>', unsafe_allow_html=True)

        eq1, eq2, eq3, eq4 = st.columns(4)
        equivalents = [
            ("🍕", f"{calories_burned/280:.1f}", "Pizza Slices"),
            ("🍔", f"{calories_burned/350:.1f}", "Burgers"),
            ("🍫", f"{calories_burned/230:.1f}", "Chocolate Bars"),
            ("🥤", f"{calories_burned/140:.1f}", "Cans of Soda"),
        ]
        for col, (icon, val, label) in zip([eq1,eq2,eq3,eq4], equivalents):
            with col:
                st.markdown(f'''
                <div class="glass" style="text-align: center; padding: 20px;">
                    <div style="font-size: 36px; animation: float 3s infinite;">{icon}</div>
                    <div style="font-family: Orbitron, sans-serif; font-size: 28px; font-weight: 900; margin: 8px 0;">
                        <span class="grad-fire">{val}</span>
                    </div>
                    <div style="font-size: 13px; color: var(--text-muted) !important; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">{label}</div>
                </div>
                ''', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
# PAGE: HEART RATE ZONES
# ════════════════════════════════════════════════════════════════
elif page == "❤️ Heart Rate Zones":
    st.markdown('''
    <div class="hero-main" style="padding: 36px 42px;">
        <div class="hero-title" style="font-size: 48px;">❤️ <span class="grad-fire">Heart Rate Zone Targeter</span></div>
        <p class="hero-sub">Enter your details to calculate target heart rate zones for different cardio goals.</p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
        <div class="glass" style="height: 100%;">
            <div style="font-family: Space Grotesk, sans-serif; font-size: 22px; font-weight: 800; margin-bottom: 16px;">📈 Heart Rate Zone Inputs</div>
        ''', unsafe_allow_html=True)
        
        hr_age = st.number_input("👤 Your Age (years)", 10, 100, 25, key="hr_age_widget")
        hr_rhr = st.number_input("❤️ Resting Heart Rate (bpm)", 30, 120, 60, key="hr_rhr_widget")
        
        max_hr = 220 - hr_age
        hrr = max_hr - hr_rhr
        
        st.markdown(f'''
            <div style="margin-top: 24px; padding-top: 16px; border-top: 1px solid var(--border-glow); text-align: center;">
                <div style="font-size: 14px; color: var(--text-muted) !important; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">Calculated Max Heart Rate</div>
                <div style="font-family: Orbitron, sans-serif; font-size: 42px; font-weight: 900; color: var(--neon-red) !important; margin-top: 4px;">{max_hr} bpm</div>
                <div style="font-size: 13px; color: var(--text-secondary) !important; font-weight: 600; margin-top: 6px;">HR Reserve (HRR): {hrr} bpm</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
    with col2:
        st.markdown('''
        <div class="glass" style="height: 100%;">
            <div style="font-family: Space Grotesk, sans-serif; font-size: 22px; font-weight: 800; margin-bottom: 16px;">🔥 Target Training Zones</div>
        ''', unsafe_allow_html=True)
        
        zones = [
            ("Zone 1: Active Recovery", 0.50, 0.60, "Warm-up / Active rest session", "var(--neon-green)"),
            ("Zone 2: Fat Burn", 0.60, 0.70, "Ideal for fat loss & long endurance distance", "var(--neon-cyan)"),
            ("Zone 3: Cardio / Aerobic", 0.70, 0.80, "Build endurance & aerobic fitness capacity", "var(--neon-purple)"),
            ("Zone 4: Anaerobic / Threshold", 0.80, 0.90, "Improve speed, power, and lactate threshold limit", "var(--neon-orange)"),
            ("Zone 5: Peak / Red Line", 0.90, 1.00, "Maximum effort interval sprints / high power", "var(--neon-red)")
        ]
        
        for name, low_f, high_f, desc, glow_color in zones:
            low_val = int(hrr * low_f + hr_rhr)
            high_val = int(hrr * high_f + hr_rhr)
            
            st.markdown(f'''
            <div style="margin-bottom: 14px; padding: 12px 16px; background: rgba(255,255,255,0.02); border-radius: 14px; border-left: 4px solid {glow_color};">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-weight: 800; font-size: 14px; color: white !important;">{name}</span>
                    <span style="font-weight: 900; font-family: Orbitron, sans-serif; color: {glow_color} !important;">{low_val} - {high_val} bpm</span>
                </div>
                <div style="font-size: 12px; color: var(--text-muted) !important; font-weight: 600; margin-bottom: 6px;">{desc}</div>
                <div class="progress-wrap" style="height: 6px; margin: 0;">
                    <div class="progress-fill" style="width: {int((high_val/max_hr)*100)}%; background: {glow_color};"></div>
                </div>
            </div>
            ''', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
# PAGE: PROGRESS TRACKER
# ════════════════════════════════════════════════════════════════
elif page == "📊 Progress Tracker":
    st.markdown('''
    <div class="hero-main" style="padding: 36px 42px;">
        <div class="hero-title" style="font-size: 48px;">📊 <span class="grad-cyan-pink">Progress Analytics</span></div>
        <p class="hero-sub">Track your fitness journey with beautiful animated charts and detailed metrics</p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Weekly summary metrics
    pm1, pm2, pm3, pm4 = st.columns(4)
    progress_metrics = [
        ("📅", "7/7", "Days Active", "change-up", "+2", "grad-green-cyan"),
        ("🔥", "4,850", "Calories Burned", "change-up", "+620", "grad-fire"),
        ("🥩", "980g", "Protein This Week", "change-up", "+120g", "grad-cyan-pink"),
        ("⚖️", "72.3 kg", "Current Weight", "change-down", "-0.4 kg", "grad-main"),
    ]
    for col, (icon, val, label, change_cls, change, grad) in zip([pm1,pm2,pm3,pm4], progress_metrics):
        with col:
            st.markdown(f'''
            <div class="glass metric-box">
                <span class="metric-icon">{icon}</span>
                <div class="metric-val {grad}">{val}</div>
                <div class="metric-label">{label}</div>
                <span class="metric-change {change_cls}">{'↑' if 'up' in change_cls else '↓'} {change}</span>
            </div>
            ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Charts
    df = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Calories Burned": [420, 580, 720, 650, 800, 880, 950],
        "Protein (g)": [120, 135, 145, 130, 155, 160, 165],
        "Weight (kg)": [73.1, 73.0, 72.8, 72.7, 72.5, 72.4, 72.3],
        "Sleep (hrs)": [6.5, 7.0, 7.5, 7.0, 8.0, 8.5, 7.5],
    })

    tab1, tab2, tab3, tab4 = st.tabs(["🔥 Calories", "🥩 Protein", "⚖️ Weight", "😴 Sleep"])

    with tab1:
        st.markdown('''
        <div class="glass" style="padding: 18px;">
            <div style="font-family: Space Grotesk, sans-serif; font-size: 20px; font-weight: 800;">🔥 Calories Burned — Weekly Trend</div>
        </div>
        ''', unsafe_allow_html=True)
        st.bar_chart(df.set_index("Day")[["Calories Burned"]], color="#00F5FF")

    with tab2:
        st.markdown('''
        <div class="glass" style="padding: 18px;">
            <div style="font-family: Space Grotesk, sans-serif; font-size: 20px; font-weight: 800;">🥩 Protein Intake — Daily Tracking</div>
        </div>
        ''', unsafe_allow_html=True)
        st.line_chart(df.set_index("Day")[["Protein (g)"]], color="#39FF14")

    with tab3:
        st.markdown('''
        <div class="glass" style="padding: 18px;">
            <div style="font-family: Space Grotesk, sans-serif; font-size: 20px; font-weight: 800;">⚖️ Weight Trend — Downward!</div>
        </div>
        ''', unsafe_allow_html=True)
        st.area_chart(df.set_index("Day")[["Weight (kg)"]], color="#A855F7")

    with tab4:
        st.markdown('''
        <div class="glass" style="padding: 18px;">
            <div style="font-family: Space Grotesk, sans-serif; font-size: 20px; font-weight: 800;">😴 Sleep Quality — Recovery Metric</div>
        </div>
        ''', unsafe_allow_html=True)
        st.line_chart(df.set_index("Day")[["Sleep (hrs)"]], color="#FFB800")

    st.markdown("<br>", unsafe_allow_html=True)

    # Body Composition Progress
    st.markdown('<div class="sec-title" style="font-size: 24px;">💪 <span class="grad-main">Body Composition Progress</span></div>', unsafe_allow_html=True)

    bp1, bp2, bp3 = st.columns(3)
    body_stats = [
        ("Muscle Mass", 82, "var(--neon-green)", "+2.3%"),
        ("Body Fat", 16, "var(--neon-orange)", "-1.8%"),
        ("Hydration", 68, "var(--neon-cyan)", "+3%"),
    ]
    for col, (label, pct, color, change) in zip([bp1,bp2,bp3], body_stats):
        with col:
            r = 50
            circ = 2 * 3.14159 * r
            offset = circ * (1 - pct / 100)
            st.markdown(f'''
            <div class="glass" style="text-align: center; padding: 28px;">
                <div class="ring-container">
                    <svg width="130" height="130" style="transform: rotate(-90deg);">
                        <circle cx="65" cy="65" r="{r}" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="10"/>
                        <circle cx="65" cy="65" r="{r}" fill="none" stroke="{color}" stroke-width="10"
                                stroke-linecap="round"
                                stroke-dasharray="{circ}" stroke-dashoffset="{offset}"
                                style="transition: stroke-dashoffset 1.5s ease-out; filter: drop-shadow(0 0 8px {color});"/>
                    </svg>
                    <div class="ring-text" style="color: {color} !important;">{pct}%</div>
                </div>
                <div style="font-weight: 800; font-size: 16px; margin-top: 12px;">{label}</div>
                <span class="metric-change change-up" style="margin-top: 6px;">{change}</span>
            </div>
            ''', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
# PAGE: ACHIEVEMENTS
# ════════════════════════════════════════════════════════════════
elif page == "🏆 Achievements":
    st.markdown('''
    <div class="hero-main" style="padding: 36px 42px;">
        <div class="hero-title" style="font-size: 48px;">🏆 <span class="grad-main">Achievements & Badges</span></div>
        <p class="hero-sub">Gamified fitness milestones — unlock badges by crushing your goals!</p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Streak
    st.markdown(f'''
    <div class="glass" style="text-align: center; padding: 32px; animation: glow 4s infinite;">
        <div style="font-size: 64px; animation: heartbeat 2s infinite;">🔥</div>
        <div style="font-family: Orbitron, sans-serif; font-size: 52px; font-weight: 900;">
            <span class="grad-fire">32 Days</span>
        </div>
        <div style="font-size: 18px; color: var(--text-secondary) !important; font-weight: 800;">Current Workout Streak</div>
        <div style="margin-top: 12px;">
            <span class="tag tag-green" style="font-size: 14px; padding: 8px 20px;">🏆 Longest: 45 days</span>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="sec-title" style="font-size: 24px;">🎖️ <span class="grad-cyan-pink">Unlocked Badges</span></div>', unsafe_allow_html=True)

    badges = [
        ("🥇", "First Workout", "Completed your first session!", "tag-green", True),
        ("🔥", "7-Day Streak", "7 consecutive workout days!", "tag-orange", True),
        ("💪", "100 Workouts", "Century of sweat!", "tag-cyan", True),
        ("🏋️", "Heavy Lifter", "Lifted 2x bodyweight", "tag-pink", True),
        ("🥗", "Nutrition Pro", "30 days meal tracking", "tag-green", True),
        ("🏃", "Marathon Runner", "Ran total 42.2 km", "tag-purple", True),
        ("😴", "Sleep Master", "7+ hrs sleep for 30 days", "tag-cyan", True),
        ("⚡", "HIIT Beast", "50 HIIT sessions completed", "tag-orange", True),
        ("🧘", "Flexibility King", "30 stretching sessions", "tag-green", False),
        ("🏆", "Elite Status", "All achievements unlocked", "tag-pink", False),
        ("💎", "Diamond Grind", "365-day streak", "tag-purple", False),
        ("🌟", "Perfect Week", "7/7 workouts + diet + sleep", "tag-cyan", False),
    ]

    badge_cols = st.columns(4)
    for i, (icon, title, desc, tag_class, unlocked) in enumerate(badges):
        col = badge_cols[i % 4]
        with col:
            opacity = "1" if unlocked else "0.35"
            lock = "" if unlocked else "🔒 "
            st.markdown(f'''
            <div class="glass d{(i%8)+1}" style="text-align: center; padding: 24px; opacity: {opacity};">
                <div style="font-size: 48px; margin-bottom: 8px; animation: {'float 3s infinite ease-in-out' if unlocked else 'none'};">
                    {icon}
                </div>
                <div style="font-weight: 900; font-size: 15px;">{lock}{title}</div>
                <div style="font-size: 12px; color: var(--text-muted) !important; font-weight: 600; margin: 6px 0;">{desc}</div>
                <span class="tag {tag_class}">{'✅ Unlocked' if unlocked else '🔒 Locked'}</span>
            </div>
            ''', unsafe_allow_html=True)

    # XP Progress
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'''
    <div class="glass" style="padding: 24px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <div style="font-family: Space Grotesk, sans-serif; font-size: 20px; font-weight: 900;">
                ⚡ Level 24 — <span class="grad-main">Fitness Warrior</span>
            </div>
            <span class="tag tag-purple">8,450 / 10,000 XP</span>
        </div>
        <div class="progress-wrap">
            <div class="progress-fill" style="width: 84.5%;"></div>
        </div>
        <div style="text-align: center; margin-top: 8px; color: var(--text-muted) !important; font-weight: 700; font-size: 14px;">
            1,550 XP to Level 25 — <span style="color: var(--neon-green) !important;">Fitness Legend</span>
        </div>
    </div>
    ''', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
# PAGE: WEEKLY REPORT
# ════════════════════════════════════════════════════════════════
elif page == "📄 Weekly Report":
    st.markdown(f'''
    <div class="hero-main" style="padding: 36px 42px;">
        <div class="hero-title" style="font-size: 48px;">📄 <span class="grad-rainbow">Weekly Fitness Report</span></div>
        <p class="hero-sub">AI-generated comprehensive analysis of your fitness week — {datetime.now().strftime("%B %d, %Y")}</p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Summary cards
    rs1, rs2, rs3, rs4, rs5 = st.columns(5)
    report_stats = [
        ("🏋️", "6/7", "Active Days", "grad-green-cyan"),
        ("🔥", "4,850", "Cal Burned", "grad-fire"),
        ("🥩", "980g", "Protein", "grad-cyan-pink"),
        ("⚖️", "-0.4kg", "Weight Δ", "grad-main"),
        ("😴", "7.3h", "Avg Sleep", "grad-fire"),
    ]
    for col, (icon, val, label, grad) in zip([rs1,rs2,rs3,rs4,rs5], report_stats):
        with col:
            st.markdown(f'''
            <div class="glass metric-box" style="min-height: 140px; padding: 18px;">
                <span class="metric-icon" style="font-size: 32px;">{icon}</span>
                <div class="metric-val {grad}" style="font-size: 28px;">{val}</div>
                <div class="metric-label" style="font-size: 11px;">{label}</div>
            </div>
            ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Detailed report
    rp1, rp2 = st.columns([3, 2])

    with rp1:
        st.markdown('''
        <div class="glass">
            <div style="font-family: Space Grotesk, sans-serif; font-size: 24px; font-weight: 900; margin-bottom: 20px;">
                📋 <span class="grad-main">Detailed Analysis</span>
            </div>

            <div style="margin-bottom: 20px;">
                <div style="font-weight: 900; font-size: 18px; color: #39FF14 !important; margin-bottom: 8px;">✅ Strengths</div>
                <div style="color: var(--text-secondary) !important; font-weight: 600; line-height: 1.7;">
                    • Excellent workout consistency (6 out of 7 days active)<br>
                    • Protein intake above target on 5 days<br>
                    • Progressive overload maintained — weights increased on all lifts<br>
                    • Sleep quality improved by 12% vs last week
                </div>
            </div>

            <div style="margin-bottom: 20px;">
                <div style="font-weight: 900; font-size: 18px; color: #FFB800 !important; margin-bottom: 8px;">⚠️ Areas to Improve</div>
                <div style="color: var(--text-secondary) !important; font-weight: 600; line-height: 1.7;">
                    • Wednesday protein was 20g below target<br>
                    • Skipped stretching/mobility on 4 days<br>
                    • Sunday was rest day — consider active recovery instead<br>
                    • Water intake inconsistent (target: 3L daily)
                </div>
            </div>

            <div>
                <div style="font-weight: 900; font-size: 18px; color: #00F5FF !important; margin-bottom: 8px;">🎯 Next Week Goals</div>
                <div style="color: var(--text-secondary) !important; font-weight: 600; line-height: 1.7;">
                    • Hit protein target all 7 days (165g minimum)<br>
                    • Add 10 min stretching post-workout daily<br>
                    • Increase squat weight by 2.5kg<br>
                    • Sleep 7.5+ hours every night<br>
                    • Track water intake (3L daily target)
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

    with rp2:
        st.markdown('''
        <div class="glass">
            <div style="font-family: Space Grotesk, sans-serif; font-size: 20px; font-weight: 900; margin-bottom: 16px;">
                🏆 Weekly Grades
            </div>
        ''', unsafe_allow_html=True)

        grades = [
            ("Training Volume", 92, "#39FF14"),
            ("Nutrition Quality", 85, "#00F5FF"),
            ("Recovery/Sleep", 78, "#A855F7"),
            ("Consistency", 95, "#FFB800"),
            ("Hydration", 72, "#FF2BD6"),
        ]

        grades_html = ""
        for name, score, color in grades:
            grades_html += f'''
            <div style="margin-bottom: 14px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-weight: 800; font-size: 14px;">{name}</span>
                    <span style="font-weight: 900; color: {color} !important; font-family: Orbitron, sans-serif;">{score}%</span>
                </div>
                <div class="progress-wrap">
                    <div class="progress-fill" style="width: {score}%; background: linear-gradient(90deg, {color}, {color}88);"></div>
                </div>
            </div>
            '''

        overall = int(sum(s for _, s, _ in grades) / len(grades))
        st.markdown(f'''
            {grades_html}
            <div style="text-align: center; margin-top: 20px; padding-top: 16px; border-top: 1px solid var(--border-glow);">
                <div style="font-size: 14px; color: var(--text-muted) !important; font-weight: 800;">OVERALL SCORE</div>
                <div style="font-family: Orbitron, sans-serif; font-size: 42px; font-weight: 900;">
                    <span class="grad-main">{overall}%</span>
                </div>
                <span class="tag tag-green" style="font-size: 14px; padding: 8px 18px;">🏅 Excellent Week!</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)

    # Overall progress bar
    st.markdown(f'''
    <br>
    <div class="glass" style="text-align: center; padding: 28px;">
        <div style="font-family: Space Grotesk, sans-serif; font-size: 22px; font-weight: 900; margin-bottom: 12px;">
            📈 Overall Fitness Journey Progress
        </div>
        <div class="progress-wrap" style="max-width: 700px; margin: 0 auto;">
            <div class="progress-fill" style="width: 86%;"></div>
        </div>
        <div style="font-family: Orbitron, sans-serif; font-size: 36px; font-weight: 900; margin-top: 14px;">
            <span class="grad-rainbow">86% → Goal</span>
        </div>
        <div style="color: var(--text-muted) !important; font-weight: 700; margin-top: 6px;">
            You're 14% away from your 12-week fitness goal. Keep pushing! 🔥
        </div>
    </div>
    ''', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
# FOOTER
# ════════════════════════════════════════════════════════════════
st.markdown(f'''
<div class="divider"></div>
<div style="background: rgba(8, 12, 40, 0.45); border: 1px solid var(--border-glow); padding: 12px 24px; display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap; gap: 10px; font-family: Orbitron, sans-serif; font-size: 11px; font-weight: 800; margin-bottom: 30px; border-radius: 16px; backdrop-filter: blur(10px);">
    <div style="color: var(--neon-green) !important; display: flex; align-items: center; gap: 5px;"><span>✓</span> ACCURACY: 99.4%</div>
    <div style="color: var(--neon-cyan) !important; display: flex; align-items: center; gap: 5px;"><span>⏱</span> LATENCY: 24ms</div>
    <div style="color: var(--neon-purple) !important; display: flex; align-items: center; gap: 5px;"><span>🌐</span> API: ACTIVE</div>
    <div style="color: var(--neon-red) !important; display: flex; align-items: center; gap: 5px;"><span>🛡</span> SECURITY: ELITE</div>
</div>
<div style="text-align: center; padding: 10px 0 48px;">
    <div style="font-size: 36px; margin-bottom: 10px; animation: heartbeat 3s infinite;">💪</div>
    <div style="font-family: Orbitron, sans-serif; font-size: 18px; font-weight: 900;">
        <span class="grad-main">FitPulse AI</span>
    </div>
    <div style="color: var(--text-muted) !important; font-size: 13px; font-weight: 700; margin-top: 6px;">
        Ultimate Animated Fitness Platform • AI-Powered • Offline Ready
    </div>
    <div style="display: flex; gap: 12px; justify-content: center; margin-top: 16px; flex-wrap: wrap;">
        <span class="tag tag-cyan">Dashboard</span>
        <span class="tag tag-pink">AI Coach</span>
        <span class="tag tag-green">Workouts</span>
        <span class="tag tag-orange">Diet</span>
        <span class="tag tag-purple">Analytics</span>
        <span class="tag tag-red">Achievements</span>
    </div>
    <div style="color: var(--text-muted) !important; font-size: 11px; margin-top: 14px; letter-spacing: 1px;">
        © 2024 FITPULSE • BUILT WITH ❤️ AND AI • ALL RIGHTS RESERVED
    </div>
</div>
''', unsafe_allow_html=True)