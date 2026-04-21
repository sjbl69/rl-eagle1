from fastapi import FastAPI
from stable_baselines3 import PPO
import gymnasium as gym
import numpy as np
import subprocess
import os

app = FastAPI()

# Charger le modèle une seule fois (optimisation)
model = PPO.load("model/ppo_final")

#HEALTH CHECK
@app.get("/")
def root():
    return {"message": "RL API is running "}

@app.get("/health")
def health():
    return {"status": "ok"}

#SIMULATION SIMPLE

@app.get("/play")
def play():
    env = gym.make("LunarLander-v3")

    obs, _ = env.reset()
    done = False

    total_reward = 0
    steps = 0

    rewards_history = []

    while not done:
        action, _ = model.predict(obs)
        obs, reward, terminated, truncated, _ = env.step(action)

        done = terminated or truncated

        total_reward += reward
        rewards_history.append(total_reward)
        steps += 1

    env.close()

    return {
        "total_reward": float(total_reward),
        "steps": steps,
        "rewards_history": rewards_history
    }

# SIMULATION AVEC VIDÉO

@app.get("/play_video")
def play_video():
    # Lance le script de génération vidéo
    subprocess.run(["python", "record.py"])

    video_folder = "videos"

    if not os.path.exists(video_folder):
        return {"error": "Dossier vidéo introuvable"}

    video_files = [f for f in os.listdir(video_folder) if f.endswith(".mp4")]

    if not video_files:
        return {"error": "Aucune vidéo générée"}

    latest_video = sorted(video_files)[-1]

    return {
        "video_path": f"{video_folder}/{latest_video}"
    }

# METRICS DASHBOARD

@app.get("/metrics")
def metrics():

    env = gym.make("LunarLander-v3")
    rewards = []

    for _ in range(10):  # 10 runs pour stats
        obs, _ = env.reset()
        done = False
        total_reward = 0

        while not done:
            action, _ = model.predict(obs)
            obs, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            total_reward += reward

        rewards.append(total_reward)

    env.close()

    return {
        "mean_reward": float(np.mean(rewards)),
        "max_reward": float(np.max(rewards)),
        "min_reward": float(np.min(rewards)),
        "std_reward": float(np.std(rewards)),
        "all_rewards": rewards
    }