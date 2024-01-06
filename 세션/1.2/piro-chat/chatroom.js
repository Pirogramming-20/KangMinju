const chatInput = document.getElementById('chat-input');
const hashtagBtn = document.getElementById('hashtag');
const sendBtn = document.getElementById('btn-send')

//새로고침 했을 때 딱 1번 실행 되면서 자동 포커스
chatInput.focus();

//input이 들어왔을 때 전송 버튼 보이고 안보이고
chatInput.addEventListener('input', (event) => {
    //텍스트 입력값
    //console.log(event.target.value) ;
    
    if(event.target.value !== '') {
        sendBtn.style.display = 'block';
        hashtagBtn.style.display ='none';
    }
    else {
        sendBtn.style.display = 'none';
        hashtagBtn.style.display ='block';
    }
})

chatInput.addEventListener('keypress', (event) => {
    if(event.code === 'Enter' ) {
        sendBtn.click();
    }
})

let flag = true; // 내 말풍성, false -> 교육팀장님

const chatBubbleContainer = document.getElementById('chat-bubble');
//전송 클릭 이벤트
sendBtn.addEventListener('click', () => {
    // 입력 값이 비어 있지 않은지 확인
    if (chatInput.value.trim() !== '') {
        const contentDiv = document.createElement('div');
        if (flag) {
            flag = false;
            // 나의 말풍선 생성
            contentDiv.className = 'my-bubble-content';
            const bubble = document.createElement('div')
            bubble.className = 'my-bubble';
            bubble.innerText = chatInput.value;
            contentDiv.appendChild(bubble);
        } else {
            flag = true;
            // 교육 팀장님 말풍선 생성
            contentDiv.className = 'your-bubble';

            const profileDiv = document.createElement('div');
            profileDiv.className = 'profile';

            const profileImg = document.createElement('img');
            profileImg.src = './profile.png'
            profileDiv.appendChild(profileImg);
            contentDiv.appendChild(profileDiv)
            
            const bubbleContent = document.createElement('div');
            bubbleContent.className = 'bubble-content';

            const name = document.createElement('div');
            name.className = 'name';
            name.innerText = '교육팀장님';

            const bubble = document.createElement('div')
            bubble.className = 'bubble';

            bubble.innerText = chatInput.value;
            
            bubbleContent.appendChild(name);
            bubbleContent.appendChild(bubble);
            contentDiv.appendChild(profileDiv);
            contentDiv.appendChild(bubbleContent);
        }
        chatBubbleContainer.appendChild(contentDiv);
        chatInput.value = '';
        chatBubbleContainer.scrollTop = chatBubbleContainer.scrollHeight;
    }
});
