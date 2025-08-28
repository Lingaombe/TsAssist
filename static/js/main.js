
function toggleMode() {
    document.body.classList.toggle('dark-mode');

    const btn = document.getElementById("mode"); 
    if (document.body.classList.contains("dark-mode")) {
        btn.src = "../static/assets/sun.png";
    } else {
        btn.src = "../static/assets/moon.png";
    }
}

//kuti akamadzasankha funso lina panambala pakhale palibe kanthu
const select = document.getElementById('questionType');
const numInput = document.getElementById('numQuestions');
select.addEventListener('change', function() {
    numInput.value = '';
});


