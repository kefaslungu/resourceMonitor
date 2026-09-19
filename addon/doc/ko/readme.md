# 리소스 모니터

* 저자: Alex Hall, Joseph Lee (이성원), beqa gozalishvili 외 공헌자들.

본 추가 기능은 CPU 사용, 메모리 사용 등 컴퓨터 리소스 사용 상태를 알려줍니다.

## 단추키

본 추가 기능 명령들은 음성 출력 요청 모드(speech on-demand)를 지원합니다.

* NVDA+Shift+E: 리소스 모니터 명령 모드를 실행하빈다.

아래 명령들을 사용하여 리소스 사용 정보를 확인할 수 있습니다:

* 스페이스(Space): 메모리(RAM) 및 프로세서 사용률을 알려줍니다.
* C: 프로세서(CPU) 평균 프로세서 사용률 및 멀티코어 CPU일 경우 각 코어 사용률)
* D: 디스크 사용량(연결된 디스크, 외부 디스크, 네트ㅜ어크 디스크 포함)
* G(보안 모드(secure mode)일때 사용 불가): GPU(비디오 카드) 정보
* Shift+G(보안 모드(secure mode)일때 사용 불가): GPU 메모리 사용량
* M: memory (used and total space for both physical and virtual RAM)
* O: 운영체제(operating system), 특히 윈도우 버전(빌드 포함) 및 프로세서 버전(AMD64/x64, ARM64)
* U: 시스템 부팅후 사용 시간(uptime)을 알려줍니다.
* W: 무선랜(wi-fi) 정보(네트ㅜ어크 이름, 보안 상태, 신호 강도)

리소스 정보 명령 모드 사용시 각 정보 핫키를 여러번 누를 수 있습니다. Escape를 눌러 명령 모드를 종료하며 명령 모드에 포함되지 않은 핫키는 포커스된 앱에 입력됩니다.

For limited backward compatibility, the previous NVDA+Shift+1 through NVDA+Shift+7 resource shortcuts remain available (these commands are planned to be removed in a future add-on version):

* NVDA+Shift+1: 프로세서(CPU)
* NVDA+Shift+2/5: memory (NVDA+Shift+5 is an alternative to NVDA+Shift+2 when the latter keyboard combination cannot be performed)
* NVDA+Shift+3: 디스크
* NVDA+Shift+4: 무선랜
* NVDA+Shift+6: 운영체제(윈도우) 버전
* NVDA+Shift+7: 부팅후 시스템 사용 시간

NVDA 단춧키 설정을 통해 위 단춧키들을 변경할 수 있습니다.

## 추가 기능 사용에 있어서

본 추가 기능은 윈도우 작업 관리자 등 리소스 사용에 관한 정보를 알려주늠 앱들을 대체하지 않습니다. 또한 다응 사항을 참고하세요:

* 리소스 정보 단춧키를 두번 눌러 해당 리소스 정보를 클립보드에 복사할 수 있습니다.
* NVDA가 보안 모드일 때(예: 로그인 창에서) 리소스 정보를 클립보드에 복사할 수 없습니다.
* CPU 사용률은 물리 코어가 아닌 논리 코어 사용률을 보여줍니다(Hyper-Threading 사용시 논리 코어 수가 물리 코어의 배가 됨; 일부 최신 프로세서는 Hyper-Threading을 탑제하지 않음).
* 디스크 사용량 확인시 대용량 파일 복사 또는 네트워크 접근과 같이 많은 시간을 필요로 하는 작업이 진행중일 때에는 정보 출력이 늦어질 수 있습니다.
* NVDA will play a sound and report a message whenever connecting to or disconnecting from wireless networks. See the next section on how to change this behavior.
* GPU 정보는 Nvidia GPU로 한정됩니다.
* 윈도우 버전 알림에 포함된 "x86" 또는 "AMD64"는 프로세서 이름이 아닌 Intel 및 AMD 32비트 또는 64비트 프로세서 아키텍처(processor architecture)를 의미합니다.
* 본 추가 기능은 윈도우 10/11 LTSC를 정식으로 지원하지 않습니다.

## Settings

You can configure the following resource usage reporting options from NVDA settings screen under Resource Monitor category:

* GPU temperature unit: Select the temperature unit reported as part of the GPU information (Celcius or Fahrenheit).
* Wi-fi connect/disconnect notification: Select how NVDA should report wi-fi connect/disconnect notifications (off, message, sound, both message and sound).

추가 기능 변경 사항은 [추가 기능 변경 내역 (영어)][1] 문서에서 확인하실 수 있습니다.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
