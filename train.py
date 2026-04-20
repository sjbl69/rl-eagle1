import gymnasium as gym
from stable_baselines3 import PPO
import os

# Créer dossier model
os.makedirs("model", exist_ok=True)

# Environnement
env = gym.make("LunarLander-v3")

# Modèle PPO final
model = PPO(
    "MlpPolicy",
    env,
    learning_rate=3e-4,
    n_steps=2048,
    batch_size=64,
    gamma=0.99,
    verbose=1,
    tensorboard_log="./logs/"   
)

# Entraînement
model.learn(total_timesteps=1000000)

# Sauvegarde
model.save("model/ppo_final")

print("Modèle PPO entraîné et sauvegardé")