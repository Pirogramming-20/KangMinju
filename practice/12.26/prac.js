// html element 가져온다
const dateNode = document.querySelector("#date");
const hourNode = document.querySelector("#hour");
const minuteNode = document.querySelector("#minute");
const secondNode = document.querySelector("#second");

//milisecond -> second 1초*1000
//1000ms -> 1s
const secondToMiliSec = 1000;
const minuteToMiliSec = secondToMiliSec * 60;
const hourToMiliSec = minuteToMiliSec * 60;
const dayToMiliSec = hourToMiliSec * 24;

function calculateDiffTime() {
    const now = new Date();
    const endDate = new Date("2024-02-20:00:00:00+0900");
    const diffTime = endDate.getTime() - now.getTime();

    const date = Math.floor(diffTime / dayToMiliSec);
    const hour = Math.floor((diffTime % dayToMiliSec) / hourToMiliSec);
    const minute = Math.floor((diffTime % hourToMiliSec) / minuteToMiliSec);
    const second = Math.floor((diffTime % minuteToMiliSec) / secondToMiliSec);

    return {
        date, hour, minute, second
    };
}



function countdown() {
    const {date, hour, second, minute} = calculateDiffTime();
    dateNode.innerText = String(date).padStart(2, "0");
    hourNode.innerText = String(hour).padStart(2, "0");
    minuteNode.innerText = String(minute).padStart(2, "0");
    secondNode.innerText = String(second).padStart(2, "0");
}

//1초마다 실행 원함, 1초 -> 1000ms
setInterval(() => {countdown()},1000);

countdown();