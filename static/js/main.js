
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

function paperGen(){
    FormData = {
        'file': document.querySelector('input[type="file"]').files[0],
        'subject': document.querySelector('input[placeholder="subject"]').value,
        'paperName': document.querySelector('input[placeholder="name of paper"]').value,
        'totalMarks': document.querySelector('input[placeholder="total marks"]').value,
        'questionType': document.getElementById('questionType').value,
        'numQuestions': document.getElementById('numQuestions').value
    };
}   

// class isunge mafunso onse ngati objects, 

document.getElementById('questionType').addEventListener('change', function() {
    const questionType = this.value;
    if (questionType == "mcq"){
        for (let i = 1; i <= 4; i++) {
            let input = document.createElement("input");
            input.type = "text";
            input.name = "option" + i;
            input.placeholder = "Option " + i;
            container.appendChild(input);
            container.appendChild(document.createElement("br"));
        }
    }
});
function addQuestion(){
    const questionText = document.getElementById('addQuestionText').value;
    const questionType = document.getElementById('questionType').value;
    const questionMarks = document.getElementById('questionMarks').value;
}

console.log("MCQ"=="mcq")