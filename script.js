// ============================================================
// ADEPR KINYINYA REGISTRATION
// Supabase Connection
// ============================================================

const SUPABASE_URL =
    "https://mtvfebrbxalqymiiqtqe.supabase.co";

const SUPABASE_KEY =
    "sb_publishable_6rY0yOE6-A-tvmJFNRQBjA_Hwci4qlh";


// Create Supabase client
const supabaseClient =
    window.supabase.createClient(
        SUPABASE_URL,
        SUPABASE_KEY
    );


// ============================================================
// FORM
// ============================================================

const form =
    document.getElementById("memberForm");

const submitButton =
    document.getElementById("submitButton");

const buttonText =
    document.getElementById("buttonText");

const loadingText =
    document.getElementById("loadingText");

const message =
    document.getElementById("message");


// ============================================================
// MESSAGE FUNCTION
// ============================================================

function showMessage(text, type) {

    message.textContent = text;

    message.className =
        "message " + type;

    message.style.display =
        "block";

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}


// ============================================================
// GET VALUE
// ============================================================

function getValue(id) {

    const element =
        document.getElementById(id);

    if (!element) {
        return null;
    }

    const value =
        element.value.trim();

    return value === ""
        ? null
        : value;
}


// ============================================================
// FORM SUBMIT
// ============================================================

form.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        // ====================================================
        // REQUIRED FIELD
        // ====================================================

        const amazina =
            getValue("amazina");


        if (!amazina) {

            showMessage(
                "❌ Amazina ni yo yonyine asabwa.",
                "error"
            );

            document
                .getElementById("amazina")
                .focus();

            return;
        }


        // ====================================================
        // DISABLE BUTTON
        // ====================================================

        submitButton.disabled =
            true;

        buttonText.style.display =
            "none";

        loadingText.style.display =
            "inline";


        message.style.display =
            "none";


        // ====================================================
        // DATA
        // ====================================================

        const data = {

            // Personal
            amazina:
                amazina,

            telephone:
                getValue("telephone"),

            irangamuntu:
                getValue("irangamuntu"),

            itariki_yamavuko:
                getValue("itariki_yamavuko"),

            igitsina:
                getValue("igitsina"),

            aho_yabatirijwe:
                getValue("aho_yabatirijwe"),


            // Birthplace
            yavukiye_intara:
                getValue("yavukiye_intara"),

            yavukiye_akarere:
                getValue("yavukiye_akarere"),

            yavukiye_umurenge:
                getValue("yavukiye_umurenge"),

            yavukiye_akagari:
                getValue("yavukiye_akagari"),

            yavukiye_umudugudu:
                getValue("yavukiye_umudugudu"),


            // Current address
            atuye_intara:
                getValue("atuye_intara"),

            atuye_akarere:
                getValue("atuye_akarere"),

            atuye_umurenge:
                getValue("atuye_umurenge"),

            atuye_akagari:
                getValue("atuye_akagari"),

            atuye_umudugudu:
                getValue("atuye_umudugudu"),


            // Church
            igihande:
                getValue("igihande"),

            umurimo_itorero:
                getValue("umurimo_itorero"),

            chorale:
                getValue("chorale"),


            // Emergency
            emergency_contact:
                getValue("emergency_contact")

        };


        // ====================================================
        // SEND TO SUPABASE
        // ====================================================

        try {

            const {
                data: insertedData,
                error
            } =
                await supabaseClient
                    .from("members")
                    .insert([data])
                    .select();


            // =================================================
            // ERROR
            // =================================================

            if (error) {

                console.error(
                    "Supabase Error:",
                    error
                );

                throw error;
            }


            // =================================================
            // SUCCESS
            // =================================================

            console.log(
                "Saved member:",
                insertedData
            );


            showMessage(
                "✅ Murakoze! Amakuru yawe yabitswe neza muri ADEPR KINYINYA.",
                "success"
            );


            // Clear form
            form.reset();


        } catch (error) {

            console.error(error);


            let errorMessage =
                "❌ Habaye ikibazo mu kubika amakuru. Ongera ugerageze.";


            if (
                error.message &&
                error.message.includes("duplicate")
            ) {

                errorMessage =
                    "❌ Iyi nimero y'irangamuntu isanzwe iri muri system.";

            }


            showMessage(
                errorMessage,
                "error"
            );


        } finally {

            // =================================================
            // ENABLE BUTTON
            // =================================================

            submitButton.disabled =
                false;

            buttonText.style.display =
                "inline";

            loadingText.style.display =
                "none";
        }

    }
);
