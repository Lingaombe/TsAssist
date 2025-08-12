document.getElementById('toggleMode').addEventListener('click', toggleMode);
function toggleMode() {
    document.body.classList.toggle('dark-mode');
    let modeIcon = document.getElementById('mode');
    if (document.body.classList.contains('dark-mode')){
        modeIcon.src = '../static/assets/moon.png'
    } else {
        modeIcon.src = "../static/assets/sun.png";
    }
}

