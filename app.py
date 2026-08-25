import streamlit as st
from datetime import date
from supabase import create_client


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ADEPR KINYINYA | Kwiyandikisha",
    page_icon="⛪",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# SUPABASE CONNECTION
# ============================================================

@st.cache_resource
def get_supabase():

    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]

        return create_client(url, key)

    except Exception as e:

        st.error(
            "❌ Ntibyashobotse guhuza na Supabase."
        )

        st.code(str(e))

        st.stop()


supabase = get_supabase()


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GLOBAL
    ======================================================== */

    html,
    body,
    [class*="css"],
    [class*="st-"],
    .stApp {

        font-family:
            Georgia,
            "Times New Roman",
            serif !important;
    }


    .stApp {

        background:
            radial-gradient(
                circle at 5% 5%,
                rgba(30, 58, 138, 0.10),
                transparent 25%
            ),

            radial-gradient(
                circle at 95% 10%,
                rgba(5, 150, 105, 0.10),
                transparent 25%
            ),

            linear-gradient(
                135deg,
                #f8fafc 0%,
                #eef2ff 50%,
                #f8fafc 100%
            );
    }


    .block-container {

        max-width: 1200px !important;

        padding-top: 2rem !important;
        padding-bottom: 4rem !important;
    }


    /* ========================================================
       HIDE STREAMLIT ELEMENTS
       ======================================================== */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }


    /* ========================================================
       HERO
       ======================================================== */

    .hero {

        position: relative;

        overflow: hidden;

        background:
            linear-gradient(
                135deg,
                #172554 0%,
                #1e3a8a 45%,
                #047857 100%
            );

        border-radius: 28px;

        padding:
            45px
            40px
            42px
            40px;

        margin-bottom: 25px;

        color: white;

        box-shadow:
            0 22px 55px
            rgba(15, 23, 42, 0.20);
    }


    .hero::before {

        content: "";

        position: absolute;

        width: 300px;
        height: 300px;

        right: -100px;
        top: -150px;

        border-radius: 50%;

        background:
            rgba(255,255,255,0.08);
    }


    .hero::after {

        content: "";

        position: absolute;

        width: 220px;
        height: 220px;

        left: 45%;
        bottom: -150px;

        border-radius: 50%;

        background:
            rgba(255,255,255,0.06);
    }


    .hero-content {

        position: relative;

        z-index: 2;
    }


    .hero-icon {

        width: 70px;
        height: 70px;

        display: flex;

        align-items: center;
        justify-content: center;

        background:
            rgba(255,255,255,0.14);

        border:
            1px solid
            rgba(255,255,255,0.22);

        border-radius: 20px;

        font-size: 36px;

        margin-bottom: 18px;
    }


    .hero-title {

        font-size: 38px;

        font-weight: 700;

        line-height: 1.15;

        margin: 0;

        color: white;
    }


    .hero-subtitle {

        font-size: 18px;

        margin-top: 9px;

        color:
            rgba(255,255,255,0.90);
    }


    .hero-description {

        max-width: 760px;

        margin-top: 14px;

        font-size: 14px;

        line-height: 1.7;

        color:
            rgba(255,255,255,0.82);
    }


    /* ========================================================
       WELCOME NOTICE
       ======================================================== */

    .welcome-card {

        background:
            rgba(255,255,255,0.95);

        border:
            1px solid #dbeafe;

        border-left:
            5px solid #1e3a8a;

        border-radius: 18px;

        padding: 20px 22px;

        margin-bottom: 22px;

        box-shadow:
            0 8px 25px
            rgba(15,23,42,0.06);
    }


    .welcome-title {

        color: #172554;

        font-size: 20px;

        font-weight: 700;

        margin-bottom: 5px;
    }


    .welcome-text {

        color: #64748b;

        font-size: 13px;

        line-height: 1.7;
    }


    /* ========================================================
       SECTION CARD
       ======================================================== */

    .section-card {

        background:
            rgba(255,255,255,0.97);

        border:
            1px solid #e2e8f0;

        border-radius: 22px;

        padding: 25px;

        margin-bottom: 20px;

        box-shadow:
            0 10px 30px
            rgba(15,23,42,0.055);
    }


    .section-header {

        display: flex;

        align-items: center;

        gap: 14px;

        margin-bottom: 20px;

        padding-bottom: 16px;

        border-bottom:
            1px solid #e5e7eb;
    }


    .section-icon {

        width: 48px;
        height: 48px;

        display: flex;

        align-items: center;
        justify-content: center;

        flex-shrink: 0;

        border-radius: 14px;

        background:
            linear-gradient(
                135deg,
                #eff6ff,
                #dbeafe
            );

        border:
            1px solid #bfdbfe;

        font-size: 23px;
    }


    .section-title {

        color: #172554;

        font-size: 20px;

        font-weight: 700;

        margin: 0;
    }


    .section-subtitle {

        color: #64748b;

        font-size: 12px;

        margin-top: 3px;
    }


    /* ========================================================
       INPUTS
       ======================================================== */

    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div,
    div[data-baseweb="textarea"] > div {

        background:
            white !important;

        border:
            1px solid #cbd5e1 !important;

        border-radius:
            11px !important;

        min-height:
            44px;
    }


    div[data-baseweb="input"] > div:hover,
    div[data-baseweb="select"] > div:hover,
    div[data-baseweb="textarea"] > div:hover {

        border-color:
            #64748b !important;
    }


    div[data-baseweb="input"] > div:focus-within,
    div[data-baseweb="select"] > div:focus-within,
    div[data-baseweb="textarea"] > div:focus-within {

        border-color:
            #1e3a8a !important;

        box-shadow:
            0 0 0 2px
            rgba(30,58,138,0.10) !important;
    }


    .stTextInput label,
    .stSelectbox label,
    .stDateInput label {

        color:
            #334155 !important;

        font-weight:
            700 !important;

        font-size:
            13px !important;
    }


    /* ========================================================
       REQUIRED LABEL
       ======================================================== */

    .required-note {

        color: #64748b;

        font-size: 12px;

        margin-top: -5px;

        margin-bottom: 15px;
    }


    .required-star {

        color: #dc2626;

        font-weight: 700;
    }


    /* ========================================================
       SUBMIT BUTTON
       ======================================================== */

    .stButton > button {

        min-height: 52px !important;

        border-radius: 13px !important;

        font-family:
            Georgia,
            "Times New Roman",
            serif !important;

        font-size: 16px !important;

        font-weight: 700 !important;

        border: none !important;

        background:
            linear-gradient(
                135deg,
                #1e3a8a,
                #047857
            ) !important;

        color: white !important;

        box-shadow:
            0 10px 25px
            rgba(30,58,138,0.20);

        transition:
            all 0.2s ease;
    }


    .stButton > button:hover {

        transform:
            translateY(-2px);

        box-shadow:
            0 14px 30px
            rgba(30,58,138,0.27);
    }


    /* ========================================================
       SUCCESS CARD
       ======================================================== */

    .success-card {

        background:
            linear-gradient(
                135deg,
                #ecfdf5,
                #f0fdf4
            );

        border:
            1px solid #86efac;

        border-radius: 20px;

        padding: 30px;

        text-align: center;

        margin: 20px 0;

        box-shadow:
            0 12px 30px
            rgba(22,101,52,0.08);
    }


    .success-icon {

        font-size: 50px;

        margin-bottom: 10px;
    }


    .success-title {

        color: #166534;

        font-size: 24px;

        font-weight: 700;
    }


    .success-text {

        color: #475569;

        font-size: 14px;

        margin-top: 8px;

        line-height: 1.7;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {

        text-align: center;

        padding:
            25px 10px 10px;

        color: #64748b;

        font-size: 12px;

        line-height: 1.7;
    }


    .footer-title {

        color: #172554;

        font-size: 15px;

        font-weight: 700;

        margin-bottom: 3px;
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 768px) {

        .block-container {

            padding-left: 1rem !important;

            padding-right: 1rem !important;
        }


        .hero {

            padding: 30px 23px;

            border-radius: 22px;
        }


        .hero-title {

            font-size: 29px;
        }


        .hero-subtitle {

            font-size: 16px;
        }


        .section-card {

            padding: 18px;

            border-radius: 18px;
        }


        .section-title {

            font-size: 18px;
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

        <div class="hero-content">

            <div class="hero-icon">
                ⛪
            </div>

            <div class="hero-title">
                ADEPR KINYINYA
            </div>

            <div class="hero-subtitle">
                Kwiyandikisha k'Umukristo
            </div>

            <div class="hero-description">
                Murakaza neza ku rubuga rwo kwiyandikisha
                rw'Itorero rya ADEPR Kinyinya.
                Uzuza amakuru akurikira kugira ngo
                amakuru yawe abikwe muri sisitemu y'Itorero.
            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# WELCOME
# ============================================================

st.markdown(
    """
    <div class="welcome-card">

        <div class="welcome-title">
            👋 Murakaza neza
        </div>

        <div class="welcome-text">
            Nyamuneka tanga amakuru yawe neza.
            <b>Amazina ni yo makuru yonyine agomba kuzuzwa.</b>
            Andi makuru ushobora kuyatanga niba uyafite.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PERSONAL INFORMATION
# ============================================================

st.markdown(
    """
    <div class="section-card">

        <div class="section-header">

            <div class="section-icon">
                👤
            </div>

            <div>

                <div class="section-title">
                    Imyirondoro y'Umukristo
                </div>

                <div class="section-subtitle">
                    Amakuru y'ibanze ajyanye n'umunyamuryango.
                </div>

            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns(2, gap="large")


with col1:

    amazina = st.text_input(
        "Amazina *",
        placeholder="Urugero: UWIMANA Jean",
        key="public_amazina"
    )

    telephone = st.text_input(
        "Telephone",
        placeholder="Urugero: 078xxxxxxx",
        key="public_telephone"
    )

    irangamuntu = st.text_input(
        "Irangamuntu",
        placeholder="Nomero y'indangamuntu",
        key="public_irangamuntu"
    )


with col2:

    itariki_yamavuko = st.date_input(
        "Itariki y'amavuko",
        value=None,
        min_value=date(1900, 1, 1),
        max_value=date.today(),
        key="public_dob"
    )

    igitsina = st.selectbox(
        "Igitsina",
        [
            "",
            "Gabo",
            "Gore"
        ],
        key="public_gender"
    )

    aho_yabatirijwe = st.text_input(
        "Aho yabatirijwe",
        placeholder="Urugero: ADEPR Kinyinya",
        key="public_baptism"
    )


st.markdown(
    '<div class="required-note">'
    '<span class="required-star">*</span> Amazina ni yo yonyine asabwa.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# BIRTHPLACE
# ============================================================

st.markdown(
    """
    <div class="section-card">

        <div class="section-header">

            <div class="section-icon">
                📍
            </div>

            <div>

                <div class="section-title">
                    Aho Yavukiye
                </div>

                <div class="section-subtitle">
                    Amakuru y'aho umunyamuryango yavukiye.
                </div>

            </div>

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
            "",
            "Kigali",
            "Iburasirazuba",
            "Amajyepfo",
            "Amajyaruguru",
            "Iburengerazuba",
            "Hanze y'u Rwanda"
        ],
        key="public_birth_province"
    )

    yavukiye_akarere = st.text_input(
        "Akarere yavukiyemo",
        placeholder="Urugero: Gasabo",
        key="public_birth_district"
    )

    yavukiye_umurenge = st.text_input(
        "Umurenge yavukiyemo",
        placeholder="Urugero: Kinyinya",
        key="public_birth_sector"
    )


with col2:

    yavukiye_akagari = st.text_input(
        "Akagari yavukiyemo",
        placeholder="Urugero: Kagugu",
        key="public_birth_cell"
    )

    yavukiye_umudugudu = st.text_input(
        "Umudugudu yavukiyemo",
        placeholder="Izina ry'umudugudu",
        key="public_birth_village"
    )


# ============================================================
# CURRENT ADDRESS
# ============================================================

st.markdown(
    """
    <div class="section-card">

        <div class="section-header">

            <div class="section-icon">
                🏠
            </div>

            <div>

                <div class="section-title">
                    Aho Atuya Ubu
                </div>

                <div class="section-subtitle">
                    Aho umunyamuryango asanzwe atuye muri iki gihe.
                </div>

            </div>

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
            "",
            "Kigali",
            "Iburasirazuba",
            "Amajyepfo",
            "Amajyaruguru",
            "Iburengerazuba",
            "Hanze y'u Rwanda"
        ],
        key="public_current_province"
    )

    atuye_akarere = st.text_input(
        "Akarere atuyemo",
        placeholder="Urugero: Gasabo",
        key="public_current_district"
    )

    atuye_umurenge = st.text_input(
        "Umurenge atuyemo",
        placeholder="Urugero: Kinyinya",
        key="public_current_sector"
    )


with col2:

    atuye_akagari = st.text_input(
        "Akagari atuyemo",
        placeholder="Urugero: Kagugu",
        key="public_current_cell"
    )

    atuye_umudugudu = st.text_input(
        "Umudugudu atuyemo",
        placeholder="Izina ry'umudugudu",
        key="public_current_village"
    )


# ============================================================
# CHURCH INFORMATION
# ============================================================

st.markdown(
    """
    <div class="section-card">

        <div class="section-header">

            <div class="section-icon">
                ⛪
            </div>

            <div>

                <div class="section-title">
                    Amakuru y'Itorero
                </div>

                <div class="section-subtitle">
                    Amakuru ajyanye n'umurimo n'uruhare mu Itorero.
                </div>

            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns(2, gap="large")


with col1:

    igihande = st.text_input(
        "Igihande abarizwamo",
        placeholder="Urugero: Igihande cya Kinyinya",
        key="public_igihande"
    )

    umurimo_itorero = st.selectbox(
        "Umurimo akora mu Itorero",
        [
            "",
            "Umuyobozi w'itorero",
            "Umudiyakoni",
            "Umuririmbyi",
            "Umukristo"
        ],
        key="public_role"
    )


with col2:

    chorale = st.text_input(
        "Chorale aririmbamo",
        placeholder="Urugero: Inshuti za Yesu",
        key="public_chorale"
    )


# ============================================================
# EMERGENCY CONTACT
# ============================================================

st.markdown(
    """
    <div class="section-card">

        <div class="section-header">

            <div class="section-icon">
                🚨
            </div>

            <div>

                <div class="section-title">
                    Uwo Bahamagara Habaye Ikibazo
                </div>

                <div class="section-subtitle">
                    Umuntu wahamagazwa mu gihe habaye ikibazo cyihutirwa.
                </div>

            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


emergency_contact = st.text_input(
    "Amazina na Telephone",
    placeholder="Urugero: Jean Bosco - 078xxxxxxx",
    key="public_emergency"
)


# ============================================================
# SUBMIT AREA
# ============================================================

st.write("")


st.markdown(
    """
    <div style="
        text-align:center;
        color:#64748b;
        font-size:13px;
        margin-bottom:12px;
    ">
        Nyuma yo kugenzura amakuru watanze,
        kanda kuri buto iri hasi.
    </div>
    """,
    unsafe_allow_html=True
)


submit = st.button(
    "📨 OHEREZA AMAKURU",
    use_container_width=True,
    type="primary"
)


# ============================================================
# SAVE TO SUPABASE
# ============================================================

if submit:

    # --------------------------------------------------------
    # ONLY REQUIRED FIELD
    # --------------------------------------------------------

    if not amazina.strip():

        st.error(
            "❌ Amazina arakenewe. "
            "Nyamuneka andika amazina yawe mbere yo kohereza."
        )

        st.stop()


    # --------------------------------------------------------
    # PREPARE DATA
    # --------------------------------------------------------

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
            if igitsina
            else None,

        "aho_yabatirijwe":
            aho_yabatirijwe.strip() or None,

        "yavukiye_intara":
            yavukiye_intara
            if yavukiye_intara
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
            if atuye_intara
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
            if umurimo_itorero
            else None,

        "chorale":
            chorale.strip() or None,

        "emergency_contact":
            emergency_contact.strip() or None
    }


    # --------------------------------------------------------
    # INSERT
    # --------------------------------------------------------

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
                <div class="success-card">

                    <div class="success-icon">
                        ✅
                    </div>

                    <div class="success-title">
                        Amakuru yoherejwe neza!
                    </div>

                    <div class="success-text">
                        Murakoze kwiyandikisha muri
                        <b>ADEPR Kinyinya</b>.
                        Amakuru yawe yabitswe neza
                        muri sisitemu y'Itorero.
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


            st.balloons()


        else:

            st.error(
                "❌ Amakuru ntiyabitswe. "
                "Nyamuneka ongera ugerageze."
            )


    except Exception as e:

        error_text = str(e)

        # ----------------------------------------------------
        # FRIENDLY UNIQUE ID ERROR
        # ----------------------------------------------------

        if (
            "duplicate" in error_text.lower()
            or "unique" in error_text.lower()
            or "irangamuntu" in error_text.lower()
        ):

            st.error(
                "❌ Iyi nimero y'irangamuntu isanzwe "
                "iri muri sisitemu."
            )

        else:

            st.error(
                "❌ Habaye ikibazo mu kohereza amakuru."
            )

            with st.expander("Technical details"):

                st.code(error_text)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        <div class="footer-title">
            ⛪ ADEPR KINYINYA
        </div>

        Management Information System

        <br>

        Kwiyandikisha k'Umukristo

        <br><br>

        © 2026 ADEPR Kinyinya
    </div>
    """,
    unsafe_allow_html=True
)
