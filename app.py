import streamlit as st
from supabase import create_client, Client
from datetime import date


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ADEPR KINYINYA | Kwiyandikisha",
    page_icon="⛪",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ============================================================
# SUPABASE CONNECTION
# ============================================================

try:

    SUPABASE_URL = st.secrets["SUPABASE_URL"]
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

    supabase: Client = create_client(
        SUPABASE_URL,
        SUPABASE_KEY
    )

except Exception as e:

    st.error(
        "❌ Supabase connection ntabwo yashoboye gutangira."
    )

    st.info(
        "Reba niba SUPABASE_URL na SUPABASE_KEY biri muri "
        "Streamlit App Settings → Secrets."
    )

    st.stop()


# ============================================================
# CUSTOM CSS — GEORGIA
# ============================================================

st.markdown(
    """
<style>

/* ============================================================
   GLOBAL
   ============================================================ */

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
            circle at 10% 8%,
            rgba(5,150,105,.10),
            transparent 28%
        ),

        radial-gradient(
            circle at 90% 10%,
            rgba(30,64,175,.10),
            transparent 28%
        ),

        radial-gradient(
            circle at 50% 100%,
            rgba(139,92,246,.06),
            transparent 30%
        ),

        linear-gradient(
            135deg,
            #f8fafc 0%,
            #eef2f7 50%,
            #f8fafc 100%
        );
}


/* ============================================================
   MAIN CONTAINER
   ============================================================ */

.block-container {

    max-width: 900px;

    padding-top: 2rem;
    padding-bottom: 3rem;

    padding-left: 1.2rem;
    padding-right: 1.2rem;
}


/* ============================================================
   HEADER
   ============================================================ */

.header {

    position: relative;

    overflow: hidden;

    background:

        linear-gradient(
            135deg,
            #0f172a 0%,
            #1e3a8a 45%,
            #064e3b 100%
        );

    padding: 42px 30px;

    border-radius: 27px;

    color: white;

    text-align: center;

    margin-bottom: 28px;

    box-shadow:
        0 18px 45px rgba(15,23,42,.20);
}


.header::before {

    content: "";

    position: absolute;

    width: 240px;
    height: 240px;

    right: -90px;
    top: -120px;

    border-radius: 50%;

    background:
        rgba(255,255,255,.08);
}


.header::after {

    content: "";

    position: absolute;

    width: 190px;
    height: 190px;

    left: -90px;
    bottom: -110px;

    border-radius: 50%;

    background:
        rgba(255,255,255,.06);
}


.header-icon {

    position: relative;

    z-index: 2;

    width: 72px;
    height: 72px;

    margin: auto;

    margin-bottom: 16px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 21px;

    background:
        rgba(255,255,255,.14);

    border:
        1px solid rgba(255,255,255,.25);

    font-size: 37px;

    box-shadow:
        0 8px 25px rgba(0,0,0,.12);
}


.header h1 {

    position: relative;

    z-index: 2;

    color: white;

    font-size: 39px;

    font-weight: 700;

    margin: 0;
}


.header-line {

    position: relative;

    z-index: 2;

    width: 75px;

    height: 3px;

    background: white;

    margin: 15px auto;

    border-radius: 20px;

    opacity: .85;
}


.header h2 {

    position: relative;

    z-index: 2;

    color: white;

    font-size: 19px;

    font-weight: 700;

    letter-spacing: 1px;

    margin: 0 0 11px 0;
}


.header p {

    position: relative;

    z-index: 2;

    color:
        rgba(255,255,255,.90);

    font-size: 14px;

    line-height: 1.6;

    margin: 5px 0;
}


.header-note {

    position: relative;

    z-index: 2;

    color:
        rgba(255,255,255,.72) !important;

    font-size: 12px !important;

    margin-top: 15px !important;
}


/* ============================================================
   FORM CONTAINER
   ============================================================ */

.form-card {

    background:
        rgba(255,255,255,.96);

    border:
        1px solid #e2e8f0;

    border-radius: 23px;

    padding: 30px;

    box-shadow:
        0 10px 32px rgba(15,23,42,.07);

    margin-bottom: 20px;
}


/* ============================================================
   SECTION TITLES
   ============================================================ */

.section-title {

    color: #064e3b;

    font-size: 22px;

    font-weight: 700;

    margin-top: 10px;

    margin-bottom: 5px;
}


.section-description {

    color: #64748b;

    font-size: 13px;

    line-height: 1.6;

    margin-bottom: 18px;
}


/* ============================================================
   INPUT LABELS
   ============================================================ */

.stTextInput label,
.stSelectbox label,
.stDateInput label {

    color:
        #334155 !important;

    font-family:
        Georgia,
        "Times New Roman",
        serif !important;

    font-weight:
        700 !important;

    font-size:
        13px !important;
}


/* ============================================================
   INPUT BOXES
   ============================================================ */

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {

    background:
        #ffffff !important;

    border:
        1px solid #cbd5e1 !important;

    border-radius:
        11px !important;

    min-height:
        43px !important;

    box-shadow:
        0 1px 2px rgba(15,23,42,.02) !important;
}


div[data-baseweb="input"] > div:hover,
div[data-baseweb="select"] > div:hover {

    border-color:
        #94a3b8 !important;
}


div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="select"] > div:focus-within {

    border-color:
        #059669 !important;

    box-shadow:
        0 0 0 2px rgba(5,150,105,.10) !important;
}


/* ============================================================
   DATE INPUT
   ============================================================ */

div[data-testid="stDateInput"] input {

    font-family:
        Georgia,
        "Times New Roman",
        serif !important;
}


/* ============================================================
   SELECTBOX
   ============================================================ */

div[data-baseweb="select"] {

    font-family:
        Georgia,
        "Times New Roman",
        serif !important;
}


/* ============================================================
   SUBMIT BUTTON
   ============================================================ */

.stButton > button {

    min-height:
        50px !important;

    border-radius:
        12px !important;

    font-family:
        Georgia,
        "Times New Roman",
        serif !important;

    font-size:
        16px !important;

    font-weight:
        700 !important;

    transition:
        all .18s ease !important;
}


button[kind="primary"] {

    background:

        linear-gradient(
            135deg,
            #047857,
            #059669
        ) !important;

    color:
        white !important;

    border:
        none !important;

    box-shadow:
        0 8px 20px rgba(5,150,105,.20);
}


button[kind="primary"]:hover {

    transform:
        translateY(-1px);

    box-shadow:
        0 12px 25px rgba(5,150,105,.27);
}


/* ============================================================
   SUCCESS MESSAGE
   ============================================================ */

.success-box {

    background:
        linear-gradient(
            135deg,
            #ecfdf5,
            #f0fdf4
        );

    border:
        1px solid #a7f3d0;

    color:
        #065f46;

    padding:
        22px;

    border-radius:
        17px;

    text-align:
        center;

    margin-top:
        20px;

    box-shadow:
        0 8px 22px rgba(5,150,105,.08);
}


.success-box-icon {

    font-size:
        42px;

    margin-bottom:
        5px;
}


.success-box-title {

    font-size:
        20px;

    font-weight:
        700;

    margin-bottom:
        5px;
}


.success-box-text {

    font-size:
        13px;

    color:
        #166534;
}


/* ============================================================
   HELP BOX
   ============================================================ */

.help-box {

    max-width:
        620px;

    margin:
        18px auto;

    display:
        flex;

    align-items:
        center;

    gap:
        14px;

    text-align:
        left;

    background:
        #f0fdf4;

    border:
        1px solid #bbf7d0;

    border-radius:
        16px;

    padding:
        16px 18px;

    color:
        #166534;
}


.help-icon {

    width:
        44px;

    height:
        44px;

    flex-shrink:
        0;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    border-radius:
        12px;

    background:
        #dcfce7;

    font-size:
        21px;
}


.help-box strong {

    font-size:
        14px;

    color:
        #166534;
}


.help-box span {

    font-size:
        12px;

    color:
        #4b5563;

    line-height:
        1.6;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {

    margin-top:
        30px;

    padding:
        30px 20px;

    text-align:
        center;

    background:
        rgba(255,255,255,.78);

    border:
        1px solid #e2e8f0;

    border-radius:
        22px;

    box-shadow:
        0 8px 25px rgba(15,23,42,.05);
}


.footer-title {

    color:
        #064e3b;

    font-size:
        21px;

    font-weight:
        700;
}


.footer-subtitle {

    color:
        #64748b;

    font-size:
        13px;

    margin-top:
        5px;
}


.footer-divider {

    width:
        55px;

    height:
        2px;

    background:
        #059669;

    margin:
        15px auto;

    border-radius:
        20px;
}


.contact {

    margin-top:
        12px;

    color:
        #1e3a8a;

    font-size:
        14px;
}


.copyright {

    margin-top:
        15px;

    color:
        #94a3b8;

    font-size:
        11px;
}


/* ============================================================
   ALERTS
   ============================================================ */

.stAlert {

    border-radius:
        13px !important;

    font-family:
        Georgia,
        "Times New Roman",
        serif !important;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 768px) {

    .block-container {

        padding-left:
            1rem;

        padding-right:
            1rem;

        padding-top:
            1rem;
    }


    .header {

        padding:
            32px 20px;

        border-radius:
            21px;
    }


    .header h1 {

        font-size:
            31px;
    }


    .header h2 {

        font-size:
            16px;
    }


    .form-card {

        padding:
            20px;

        border-radius:
            19px;
    }


    .section-title {

        font-size:
            19px;
    }


    .help-box {

        align-items:
            flex-start;
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
<div class="header">

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
""",
    unsafe_allow_html=True
)


# ============================================================
# FORM CARD START
# ============================================================

st.markdown(
    '<div class="form-card">',
    unsafe_allow_html=True
)


# ============================================================
# PERSONAL INFORMATION
# ============================================================

st.markdown(
    """
<div class="section-title">
    👤 Imyirondoro y'Umukristo
</div>

<div class="section-description">
    Amazina ni yo makuru asabwa. Andi makuru ushobora kuyuzuza
    niba uyafite.
</div>
""",
    unsafe_allow_html=True
)


# ------------------------------------------------------------
# NAME
# ------------------------------------------------------------

amazina = st.text_input(
    "Amazina *",
    placeholder="Urugero: UWIMANA Jean"
)


# ------------------------------------------------------------
# PHONE
# ------------------------------------------------------------

telephone = st.text_input(
    "Telephone",
    placeholder="Urugero: 078xxxxxxx"
)


# ------------------------------------------------------------
# NATIONAL ID
# ------------------------------------------------------------

irangamuntu = st.text_input(
    "Irangamuntu",
    placeholder="Nomero y'indangamuntu"
)


# ------------------------------------------------------------
# DOB + GENDER
# ------------------------------------------------------------

col1, col2 = st.columns(2, gap="large")


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


# ------------------------------------------------------------
# BAPTISM
# ------------------------------------------------------------

aho_yabatirijwe = st.text_input(
    "Aho yabatirijwe",
    placeholder="Urugero: ADEPR Kinyinya"
)


# ============================================================
# BIRTHPLACE
# ============================================================

st.markdown(
    """
<div class="section-title">
    📍 Aho yavukiye
</div>

<div class="section-description">
    Amakuru y'aho umunyamuryango yavukiye.
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
        ]
    )

    yavukiye_akarere = st.text_input(
        "Akarere yavukiyemo",
        placeholder="Urugero: Gasabo"
    )

    yavukiye_umurenge = st.text_input(
        "Umurenge yavukiyemo",
        placeholder="Urugero: Kinyinya"
    )


with col2:

    yavukiye_akagari = st.text_input(
        "Akagari yavukiyemo",
        placeholder="Urugero: Kagugu"
    )

    yavukiye_umudugudu = st.text_input(
        "Umudugudu yavukiyemo",
        placeholder="Izina ry'umudugudu"
    )


# ============================================================
# CURRENT ADDRESS
# ============================================================

st.markdown(
    """
<div class="section-title">
    🏠 Aho atuye ubu
</div>

<div class="section-description">
    Aho umunyamuryango asanzwe atuye muri iki gihe.
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
        ]
    )

    atuye_akarere = st.text_input(
        "Akarere atuyemo",
        placeholder="Urugero: Gasabo"
    )

    atuye_umurenge = st.text_input(
        "Umurenge atuyemo",
        placeholder="Urugero: Kinyinya"
    )


with col2:

    atuye_akagari = st.text_input(
        "Akagari atuyemo",
        placeholder="Urugero: Kagugu"
    )

    atuye_umudugudu = st.text_input(
        "Umudugudu atuyemo",
        placeholder="Izina ry'umudugudu"
    )


# ============================================================
# CHURCH INFORMATION
# ============================================================

st.markdown(
    """
<div class="section-title">
    ⛪ Amakuru y'Itorero
</div>

<div class="section-description">
    Amakuru ajyanye n'uruhare rw'umukristo mu itorero.
</div>
""",
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
# EMERGENCY CONTACT
# ============================================================

st.markdown(
    """
<div class="section-title">
    🚨 Uwo bahamagara habaye ikibazo
</div>

<div class="section-description">
    Umuntu wahamagazwa mu gihe habaye ikibazo cyihutirwa.
</div>
""",
    unsafe_allow_html=True
)


emergency_contact = st.text_input(
    "Amazina na Telephone",
    placeholder="Urugero: Jean Bosco - 078xxxxxxx"
)


# ============================================================
# SPACING
# ============================================================

st.write("")


# ============================================================
# SUBMIT BUTTON
# ============================================================

submitted = st.button(
    "💾 OHEREZA AMAKURU",
    type="primary",
    use_container_width=True
)


# ============================================================
# SAVE TO SUPABASE
# ============================================================

if submitted:

    # --------------------------------------------------------
    # ONLY REQUIRED FIELD
    # --------------------------------------------------------

    if not amazina.strip():

        st.error(
            "❌ Amazina y'umukristo ni ngombwa. "
            "Nyamuneka andika amazina mbere yo kohereza."
        )

        st.stop()


    # --------------------------------------------------------
    # PREPARE DATA
    # --------------------------------------------------------

    data = {

        "amazina":
            amazina.strip(),

        "telephone":
            telephone.strip()
            if telephone.strip()
            else None,

        "irangamuntu":
            irangamuntu.strip()
            if irangamuntu.strip()
            else None,

        "itariki_yamavuko":
            str(itariki_yamavuko)
            if itariki_yamavuko
            else None,

        "igitsina":
            igitsina
            if igitsina
            else None,

        "aho_yabatirijwe":
            aho_yabatirijwe.strip()
            if aho_yabatirijwe.strip()
            else None,

        "yavukiye_intara":
            yavukiye_intara
            if yavukiye_intara
            else None,

        "yavukiye_akarere":
            yavukiye_akarere.strip()
            if yavukiye_akarere.strip()
            else None,

        "yavukiye_umurenge":
            yavukiye_umurenge.strip()
            if yavukiye_umurenge.strip()
            else None,

        "yavukiye_akagari":
            yavukiye_akagari.strip()
            if yavukiye_akagari.strip()
            else None,

        "yavukiye_umudugudu":
            yavukiye_umudugudu.strip()
            if yavukiye_umudugudu.strip()
            else None,

        "atuye_intara":
            atuye_intara
            if atuye_intara
            else None,

        "atuye_akarere":
            atuye_akarere.strip()
            if atuye_akarere.strip()
            else None,

        "atuye_umurenge":
            atuye_umurenge.strip()
            if atuye_umurenge.strip()
            else None,

        "atuye_akagari":
            atuye_akagari.strip()
            if atuye_akagari.strip()
            else None,

        "atuye_umudugudu":
            atuye_umudugudu.strip()
            if atuye_umudugudu.strip()
            else None,

        "igihande":
            igihande.strip()
            if igihande.strip()
            else None,

        "umurimo_itorero":
            umurimo_itorero
            if umurimo_itorero
            else None,

        "chorale":
            chorale.strip()
            if chorale.strip()
            else None,

        "emergency_contact":
            emergency_contact.strip()
            if emergency_contact.strip()
            else None
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


        # ----------------------------------------------------
        # SUCCESS
        # ----------------------------------------------------

        if response.data:

            st.markdown(
                """
                <div class="success-box">

                    <div class="success-box-icon">
                        ✅
                    </div>

                    <div class="success-box-title">
                        Murakoze kwiyandikisha!
                    </div>

                    <div class="success-box-text">
                        Amakuru yanyu yabitswe neza muri
                        ADEPR KINYINYA.
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.error(
                "❌ Amakuru ntabwo yabitswe. "
                "Nyamuneka ongera ugerageze."
            )


    # --------------------------------------------------------
    # ERROR
    # --------------------------------------------------------

    except Exception as e:

        error_text = str(e).lower()


        if "duplicate" in error_text:

            st.error(
                "❌ Iyi ndangamuntu isanzwe iri muri system."
            )


        elif "unique" in error_text:

            st.error(
                "❌ Amakuru watanze asanzwe ari muri system."
            )


        else:

            st.error(
                "❌ Habaye ikibazo mu kubika amakuru."
            )

            st.caption(
                f"Technical error: {e}"
            )


# ============================================================
# CLOSE FORM CARD
# ============================================================

st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# ============================================================
# HELP SECTION
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
