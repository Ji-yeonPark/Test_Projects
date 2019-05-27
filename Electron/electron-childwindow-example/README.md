# ELECTRON-CHILDWINDOW_EXAMPLE
---
[원문 - How to Login Electron Application with Child Windows](https://steemit.com/utopian-io/@pckurdu/how-to-login-electron-application-with-child-windows)

---

### 1. 목적
main window 를 활성화하기 전 child window를 띄워 로그인 등 특정 작업을 완료 해야지 main window가 표시되도록 기능을 설정하기 위해 해당 글을 보고 테스트했다.

<br/>

### 2. 결과
1) CreateWindow에서 부모 창(win)에 mainWindowState, maximize 등 기능(조건) 추가하면 부모창도 같이 활성화된다.
  > mainWindowState.manage(win);  // 윈도우 사이즈(상태) 저장<br/>
  > win.maximize();               // 윈도우 풀스크린으로 활성화


