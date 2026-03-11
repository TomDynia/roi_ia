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
        --success-green: #27ae60;
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

    .funding-badge {
        background-color: #e6fffa;
        color: #2c7a7b;
        padding: 1rem;
        border-radius: 0.75rem;
        border: 1px solid #b2f5ea;
        margin-bottom: 1.5rem;
        font-weight: 600;
        text-align: center;
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
    hours_per_week = st.slider("Heures / semaine sur cette tâche", 1, 40, 10)
    hourly_cost = st.number_input("Votre coût horaire (€)", min_value=10, value=50, step=5)
    
    st.markdown("---")
    st.subheader("🛡️ Financement")
    is_funded = st.checkbox("Ma formation est prise en charge (OPCO, FAF...)", value=True)
    
    if is_funded:
        st.markdown('<div class="funding-badge">✅ Reste à charge formation : 0€</div>', unsafe_allow_html=True)

# --- CALCULS ---
WEEKS_PER_YEAR = 52
AUTOMATION_RATE = 0.80

annual_hours_current = hours_per_week * WEEKS_PER_YEAR
annual_cost_current = annual_hours_current * hourly_cost

new_hours_per_week = hours_per_week * (1 - AUTOMATION_RATE)
annual_hours_new = new_hours_per_week * WEEKS_PER_YEAR
annual_cost_new = annual_hours_new * hourly_cost

annual_time_saved = annual_hours_current - annual_hours_new
annual_money_saved = annual_cost_current - annual_cost_new

# --- SECTION RÉSULTATS (COLONNE DROITE) ---
with col_results:
    st.subheader(f"📈 Votre Nouveau Bilan")
    
    m1, m2, m3, m4 = st.columns(4)
    
    m1.metric("Temps Gagné / An", f"{int(annual_time_saved)} h")
    m2.metric("Argent Économisé / An", f"{int(annual_money_saved):,} €")
    m3.metric("Reste à charge", "0 €" if is_funded else "À définir")
    m4.metric("ROI", "Immédiat" if is_funded else "Très rapide")

    st.write("### 📊 Comparaison des coûts annuels")
    
    # Préparation des données pour le graphique avec 3 barres
    chart_data = pd.DataFrame({
        "Catégorie": ["Coût Humain Actuel", "Nouveau Coût (IA)", "Votre Investissement"],
        "Montant (€)": [annual_cost_current, annual_cost_new, 0 if is_funded else 0]
    })
    
    # Affichage du graphique
    # On utilise une couleur différente pour l'investissement pour bien le distinguer
    st.bar_chart(chart_data, x="Catégorie", y="Montant (€)", color="#1e3799")
    
    st.caption("Ce graphique montre que votre transition vers l'IA ne vous coûte rien grâce au financement de la formation.")

# --- PIED DE PAGE ---
st.markdown(f"""
    <div class="cta-box">
        <h2>ROI IMMÉDIAT : Vous récupérez {int(annual_money_saved):,} € dès la première année.</h2>
        <p style="font-size: 1.2rem; opacity: 0.9;">
            Puisque votre formation est prise en charge, chaque heure automatisée est un bénéfice pur pour votre entreprise.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col_btn_1, col_btn_2, col_btn_3 = st.columns([1, 2, 1])
with col_btn_2:
    st.link_button(
        "🚀 Vérifier mon éligibilité au financement", 
        "mailto:thomas@dynia.fr", 
        use_container_width=True,
        type="primary"
    )

st.markdown(f"""
    <div style="text-align: center; color: #94a3b8; font-size: 0.8rem; margin-top: 2rem;">
        © 2024 DYNIA IA - Expert en Rentabilité Opérationnelle
    </div>
""", unsafe_allow_html=True)