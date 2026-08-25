/* =========================================================
   ADEPR KINYINYA REGISTRATION
   SUPABASE CONNECTION
========================================================= */


/* =========================================================
   SUPABASE
========================================================= */

const SUPABASE_URL =
    "https://mtvfebrbxalqymiiqtqe.supabase.co";

const SUPABASE_PUBLISHABLE_KEY =
    "sb_publishable_6rY0yOE6-A-tvmJFNRQBjA_Hwci4qlh";


const supabaseClient =
    window.supabase.createClient(
        SUPABASE_URL,
        SUPABASE_PUBLISHABLE_KEY
    );


/* =========================================================
   RWANDA ADMINISTRATIVE DATA
   API SOURCE
========================================================= */

const RWANDA_API =
    "https://rwanda-province-district-sector-cel.vercel.app/api";


/* =========================================================
   ELEMENT HELPERS
========================================================= */

function getElement(id) {

    return document.getElementById(id);

}


function clearSelect(select, placeholder) {

    select.innerHTML = "";

    const option =
        document.createElement("option");

    option.value = "";

    option.textContent = placeholder;

    select.appendChild(option);

}


function setLoading(select, text) {

    select.disabled = true;

    clearSelect(select, text);

}


/* =========================================================
   FETCH JSON
========================================================= */

async function getJSON(url) {

    const response =
        await fetch(url);

    if (!response.ok) {

        throw new Error(
            "Location data could not be loaded."
        );

    }

    return await response.json();

}


/* =========================================================
   ADD OPTIONS
========================================================= */

function addOptions(
    select,
    items,
    valueKey,
    textKey
) {

    items.forEach(item => {

        const option =
            document.createElement("option");

        option.value =
            item[valueKey];

        option.textContent =
            item[textKey];

        select.appendChild(option);

    });

}


/* =========================================================
   PROVINCES
========================================================= */

async function loadProvinces(
    provinceSelect
) {

    clearSelect(
        provinceSelect,
        "Hitamo Intara"
    );

    try {

        const data =
            await getJSON(
                `${RWANDA_API}/provinces`
            );


        /*
         The API normally returns:
         [
             {
                id: 1,
                provinceName: "Kigali"
             }
         ]
        */

        data.forEach(item => {

            const option =
                document.createElement("option");

            option.value =
                item.id;

            option.textContent =
                item.provinceName;

            provinceSelect.appendChild(
                option
            );

        });

        provinceSelect.disabled = false;

    } catch (error) {

        console.error(error);

        clearSelect(
            provinceSelect,
            "Andika Intara"
        );

        provinceSelect.disabled = false;

    }

}


/* =========================================================
   DISTRICTS
========================================================= */

async function loadDistricts(
    provinceId,
    districtSelect,
    sectorSelect,
    cellSelect,
    villageSelect
) {

    setLoading(
        districtSelect,
        "Gutegereza Akarere..."
    );

    setLoading(
        sectorSelect,
        "Banza uhitemo Akarere"
    );

    setLoading(
        cellSelect,
        "Banza uhitemo Umurenge"
    );

    setLoading(
        villageSelect,
        "Banza uhitemo Akagari"
    );


    if (!provinceId) {

        clearSelect(
            districtSelect,
            "Banza uhitemo Intara"
        );

        districtSelect.disabled = true;

        return;

    }


    try {

        const data =
            await getJSON(
                `${RWANDA_API}/districts/${provinceId}`
            );


        clearSelect(
            districtSelect,
            "Hitamo Akarere"
        );


        data.forEach(item => {

            const option =
                document.createElement("option");

            option.value =
                item.id;

            option.textContent =
                item.districtName;

            districtSelect.appendChild(
                option
            );

        });


        districtSelect.disabled = false;

    } catch (error) {

        console.error(error);

        clearSelect(
            districtSelect,
            "Andika Akarere"
        );

        districtSelect.disabled = false;

    }

}


/* =========================================================
   SECTORS
========================================================= */

async function loadSectors(
    provinceId,
    districtId,
    sectorSelect,
    cellSelect,
    villageSelect
) {

    setLoading(
        sectorSelect,
        "Gutegereza Umurenge..."
    );

    setLoading(
        cellSelect,
        "Banza uhitemo Umurenge"
    );

    setLoading(
        villageSelect,
        "Banza uhitemo Akagari"
    );


    if (!districtId) {

        clearSelect(
            sectorSelect,
            "Banza uhitemo Akarere"
        );

        sectorSelect.disabled = true;

        return;

    }


    try {

        const url =
            `${RWANDA_API}/sectors/${provinceId}/${districtId}`;


        const data =
            await getJSON(url);


        clearSelect(
            sectorSelect,
            "Hitamo Umurenge"
        );


        data.forEach(item => {

            const option =
                document.createElement("option");

            option.value =
                item.id;

            option.textContent =
                item.sectorName;

            sectorSelect.appendChild(
                option
            );

        });


        sectorSelect.disabled = false;

    } catch (error) {

        console.error(error);

        clearSelect(
            sectorSelect,
            "Andika Umurenge"
        );

        sectorSelect.disabled = false;

    }

}


/* =========================================================
   CELLS
========================================================= */

async function loadCells(
    provinceId,
    districtId,
    sectorId,
    cellSelect,
    villageSelect
) {

    setLoading(
        cellSelect,
        "Gutegereza Akagari..."
    );

    setLoading(
        villageSelect,
        "Banza uhitemo Akagari"
    );


    if (!sectorId) {

        clearSelect(
            cellSelect,
            "Banza uhitemo Umurenge"
        );

        cellSelect.disabled = true;

        return;

    }


    try {

        const url =
            `${RWANDA_API}/cells/${provinceId}/${districtId}/${sectorId}`;


        const data =
            await getJSON(url);


        clearSelect(
            cellSelect,
            "Hitamo Akagari"
        );


        data.forEach(item => {

            const option =
                document.createElement("option");

            option.value =
                item.id;

            option.textContent =
                item.cellName;

            cellSelect.appendChild(
                option
            );

        });


        cellSelect.disabled = false;

    } catch (error) {

        console.error(error);

        clearSelect(
            cellSelect,
            "Andika Akagari"
        );

        cellSelect.disabled = false;

    }

}


/* =========================================================
   VILLAGES
========================================================= */

async function loadVillages(
    provinceId,
    districtId,
    sectorId,
    cellId,
    villageSelect
) {

    setLoading(
        villageSelect,
        "Gutegereza Umudugudu..."
    );


    if (!cellId) {

        clearSelect(
            villageSelect,
            "Banza uhitemo Akagari"
        );

        villageSelect.disabled = true;

        return;

    }


    try {

        const url =
            `${RWANDA_API}/villages/${provinceId}/${districtId}/${sectorId}/${cellId}`;


        const data =
            await getJSON(url);


        clearSelect(
            villageSelect,
            "Hitamo Umudugudu"
        );


        data.forEach(item => {

            const option =
                document.createElement("option");

            option.value =
                item.id;

            option.textContent =
                item.villageName;

            villageSelect.appendChild(
                option
            );

        });


        villageSelect.disabled = false;

    } catch (error) {

        console.error(error);

        clearSelect(
            villageSelect,
            "Andika Umudugudu"
        );

        villageSelect.disabled = false;

    }

}


/* =========================================================
   LOCATION SETUP
========================================================= */

function setupLocation(prefix) {

    const province =
        getElement(
            `${prefix}_province`
        );

    const district =
        getElement(
            `${prefix}_district`
        );

    const sector =
        getElement(
            `${prefix}_sector`
        );

    const cell =
        getElement(
            `${prefix}_cell`
        );

    const village =
        getElement(
            `${prefix}_village`
        );


    /*
     Load provinces
    */

    loadProvinces(
        province
    );


    /*
     Province changed
    */

    province.addEventListener(
        "change",
        function () {

            loadDistricts(
                this.value,
                district,
                sector,
                cell,
                village
            );

        }
    );


    /*
     District changed
    */

    district.addEventListener(
        "change",
        function () {

            loadSectors(
                province.value,
                this.value,
                sector,
                cell,
                village
            );

        }
    );


    /*
     Sector changed
    */

    sector.addEventListener(
        "change",
        function () {

            loadCells(
                province.value,
                district.value,
                this.value,
                cell,
                village
            );

        }
    );


    /*
     Cell changed
    */

    cell.addEventListener(
        "change",
        function () {

            loadVillages(
                province.value,
                district.value,
                sector.value,
                this.value,
                village
            );

        }
    );

}


/* =========================================================
   INITIALIZE LOCATIONS
========================================================= */

document.addEventListener(
    "DOMContentLoaded",
    function () {

        setupLocation(
            "birth"
        );

        setupLocation(
            "current"
        );

    }
);


/* =========================================================
   VALUE HELPER
========================================================= */

function value(id) {

    const element =
        getElement(id);

    if (!element) {

        return null;

    }

    const result =
        element.value.trim();

    return result === ""
        ? null
        : result;

}


/* =========================================================
   FORM
========================================================= */

const form =
    getElement("memberForm");


form.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        /*
         Hide old messages
        */

        getElement(
            "successMessage"
        ).classList.add("hidden");

        getElement(
            "errorMessage"
        ).classList.add("hidden");


        /*
         Button loading
        */

        const button =
            getElement("submitButton");

        const buttonText =
            getElement("buttonText");

        const spinner =
            getElement("loadingSpinner");


        button.disabled = true;

        buttonText.textContent =
            "Kubika amakuru...";

        spinner.classList.remove(
            "hidden"
        );


        /*
         Prepare data
        */

        const data = {

            amazina:
                value("amazina"),

            telephone:
                value("telephone"),

            irangamuntu:
                value("irangamuntu"),

            itariki_yamavuko:
                value("itariki_yamavuko"),

            igitsina:
                value("igitsina"),

            aho_yabatirijwe:
                value("aho_yabatirijwe"),


            /*
             Birthplace
            */

            yavukiye_intara:
                getSelectedText(
                    "birth_province"
                ),

            yavukiye_akarere:
                getSelectedText(
                    "birth_district"
                ),

            yavukiye_umurenge:
                getSelectedText(
                    "birth_sector"
                ),

            yavukiye_akagari:
                getSelectedText(
                    "birth_cell"
                ),

            yavukiye_umudugudu:
                getSelectedText(
                    "birth_village"
                ),


            /*
             Current residence
            */

            atuye_intara:
                getSelectedText(
                    "current_province"
                ),

            atuye_akarere:
                getSelectedText(
                    "current_district"
                ),

            atuye_umurenge:
                getSelectedText(
                    "current_sector"
                ),

            atuye_akagari:
                getSelectedText(
                    "current_cell"
                ),

            atuye_umudugudu:
                getSelectedText(
                    "current_village"
                ),


            /*
             Church
            */

            igihande:
                value("igihande"),

            umurimo_itorero:
                value("umurimo_itorero"),

            chorale:
                value("chorale"),


            /*
             Emergency
            */

            emergency_contact:
                value("emergency_contact")

        };


        /*
         Empty strings -> null
        */

        Object.keys(data).forEach(
            key => {

                if (
                    data[key] === ""
                    ||
                    data[key] === undefined
                ) {

                    data[key] = null;

                }

            }
        );


        try {

            const {
                data: insertedData,
                error
            } =
                await supabaseClient
                    .from("members")
                    .insert([data])
                    .select();


            if (error) {

                throw error;

            }


            /*
             SUCCESS
            */

            getElement(
                "successMessage"
            ).classList.remove(
                "hidden"
            );


            /*
             Scroll to success
            */

            getElement(
                "successMessage"
            ).scrollIntoView({
                behavior: "smooth",
                block: "center"
            });


            /*
             Reset form
            */

            form.reset();


            /*
             Reset locations
            */

            resetLocation(
                "birth"
            );

            resetLocation(
                "current"
            );


        } catch (error) {

            console.error(
                "Supabase error:",
                error
            );


            let message =
                "Ntabwo amakuru yabitswe. " +
                "Ongera ugerageze.";


            if (
                error &&
                error.message
            ) {

                message =
                    error.message;

            }


            getElement(
                "errorText"
            ).textContent =
                message;


            getElement(
                "errorMessage"
            ).classList.remove(
                "hidden"
            );


            getElement(
                "errorMessage"
            ).scrollIntoView({
                behavior: "smooth",
                block: "center"
            });

        } finally {

            button.disabled = false;

            buttonText.textContent =
                "💾 BIKA AMAKURU";

            spinner.classList.add(
                "hidden"
            );

        }

    }
);


/* =========================================================
   SELECTED TEXT
========================================================= */

function getSelectedText(id) {

    const select =
        getElement(id);

    if (!select) {

        return null;

    }

    if (
        select.selectedIndex < 0
    ) {

        return null;

    }

    const option =
        select.options[
            select.selectedIndex
        ];


    if (
        !option
        ||
        !option.value
    ) {

        return null;

    }


    return option.textContent.trim();

}


/* =========================================================
   RESET LOCATION
========================================================= */

function resetLocation(prefix) {

    const province =
        getElement(
            `${prefix}_province`
        );

    const district =
        getElement(
            `${prefix}_district`
        );

    const sector =
        getElement(
            `${prefix}_sector`
        );

    const cell =
        getElement(
            `${prefix}_cell`
        );

    const village =
        getElement(
            `${prefix}_village`
        );


    clearSelect(
        district,
        "Banza uhitemo Intara"
    );

    clearSelect(
        sector,
        "Banza uhitemo Akarere"
    );

    clearSelect(
        cell,
        "Banza uhitemo Umurenge"
    );

    clearSelect(
        village,
        "Banza uhitemo Akagari"
    );


    district.disabled = true;
    sector.disabled = true;
    cell.disabled = true;
    village.disabled = true;


    /*
     Reload provinces
    */

    loadProvinces(
        province
    );

}
