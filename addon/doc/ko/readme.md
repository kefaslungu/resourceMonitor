# 리소스 모니터 #

* 저자: Alex Hall, Joseph Lee (이성원), beqa gozalishvili 외 공헌자들.
* Stable version: [version 2.4][1]
* Development version: [version 3.0-dev][2]

사용자 컴퓨터의 프로세서, 메모리, 디스크 및 베터리 사용에 관한 정보를 알려주는 기능입니다.

# 단추키 #

* NVDA+Shift+E 프로세서, 메모리 및 베터리 사용 정보를 알려줍니다.
* NVDA+Shift+1 프로세서 사용 정보를 알려줍니다.
* NVDA+Shift+2/5 메로리 (렘 및 가상 메모리) 사용 정보를 알려줍니다.
* NVDA+Shift+3 디스크 사용 정보를 알려줍니다.
* NVDA+Shift+4 베터리 정보를 알려줍니다.
* NVDA+Shift+6 Presents currently installed Windows version, CPU bit (32 or
  64-bit) and service pack if any (version 3.0-dev).

## Usage notes ##

This add-on does not replace task manager and other system information
programs for Windows. Also note the following:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper Threading where number of CPU's
  is twice the number of CPU cores.
* There might be a short delay when getting processor usage information.

## Changes for 3.0-dev ##

* Updated psutil dependency to 1.2.1.
* Added a command (NVDA+Shift+6) to report the version of Windows you are
  using, CPU bit and service packs if any.
* Ability to change add-on shortcut keys (NVDA 2013.3 or later).
* Ability to copy individual resource information to clipboard by pressing
  resource commands two times.

## 버전 2.4 ##

* 새 언어: 우크라이나어, 중국어 (간채).
* 여러 언어 번역 수정.

## 버전 2.3 ##

* 불가리아어 번역 추가.

## 버전 2.2 ##

* 다음 언어 추가: 갈라티아어, 네덜란드어, 네팔어, 독일어, 러시아어, 스페인어, 슬로바키아어, 슬로베니아어, 아라곤어,
  크로아티아어, 포루투갈어 (브라질), 프랑스어, 핀란드어, 타밀어, 터키어, 한국어, 헝가리어.

## 버전 2.1 ##

* psutil 0.6.1로 업데이트함.
* 드라이브 정보 확인 속도 향상.
* 데이타 이름 정리.
* `코드 정리.

## 버전 2.0 ##

* 번역 지원 추가.

## 버전 1.0 ##

* 첫 출시 버전.

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
