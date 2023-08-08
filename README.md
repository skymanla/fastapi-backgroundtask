# fastapi-backgroundtask
간단한 backgroundtask 및 서버 다운 알림(slack)

## 원리
- alb에서 health에 신호를 주는 것을 토대로 제작
- 주 서비스 어플리케이션과는 별개의 로컬 어플리케이션으로 구동 -> 로컬 어플리케이션에서 주 어플리케이션의 health에 10초 간격으로 request 전송
- health에 접근이 안되는 경우(5xx error) 지정된 슬랙 채널로 서버 다운 메세지 발송
