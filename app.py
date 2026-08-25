import streamlit as st
from supabase import create_client, Client
from datetime import date

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ADEPR KINYINYA - Kwiyandikisha",
    page_icon="⛪",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# SUPABASE
# ============================================================

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

# ============================================================
# CSS - GEORGIA
# ============================================================

st.markdown("""
<style>

* {
    font-family: Georgia, "Times New Roman", serif !important;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(5,150,105,.10),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(30,64,175,.10),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #f8fafc,
            #eef2f7
        );
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.header {
    background:
        linear-gradient(
            135deg,
            #064e3b,
            #047857,
            #059669
        );
    padding: 35px;
    border-radius: 25px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0 15px 40px rgba(6,78,59,.20);
}

.header h1 {
    color: white;
    margin-bottom: 8px;
    font-size: 34px;
}

.header p {
    color: rgba(255,255,255,.90);
    font-size: 16px;
}

.form-card {
    background: white;
    padding: 28px;
    border-radius: 22px;
    box-shadow: 0 8px 30px rgba(15,23,42,.07);
    border: 1px solid #e2e8f0;
}

.section-title {
    color: #064e3b;
    font-size: 21px;
    font-weight: bold;
    margin-top: 15px;
    margin-bottom: 5px;
}

.section-description {
    color: #64748b;
    font-size: 13px;
    margin-bottom: 18px;
}

label {
    font-weight: bold !important;
    color: #334155 !important;
}

button[kind="primary"] {
    background:
        linear-gradient(
            135deg,
            #047857,
            #059669
        ) !important;

    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    min-height: 48px !important;
    font-size: 16px !important;
}

.success-box {
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    color: #065f46;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    margin-top: 20px;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="header">

    <div style="font-size:48px;">⛪</div>

    <h1>ADEPR KINYINYA</h1>

    <p>
        Kwiyandikisha nk'umukristo
    </p>

</div>
""", unsafe_allow_html=True)

# ============================================================
# FORM
# ============================================================

st.markdown("""
<div class="form-card">
""", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">👤 Imyirondoro y\'Umukristo</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Amazina ni yo makuru asabwa. Andi makuru ushobora kuyuzuza niba uyafite.'
    '</div>',
    unsafe_allow_html=True
)

# ============================================================
# PERSONAL INFORMATION
# ============================================================

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

col1, col2 = st.columns(2)

with col1:

    itariki_yamavuko = st.date_input(
        "Itariki y'amavuko",
        value=date(2000, 1, 1),
        min_value=date(1900, 1, 1),
        max_value=date.today()
    )

with col2:

    igitsina = st.selectbox(
        "Igitsina",
        [
            "",
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
    '<div class="section-title">📍 Aho yavukiye</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    yavukiye_intara = st.selectbox(
        "Intara yavukiyemo",
        [
            "",
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
    '<div class="section-title">🏠 Aho atuye ubu</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    atuye_intara = st.selectbox(
        "Intara atuyemo",
        [
            "",
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
# CHURCH
# ============================================================

st.markdown(
    '<div class="section-title">⛪ Amakuru y\'Itorero</div>',
    unsafe_allow_html=True
)

igihande = st.text_input(
    "Igihande abarizwamo",
    placeholder="Urugero: Igihande cya Kinyinya"
)

umurimo_itorero = st.selectbox(
    "Umurimo akora mu itorero",
    [
        "",
        "Umuyobozi w'itorero",
        "Umudiyakoni",
        "Umuririmbyi",
        "Umukristo"
    ]
)

chorale = st.text_input(
    "Chorale aririmbamo",
    placeholder="Urugero: Inshuti za Yesu"
)

# ============================================================
# EMERGENCY
# ============================================================

st.markdown(
    '<div class="section-title">🚨 Uwo bahamagara habaye ikibazo</div>',
    unsafe_allow_html=True
)

emergency_contact = st.text_input(
    "Amazina na Telephone",
    placeholder="Urugero: Jean Bosco - 078xxxxxxx"
)

# ============================================================
# SUBMIT
# ============================================================

st.write("")

submitted = st.button(
    "💾 OHEREZA AMAKURU",
    type="primary",
    use_container_width=True
)

# ============================================================
# SAVE
# ============================================================

if submitted:

    if not amazina.strip():

        st.error(
            "❌ Amazina y'umukristo ni ngombwa."
        )

        st.stop()

    data = {

        "amazina": amazina.strip(),

        "telephone":
            telephone.strip() or None,

        "irangamuntu":
            irangamuntu.strip() or None,

        "itariki_yamavuko":
            str(itariki_yamavuko)
            if itariki_yamavuko
            else None,

        "igitsina":
            igitsina or None,

        "aho_yabatirijwe":
            aho_yabatirijwe.strip() or None,

        "yavukiye_intara":
            yavukiye_intara or None,

        "yavukiye_akarere":
            yavukiye_akarere.strip() or None,

        "yavukiye_umurenge":
            yavukiye_umurenge.strip() or None,

        "yavukiye_akagari":
            yavukiye_akagari.strip() or None,

        "yavukiye_umudugudu":
            yavukiye_umudugudu.strip() or None,

        "atuye_intara":
            atuye_intara or None,

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
            umurimo_itorero or None,

        "chorale":
            chorale.strip() or None,

        "emergency_contact":
            emergency_contact.strip() or None
    }

    try:

        response = (
            supabase
            .table("members")
            .insert(data)
            .execute()
        )

        if response.data:

            st.markdown("""
            <div class="success-box">

                <div style="font-size:40px;">✅</div>

                <h3>Murakoze kwiyandikisha!</h3>

                <p>
                Amakuru yanyu yabitswe neza muri ADEPR KINYINYA.
                </p>

            </div>
            """, unsafe_allow_html=True)

        else:

            st.error(
                "❌ Amakuru ntabwo yabitswe."
            )

    except Exception as e:

        error_text = str(e)

        if "duplicate" in error_text.lower():

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

st.markdown("""
<div class="footer">

    ⛪ ADEPR KINYINYA<br>
    Management Information System<br>
    © 2026 ADEPR KINYINYA

</div>
""", unsafe_allow_html=True)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)
