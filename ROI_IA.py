import streamlit as st
import pandas as pd
import os

# Configuration de la page
st.set_page_config(
    page_title="Dynia IA : Simulateur de Rentabilité",
    page_icon="💰",
    layout="wide"
)

# --- CHARTE GRAPHIQUE DYNIA (CSS Personnalisé) ---
st.markdown("""
    <style>
    :root {
        --brand-deep: #0c2461;
        --brand-primary: #1e3799;
        --brand-medium: #4a69bd;
        --brand-light: #f0f7ff;
    }
    
    .main {
        background-color: #f8fafc;
    }
    
    h1, h2, h3 {
        color: var(--brand-deep) !important;
    }
    
    /* Style des cartes de metrics */
    [data-testid="stMetric"] {
        background-color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }

    .cta-box {
        background-color: var(--brand-deep);
        color: white;
        padding: 2.5rem;
        border-radius: 1.5rem;
        text-align: center;
        margin-top: 3rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- EN-TÊTE ---
col_header_logo, col_header_title = st.columns([1, 4])

with col_header_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=150)
    else:
        st.title("DYNIA")

with col_header_title:
    st.title("💰 Mesurez votre Gain de Temps et d'Argent")
    st.markdown("""
        **L'IA et l'automatisation ne sont pas des coûts, ce sont des investissements.**  
        Calculez votre retour sur investissement (ROI) immédiat avec les méthodes Dynia IA.
    """)

st.divider()

# --- SECTION SAISIE (COLONNE GAUCHE) & RÉSULTATS (COLONNE DROITE) ---
col_input, col_results = st.columns([1, 2], gap="large")

with col_input:
    st.subheader("⚙️ Vos Données Actuelles")
    st.write("Dites-nous comment vous travaillez aujourd'hui.")
    
    task_name = st.text_input("Nom de la tâche à automatiser", placeholder="ex: Tri de leads, Rédaction d'emails...")
    
    hours_per_week = st.slider("Temps passé sur cette tâche (h / semaine)", 1, 40, 10)
    
    hourly_cost = st.number_input("Coût horaire (votre temps ou celui d'un employé) en €", min_value=10, value=50, step=5)
    
    st.info("""
        **Hypothèse Dynia IA :**  
        Nos solutions (Claude Code + n8n) automatisent en moyenne **80%** de la charge de travail. Vous ne gardez que 20% pour la supervision finale.
    """)

# --- CALCULS BUSINESS ANALYST ---
WEEKS_PER_YEAR = 52
AUTOMATION_RATE = 0.80

# État actuel
annual_hours_current = hours_per_week * WEEKS_PER_YEAR
annual_cost_current = annual_hours_current * hourly_cost

# État avec Dynia IA
new_hours_per_week = hours_per_week * (1 - AUTOMATION_RATE)
annual_hours_new = new_hours_per_week * WEEKS_PER_YEAR
annual_cost_new = annual_hours_new * hourly_cost

# Gains
annual_time_saved = annual_hours_current - annual_hours_new
annual_money_saved = annual_cost_current - annual_cost_new

# --- SECTION RÉSULTATS (COLONNE DROITE) ---
with col_results:
    st.subheader(f"📈 Votre Nouveau Bilan : {task_name if task_name else ''}")
    
    m1, m2, m3 = st.columns(3)
    
    m1.metric("Temps Gagné / An", f"{int(annual_time_saved)} h", help="Heures libérées pour des tâches à haute valeur ajoutée.")
    m2.metric("Argent Économisé / An", f"{int(annual_money_saved):,} €", delta=f"-{int(AUTOMATION_RATE*100)}%", delta_color="normal")
    m3.metric("Nouveau Temps / Semaine", f"{new_hours_per_week:.1f} h", help="Temps restant pour la simple vérification humaine.")

    st.write("### 📊 Comparaison des coûts annuels")
    
    # Préparation des données pour le graphique
    chart_data = pd.DataFrame({
        "Scénario": ["Sans IA (Actuel)", "Avec Dynia IA"],
        "Coût Annuel (€)": [annual_cost_current, annual_cost_new]
    })
    
    # Affichage du graphique
    st.bar_chart(chart_data, x="Scénario", y="Coût Annuel (€)", color="#1e3799")
    
    st.caption("Ce graphique montre l'effondrement de vos coûts opérationnels après l'implémentation de nos automatisations.")

# --- PIED DE PAGE (CALL TO ACTION) ---
st.markdown(f"""
    <div class="cta-box">
        <h2>Imaginez ce que vous pourriez faire de ces {int(annual_time_saved)} heures récupérées...</h2>
        <p style="font-size: 1.2rem; opacity: 0.9;">
            Plus de stratégie, plus de clients, ou simplement plus de temps libre. 
            Récupérez vos <b>{int(annual_money_saved):,} €</b> de marge perdue dès maintenant.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Bouton de contact centré
col_btn_1, col_btn_2, col_btn_3 = st.columns([1, 2, 1])
with col_btn_2:
    # Lien vers votre Calendly ou WhatsApp (à remplacer par votre lien réel)
    st.link_button(
        "🚀 Prendre RDV pour automatiser cette tâche", 
        "mailto:thomas@dynia.fr", 
        use_container_width=True,
        type="primary"
    )

st.markdown(f"""
    <div style="text-align: center; color: #94a3b8; font-size: 0.8rem; margin-top: 2rem;">
        © 2024 DYNIA IA - Expert en Rentabilité Opérationnelle
    </div>
""", unsafe_allow_html=True)