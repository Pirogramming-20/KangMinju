let intervalId;
let time = 0;
let isRunning = false;

const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');
const resetBtn = document.getElementById('resetBtn');
const second = document.getElementById('second');
const millisecond = document.getElementById('millisecond');
const recordMain = document.getElementById('recordMain');
const deleteBtn = document.getElementById('delete');
const checkAll = document.getElementById('checkAll');

startBtn.addEventListener('click', function() {
    if (!isRunning) {
        isRunning = true;
        intervalId = setInterval(function() {
            time += 10;
            let sec = Math.floor(time / 1000);
            let ms = Math.floor((time % 1000) / 10);
            second.textContent = sec < 10 ? '0' + sec : sec;
            millisecond.textContent = ms < 10 ? '0' + ms : ms;
        }, 10);
    }
});

stopBtn.addEventListener('click', function() {
    clearInterval(intervalId);
    isRunning = false;
    let recordDiv = document.createElement('div');
    let record = document.createElement('div');
    let check = document.createElement('div');

    record.textContent = second.textContent + ':' + millisecond.textContent;
    check.classList.add('clickAdd');
    recordDiv.appendChild(check);
    recordDiv.appendChild(record);
    recordMain.appendChild(recordDiv);
});

document.addEventListener('click', function(event) {
    if (event.target.classList.contains('clickAdd')) {
        if (event.target.style.backgroundColor === 'black') {
            event.target.style.backgroundColor = ''; 
        } else {
            event.target.style.backgroundColor = 'black'; 
        }
    }
});
resetBtn.addEventListener('click', function() {
    clearInterval(intervalId);
    time = 0;
    isRunning = false;
    second.textContent = '00';
    millisecond.textContent = '00';
});

deleteBtn.addEventListener('click', function() {
    const checkedElements = document.querySelectorAll('.clickAdd[style="background-color: black;"]');

    checkedElements.forEach(function(element) {
        element.parentElement.remove();

    });

});

checkAll.addEventListener('click', function(event) {
    const allCheckElements = document.querySelectorAll('.clickAdd');

    if (event.target.style.backgroundColor === 'black') {
        event.target.style.backgroundColor = ''; 
    } else {
        event.target.style.backgroundColor = 'black'; 
    }
    allCheckElements.forEach(function(element) {
        element.style.backgroundColor = element.style.backgroundColor === 'black' ? '' : 'black';
    });
});
