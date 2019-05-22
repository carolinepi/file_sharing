window.onload = function() {
    document.getElementById("sectionCurrent").style.display = "none";
    document.getElementById("sectionBlocked").style.display = "none";
};

function changeSection(value) {
    if (value == "sectionAll") {
        document.getElementById("sectionAll").style.display = "";
        document.getElementById("sectionCurrent").style.display = "none";
        document.getElementById("sectionBlocked").style.display = "none";
    } else if (value == "sectionCurrent"){
        document.getElementById("sectionAll").style.display = "none";
        document.getElementById("sectionCurrent").style.display = "";
        document.getElementById("sectionBlocked").style.display = "none";
    } else if (value == "sectionBlocked"){
        document.getElementById("sectionAll").style.display = "none";
        document.getElementById("sectionCurrent").style.display = "none";
        document.getElementById("sectionBlocked").style.display = "";
    }
}