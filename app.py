import streamlit as st
import pandas as pd
import joblib

# Nécessaire si IGRClipper est présent dans le pipeline sauvegardé
from preprocessing import IGRClipper


# CONFIGURATION

st.set_page_config(
    page_title="EduPredict",
    page_icon="🎓",
    layout="wide"
)


# CHARGEMENT DU PIPELINE

@st.cache_resource
def load_model():

    return joblib.load("meilleur_model.joblib")


model = load_model()


# TITRE

st.title(" EduPredict")

st.subheader(
    "Prédiction de la performance académique des étudiants"
)

st.write(
    """
    Cette application utilise un modèle de Machine Learning
    pour estimer le score d'examen d'un étudiant à partir
    de son profil académique, personnel et scolaire.
    """
)

st.divider()


# PROFIL ACADÉMIQUE

st.header(" Profil académique")

col1, col2, col3 = st.columns(3)


with col1:

    hours_studied = st.slider(
        "Heures étudiées",
        min_value=1,
        max_value=44,
        value=20
    )


with col2:

    attendance = st.slider(
        "Taux de présence (%)",
        min_value=60,
        max_value=100,
        value=80
    )


with col3:

    previous_scores = st.slider(
        "Scores précédents",
        min_value=50,
        max_value=100,
        value=70
    )


col1, col2, col3 = st.columns(3)


with col1:

    sleep_hours = st.slider(
        "Heures de sommeil",
        min_value=4,
        max_value=10,
        value=7
    )


with col2:

    tutoring_sessions = st.slider(
        "Séances de tutorat",
        min_value=0,
        max_value=8,
        value=2
    )


with col3:

    physical_activity = st.slider(
        "Activité physique",
        min_value=0,
        max_value=6,
        value=3
    )


# PROFIL PERSONNEL

st.header(" Profil personnel")

col1, col2, col3 = st.columns(3)


with col1:

    gender = st.selectbox(
        "Genre",
        ["Male", "Female"]
    )


with col2:

    learning_disabilities = st.selectbox(
        "Troubles d'apprentissage",
        ["No", "Yes"]
    )


with col3:

    family_income = st.selectbox(
        "Revenu familial",
        ["Low", "Medium", "High"]
    )


# ENVIRONNEMENT SCOLAIRE

st.header(" Environnement scolaire")

col1, col2, col3 = st.columns(3)


with col1:

    parental_involvement = st.selectbox(
        "Implication parentale",
        ["Low", "Medium", "High"]
    )


with col2:

    access_to_resources = st.selectbox(
        "Accès aux ressources",
        ["Low", "Medium", "High"]
    )


with col3:

    extracurricular = st.selectbox(
        "Activités extrascolaires",
        ["No", "Yes"]
    )


col1, col2, col3 = st.columns(3)


with col1:

    motivation_level = st.selectbox(
        "Niveau de motivation",
        ["Low", "Medium", "High"]
    )


with col2:

    internet_access = st.selectbox(
        "Accès à Internet",
        ["Yes", "No"]
    )


with col3:

    teacher_quality = st.selectbox(
        "Qualité de l'enseignant",
        ["Low", "Medium", "High"]
    )


col1, col2, col3 = st.columns(3)


with col1:

    school_type = st.selectbox(
        "Type d'école",
        ["Public", "Private"]
    )


with col2:

    peer_influence = st.selectbox(
        "Influence des pairs",
        ["Positive", "Negative", "Neutral"]
    )


with col3:

    parental_education = st.selectbox(
        "Niveau d'éducation des parents",
        [
            "High School",
            "College",
            "Postgraduate"
        ]
    )


col1, col2 = st.columns(2)


with col1:

    distance_from_home = st.selectbox(
        "Distance du domicile",
        [
            "Near",
            "Moderate",
            "Far"
        ]
    )


st.divider()


# CONSTRUCTION DES DONNÉES D'ENTRÉE

input_data = pd.DataFrame({

    "Hours_Studied": [hours_studied],

    "Attendance": [attendance],

    "Parental_Involvement": [parental_involvement],

    "Access_to_Resources": [access_to_resources],

    "Extracurricular_Activities": [extracurricular],

    "Sleep_Hours": [sleep_hours],

    "Previous_Scores": [previous_scores],

    "Motivation_Level": [motivation_level],

    "Internet_Access": [internet_access],

    "Tutoring_Sessions": [tutoring_sessions],

    "Family_Income": [family_income],

    "Teacher_Quality": [teacher_quality],

    "School_Type": [school_type],

    "Peer_Influence": [peer_influence],

    "Physical_Activity": [physical_activity],

    "Learning_Disabilities": [learning_disabilities],

    "Parental_Education_Level": [parental_education],

    "Distance_from_Home": [distance_from_home],

    "Gender": [gender]
})


# BOUTON DE PRÉDICTION

if st.button(
    " Estimer le score",
    use_container_width=True
):

    # Prédiction

    prediction = model.predict(input_data)

    score = prediction[0]


    # Affichage du score

    st.divider()

    st.header(" Résultat")

    st.metric(
        label="Score d'examen estimé",
        value=f"{score:.2f} / 100"
    )


    # Signalement

    if score < 50:

        st.error(
            "⚠️ Étudiant à risque : le score estimé "
            "est inférieur à 50."
        )

    elif score < 70:

        st.warning(
            "🟠 Vigilance : le score estimé indique "
            "une performance intermédiaire."
        )

    else:

        st.success(
            "🟢 Performance satisfaisante : "
            "le score estimé est supérieur ou égal à 70."
        )