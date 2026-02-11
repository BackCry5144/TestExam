
### 📂 [FILE 2] 최종 점검: Must Memorize 치트 시트

시험장에 들어가기 전 반드시 머릿속에 넣어야 할 비교표입니다.

#### **1. UI 위젯 비교 (핵심)**

| 위젯 | 주요 용도 | 비고 |
| --- | --- | --- |
| **Expression** | 단순 텍스트/계산값 출력 | HTML 렌더링 가능 (Sanitize 확인) |
| **Label** | Input 위젯의 이름을 표시 | `Target` 속성으로 Input과 연결 가능 |
| **Input** | 사용자 데이터 입력 받기 | `Variable` 매핑 필수, `Prompt` 텍스트 설정 가능 |
| **Placeholder** | Block 내부에 뚫어놓은 빈 공간 | 부모가 원하는 내용을 채워 넣음 |

#### **2. 변수의 수명 주기 (Lifecycle)**

| 변수 타입 | 위치 | 수명 (Life Span) | 특징 |
| --- | --- | --- | --- |
| **Local Variable** | Screen / Action | 해당 화면/액션이 종료될 때까지 | 휘발성, 빠른 접근 |
| **Input Parameter** | Screen / Action | 해당 화면/액션이 종료될 때까지 | 외부에서 전달받는 값 |
| **Client Variable** | Browser | 브라우저 세션 또는 쿠키 | 사용자별 설정 저장, 기본 타입만 가능 |
| **Site Property** | Server | 애플리케이션 실행 중 계속 | 모든 사용자가 공유, 관리자가 상시 변경 가능 |

#### **3. Delete Rule (무조건 나옴)**

* **Protect:** 자식이 있으면 부모 삭제 불가 (가장 안전)
* **Delete:** 부모 삭제 시 자식도 자동 삭제 (위험하지만 깔끔)
* **Ignore:** 무시하고 삭제 (데이터 꼬임 발생 가능)

#### **4. Screen Lifecycle 이벤트 순서**

1. **On Initialize:** 데이터 가져오기 전, 변수 초기화. (가장 먼저)
2. **On Ready:** DOM 트리 준비 완료. (JS 초기화 등)
3. **On Render:** 화면이 그려질 때마다. (자주 실행되므로 무거운 로직 금지)
4. **On After Fetch:** 데이터 조회가 끝난 직후. (조회 데이터 가공)
5. **On Parameters Changed:** 부모로부터 전달받은 Input값이 바뀔 때.
