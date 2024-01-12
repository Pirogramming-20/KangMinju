have to - css  
구현한 기능: 1,2,3,4,5,6,7,8,9,10,11

구현하지 못한 기능: X

🔥챌린지 도전합니다🔥
1. 장르 선택기능 구현 완료<br>
   * create, update html에서 option을 하나씩 추가했었는데 for문으로 option생성. <br>
2. 러닝타임 분 단위 -> 시간 단위 구현 완료<br>
    *movie.time을 int로 변환하고 시간이 변환되기 때문에 상영시간을 작성하지 않으면 에러 발생.<br>
    * view.py에서 시간 변환 후 전송. <br>
    * 리스트에 상영시간 hour min 출력하는데 오래걸림...<br>
        * 첫시도 : def read_list에 pk 받아서 해보려함 -> 받을 pk없어서 불가<br>
        * 두번째시도 : 모든 min 을 hour 로 바꾼 후 list 저장 -> 전송, 백에서는 잘보냈지만 html에서 출력이 안됨(한 for문에 두개의 객체가 출력이 안됨)<br>
        * 세번째시도 : def read_list에서 movies와 movie_durations를 zip으로 묶고 info_list로 전송 후 html에서 출력 (구글 감사합니다 진짜)<br>

3. 리스트 페이지 정렬 기능(제목 순, 별점 순, 상영시간 순, 개봉년도 순) 구현 완료<br>
    * 별점 -> 내림차순, 상영시간 -> 오름차순, 개봉년도 -> 최신순(내림차순)<br>

⚪ JS, CSS ⚪
1. 삭제버튼 누르면 confirm을 통해 삭제 여부 확인 후 삭제 <br>