let answer = [];
let attempts = 0;

function initialize_game() {
    attempts = 10;

    answer = [];
    while (answer.length < 3) {
        let num = Math.floor(Math.random() * 10);
        if (answer.indexOf(num) === -1) 
            answer.push(num);
        }
    
    document
        .getElementById('number1')
        .value = '';
    document
        .getElementById('number2')
        .value = '';
    document
        .getElementById('number3')
        .value = '';
    document
        .querySelector('.result-display')
        .innerHTML = '';
    
    console.log(answer[0]);
    console.log(answer[1]);
    console.log(answer[2]);
}

function check_numbers() {
    let input1 = document
        .getElementById('number1')
        .value;
    let input2 = document
        .getElementById('number2')
        .value;
    let input3 = document
        .getElementById('number3')
        .value;

    if (input1 === '' || input2 === '' || input3 === '') {
        alert('숫자를 입력하세요');
        return;
    }

    let input = [parseInt(input1), parseInt(input2), parseInt(input3)];

    let strike = 0;
    let ball = 0;
    for (let i = 0; i < 3; i++) {
        if (input[i] === answer[i]) {
            strike++;
        } else if (answer.includes(input[i])) {
            ball++;
        }
    }

    let resultDisplay = document.querySelector('.result-display');
    let resultDiv = document.createElement('div');
    resultDiv.className = 'check-result';
    if (strike + ball === 0) {
        resultDiv.innerHTML += `<div class="left">${input.join(' ')}</div> : <div class="right"><div class="out num-result">O</div>`;
        resultDiv.innerHTML += `</div>`;
    }else {
    resultDiv.innerHTML = `<div class="left">${input.join(' ')}</div> : <div class="right">${strike} <div class="strike num-result">S</div> ${ball} <div class="ball num-result">B</div></div>`;
    }
    resultDisplay.appendChild(resultDiv);

    resultDisplay.scrollTop = resultDisplay.scrollHeight;

    attempts--;
    if (strike === 3) {
        document
            .getElementById('game-result-img')
            .src = 'success.png';
        document
            .querySelector('.submit-button')
            .disabled = true;
    } else if (attempts === 0) {
        document
            .getElementById('game-result-img')
            .src = 'fail.png';
        document
            .querySelector('.submit-button')
            .disabled = true;
    }

    document
        .getElementById('number1')
        .value = '';
    document
        .getElementById('number2')
        .value = '';
    document
        .getElementById('number3')
        .value = '';
}

initialize_game();
