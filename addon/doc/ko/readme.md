# 리소스 모니터

* 저자: Alex Hall, Joseph Lee (이성원), beqa gozalishvili 외 공헌자들.

본 추가 기능은 CPU 사용, 메모리 사용 등 컴퓨터 리소스 사용 상태를 알려줍니다.

## 단추키

All commands support speech on demand mode.

* NVDA+Shift+E: 메모리(RAM) 및 프로세서 사용ㄹㄹ을 알려줍니다.
* NVDA+Shift+1: presents the average processor load and if multicore CPU's are present the load of each core.
* NVDA+Shift+2/5: 
물리 및 가상 메모리 사욜률을 알려줍니다(NVDA+Shift+2가 동작하지 않을 겨웅 NVDA+Shift+5를 사용하세요).
* NVDA+Shift+3: 디스크 사용량(연결된 디스크, 외부 디스크, 네트ㅜ어크 디스크)을 알려줍니다.
* NVDA+Shift+4: 연결된 무선랜 정보(네트ㅜ어크 이름, 보안 상태, 신호 강도)를 알려줍니다.
* NVDA+Shift+6: 윈도우 버전(빌드 포함) 및 프로세서 버전(AMD64/x64, ARM64) 정보를 알려줍니다.
* NVDA+Shift+7: 시스템 부팅후 사용 시간을 알려줍니다.
* 단춧키 설정 가능: GPU(비디오 카드) 정보를 알려줍니다.
* 단춧키 설정 가능: GPU 메모리 정보를 알려줍니다.

NVDA 단춧키 설정을 통해 위 단춧키들을 변경할 수 있습니다.

## 추가 기능 사용에 있어서

본 추가 기능은 윈도우 작업 관리자 등 리소스 사용에 관한 정보를 알려주늠 앱들을 대체하지 않습니다. 또한 다응 사항을 참고하세요:

* 전체 리소스 사용 알림 기능(NVDA+Shift+E) 외 다른 단춧키를 두번 눌러 해당 리소스 정보를 클립보드에 복사할 수 있습니다.
* NVDA가 보안 모드일 때(예: 로그인 창에서) 리소스 정보를 클립보드에 복사할 수 없습니다.
* CPU usage is given for logical processors, not physical cores. This is noticeable for processors with Hyper-Threading where number of CPU's is twice the number of CPU cores. On some newer computers, not all CPU cores will have hyper-threading enabled.
* 디스크 사용량 확인시 대용량 파일 복사 또는 네트워크 접근과 같이 많은 시간을 필요로 하는 작업이 진행중일 때에는 정보 출력이 늦어질 수 있습니다.
* GPU 정보는 Nvidia GPU로 한정됩니다.
* When announcing processor architecture information as part of Windows version reporting, "AMD64" refer to 64-bit (x64) Intel and AMD processors. This information does not refer to the name of the actual processor in use.
* 본 추가 기능은 윈도우 10/11 LTSC를 정식으로 지원하지 않습니다.

추가 기능 변경 사항은 [추가 기능 변경 내역 (영어)][1] 문서에서 확인하실 수 있습니다.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
