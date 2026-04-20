import streamlit as st
import requests
import numpy as np

st.set_page_config(page_title="RL Eagle-1", layout="wide")

# HEADER

st.title(" RL Eagle-1 - Lunar Lander AI")
st.markdown("Simulation d’un agent **Reinforcement Learning (PPO)** sur LunarLander")

#MENU

menu = st.sidebar.selectbox(
    "Navigation",
    [" Simulation", " Visualisation", " Dashboard"]
)

API_URL = "http://127.0.0.1:8000"

# SIMULATION

if menu == " Simulation":
    st.header(" Simulation simple")

    if st.button("Lancer une simulation"):
        with st.spinner("Simulation en cours..."):
            response = requests.get(f"{API_URL}/play")
            result = response.json()

        st.success("Simulation terminée")

        col1, col2 = st.columns(2)

        col1.metric("Reward total", round(result["total_reward"], 2))
        col2.metric("Nombre de steps", result["steps"])

        #  Courbe de reward
        rewards = result.get("rewards_history", [])
        if rewards:
            st.subheader(" Évolution du reward")
            st.line_chart(rewards)

# VISUALISATION

elif menu == " Visualisation":
    st.header(" Visualisation de l'agent")

    st.write("Voir une **vraie partie jouée** par l'agent PPO")

    if st.button(" Générer la vidéo"):
        with st.spinner("Génération de la vidéo..."):
            response = requests.get(f"{API_URL}/play_video")
            data = response.json()

        if "video_path" in data:
            st.success("Vidéo générée")

            video_path = data["video_path"]

            video_file = open(video_path, "rb")
            video_bytes = video_file.read()

            st.video(video_bytes)

        else:
            st.error("Erreur lors de la génération de la vidéo")

# DASHBOARD

elif menu == " Dashboard":
    st.header(" Dashboard des performances")

    st.write("Analyse des performances de l’agent sur plusieurs simulations")

    if st.button(" Charger les métriques"):
        with st.spinner("Calcul des métriques..."):
            response = requests.get(f"{API_URL}/metrics")
            data = response.json()

        rewards = data["all_rewards"]

        #  KPIs
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Reward moyen", round(data["mean_reward"], 2))
        col2.metric("Max reward", round(data["max_reward"], 2))
        col3.metric("Min reward", round(data["min_reward"], 2))
        col4.metric("Std (stabilité)", round(data["std_reward"], 2))

        #  Distribution
        st.subheader(" Distribution des rewards")
        st.bar_chart(rewards)

        #  Analyse stabilité
        st.subheader(" Analyse de stabilité")
        st.line_chart(rewards)

        #  Interprétation
        st.subheader(" Interprétation")

        if data["mean_reward"] > 200:
            st.success("Agent performant ")
        elif data["mean_reward"] > 100:
            st.warning("Agent correct mais améliorable ")
        else:
            st.error("Agent instable ")