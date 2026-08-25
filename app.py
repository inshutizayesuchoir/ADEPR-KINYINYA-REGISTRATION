import streamlit as st
from supabase import create_client, Client
from datetime import date
import re


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
# SUPABASE CONNECTION
# ============================================================

@st.cache_resource
def get_supabase() -> Client:

    try:

        supabase_url = st.secrets["SUPABASE_URL"]
        supabase_key = st.secrets["SUPABASE_KEY"]

        return create_client(
            supabase_url,
            supabase_key
        )

    except Exception as e:

        st.error(
            "❌ Habaye ikibazo mu guhuza na database."
        )

        st.code(str(e))

        st.stop()


supabase = get_supabase()


# ============================================================
# CUSTOM CSS
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
                rgba(30, 64, 175, 0.08),
                transparent 25%
            ),

            radial-gradient(
                circle at 95% 10%,
                rgba(5, 150, 105, 0.08),
                transparent 25%
            ),

            linear-gradient(
                135deg,
                #f8fafc 0%,
                #f1f5f9 50%,
                #ffffff 100%
            );
    }


    .block-container {

        max-width: 1100px !important;

        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
    }


    /* ========================================================
       HEADER
    ======================================================== */

    .main-header {

        background:
            linear-gradient(
                135deg,
                #0f172a 0%,
                #172554 45%,
                #1e3a8a 100%
            );

        border-radius: 28px;

        padding:
            45px
            30px
            42px
            30px;

        text-align: center;

        color: white;

        box-shadow:
            0 20px 50px
            rgba(15, 23, 42, 0.20);

        margin-bottom: 28px;

        position: relative;

        overflow: hidden;
    }


    .main-header::before {

        content: "";

        position: absolute;

        width: 260px;
        height: 260px;

        right: -100px;
        top: -130px;

        border-radius: 50%;

        background:
            rgba(255,255,255,0.07);
    }


    .main-header::after {

        content: "";

        position: absolute;

        width: 180px;
        height: 180px;

        left: -80px;
        bottom: -100px;

        border-radius: 50%;

        background:
            rgba(255,255,255,0.05);
    }


    .header-content {

        position: relative;

        z-index: 2;
    }


    .header-icon {

        width: 78px;
        height: 78px;

        margin:
            0 auto
            18px
            auto;

        display: flex;

        align-items: center;
        justify-content: center;

        border-radius: 22px;

        background:
            rgba(255,255,255,0.12);

        border:
            1px solid
            rgba(255,255,255,0.20);

        font-size: 40px;

        box-shadow:
            0 10px 25px
            rgba(0,0,0,0.15);
    }


    .main-header h1 {

        margin: 0;

        font-size: 40px;

        font-weight: 700;

        color: white !important;

        letter-spacing: 1px;
    }


    .header-line {

        width: 80px;

        height: 3px;

        margin:
            17px
            auto;

        border-radius: 10px;

        background:
            linear-gradient(
                90deg,
                #60a5fa,
                #34d399
            );
    }


    .main-header h2 {

        margin: 0;

        font-size: 22px;

        font-weight: 700;

        color: #e2e8f0 !important;

        letter-spacing: 0.5px;
    }


    .main-header p {

        margin:
            10px
            auto
            0
            auto;

        max-width: 700px;

        color:
            rgba(255,255,255,0.85);

        font-size: 15px;

        line-height: 1.7;
    }


    .header-note {

        margin-top: 17px !important;

        color:
            #d1fae5 !important;

        font-size: 13px !important;

        font-weight: 700;
    }


    /* ========================================================
       INTRO
    ======================================================== */

    .intro-card {

        background:
            rgba(255,255,255,0.96);

        border:
            1px solid #e2e8f0;

        border-radius: 20px;

        padding: 20px 23px;

        margin-bottom: 22px;

        box-shadow:
            0 8px 25px
            rgba(15,23,42,0.05);
    }


    .intro-title {

        color:
            #1e3a8a;

        font-size: 19px;

        font-weight: 700;

        margin-bottom: 5px;
    }


    .intro-text {

        color:
            #64748b;

        font-size: 13px;

        line-height: 1.7;
    }


    /* ========================================================
       SECTION CARDS
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
            0 8px 28px
            rgba(15,23,42,0.055);
    }


    .section-header {

        display: flex;

        align-items: center;

        gap: 14px;

        margin-bottom: 7px;

        padding-bottom: 15px;

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

        font-size: 22px;
    }


    .section-title {

        color:
            #1e3a8a;

        font-size: 20px;

        font-weight: 700;
    }


    .section-description {

        color:
            #64748b;

        font-size: 12px;

        line-height: 1.6;

        margin-bottom: 18px;
    }


    /* ========================================================
       INPUTS
    ======================================================== */

    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div,
    div[data-baseweb="textarea"] > div {

        background:
            #ffffff !important;

        border:
            1px solid #cbd5e1 !important;

        border-radius:
            11px !important;

        min-height:
            44px !important;

        transition:
            all 0.2s ease !important;
    }


    div[data-baseweb="input"] > div:hover,
    div[data-baseweb="select"] > div:hover,
    div[data-baseweb="textarea"] > div:hover {

        border-color:
            #94a3b8 !important;
    }


    div[data-baseweb="input"] > div:focus-within,
    div[data-baseweb="select"] > div:focus-within,
    div[data-baseweb="textarea"] > div:focus-within {

        border-color:
            #2563eb !important;

        box-shadow:
            0 0 0 3px
            rgba(37,99,235,0.10) !important;
    }


    .stTextInput label,
    .stSelectbox label,
    .stDateInput label {

        color:
            #334155 !important;

        font-size:
            13px !important;

        font-weight:
            700 !important;
    }


    /* ========================================================
       REQUIRED LABEL
    ======================================================== */

    .required-note {

        color:
            #64748b;

        font-size:
            12px;

        margin-top:
            -8px;

        margin-bottom:
            15px;
    }


    /* ========================================================
       SUBMIT BUTTON
    ======================================================== */

    .stButton > button {

        min-height:
            52px !important;

        border-radius:
            13px !important;

        font-family:
            Georgia,
            "Times New Roman",
            serif !important;

        font-size:
            16px !important;

        font-weight:
            700 !important;

        border:
            none !important;

        background:
            linear-gradient(
                135deg,
                #1e3a8a,
                #2563eb
            ) !important;

        color:
            white !important;

        box-shadow:
            0 10px 25px
            rgba(30,64,175,0.20);

        transition:
            all 0.2s ease !important;
    }


    .stButton > button:hover {

        transform:
            translateY(-2px);

        box-shadow:
            0 14px 30px
            rgba(30,64,175,0.25);
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

        border-radius:
            20px;

        padding:
            25px;

        text-align:
            center;

        margin:
            20px 0;
    }


    .success-icon {

        font-size:
            45px;

        margin-bottom:
            8px;
    }


    .success-title {

        color:
            #166534;

        font-size:
            22px;

        font-weight:
            700;

        margin-bottom:
            5px;
    }


    .success-text {

        color:
            #166534;

        font-size:
            14px;

        line-height:
            1.7;
    }


    /* ========================================================
       FOOTER
    ======================================================== */

    .footer {

        margin-top:
            35px;

        padding:
            35px
            25px;

        text-align:
            center;

        background:
            linear-gradient(
                135deg,
                #0f172a,
                #172554,
                #1e3a8a
            );

        border-radius:
            25px;

        color:
            white;

        box-shadow:
            0 15px 40px
            rgba(15,23,42,0.16);
    }


    .footer-title {

        font-size:
            23px;

        font-weight:
            700;

        margin-bottom:
            5px;
    }


    .footer-subtitle {

        color:
            #cbd5e1;

        font-size:
            13px;
    }


    .footer-divider {

        width:
            65px;

        height:
            2px;

        margin:
            18px
            auto;

        background:
            linear-gradient(
                90deg,
                #60a5fa,
                #34d399
            );

        border-radius:
            10px;
    }


    .help-box {

        max-width:
            650px;

        margin:
            0
            auto
            18px
            auto;

        display:
            flex;

        align-items:
            center;

        gap:
            14px;

        text-align:
            left;

        padding:
            16px 18px;

        border:
            1px solid
            rgba(255,255,255,0.12);

        background:
            rgba(255,255,255,0.06);

        border-radius:
            15px;
    }


    .help-icon {

        width:
            43px;

        height:
            43px;

        display:
            flex;

        align-items:
            center;

        justify-content:
            center;

        flex-shrink:
            0;

        border-radius:
            12px;

        background:
            rgba(255,255,255,0.10);

        font-size:
            20px;
    }


    .help-box strong {

        color:
            white;

        font-size:
            14px;
    }


    .help-box span {

        color:
            #cbd5e1;

        font-size:
            12px;

        line-height:
            1.6;
    }


    .contact {

        font-size:
            14px;

        color:
            #e2e8f0;

        margin-top:
            12px;
    }


    .copyright {

        margin-top:
            20px;

        padding-top:
            15px;

        border-top:
            1px solid
            rgba(255,255,255,0.10);

        color:
            #94a3b8;

        font-size:
            11px;
    }


    /* ========================================================
       MOBILE
    ======================================================== */

    @media (max-width: 768px) {

        .block-container {

            padding-left:
                1rem !important;

            padding-right:
                1rem !important;
        }


        .main-header {

            padding:
                32px
                20px;
        }


        .main-header h1 {

            font-size:
                30px;
        }


        .main-header h2 {

            font-size:
                18px;
        }


        .section-card {

            padding:
                18px;
        }


        .header-icon {

            width:
                65px;

            height:
                65px;

            font-size:
                32px;
        }


        .help-box {

            text-align:
                left;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="main-header">

        <div class="header-content">

            <div class="header-icon">
                ⛪
            </div>

            <h1>
                ADEPR KINYINYA
            </h1>

            <div class="header-line"></div>

            <h2>
                KWIYANDIKISHA NK'UMUKRISTO
            </h2>

            <p>
                Murakaza neza kuri gahunda yo kwiyandikisha
                nk'umukristo wa ADEPR Kinyinya.
            </p>

            <p class="header-note">
                ✦ Uzuza amakuru yawe neza kandi utange amakuru y'ukuri.
            </p>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# INTRODUCTION
# ============================================================

st.markdown(
    """
    <div class="intro-card">

        <div class="intro-title">
            📝 Amabwiriza yo Kwiyandikisha
        </div>

        <div class="intro-text">
            Amazina ni yo makuru y'ingenzi asabwa kugira ngo
            kwiyandikisha birangire. Andi makuru yose ushobora
            kuyuzuza niba uyafite.
        </div>

        <div class="required-note">
            <strong>*</strong> = Amakuru asabwa
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

            <div class="section-title">
                Imyirondoro y'Umukristo
            </div>

        </div>

        <div class="section-description">
            Amakuru y'ibanze ajyanye n'umukristo.
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
        placeholder="Urugero: 0787442721",
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
        value=date(2000, 1, 1),
        min_value=date(1900, 1, 1),
        max_value=date.today(),
        key="public_dob"
    )

    igitsina = st.selectbox(
        "Igitsina",
        [
            "Ntabwo nshaka kubivuga",
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

            <div class="section-title">
                Aho yavukiye
            </div>

        </div>

        <div class="section-description">
            Amakuru y'aho umunyamuryango yavukiye.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


birth1, birth2 = st.columns(2, gap="large")


with birth1:

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


with birth2:

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

            <div class="section-title">
                Aho atuye ubu
            </div>

        </div>

        <div class="section-description">
            Aho umunyamuryango asanzwe atuye muri iki gihe.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


current1, current2 = st.columns(2, gap="large")


with current1:

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


with current2:

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

            <div class="section-title">
                Amakuru y'Itorero
            </div>

        </div>

        <div class="section-description">
            Amakuru ajyanye n'uruhare rw'umukristo mu itorero.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


church1, church2 = st.columns(2, gap="large")


with church1:

    igihande = st.text_input(
        "Igihande abarizwamo",
        placeholder="Urugero: Igihande cya Kinyinya",
        key="public_igihande"
    )

    umurimo_itorero = st.selectbox(
        "Umurimo akora mu itorero",
        [
            "Umukristo",
            "Umuririmbyi",
            "Umudiyakoni",
            "Umuyobozi w'itorero"
        ],
        key="public_role"
    )


with church2:

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

            <div class="section-title">
                Uwo bahamagara habaye ikibazo
            </div>

        </div>

        <div class="section-description">
            Umuntu wahamagazwa mu gihe habaye ikibazo cyihutirwa.
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
# SUBMIT
# ============================================================

st.write("")


submit = st.button(
    "📋 OHEREZA KWiyANDIKISHA",
    use_container_width=True,
    type="primary",
    key="submit_registration"
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
            "❌ Amazina ni yo makuru asabwa. "
            "Nyamuneka andika amazina yawe mbere yo kohereza."
        )

        st.stop()


    # --------------------------------------------------------
    # TELEPHONE VALIDATION
    # --------------------------------------------------------

    cleaned_phone = telephone.strip()

    if cleaned_phone:

        phone_digits = re.sub(
            r"\D",
            "",
            cleaned_phone
        )

        if len(phone_digits) < 9:

            st.error(
                "❌ Telephone isa nk'aho ituzuye. "
                "Nyamuneka reba nomero wanditse."
            )

            st.stop()


    # --------------------------------------------------------
    # PREPARE DATA
    # --------------------------------------------------------

    data = {

        "amazina":
            amazina.strip(),

        "telephone":
            telephone.strip(),

        "irangamuntu":
            irangamuntu.strip()
            if irangamuntu.strip()
            else None,

        "itariki_yamavuko":
            str(itariki_yamavuko),

        "igitsina":
            igitsina
            if igitsina != ""
            else None,

        "aho_yabatirijwe":
            aho_yabatirijwe.strip(),

        "yavukiye_intara":
            yavukiye_intara
            if yavukiye_intara
            else None,

        "yavukiye_akarere":
            yavukiye_akarere.strip(),

        "yavukiye_umurenge":
            yavukiye_umurenge.strip(),

        "yavukiye_akagari":
            yavukiye_akagari.strip(),

        "yavukiye_umudugudu":
            yavukiye_umudugudu.strip(),

        "atuye_intara":
            atuye_intara
            if atuye_intara
            else None,

        "atuye_akarere":
            atuye_akarere.strip(),

        "atuye_umurenge":
            atuye_umurenge.strip(),

        "atuye_akagari":
            atuye_akagari.strip(),

        "atuye_umudugudu":
            atuye_umudugudu.strip(),

        "igihande":
            igihande.strip(),

        "umurimo_itorero":
            umurimo_itorero,

        "chorale":
            chorale.strip(),

        "emergency_contact":
            emergency_contact.strip()
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
                        Kwiyandikisha Byagenze Neza!
                    </div>

                    <div class="success-text">
                        Murakoze kwiyandikisha nk'umukristo
                        wa ADEPR Kinyinya.
                        <br>
                        Amakuru watanze yakiriwe kandi yabitswe
                        muri ADEPR Kinyinya Management Information System.
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.balloons()


        else:

            st.error(
                "❌ Ntabwo amakuru yashoboye kubikwa. "
                "Nyamuneka ongera ugerageze."
            )


    except Exception as e:

        st.error(
            "❌ Habaye ikibazo mu kohereza amakuru."
        )

        st.caption(
            "Niba ikibazo gikomeje, hamagara Steven kuri "
            "078 744 2721."
        )

        with st.expander("Technical information"):

            st.code(str(e))


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        <div class="footer-title">
            ⛪ ADEPR KINYINYA
        </div>

        <div class="footer-subtitle">
            Management Information System
        </div>

        <div class="footer-divider"></div>

        <div class="help-box">

            <div class="help-icon">
                💬
            </div>

            <div>

                <strong>
                    Ukeneye ubufasha?
                </strong>

                <br>

                <span>
                    Niba ufite ikibazo cyangwa ukeneye ubufasha
                    mu kwiyandikisha, turahari kugira ngo tugufashe.
                </span>

            </div>

        </div>

        <div class="contact">

            📞
            <strong>Steven:</strong>
            078 744 2721

        </div>

        <div class="copyright">

            © 2026 ADEPR KINYINYA · All Rights Reserved

        </div>

    </div>
    """,
    unsafe_allow_html=True
)
