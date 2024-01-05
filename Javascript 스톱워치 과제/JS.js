let intervalId;
let time = 0;
let isRunning = false;

const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');
const resetBtn = document.getElementById('resetBtn');
const second = document.getElementById('second');
const millisecond = document.getElementById('millisecond');

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
});

resetBtn.addEventListener('click', function() {
    clearInterval(intervalId);
    time = 0;
    isRunning = false;
    second.textContent = '00';
    millisecond.textContent = '00';
});
