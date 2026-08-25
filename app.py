import streamlit as st
from datetime import date
from supabase import create_client


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ADEPR KINYINYA - Kwiyandikisha",
    page_icon="⛪",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# SUPABASE
# ============================================================

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


# ============================================================
# CSS — GEORGIA PROFESSIONAL DESIGN
# ============================================================

st.markdown(
    """
    <style>

    * {
        font-family: Georgia, "Times New Roman", serif !important;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(16,185,129,0.10),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 10%,
                rgba(30,64,175,0.10),
                transparent 28%
            ),
            linear-gradient(
                135deg,
                #f8fafc,
                #eef2f7
            );
    }

    .block-container {
        max-width: 1050px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* HEADER */

    .hero {
        background:
            linear-gradient(
                135deg,
                #064e3b,
                #047857,
                #059669
            );

        border-radius: 28px;

        padding: 42px 35px;

        text-align: center;

        color: white;

        margin-bottom: 25px;

        box-shadow:
            0 20px 45px rgba(6,78,59,0.20);
    }

    .hero-icon {
        font-size: 52px;
        margin-bottom: 8px;
    }

    .hero h1 {
        font-size: 38px;
        margin: 0;
        color: white;
        font-weight: 700;
    }

    .hero h2 {
        font-size: 20px;
        margin-top: 8px;
        color: rgba(255,255,255,0.90);
        font-weight: 400;
    }

    .hero p {
        font-size: 14px;
        margin-top: 15px;
        color: rgba(255,255,255,0.82);
    }

    /* CARD */

    .card {
        background: rgba(255,255,255,0.96);

        border:
            1px solid #e2e8f0;

        border-radius: 22px;

        padding: 25px;

        margin-bottom: 20px;

        box-shadow:
            0 10px 30px rgba(15,23,42,0.06);
    }

    .card-title {
        color: #064e3b;

        font-size: 22px;

        font-weight: 700;

        margin-bottom: 5px;
    }

    .card-description {
        color: #64748b;

        font-size: 13px;

        margin-bottom: 20px;
    }

    /* INPUTS */

    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div,
    div[data-baseweb="textarea"] > div {

        background: white !important;

        border:
            1px solid #cbd5e1 !important;

        border-radius: 11px !important;
    }

    div[data-baseweb="input"] > div:focus-within,
    div[data-baseweb="select"] > div:focus-within,
    div[data-baseweb="textarea"] > div:focus-within {

        border-color:
            #059669 !important;

        box-shadow:
            0 0 0 2px rgba(5,150,105,0.10) !important;
    }

    label {
        font-weight: 700 !important;
        color: #334155 !important;
    }

    /* BUTTON */

    .stButton > button {

        width: 100%;

        min-height: 50px;

        border-radius: 12px;

        border: none;

        background:
            linear-gradient(
                135deg,
                #047857,
                #059669
            );

        color: white;

        font-size: 16px;

        font-weight: 700;

        box-shadow:
            0 8px 20px rgba(5,150,105,0.20);

        transition:
            all 0.2s ease;
    }

    .stButton > button:hover {

        transform:
            translateY(-2px);

        box-shadow:
            0 12px 25px rgba(5,150,105,0.28);
    }

    /* FOOTER */

    .footer {
        text-align: center;

        color: #64748b;

        font-size: 12px;

        margin-top: 30px;

        padding-top: 20px;

        border-top:
            1px solid #e2e8f0;
    }

    /* SUCCESS */

    .success-box {

        background:
            #ecfdf5;

        border:
            1px solid #a7f3d0;

        border-radius: 16px;

        padding: 20px;

        text-align: center;

        color: #065f46;

        font-size: 17px;

        font-weight: 700;

        margin-bottom: 20px;
    }

    @media(max-width:768px){

        .hero {
            padding: 30px 20px;
        }

        .hero h1 {
            font-size: 29px;
        }

        .hero h2 {
            font-size: 17px;
        }

        .card {
            padding: 18px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-icon">⛪</div>

        <h1>ADEPR KINYINYA</h1>

        <h2>Kwiyandikisha nk'Umukristo</h2>

        <p>
            Uzuza aya makuru kugira ngo wiyandikishe
            muri ADEPR Kinyinya.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PERSONAL INFORMATION
# ============================================================

st.markdown(
    """
    <div class="card">

        <div class="card-title">
            👤 Imyirondoro y'Umukristo
        </div>

        <div class="card-description">
            Amazina ni yo makuru yonyine asabwa.
            Andi makuru ushobora kuyuzuza niba uyafite.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns(2, gap="large")


with col1:

    amazina = st.text_input(
        "Amazina *",
        placeholder="Urugero: UWIMANA Jean"
    )

    telephone = st.text_input(
        "Telephone",
        placeholder="Urugero: 078xxxxxxx"
    )

    irangamuntu = st.text_input(
        "Irangamuntu",
        placeholder="Nomero y'indangamuntu"
    )

    itariki_yamavuko = st.date_input(
        "Itariki y'amavuko",
        value=None,
        min_value=date(1900, 1, 1),
        max_value=date.today()
    )


with col2:

    igitsina = st.selectbox(
        "Igitsina",
        [
            "Hitamo",
            "Gabo",
            "Gore"
        ]
    )

    aho_yabatirijwe = st.text_input(
        "Aho yabatirijwe",
        placeholder="Urugero: ADEPR Kinyinya"
    )


# ============================================================
# BIRTHPLACE
# ============================================================

st.markdown(
    """
    <div class="card">

        <div class="card-title">
            📍 Aho Yavukiye
        </div>

        <div class="card-description">
            Amakuru y'aho wavukiye.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns(2, gap="large")


with col1:

    yavukiye_intara = st.selectbox(
        "Intara yavukiyemo",
        [
            "Hitamo",
            "Kigali",
            "Iburasirazuba",
            "Amajyepfo",
            "Amajyaruguru",
            "Iburengerazuba",
            "Hanze y'u Rwanda"
        ]
    )

    yavukiye_akarere = st.text_input(
        "Akarere yavukiyemo"
    )

    yavukiye_umurenge = st.text_input(
        "Umurenge yavukiyemo"
    )


with col2:

    yavukiye_akagari = st.text_input(
        "Akagari yavukiyemo"
    )

    yavukiye_umudugudu = st.text_input(
        "Umudugudu yavukiyemo"
    )


# ============================================================
# CURRENT ADDRESS
# ============================================================

st.markdown(
    """
    <div class="card">

        <div class="card-title">
            🏠 Aho Atuyе Ubu
        </div>

        <div class="card-description">
            Aho usanzwe utuye muri iki gihe.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns(2, gap="large")


with col1:

    atuye_intara = st.selectbox(
        "Intara atuyemo",
        [
            "Hitamo",
            "Kigali",
            "Iburasirazuba",
            "Amajyepfo",
            "Amajyaruguru",
            "Iburengerazuba",
            "Hanze y'u Rwanda"
        ]
    )

    atuye_akarere = st.text_input(
        "Akarere atuyemo"
    )

    atuye_umurenge = st.text_input(
        "Umurenge atuyemo"
    )


with col2:

    atuye_akagari = st.text_input(
        "Akagari atuyemo"
    )

    atuye_umudugudu = st.text_input(
        "Umudugudu atuyemo"
    )


# ============================================================
# CHURCH INFORMATION
# ============================================================

st.markdown(
    """
    <div class="card">

        <div class="card-title">
            ⛪ Amakuru y'Itorero
        </div>

        <div class="card-description">
            Amakuru ajyanye n'aho abarizwa n'umurimo akora.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns(2, gap="large")


with col1:

    igihande = st.text_input(
        "Igihande abarizwamo",
        placeholder="Urugero: Igihande cya Kinyinya"
    )

    umurimo_itorero = st.selectbox(
        "Umurimo akora mu itorero",
        [
            "Hitamo",
            "Umuyobozi w'itorero",
            "Umudiyakoni",
            "Umuririmbyi",
            "Umukristo"
        ]
    )


with col2:

    chorale = st.text_input(
        "Chorale aririmbamo",
        placeholder="Urugero: Inshuti za Yesu"
    )

    emergency_contact = st.text_input(
        "Uwo bahamagara habaye ikibazo",
        placeholder="Amazina na Telephone"
    )


# ============================================================
# SUBMIT
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

if st.button(
    "📝 OHEREZA AMAKURU YO KWIYANDIKISHA"
):

    # ONLY REQUIRED FIELD

    if not amazina.strip():

        st.error(
            "❌ Amazina arakenewe."
        )

        st.stop()


    # ========================================================
    # PREPARE DATA
    # ========================================================

    data = {

        "amazina":
            amazina.strip(),

        "telephone":
            telephone.strip() or None,

        "irangamuntu":
            irangamuntu.strip() or None,

        "itariki_yamavuko":
            str(itariki_yamavuko)
            if itariki_yamavuko
            else None,

        "igitsina":
            igitsina
            if igitsina != "Hitamo"
            else None,

        "aho_yabatirijwe":
            aho_yabatirijwe.strip() or None,

        "yavukiye_intara":
            yavukiye_intara
            if yavukiye_intara != "Hitamo"
            else None,

        "yavukiye_akarere":
            yavukiye_akarere.strip() or None,

        "yavukiye_umurenge":
            yavukiye_umurenge.strip() or None,

        "yavukiye_akagari":
            yavukiye_akagari.strip() or None,

        "yavukiye_umudugudu":
            yavukiye_umudugudu.strip() or None,

        "atuye_intara":
            atuye_intara
            if atuye_intara != "Hitamo"
            else None,

        "atuye_akarere":
            atuye_akarere.strip() or None,

        "atuye_umurenge":
            atuye_umurenge.strip() or None,

        "atuye_akagari":
            atuye_akagari.strip() or None,

        "atuye_umudugudu":
            atuye_umudugudu.strip() or None,

        "igihande":
            igihande.strip() or None,

        "umurimo_itorero":
            umurimo_itorero
            if umurimo_itorero != "Hitamo"
            else None,

        "chorale":
            chorale.strip() or None,

        "emergency_contact":
            emergency_contact.strip() or None
    }


    # ========================================================
    # SEND TO SUPABASE
    # ========================================================

    try:

        response = (
            supabase
            .table("members")
            .insert(data)
            .execute()
        )


        if response.data:

            st.markdown(
                """
                <div class="success-box">

                    ✅ Kwiyandikisha byagenze neza!

                    <br><br>

                    Murakoze kwiyandikisha muri
                    <b>ADEPR Kinyinya</b>.

                </div>
                """,
                unsafe_allow_html=True
            )

            st.balloons()

        else:

            st.error(
                "❌ Ntabwo amakuru yabitswe."
            )


    except Exception as e:

        error_message = str(e)

        if "duplicate" in error_message.lower():

            st.error(
                "❌ Iyi ndangamuntu isanzwe iri muri system."
            )

        else:

            st.error(
                f"❌ Habaye ikibazo mu kubika amakuru: {e}"
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        ⛪ <b>ADEPR KINYINYA</b>

        <br>

        Management Information System

        <br><br>

        © 2026 ADEPR Kinyinya

    </div>
    """,
    unsafe_allow_html=True
)
