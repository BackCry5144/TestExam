**1.** [Data] `Employee` 엔티티에서 성별을 구분하기 위해 `Gender`라는 Static Entity를 만들었습니다. `Gender` 엔티티에 기본적으로 생성되는 속성이 **아닌** 것은?
A. Id
B. Order
C. Is_Active
D. Description

**2.** [Security] `Role`을 생성하면 시스템이 자동으로 생성해주는 액션이 **아닌** 것은?
A. Check{Role}
B. Grant{Role}
C. Revoke{Role}
D. Delete{Role}

**3.** [Logic] `Server Action` 내부에서 `CommitTransaction`을 호출한 후 에러가 발생하면 어떻게 됩니까?
A. 전체가 롤백된다.
B. Commit 이후의 로직만 취소되고, 이미 커밋된 내용은 유지된다.
C. 데이터베이스가 손상된다.
D. 에러가 무시된다.

**4.** [UI] 화면에 `List` 위젯을 배치했습니다. `Source` 속성에는 무엇이 들어가야 합니까?
A. 단일 변수
B. Aggregate나 Data Action의 결과물인 List
C. Entity 자체
D. SQL 구문

**5.** [Logic] `Client Action`에서 `Server Action`을 호출하면 브라우저는 어떤 상태가 됩니까?
A. 서버의 응답을 기다리는 동안 로직이 멈춘다 (Synchronous wait).
B. 백그라운드에서 실행되며 즉시 다음 클라이언트 노드로 넘어간다.
C. 화면이 새로고침된다.
D. 브라우저가 종료된다.

**6.** [Data] `Aggregate`에서 `Join`을 할 때 조인 조건을 수동으로 수정할 수 있습니까?
A. 예, 조인 탭에서 수정 가능합니다.
B. 아니요, 오직 ID 관계에 의해서만 자동 설정됩니다.
C. SQL 위젯에서만 가능합니다.
D. 한 번 설정하면 바꿀 수 없습니다.

**7.** [Lifecycle] 화면이 처음 로드될 때 API에서 초기 데이터를 가져와야 합니다. 어느 이벤트에서 호출하는 것이 가장 좋습니까?
A. On Render
B. On Initialize
C. Data Action 사용 (At Start)
D. On Destroy

**8.** [Exception] `Database Exception`이 발생했을 때 처리할 핸들러가 없으면 어떻게 됩니까?
A. 앱이 그냥 꺼진다.
B. 상위의 `All Exceptions` 핸들러가 처리한다.
C. 아무 일도 일어나지 않는다.
D. 데이터가 강제로 저장된다.

**9.** [UI] `Button` 위젯의 `Method` 속성을 `Ajax Submit`으로 설정하는 것은 어떤 버전에 해당합니까?
A. Reactive Web
B. Traditional Web
C. Mobile
D. 모든 버전

**10.** [Logic] `Preparation`이라는 개념은 어떤 OutSystems 애플리케이션 타입에만 존재합니까?
A. Reactive Web
B. Traditional Web
C. Mobile App
D. Progressive Web App (PWA)

**11.** Aggregate에서 데이터베이스로부터 데이터를 가져올 때, **정렬(Sorting)** 기준을 사용자가 화면에서 클릭하는 컬럼에 따라 동적으로 변경하고 싶습니다. 이를 위해 Aggregate의 Sorting 탭에서 무엇을 설정해야 합니까?
A. Text 변수를 입력받는 'Dynamic Sort'를 추가한다.
B. If 위젯을 사용하여 분기한다.
C. 각 컬럼별로 별도의 Aggregate를 만든다.
D. SQL 위젯을 사용해야만 가능하다.

**12.** `GetProducts` Aggregate의 `On After Fetch` 이벤트 핸들러를 구현했습니다. 이 핸들러는 언제 실행됩니까?
A. 데이터를 가져오기 직전에 실행된다.
B. 데이터를 가져오는 도중(Fetching)에 실행된다.
C. 데이터를 모두 가져온 후, 결과 리스트가 메모리에 준비된 직후에 실행된다.
D. 화면이 렌더링 된 후에 실행된다.

**13.** 복잡한 SQL 쿼리나 외부 REST API 결과를 결합하여 화면에 보여줘야 합니다. `Data Action`을 사용할 때, 출력값(Output Parameter)을 화면의 위젯에 바인딩하려면 Data Action의 어떤 속성을 확인해야 합니까?
A. Is Public
B. Fetch Property (At Start / On Demand)
C. Cache in Minutes
D. Function

**14.** `GetOrders` Aggregate의 필터 조건으로 `Order.CreatedDate = CurrDate()`를 사용했습니다. 이 필터가 의미하는 바는?
A. 오늘 날짜에 생성된 주문만 가져온다.
B. 어제 생성된 주문만 가져온다.
C. 생성 날짜가 비어있는 주문만 가져온다.
D. 모든 주문을 가져온다.

**15.** 대량의 데이터를 처리할 때 `For Each` 루프 대신 SQL 위젯(Bulk Operation)을 사용하는 주된 이유는 무엇입니까?
A. 코드 가독성을 위해서
B. 성능(Performance) 최적화를 위해서 (DB Round-trip 감소)
C. 보안을 강화하기 위해서
D. 디버깅을 쉽게 하기 위해서

**16.** **Server Action** 내에서 `Current User`의 `Id`를 확인하기 위해 `GetUserId()` 함수를 사용했습니다. 이 함수는 어떤 값을 반환합니까?
A. 현재 세션의 로그인된 사용자 ID (없으면 NullIdentifier)
B. 데이터베이스의 첫 번째 사용자 ID
C. 항상 Null
D. 관리자(Admin) ID

**17.** **Client Action** 흐름(Flow) 중에 `Destination` 노드(화면 이동)가 있습니다. 이 노드에 도달하면 어떤 일이 발생합니까?
A. 즉시 해당 화면으로 이동하고, 현재 Action의 나머지 로직은 중단된다.
B. 현재 Action의 로직을 끝까지 다 실행한 후 화면으로 이동한다.
C. 에러가 발생한다.
D. 사용자에게 이동할지 묻는 팝업이 뜬다.

**18.** 로직에서 **Exception**이 발생하여 `Exception Handler`로 흐름이 넘어갔습니다. 핸들러 내의 로직이 모두 실행된 후에는 흐름이 어디로 갑니까?
A. 에러가 발생했던 지점으로 다시 돌아간다.
B. 로직이 종료된다 (End).
C. 화면을 새로고침한다.
D. 애플리케이션이 재시작된다.

**19.** `Run Server Action` 노드를 Client Action에 배치했습니다. OutSystems는 내부적으로 이를 어떻게 처리합니까?
A. 동기식(Synchronous) REST API 호출로 처리한다.
B. 웹소켓을 연결한다.
C. 브라우저 내부에서 코드를 실행한다.
D. 페이지 전체를 다시 로드한다.

**20.** **Site Property** 값을 변경하면 애플리케이션에 어떤 영향을 미칩니까?
A. 영향이 없다.
B. 변경된 값은 다음 배포 시에만 적용된다.
C. 즉시 값이 적용되지만, 캐시 갱신을 위해 애플리케이션 풀(Application Pool)이 리로드될 수 있다.
D. 데이터베이스가 초기화된다.

**21.** **Block**을 만들 때, 부모 화면으로부터 데이터를 전달받기 위해 사용하는 변수는?
A. Local Variable
B. Input Parameter
C. Output Parameter
D. Client Variable

**22.** **Block** 내부에서 버튼을 클릭했을 때, 부모 화면(Screen)에 있는 특정 액션을 실행시키고 싶습니다. 올바른 순서는?
A. Block에서 Event 발생(Trigger) -> 부모 화면에서 Handler로 액션 연결
B. 부모 화면에서 Block의 액션을 직접 호출
C. Block에서 부모 화면 이름을 직접 명시하여 이동
D. Client Variable을 통해 통신

**23.** **Form** 위젯 내부의 `Save` 버튼을 눌렀을 때, 필수 입력 항목(Mandatory)이 비어있으면 브라우저는 어떻게 반응합니까?
A. 서버로 요청을 보내고 DB 에러를 받는다.
B. 브라우저 자체 기능으로 "이 입력란을 작성하세요"라는 메시지를 띄우고 서버 요청을 막는다 (Built-in Validation).
C. 아무 반응이 없다.
D. 앱이 종료된다.

**24.** 리스트의 페이지네이션(Pagination)을 구현할 때, `StartIndex` 변수는 무엇을 제어합니까?
A. 한 페이지에 보여줄 개수
B. 가져올 데이터의 시작 위치 (Offset)
C. 전체 페이지 수
D. 정렬 순서

**25.** 화면에 팝업창(Modal)을 띄우기 위해 사용하는 OutSystems UI 위젯/패턴은?
A. Alert
B. Popup
C. Dialog
D. Notification

**26.** 모바일 기기에서 테이블(Table)의 컬럼이 너무 많아 화면을 넘어갈 때, 특정 컬럼을 숨기거나 조정하려면 어떤 속성을 사용합니까?
A. Column Breakpoint / Phone Behavior
B. Visible
C. Display
D. If Widget

**27.** 사용자가 파일을 업로드하기 위해 `Upload` 위젯을 사용했습니다. 사용자가 선택한 파일의 실제 데이터(Binary)는 위젯의 어떤 속성에 담깁니까?
A. Filename
B. Type
C. Content
D. Size

**28.** 화면 상단에 녹색(성공), 빨간색(에러) 등으로 사용자에게 알림 메시지를 잠시 보여주는 액션은?
A. Show Message
B. Feedback Message
C. Alert Message
D. Notify Widget

**29.** **Container** 위젯을 클릭 가능하게 만들고 싶습니다. (예: 카드 전체 클릭). 어떻게 해야 합니까?
A. 불가능하다.
B. Container 내부의 `On Click` 이벤트를 설정한다.
C. Container 안에 Link를 넣고, Link로 Container를 감싼다. (혹은 Container 자체의 Event 속성 사용)
D. Button 위젯으로 변경한다.

**30.** **Expression** 위젯에서 HTML 태그(예: `<b>Bold</b>`)를 그대로 렌더링하려면 `Escape Content` 속성을 어떻게 설정해야 합니까?
A. Yes
B. No
C. Auto
D. Text

**31.** 모듈(Module)을 **Service Module**로 설정했습니다. 이 모듈의 특징은?
A. UI(화면)를 가질 수 없다.
B. UI만 가질 수 있다.
C. 데이터베이스를 가질 수 없다.
D. 다른 모듈에서 참조할 수 없다.

**32.** 아키텍처 캔버스(Architecture Canvas) 검사 도구인 **Discovery** (또는 AI Mentor Studio)가 경고하는 **Side Reference**란 무엇입니까?
A. 상위 레이어가 하위 레이어를 참조하는 것
B. End-User 모듈끼리 서로 참조하거나, Core 모듈끼리 서로 참조하는 것 (동일 레이어 참조)
C. 하위 레이어가 상위 레이어를 참조하는 것
D. 외부 REST API를 참조하는 것

**33.** **Public**으로 설정된 Server Action의 `Is Function` 속성을 `Yes`로 하려면 반드시 지켜야 할 제약 조건은?
A. 로직 내에서 데이터베이스 쓰기(Create/Update/Delete)를 하면 안 된다.
B. Output Parameter는 반드시 1개여야 한다.
C. Input Parameter가 없어야 한다.
D. Client Action에서만 호출해야 한다.

**34.** 사용자 관리(User Provider)를 **Current eSpace**로 설정하면 어떤 일이 발생합니까?
A. 전사적 통합 로그인(SSO)이 적용된다.
B. 이 모듈은 독립적인 사용자 및 세션 테이블을 사용하여, 다른 모듈과 로그인을 공유하지 않는다.
C. 익명 사용자만 접근 가능하다.
D. 관리자 권한이 부여된다.

**35.** **Role** 기반 보안 검사에서 `CheckRegisteredRole(UserId)` 함수가 `True`를 반환하는 경우는?
A. 사용자가 로그인하지 않은 상태일 때
B. 사용자가 로그인한 상태일 때 (모든 로그인 사용자)
C. 사용자가 관리자일 때만
D. 사용자가 차단된 상태일 때

**36.** 다음 중 **Strong Dependency**를 유발하는 요소는?
A. Server Action
B. Service Action
C. Structure (공유 시)
D. Static Entity (공유 시)

**37.** **Producer** 모듈에서 Public Server Action의 로직만 수정하고 인터페이스(파라미터)는 그대로 두었습니다. **Consumer** 모듈은 어떻게 해야 합니까?
A. 반드시 Service Studio에서 Refresh Reference를 해야 한다.
B. Producer만 배포하면, Consumer는 런타임에 자동으로 변경된 로직을 사용한다.
C. Consumer도 반드시 다시 배포(Republish)해야 변경된 로직이 적용된다.
D. 전체 솔루션을 재배포해야 한다.

**38.** [Scenario] 상품 목록 화면에서 '가격'으로 정렬하면, 가격이 동일한 상품들이 매번 다른 순서로 나타나 사용자 경험을 해치고 있습니다. 해결책은?
A. 정렬 기능을 뺀다.
B. 2차 정렬 조건(예: 상품명, 등록일)을 추가하여 순서를 확정(Deterministic) 짓는다.
C. DB 인덱스를 다시 만든다.
D. 캐시를 끈다.

**39.** [Logic] `Switch` 문을 사용하여 상태값(Status)에 따라 분기 처리를 하려 합니다. '대기(Pending)', '진행(Active)', '완료(Closed)' 세 가지 경로가 있고, 그 외의 모든 상태는 '에러(Error)' 처리하고 싶습니다. '에러' 처리를 위해 필요한 것은?
A. If 위젯 사용
B. Exception Handler 추가
C. Otherwise (Default) 분기 연결
D. Switch 문을 하나 더 추가

**40.** [Data] 엔티티의 속성 타입이 `Text` (Length 50)인데, 사용자가 100글자를 입력했습니다. DB에 저장될 때 어떤 일이 발생합니까?
A. 자동으로 길이가 늘어나서 저장된다.
B. 앞의 50글자만 잘려서 저장된다.
C. 데이터베이스 에러(예외)가 발생한다. (String or binary data would be truncated)
D. 저장이 거부되고 롤백된다.

**41.** [Lifecycle] 화면의 `OnReady` 액션에서 자바스크립트로 `document.getElementById('myInput').focus()`를 실행했는데 동작하지 않습니다. 가장 유력한 원인은?
A. 자바스크립트가 잘못되었다.
B. 해당 위젯('myInput')의 `Name` 속성을 지정하지 않아 ID가 생성되지 않았다.
C. OnReady는 너무 늦게 실행되기 때문이다.
D. 보안 설정 때문이다.

**42.** [UI] **Input** 위젯을 **Integer** 타입 변수에 연결했습니다. 사용자가 "abc"라고 입력하면 Input 위젯의 유효성(Valid) 속성은?
A. True
B. False
C. Null
D. Undefined

**43.** [Arch] 팀원 A가 Core 모듈을 수정하고 배포했습니다. 팀원 B가 End-User 모듈을 배포하려고 하니 "Incompatible Producer" 에러가 뜹니다. 이유는?
A. 팀원 A가 개발 환경을 삭제해서
B. Core 모듈의 변경으로 인해 의존성(참조)이 깨졌기 때문 (Refresh Reference 필요)
C. 팀원 B의 권한이 없어서
D. 네트워크 오류

**44.** [Logic] `JSON Deserialize`를 사용할 때, JSON 문자열의 구조와 매핑할 OutSystems 데이터 타입은 무엇이어야 합니까?
A. Entity
B. Structure (또는 List of Structure)
C. Static Entity
D. Local Variable

**45.** [Data] `GetEmployees` Aggregate를 최적화하려고 합니다. 사용되지 않는 컬럼(Attribute)들을 Aggregate에서 숨기면(Hide) 성능에 도움이 됩니까?
A. 아니요, 화면에서 안 보일 뿐 데이터는 다 가져옵니다.
B. 예, OutSystems 최적화 엔진이 실제 사용되는 컬럼만 SELECT 절에 포함시키므로 DB 부하가 줄어듭니다.
C. 예, 하지만 네트워크 전송량만 줄어듭니다.
D. 컴파일 에러가 발생합니다.

**46.** [Security] SQL Injection을 방지하기 위해 `Advanced SQL` 위젯 사용 시 필수적으로 사용해야 하는 함수는?
A. `EncodeHtml()`
B. `EncodeSql()` (단, Expand Inline 파라미터 사용 시)
C. `EncryptPassword()`
D. `SanitizeUrl()`

**47.** [UI] 화면의 레이아웃(Layout)을 변경하고 싶습니다. 모든 화면에 공통적으로 적용된 레이아웃 블록은 주로 어디에 있습니까?
A. OutSystemsUI 모듈
B. Common UI Flow (보통 Theme 모듈이나 현재 모듈의 Common)
C. Main Flow
D. Resources 폴더

**48.** [Logic] Client Action에서 서버 호출 없이 즉시 데이터를 변경하고 화면에 반영하고 싶습니다. 리스트 데이터 조작을 위해 사용하는 액션이 **아닌** 것은?
A. ListAppend
B. ListRemove
C. CreateOrUpdateAction (Entity Action)
D. ListSort

**49.** [Lifecycle] 사용자가 브라우저의 '뒤로 가기' 버튼을 눌렀을 때, 이전 화면의 `On Initialize`가 다시 실행됩니까? (Reactive Web 기준)
A. 무조건 다시 실행된다.
B. 이전 화면이 메모리(DOM)에 남아있다면(Preserved) 실행되지 않고 `On Render`만 실행될 수 있다.
C. 절대 실행되지 않는다.
D. 에러가 발생한다.

**50.** [Final] OutSystems 자격증 시험을 볼 때 가장 중요한 마음가짐은? (서비스 문제)
A. 모르면 찍는다.
B. 실무 경험과 개념을 연결하여 논리적으로 판단한다.
C. 속독으로 10분 만에 푼다.
D. 포기한다.


드디어 마지막 **Set 3(50문제)**에 대한 정답과 상세 해설입니다!

이번 세트는 실제 시험의 합격 기준인 70점을 넘어 **고득점(85점 이상)**을 목표로 하는 분들을 위해, 미묘한 개념 차이를 묻는 문제들을 집중적으로 다뤘습니다. SI 실무 프로젝트에서 겪을 법한 예외 상황들이 많으니 해설을 꼼꼼히 읽어보시길 권장합니다.

---

### 📂 [FILE 3-2] Set 3: 정답 및 상세 해설 (Answer Key)

> **[Set 3] 정답 요약표**
> **1-10:** D | D | B | B | A | A | C | B | B | B
> **11-20:** A | C | B | A | B | A | A | B | A | C
> **21-30:** B | A | B | B | B | A | C | B | C | B
> **31-40:** A | B | B | B | B | A | C | B | C | C
> **41-50:** B | B | B | B | B | B | B | C | B | B

#### **[상세 해설]**

**1. 정답: D**

* **해설:** Static Entity 생성 시 시스템이 자동으로 부여하는 속성은 `Id`, `Order`, `Is_Active`, `Label`의 4가지입니다. `Description`은 필요할 경우 개발자가 수동으로 추가해야 하는 속성입니다.

**2. 정답: D**

* **해설:** Role을 생성하면 시스템은 해당 권한을 확인하고 부여/취소하기 위한 `Check{Role}`, `Grant{Role}`, `Revoke{Role}` 액션을 자동으로 생성합니다. `Delete{Role}` 액션은 존재하지 않습니다.

**3. 정답: B**

* **해설:** `CommitTransaction`이 호출된 시점까지의 데이터베이스 변경 사항은 **확정 저장**됩니다. 그 이후에 발생하는 에러는 해당 지점 이후의 로직만 취소(롤백)시킵니다.

**4. 정답: B**

* **해설:** `List` 위젯은 여러 레코드를 보여주기 위한 도구이므로, 데이터 소스로 반드시 **Aggregate**나 **Data Action**의 결과물인 리스트 형태를 전달해야 합니다.

**5. 정답: A**

* **해설:** Reactive Web 아키텍처에서 Client Action이 Server Action을 호출하면 브라우저는 서버의 응답을 받을 때까지 해당 로직 라인에서 **대기**합니다.

**6. 정답: A**

* **해설:** Aggregate에서 엔티티를 조인하면 기본적으로 ID 관계에 의해 조인 조건이 생성되지만, **Joins 탭**에서 해당 조건을 클릭하여 사용자가 원하는 로직으로 수동 수정이 가능합니다.

**7. 정답: C**

* **해설:** 화면 로딩 시 외부 API에서 데이터를 가져와야 한다면, **Data Action**을 생성하고 `Fetch` 속성을 **At Start**로 설정하는 것이 가장 표준적이고 효율적입니다.

**8. 정답: B**

* **해설:** 특정 예외(Database Exception)에 대한 전용 핸들러가 없으면, 예외는 상위로 전파(Bubble up)되어 가장 포괄적인 **All Exceptions** 핸들러에서 처리됩니다.

**9. 정답: B**

* **해설:** **Ajax Submit**은 Traditional Web 방식의 유물입니다. Reactive Web은 기본적으로 모든 서버 통신이 비동기로 이루어지므로 버튼에 별도의 Ajax 설정을 할 필요가 없습니다.

**10. 정답: B**

* **해설:** **Preparation**은 서버 사이드 렌더링 방식인 Traditional Web에서만 사용되는 데이터 준비 단계입니다. Reactive Web은 화면 로딩과 동시에 비동기로 데이터를 가져오는 방식을 채택합니다.

**11. 정답: A**

* **해설:** 사용자가 클릭한 컬럼에 따라 정렬을 바꾸는 '동적 정렬'을 구현하려면, 정렬 기준이 담긴 Text 변수를 Aggregate의 **Dynamic Sort** 부분에 매핑해야 합니다.

**12. 정답: C**

* **해설:** `On After Fetch` 이벤트는 Aggregate가 서버로부터 데이터를 성공적으로 가져와 결과 리스트가 메모리에 준비된 **직후**에 실행됩니다. 데이터를 가공하거나 초기 변수값을 설정하기에 최적의 장소입니다.

**13. 정답: B**

* **해설:** Data Action의 결과물을 화면 위젯에 바인딩하여 보여주려면, 해당 액션이 화면 로드 시 자동으로 실행되도록 **Fetch** 속성이 **At Start**로 되어 있는지 확인해야 합니다.

**14. 정답: A**

* **해설:** `CurrDate()` 함수는 시스템의 오늘 날짜(시간 제외)를 반환하므로, 오늘 날짜와 생성일이 일치하는 주문들만 필터링하게 됩니다.

**15. 정답: B**

* **해설:** 루프(For Each) 내에서 개별 `Create` 액션을 반복하면 데이터베이스와의 통신(Round-trip)이 빈번해져 성능이 급격히 저하됩니다. 대량 데이터는 **SQL 위젯의 벌크 연산**이 훨씬 효율적입니다.

**16. 정답: A**

* **해설:** `GetUserId()` 내장 함수는 현재 로그인된 세션의 사용자 ID를 반환합니다. 로그인하지 않은 익명 사용자의 경우 `NullIdentifier()`를 반환합니다.

**17. 정답: A**

* **해설:** 흐름 제어 노드인 `Destination`을 만나면 현재 실행 중인 액션의 나머지 로직은 무시되고 즉시 지정된 화면으로 이동합니다.

**18. 정답: B**

* **해설:** Exception Handler는 예외 발생 시 흐름을 가로채서 처리하는 종착역과 같습니다. 핸들러 내부의 로직이 모두 실행되면 해당 액션의 흐름은 **종료(End)**됩니다.

**19. 정답: A**

* **해설:** Client Action 내부에서 `Run Server Action`을 배치하면, OutSystems는 내부적으로 이를 보안이 적용된 **REST API 호출**로 변환하여 처리합니다.

**20. 정답: C**

* **해설:** Site Property는 모든 세션이 공유하는 서버 변수입니다. 값을 변경하면 즉시 반영되지만, 서버는 캐시 갱신을 위해 애플리케이션 풀을 재시작할 수 있어 일시적인 성능 영향이 있을 수 있습니다.

**21. 정답: B**

* **해설:** 블록(Block)은 재사용 가능한 부품이므로, 부모로부터 필요한 데이터를 전달받기 위해 **Input Parameter**를 사용합니다.

**22. 정답: A**

* **해설:** 하위 요소(Block)가 상위 요소(Screen)를 직접 호출할 수는 없습니다. 따라서 **블록에서 이벤트를 발생(Trigger Event)**시키고, **부모 화면에서 해당 이벤트의 핸들러(Handler)**를 통해 로직을 실행해야 합니다.

**23. 정답: B**

* **해설:** Form 위젯의 `Save` 버튼 클릭 시 필수 항목이 누락되었다면, 서버에 데이터를 보내기 전 브라우저 수준에서 **Built-in Validation**을 수행하여 사용자에게 알립니다.

**24. 정답: B**

* **해설**: 페이지네이션(Pagination)에서 **StartIndex**는 현재 화면에 보여줄 리스트가 전체 데이터 중 몇 번째 인덱스부터 시작하는지(Offset)를 결정합니다. 예를 들어, 페이지당 10개씩 보여준다면 2페이지의 StartIndex는 10이 됩니다.

**25. 정답: B**

* **해설**: 화면 위에 별도의 작은 창을 띄워 사용자에게 정보를 보여주거나 입력을 받는 위젯은 **Popup**입니다. OutSystems UI에서 제공하는 패턴으로, 특정 조건이나 버튼 클릭 시 `showPopup` 액션 등을 통해 제어합니다.

**26. 정답: A**

* **해설**: Table 위젯의 각 컬럼에는 **Column Breakpoint** 속성이 있습니다. 이를 통해 특정 기기(예: Phone)에서 해당 컬럼을 자동으로 숨기거나 표시할지 결정하여 반응형 UI를 구현합니다.

**27. 정답: C**

* **해설**: Upload 위젯을 통해 선택된 파일의 바이너리(실제 데이터)는 위젯과 연결된 **Content** 속성에 저장됩니다. 파일명은 `Filename`, 파일 형식은 `Type` 속성에서 확인할 수 있습니다.

**28. 정답: B**

* **해설**: 사용자에게 처리 결과(성공, 에러, 경고 등)를 화면 상단에 잠시 띄워주는 시스템 액션은 **Feedback Message**입니다. 실무에서 가장 빈번하게 사용되는 알림 방식입니다.

**29. 정답: C**

* **해설**: Container 자체는 기본적으로 클릭 이벤트를 가지지 않지만, **Events** 탭에서 `On Click` 핸들러를 설정하거나 Container를 **Link** 위젯으로 감싸면 카드 전체를 클릭 가능하게 만들 수 있습니다.

**30. 정답: B**

* **해설:** `Escape Content` 속성을 **No**로 설정하면 HTML 태그를 텍스트로 보지 않고 코드로 해석하여 렌더링합니다. 단, 사용자 입력값을 직접 노출할 경우 보안 위협(XSS)이 있으므로 주의해야 합니다.

**31. 정답: A**

* **해설:** **Service Module**은 오직 비즈니스 로직과 데이터 서비스만을 제공하기 위해 설계되었으므로, **UI(Screen) 요소를 포함할 수 없습니다.**

**32. 정답: B**

* **해설:** **Side Reference**는 같은 레이어에 있는 모듈끼리 참조하는 것을 말합니다. (예: End-User 모듈 A가 End-User 모듈 B를 참조). 이는 아키텍처 위반은 아니지만 순환 참조 위험이 있어 주의가 필요합니다.

**33. 정답: B**

* **해설:** Server Action을 표현식(Expression)에서 함수처럼 쓰려면(`Is Function = Yes`), 결과를 반환할 **Output Parameter가 반드시 정확히 1개**여야 합니다.

**34. 정답: B**

* **해설**: **User Provider**를 `Current eSpace`로 설정하면, 해당 모듈은 다른 모듈과 사용자 정보를 공유하지 않는 독립적인 사용자 환경을 가집니다. 주로 멀티테넌시(Multi-tenancy) 환경이나 완전히 분리된 보안이 필요한 모듈에서 사용합니다.

**35. 정답: B**

* **해설**: `CheckRegisteredRole` 함수는 해당 사용자가 시스템에 **로그인한 상태**인지를 확인합니다. OutSystems에서 모든 로그인 사용자는 기본적으로 `Registered` 역할을 부여받기 때문입니다.

**36. 정답: A**

* **해설**: 다른 모듈의 **Server Action**을 참조하면 **Strong Dependency**가 발생합니다. 반면 **Service Action**을 참조하면 **Weak Dependency**가 발생하여, 로직 수정 시 참조 모듈을 매번 다시 배포하지 않아도 됩니다.

**37. 정답: C**

* **해설:** **Strong Dependency**(Server Action 등) 관계에서 Producer의 로직이 변경되었다면, Consumer 모듈을 반드시 **다시 배포(Republish)**해야만 변경된 로직 바이너리가 적용됩니다.

**38. 정답: B**

* **해설:** 동일한 값(가격)을 가진 레코드들의 정렬 순서가 매번 바뀌는 것을 막으려면, 고유한 값(예: Id, 등록일)을 **2차 정렬 조건**으로 추가하여 결과 순서를 확정(Deterministic)시켜야 합니다.

**39. 정답: C**

* **해설:** Switch 문에서 정의한 특정 조건들 외에 나머지 모든 경우를 한꺼번에 처리하려면 **Otherwise (Default)** 분기에 에러 처리 로직을 연결하면 됩니다.

**40. 정답: C**

* **해설:** 데이터베이스 속성 길이(50)보다 긴 값(100)을 강제로 저장하려 하면 데이터베이스 레벨에서 **데이터 잘림 예외(Database Exception)**가 발생합니다.

**41. 정답: B**

* **해설:** OutSystems에서 JavaScript로 특정 위젯을 조작하려면, 해당 위젯의 **Name 속성**이 반드시 지정되어 있어야 런타임에 고유한 HTML ID가 생성됩니다.

**42. 정답: B**

* **해설:** Integer 타입 변수에 텍스트("abc")를 입력하면 OutSystems의 내장 유효성 검사기가 이를 감지하여 해당 위젯의 **Valid 속성을 False**로 변경합니다.

**43. 정답: B**

* **해설:** 하위 모듈(Core)의 구조가 바뀌었는데 상위 모듈(End-User)이 이를 반영(Refresh Reference)하지 않은 채 배포를 시도하면 **Incompatible Producer** 에러가 발생합니다.

**44. 정답: B**

* **해설:** JSON 문자열은 복잡한 구조를 가지므로, 이를 OutSystems 데이터로 변환할 때는 그 구조와 일치하는 **Structure** (또는 List of Structure) 타입이 필요합니다.

**45. 정답: B**

* **해설:** OutSystems는 Aggregate에서 화면이나 로직에 실제로 바인딩되지 않은 컬럼을 감지하여 SQL 쿼리 시 자동으로 제외하는 **조회 최적화**를 수행합니다.

**46. 정답: B**

* **해설:** SQL 위젯에서 `Expand Inline` 파라미터를 사용하여 쿼리를 동적으로 생성할 때, 보안을 위해 반드시 해당 파라미터를 **EncodeSql()** 함수로 감싸야 합니다.

**47. 정답: B**

* **해설:** 애플리케이션의 공통 레이아웃(헤더, 푸터 포함)은 보통 **Common UI Flow** 안에 블록 형태로 정의되어 있으며, 테마(Theme)와 연결되어 관리됩니다.

**48. 정답: C**

* **해설:** `CreateOrUpdate...`는 서버와 통신하여 데이터베이스를 수정하는 **Server/Entity Action**입니다. 클라이언트 내에서 리스트 데이터를 조작하는 액션은 `ListAppend`, `ListRemove` 등입니다.

**49. 정답: B**

* **해설:** Reactive Web에서 뒤로 가기를 하면 브라우저 메모리에 유지된 상태를 보여주기도 하므로, **On Initialize**가 항상 다시 실행되지는 않습니다. 확실한 갱신이 필요하면 `OnReady` 등을 고려해야 합니다.

**50. 정답: B**

* **해설:** OutSystems 자격증 시험은 단순히 이론만 묻는 것이 아니라, "특정 비즈니스 시나리오에서 어떤 기능이 가장 적합한가?"를 묻는 문제가 대부분입니다. 따라서 단순히 정답을 외우기보다는, 강사 Gem과 함께 공부한 **개념(Lifecycle, Architecture, Security 등)**을 본인의 **실무 경험(MES, 공장 관리 등)**과 연결하여 논리적으로 판단하는 것이 합격의 가장 큰 비결입니다.