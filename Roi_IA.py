import streamlit as st
import pandas as pd
import os

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="Dynia IA : Simulateur de Rentabilité",
    page_icon="💰",
    layout="wide"
)

# 2. CHARTE GRAPHIQUE DYNIA (CSS)
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
        font-weight: 700 !important;
    }
    
    /* Style des cartes de metrics */
    [data-testid="stMetric"] {
        background-color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }

    /* Boîte d'appel à l'action finale */
    .cta-box {
        background-color: var(--brand-deep);
        color: white;
        padding: 2.5rem;
        border-radius: 1.5rem;
        text-align: center;
        margin-top: 3rem;
    }

    /* Badge de financement */
    .funding-badge {
        background-color: #e6fffa;
        color: #2c7a7b;
        padding: 1rem;
        border-radius: 0.75rem;
        border: 1px solid #b2f5ea;
        margin-top: 1rem;
        font-weight: 600;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. EN-TÊTE
col_logo, col_title = st.columns([1, 4])

with col_logo:
    # Utilisation du logo local comme demandé
    if os.path.exists("logo.png"):
        st.image("logo.png", width=150)
    else:
        st.title("DYNIA")

with col_title:
    st.title("💰 Mesurez votre Gain de Temps et d'Argent")
    st.markdown("""
        **L'IA et l'automatisation ne sont pas des coûts, ce sont des investissements.**  
        Calculez votre retour sur investissement (ROI) immédiat avec les méthodes Dynia IA.
    """)

st.divider()

# 4. SECTION SAISIE (COLONNE GAUCHE)
col_input, col_results = st.columns([1, 2], gap="large")

with col_input:
    st.subheader("⚙️ Vos Données Actuelles")
    
    # Liste des tâches (ordre respecté, sans emojis)
    tasks_list = [
        "Tri et rédaction de réponses aux emails",
        "Saisie de données (Factures, PDF vers Excel)",
        "Création et envoi de devis personnalisés",
        "Qualification et recherche de nouveaux prospects",
        "Création de publications pour les réseaux sociaux",
        "Synthèse de réunions et comptes-rendus",
        "Rédaction de newsletters et mailings",
        "Mise à jour de CRM et bases de données",
        "Gestion et réponse aux avis clients",
        "Rédaction de tutoriels ou documentations"
    ]
    
    task_name = st.selectbox("Tâche à automatiser", tasks_list)
    
    hours_per_week = st.slider("Temps passé sur cette tâche (h / semaine)", 1, 40, 10)
    
    hourly_cost = st.number_input("Votre coût horaire (ou celui d'un employé) en €", min_value=10, value=50, step=5)
    
    st.markdown("---")
    st.subheader("🛡️ Financement")
    is_funded = st.checkbox("Ma formation est prise en charge (OPCO, FAF...)", value=True)
    
    if is_funded:
        st.markdown('<div class="funding-badge">✅ Reste à charge formation : 0€</div>', unsafe_allow_html=True)
    
    st.caption("Hypothèse Dynia IA : Automatisation de 80% de la tâche (20% restant pour la supervision).")

# 5. LOGIQUE DE CALCUL (BUSINESS ANALYST)
WEEKS_PER_YEAR = 52
AUTOMATION_RATE = 0.80

# État Actuel
annual_hours_current = hours_per_week * WEEKS_PER_YEAR
annual_cost_current = annual_hours_current * hourly_cost

# État Dynia IA
new_hours_per_week = hours_per_week * (1 - AUTOMATION_RATE)
annual_hours_new = new_hours_per_week * WEEKS_PER_YEAR
annual_cost_new = annual_hours_new * hourly_cost

# Gains
annual_time_saved = annual_hours_current - annual_hours_new
annual_money_saved = annual_cost_current - annual_cost_new

# 6. SECTION RÉSULTATS (COLONNE DROITE)
with col_results:
    st.subheader("📈 Votre Nouveau Bilan avec Dynia IA")
    st.write(f"Analyse pour la tâche : **{task_name}**")
    
    m1, m2, m3, m4 = st.columns(4)
    
    m1.metric("Temps Gagné / An", f"{int(annual_time_saved)} h")
    m2.metric("Argent Économisé / An", f"{int(annual_money_saved):,} €")
    m3.metric("Reste à charge", "0 €" if is_funded else "À définir")
    m4.metric("ROI", "Immédiat" if is_funded else "Très rapide")

    st.write("### 📊 Comparaison des coûts annuels")
    
    # Création du DataFrame pour le graphique
    chart_data = pd.DataFrame({
        "Scénario": ["Coût Humain Actuel", "Nouveau Coût (IA)", "Votre Investissement"],
        "Montant (€)": [annual_cost_current, annual_cost_new, 0]
    })
    
    # Affichage du graphique à barres
    st.bar_chart(chart_data, x="Scénario", y="Montant (€)", color="#1e3799")
    
    st.caption("Ce graphique montre l'effondrement de vos coûts et l'absence de reste à charge pour la transition.")

# 7. PIED DE PAGE (CALL TO ACTION)
st.markdown(f"""
    <div class="cta-box">
        <h2>ROI IMMÉDIAT : Vous récupérez {int(annual_money_saved):,} € dès la première année.</h2>
        <p style="font-size: 1.2rem; opacity: 0.9;">
            Imaginez ce que vous pourriez faire de ces {int(annual_time_saved)} heures récupérées... 
            Plus de stratégie, plus de clients, ou simplement plus de temps libre.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Bouton de contact centré
col_btn_1, col_btn_2, col_btn_3 = st.columns([1, 2, 1])
with col_btn_2:
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