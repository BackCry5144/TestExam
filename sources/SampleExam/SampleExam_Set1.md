**1.** `Customer` 엔티티와 `Order` 엔티티는 1:N 관계입니다. `Order` 엔티티의 `CustomerId` 속성(Foreign Key)에 설정된 **Delete Rule**이 **Delete**입니다. 사용자가 특정 `Customer` 레코드를 삭제하면 어떤 일이 발생합니까?
A. `Customer`만 삭제되고 `Order`는 남는다.
B. `Order`가 하나라도 있으면 `Customer` 삭제가 거부된다.
C. `Customer`가 삭제되고, 해당 고객의 모든 `Order`도 함께 삭제된다.
D. `Customer`는 삭제되지 않고 `Order`만 삭제된다.

**2.** 런타임(애플리케이션 실행 중)에 레코드를 추가하거나 수정할 수 **없는** 엔티티는 무엇입니까?
A. Static Entity
B. Entity
C. Structure
D. External Entity

**3.** `Employee` 엔티티에 `Email` 속성이 있습니다. 동일한 이메일 주소가 중복되어 저장되는 것을 방지하기 위해 가장 적절한 방법은?
A. Email 속성을 Mandatory로 설정한다.
B. Email 속성에 Unique Index를 생성한다.
C. OnBeforeSave 로직에서 중복 체크를 한다.
D. 엔티티의 Expose Read Only를 Yes로 설정한다.

**4.** Many-to-Many (N:N) 관계, 예를 들어 `Student`와 `Class` 관계를 구현하기 위한 가장 일반적인 방법은?
A. `Student` 엔티티에 `ClassId`를 추가한다.
B. `Class` 엔티티에 `StudentId`를 추가한다.
C. 두 엔티티를 연결하는 세 번째 Junction(교차) 엔티티를 생성한다.
D. Static Entity를 사용하여 두 엔티티를 매핑한다.

**5.** Entity의 속성(Attribute) 데이터 타입으로 설정할 수 **없는** 것은?
A. Text
B. Binary Data
C. Date Time
D. List

**6.** 기존 데이터베이스 엔티티를 OutSystems로 가져오려 합니다. 이를 위해 사용해야 하는 도구는?
A. Service Studio
B. Integration Studio
C. Service Center
D. LifeTime

**7.** Entity 속성의 `Is Mandatory`가 **Yes**로 설정되어 있습니다. 데이터베이스에 레코드를 생성할 때 값을 제공하지 않으면 어떻게 됩니까?
A. 데이터베이스 오류(Database Exception)가 발생한다.
B. Null 값이 저장된다.
C. 해당 데이터 타입의 기본값(Default Value)이 저장된다.
D. 컴파일 오류가 발생한다.

**8.** `Order` 엔티티의 `StatusId`는 `OrderStatus`라는 Static Entity를 참조합니다. 코드 내에서 "Shipped" 상태인지 확인하는 가장 좋은 방법은?
A. `Order.StatusId = 3` (3은 Shipped의 ID)
B. `Order.StatusId = "Shipped"`
C. `Order.StatusId = Entities.OrderStatus.Shipped`
D. `GetOrderStatus(Order.StatusId).Label = "Shipped"`

**9.** Aggregate에서 `Employee`와 `Department` 엔티티를 조인했습니다. Join 규칙은 **With or Without**입니다. 이 결과는 SQL의 어떤 조인과 같습니까?
A. Inner Join
B. Left Join
C. Right Join
D. Full Outer Join

**10.** 화면(Screen)에 진입하자마자 데이터를 가져오지 않고, 사용자가 "검색" 버튼을 눌렀을 때만 Aggregate를 실행하고 싶습니다. Aggregate의 **Fetch** 속성을 어떻게 설정해야 합니까?
A. At Start
B. On Demand
C. Only on Click
D. Lazy Load

**11.** Aggregate에서 결과의 개수를 제한(예: 상위 10개만 표시)하기 위해 사용하는 속성은?
A. Length
B. Count
C. Max Records
D. Start Index

**12.** `GetEmployees` Aggregate가 있습니다. 사용자가 입력한 검색어(`SearchKeyword`)가 이름(Name)에 포함된 직원만 필터링하는 올바른 Filter 조건식은?
A. `Employee.Name = SearchKeyword`
B. `Employee.Name like "%" + SearchKeyword + "%"`
C. `Index(Employee.Name, SearchKeyword) > -1`
D. `Filter(Employee.Name, SearchKeyword)`

**13.** Data Action을 Aggregate 대신 사용해야 하는 가장 적절한 시나리오는?
A. 데이터베이스에서 단순 조회할 때
B. 데이터를 가져온 후 복잡한 로직(예: 외부 API 호출 결과와 결합)이 필요할 때
C. 데이터를 정렬(Sorting)해야 할 때
D. 데이터를 페이징(Pagination)해야 할 때

**14.** Aggregate의 실행이 완료된 직후에 특정 로직을 수행하려면 어떤 이벤트를 사용해야 합니까?
A. On Initialize
B. On Ready
C. On After Fetch
D. On Render

**15.** `GetOrders` Aggregate의 결과 목록(`List`)이 비어있는지 확인하는 가장 효율적인 방법은?
A. `GetOrders.List.Empty`
B. `GetOrders.List.Length = 0`
C. `GetOrders.Count = 0`
D. `GetOrders.List.Current = Null`

**16.** Aggregate에서 계산된 컬럼(Calculated Attribute)을 추가했습니다. 예를 들어 `Price * Quantity`를 `Total`이라는 이름으로 만들었습니다. 이 `Total` 값으로 정렬(Sorting)할 수 있습니까?
A. 아니요, 데이터베이스 컬럼만 정렬 가능합니다.
B. 예, 하지만 오름차순만 가능합니다.
C. 예, 계산된 속성도 정렬 기준(Sort) 탭에서 사용할 수 있습니다.
D. 아니요, Data Action을 사용해야 합니다.

**17.** 두 개의 Aggregate `GetProducts`와 `GetCategories`가 있습니다. `GetProducts`의 실행이 완료된 후 `GetCategories`를 실행해야 합니다. 어떻게 구현합니까?
A. 두 Aggregate의 순서를 드래그하여 변경한다.
B. `GetProducts`의 On After Fetch 액션 내에서 `Refresh Data`로 `GetCategories`를 호출한다.
C. OutSystems는 자동으로 순차 실행하므로 설정할 필요가 없다.
D. JavaScript를 사용해야 한다.

**18.** SQL Widget(Advanced SQL)을 사용할 때, 외부로부터 받은 입력 파라미터를 쿼리에 직접 연결하면 발생하는 보안 위험은?
A. Cross-Site Scripting (XSS)
B. SQL Injection
C. Cross-Site Request Forgery (CSRF)
D. Buffer Overflow

**19.** 화면(Screen)의 수명 주기(Lifecycle) 이벤트가 실행되는 올바른 순서는?
A. On Initialize -> On Ready -> On Render
B. On Ready -> On Initialize -> On Render
C. On Initialize -> On Render -> On Ready
D. On Render -> On Ready -> On Initialize

**20.** 웹 블록(Block) 내부에서 발생한 이벤트를 부모 화면(Parent Screen)에 알리기 위해 사용하는 것은?
A. Input Parameter
B. Client Variable
C. Event & Handler
D. Site Property

**21.** 사용자가 입력한 데이터가 유효한지 검사하기 위해 `Form` 위젯을 사용 중입니다. 버튼을 클릭했을 때 클라이언트 측 유효성 검사가 통과했는지 확인하는 프로퍼티는?
A. `Form.IsValid`
B. `Form.CheckValidity`
C. `Input.Valid`
D. `Button.Enabled`

**22.** 여러 화면에서 공통으로 사용되는 UI 요소(예: 헤더, 메뉴)를 재사용하기 위해 만드는 것은?
A. Web Screen
B. Block
C. External Site
D. Container

**23.** 목록(List) 데이터를 테이블 형태로 보여주되, 모바일 기기에서는 카드 형태로 보여주고 싶습니다. OutSystems UI가 제공하는 반응형 동작을 위해 테이블 위젯에 어떤 설정을 확인해야 합니까?
A. 아무것도 하지 않아도 자동으로 변환된다.
B. Table 위젯은 모바일을 지원하지 않는다.
C. Adaptive 속성을 True로 설정한다.
D. Table Records 위젯을 사용해야 한다.

**24.** `Link` 위젯이나 `Button` 위젯을 클릭하여 다른 화면으로 이동할 때 데이터를 전달하는 방법은?
A. Session Variable 사용
B. Global Variable 사용
C. 대상 화면의 Input Parameter에 값 매핑
D. Database에 임시 저장

**25.** 화면에 있는 데이터를 엑셀 파일로 다운로드하는 기능을 구현하려 합니다. 버튼을 클릭했을 때 호출되는 액션은 어디에 위치해야 합니까?
A. Client Action (Download 위젯 사용)
B. Server Action (Download 위젯 사용)
C. Client Action에서 JavaScript 사용
D. Aggregate 속성

**26.** Container 위젯의 `Display` 속성이 `False`인 경우와 `Visible` 속성이 `False`인 경우의 차이점은?
A. 차이 없음.
B. Display는 CSS로 숨기고(공간 차지함), Visible은 DOM에서 제거된다.
C. Visible은 CSS로 숨기고(공간 차지함), Display는 DOM에 렌더링되지 않는다(If 위젯 효과).
D. Display는 서버 사이드, Visible은 클라이언트 사이드 속성이다.

**27.** Client Action 내에서 데이터베이스에 데이터를 저장(CreateOrUpdate)하려고 합니다. 올바른 방법은?
A. Client Action 내에서 Entity Action(CreateOrUpdate)을 직접 호출한다.
B. Server Action을 만들고 그 안에서 Entity Action을 호출한 뒤, Client Action에서 이 Server Action을 호출한다.
C. SQL 위젯을 Client Action에 배치한다.
D. Aggregate를 사용하여 저장한다.

**28.** Server Action의 `Function` 속성을 **Yes**로 설정했습니다. 이에 대한 설명으로 옳은 것은?
A. 이 액션은 Client Side에서만 실행된다.
B. 이 액션은 Output Parameter를 하나만 가질 수 있으며, 표현식(Expression) 내에서 직접 사용할 수 있다.
C. 이 액션은 데이터베이스 트랜잭션을 사용하지 않는다.
D. 이 액션은 비동기(Asynchronous)로 실행된다.

**29.** `For Each` 루프를 사용하여 리스트를 순회하던 중, 특정 조건에서 루프를 완전히 종료하고 싶습니다. 어떤 요소를 연결해야 합니까?
A. End
B. Cycle
C. Connect to the For Each node again
D. Raise Exception

**30.** 예외(Exception)가 발생했을 때 처리되는 순서(우선순위)로 올바른 것은?
A. Global Exception Handler -> UI Exception Handler -> Action Exception Handler
B. Action Exception Handler -> UI Exception Handler -> Global Exception Handler
C. UI Exception Handler -> Action Exception Handler -> Global Exception Handler
D. 무작위로 실행된다.

**31.** Logic Flow에서 `Assign` 위젯의 역할은?
A. 변수의 값을 변경한다.
B. 변수의 타입을 변경한다.
C. 새로운 변수를 선언한다.
D. 데이터베이스에 값을 할당한다.

**32.** 디버깅(Debugging) 중 `Suspend Execution` 기능을 켰습니다. 애플리케이션이 멈추는 지점은?
A. 오류가 발생한 지점
B. 사용자가 설정한 Breakpoint
C. 모든 Server Action의 시작점
D. 화면이 로딩되는 시점

**33.** Client Variable의 특징으로 **틀린** 것은?
A. 브라우저의 로컬 스토리지 등에 저장된다.
B. 사용자가 로그아웃해도 값이 유지될 수 있다.
C. 비밀번호와 같은 민감한 정보를 저장하기에 적합하다.
D. 기본 데이터 타입(Text, Integer, Boolean 등)만 저장 가능하다.

**34.** JSON 형식의 텍스트 데이터를 OutSystems의 Record 또는 List로 변환하는 액션은?
A. JSON Serialize
B. JSON Deserialize
C. XML To Record
D. Text To Object

**35.** 비동기적으로(백그라운드에서) 로직을 실행하기 위해 사용하는 요소는?
A. Server Action
B. Service Action
C. Timer
D. Process

**36.** 애플리케이션의 모든 사용자가 로그인 없이 접근할 수 있는 화면을 만들고 싶습니다. 해당 화면의 Role 설정은?
A. Registered 체크
B. Anonymous 체크
C. Everyone 체크
D. Internal 체크

**37.** 특정 버튼을 'Admin' 권한(Role)을 가진 사용자에게만 보여주고 싶습니다. 가장 적절한 방법은?
A. 버튼을 삭제한다.
B. 버튼을 If 위젯으로 감싸고, 조건에 `CheckAdminRole(UserId)`을 사용한다.
C. 버튼의 Visible 속성을 False로 한다.
D. CSS로 `display: none` 처리한다.

**38.** `Registered` Role은 어떤 사용자에게 부여됩니까?
A. OutSystems에 등록된 모든 사용자 (로그인한 사용자)
B. 익명 사용자
C. 관리자 그룹
D. 특정 애플리케이션 사용자

**39.** 모듈(Module) 간의 참조(Dependency)에서 `Strong Reference`가 발생하는 경우는?
A. Server Action을 참조할 때
B. Service Action을 참조할 때
C. Structure를 참조할 때
D. Client Action을 참조할 때

**40.** User 엔티티의 비밀번호를 저장할 때 OutSystems가 자동으로 처리하는 보안 방식은?
A. 평문 저장 (Plain Text)
B. 양방향 암호화 (AES)
C. 해시 처리 (One-way Hash)
D. 저장하지 않음

**41.** [Fetch] Aggregate에서 'Group By'를 사용하여 부서별 직원 수를 세려고 합니다. Group By를 적용하면 Aggregate의 출력 결과(Output List)는 어떻게 변합니까?
A. 변화 없다.
B. 그룹화된 속성과 집계 함수 결과만 포함된 새로운 구조로 변경된다.
C. 기존 엔티티의 모든 속성을 유지한다.
D. 컴파일 오류가 발생한다.

**42.** [UI] Dropdown 위젯에 데이터베이스의 값을 표시하려면 어떤 속성을 설정해야 합니까?
A. List, Variable, Option Text, Option Value
B. Source Record List, Destination
C. Entities, Attribute
D. Input Parameter

**43.** [Logic] Server Action 'A'가 Server Action 'B'를 호출합니다. 'A'와 'B' 모두 `Public = Yes`입니다. 만약 'B'에서 에러가 발생하여 `Abort Transaction`이 실행되면 'A'에서 수행한 데이터베이스 변경 사항은?
A. 커밋된다 (저장됨).
B. 롤백된다 (취소됨).
C. 부분적으로 저장된다.
D. 'A'의 설정에 따라 다르다.

**44.** [Data] Static Entity의 `Records` 중 하나를 우클릭하여 'Identifier'를 변경했습니다. 이 변경 사항을 적용하려면 어떻게 해야 합니까?
A. 즉시 적용된다.
B. 1-Click Publish를 해야 한다.
C. 데이터베이스를 직접 수정해야 한다.
D. 변경할 수 없다.

**45.** [UI] Pagination(페이지네이션) 패턴을 사용할 때, `MaxRecords`와 `StartIndex` 변수는 주로 어디에 연결됩니까?
A. Screen의 Input Parameter
B. Local Variable 및 Aggregate의 속성
C. Site Property
D. Session Variable

**46.** [Security] `GrantRegisterRole` 액션을 사용하여 사용자에게 역할을 부여했습니다. 이 변경 사항이 현재 로그인된 세션에 즉시 반영됩니까?
A. 예, 즉시 반영됩니다.
B. 아니요, 다음 로그인 시부터 반영됩니다.
C. 아니요, 로그아웃 후 다시 로그인해야 합니다. (단, 프로그래밍적으로 세션 갱신 가능)
D. 서버를 재시작해야 합니다.

**47.** [Arch] 4-Layer Architecture (Canvas)의 레이어 순서(아래에서 위로)가 맞는 것은?
A. Foundation -> Core -> End User -> Orchestration
B. Library -> Core -> End User -> Orchestration
C. Data -> Logic -> Interface -> Process
D. Core -> Library -> Foundation -> End User

**48.** [Data] Text 타입의 속성 길이를 50에서 100으로 늘렸습니다. Publish 시 데이터베이스에는 어떤 일이 발생합니까?
A. 데이터 손실 없이 컬럼 크기가 커진다.
B. 기존 데이터가 모두 삭제된다.
C. 새로운 컬럼이 생성된다.
D. 에러가 발생하여 Publish 되지 않는다.

**49.** [Logic] `Switch` 위젯은 여러 분기를 가질 수 있습니다. 만약 조건이 True인 분기가 여러 개라면 흐름은 어디로 갑니까?
A. 모든 True 분기를 병렬로 실행한다.
B. 가장 먼저 정의된(위쪽에 있는) True 분기 하나만 실행한다.
C. Random하게 하나를 실행한다.
D. 오류가 발생한다.

**50.** [Lifecycle] 화면의 Input Parameter 값이 변경되면 자동으로 다시 실행되는 수명 주기 이벤트는?
A. On Initialize
B. On Ready
C. On Parameters Changed
D. On Render


#### **[상세 해설]**

**1. 정답: C**

* **해설:** Delete Rule이 `Delete` (Cascade Delete)인 경우, 부모 레코드가 삭제되면 이를 참조하는 모든 자식 레코드도 자동으로 삭제됩니다. (실무: 데이터 무결성을 위해 `Protect`를 권장하나, 로그 데이터 등은 `Delete`를 쓰기도 함)

**2. 정답: A**

* **해설:** `Static Entity`는 개발 시점(Service Studio)에서만 레코드 정의가 가능하며, 런타임에 변경할 수 없습니다.

**3. 정답: B**

* **해설:** 데이터베이스 레벨에서 중복을 원천 차단하는 가장 확실한 방법은 해당 속성(Attribute)의 인덱스(Indexes) 설정에서 `Unique = Yes`로 설정하는 것입니다.

**4. 정답: C**

* **해설:** RDB에서 N:N 관계는 직접 연결할 수 없으므로, 두 엔티티의 ID를 FK로 가지는 `Junction Entity` (교차 엔티티)를 만들어 1:N, N:1로 풀어냅니다.

**5. 정답: D**

* **해설:** 엔티티의 속성으로는 List나 Record 같은 복합 타입(Complex Type)을 직접 저장할 수 없습니다. 별도의 엔티티로 분리해야 합니다.

**6. 정답: B**

* **해설:** 외부 DB와 연결하여 Extension을 생성하는 도구는 `Integration Studio`입니다.

**7. 정답: A**

* **해설:** `Is Mandatory = Yes`인 속성에 값을 넣지 않고 저장하려 하면, OutSystems가 아닌 **데이터베이스 레벨**에서 제약 조건 위반으로 예외(Exception)를 발생시킵니다.

**8. 정답: C**

* **해설:** Static Entity의 레코드는 코드에서 `Entities.[EntityName].[RecordName]` 형태로 접근해야 가독성이 좋고 유지보수에 유리합니다. (하드코딩 지양)

**9. 정답: B**

* **해설:**
* `Only With` = Inner Join
* `With or Without` = Left Join (왼쪽은 다 나오고, 오른쪽은 있으면 나오고 없으면 Null)
* `With` = Right Join

**10. 정답: B**

* **해설:** `At Start`는 화면 로딩 시 자동 실행, `On Demand`는 명시적으로 `Refresh Data`를 호출할 때만 실행됩니다.

**11. 정답: C**

* **해설:** `Max Records` 속성을 통해 쿼리 결과의 최대 개수를 제한합니다.

**12. 정답: B**

* **해설:** 부분 일치 검색(Like 검색)을 구현하려면 `like "%" + Keyword + "%"` 패턴을 사용합니다.

**13. 정답: B**

* **해설:** Aggregate는 단순 DB 조회에 최적화되어 있습니다. REST API 호출 결과와 DB 데이터를 합치거나 복잡한 가공이 필요하면 `Data Action`을 씁니다.

**14. 정답: C**

* **해설:** 데이터 조회가 끝난 후 실행되는 이벤트는 `On After Fetch`입니다. 여기서 결과값을 이용한 계산이나 다른 변수 설정을 합니다.

**15. 정답: A**

* **해설:** OutSystems는 리스트가 비었는지 확인하는 내장 속성 `List.Empty` (Boolean)를 제공합니다. 가장 직관적입니다.

**16. 정답: C**

* **해설:** Aggregate 내에서 만든 계산된 컬럼(Calculated Attribute)도 Sorting 탭에 추가하여 정렬 기준으로 사용할 수 있습니다.

**17. 정답: B**

* **해설:** Reactive Web에서 Aggregate는 비동기로 병렬 실행됩니다. 순서를 보장하려면 선행 Aggregate의 `On After Fetch`에서 후행 Aggregate를 `Refresh Data` 해야 합니다.

**18. 정답: B**

* **해설:** 입력값을 쿼리 스트링에 직접 연결하면 SQL Injection 공격에 취약해집니다. 반드시 `Query Parameter` 기능을 사용해야 합니다.

**19. 정답: C**

* **해설:** `On Initialize` (변수 초기화) -> `On Render` (DOM 그리기 시작) -> `On Ready` (DOM 완성) 순서입니다.

**20. 정답: C**

* **해설:** Block -> Parent Screen 통신은 **Event**를 Trigger하고, Parent는 이를 **Handler**로 받아서 처리합니다.

**21. 정답: A**

* **해설:** Form 전체의 유효성은 `Form.IsValid`로 확인합니다. 하나라도 유효하지 않은 Input이 있으면 False가 됩니다.

**22. 정답: B**

* **해설:** 재사용 가능한 UI 조각은 **Block**입니다.

**23. 정답: A**

* **해설:** OutSystems UI의 기본 Table 위젯은 반응형으로, 모바일에서는 자동으로 List/Card 형태로 스타일이 조정됩니다. (별도 설정 불필요, 다만 컬럼별 Show/Hide 설정 가능)

**24. 정답: C**

* **해설:** 화면 이동 시 데이터 전달은 대상 화면(Screen)의 **Input Parameter**에 값을 매핑하여 전달합니다.

**25. 정답: B**

* **해설:** (중요) 파일 다운로드는 HTTP 응답 헤더 처리가 필요하므로, 반드시 **Server Action** 끝단에서 `Download` 위젯을 사용해야 합니다. Reactive의 Client Action에는 Download 위젯이 없습니다.

**26. 정답: C**

* **해설:**
* `Display`는 If 위젯처럼 동작하여 조건이 False면 **DOM에 아예 생성되지 않습니다.**
* `Visible`은 스타일(`display: none`)로 숨기지만 DOM에는 존재합니다.



**27. 정답: B**

* **해설:** 보안상의 이유로 Reactive Web의 Client Action에서 DB 엔티티 액션(Create, Update 등)을 직접 호출할 수 없습니다. Server Action을 거쳐야 합니다.

**28. 정답: B**

* **해설:** `Function = Yes`인 Server Action은 **반드시 1개의 Output Parameter**만 가질 수 있으며, Expression 내에서 함수처럼 쓸 수 있습니다. (예: `GetStatusLabel(Id)`)

**29. 정답: A**

* **해설:** 루프를 즉시 종료하려면 현재 흐름을 `End` 노드로 연결하면 됩니다. (Break). 다음 반복으로 넘어가려면 흐름을 다시 For Each 노드로 연결합니다 (Continue).

**30. 정답: B**

* **해설:** 예외 처리는 가장 구체적인 곳에서 일반적인 곳으로 전파됩니다. Action 내부 Handler -> UI(Screen) Handler -> Global Handler 순입니다.

**31. 정답: A**

* **해설:** Assign은 변수의 값을 변경(할당)하는 위젯입니다.

**32. 정답: B**

* **해설:** 디버거는 개발자가 설정한 **Breakpoint**에서 멈춥니다.

**33. 정답: C**

* **해설:** Client Variable은 브라우저 쿠키/스토리지 등을 사용하므로 암호화되지 않습니다. 민감 정보 저장 금지.

**34. 정답: B**

* **해설:** JSON String -> Object (Record/List) 변환은 `JSON Deserialize`입니다.

**35. 정답: C**

* **해설:** 백그라운드에서 예약된 시간에 혹은 주기적으로 로직을 실행하는 것은 **Timer**입니다. (Process는 BPT)

**36. 정답: B**

* **해설:** 로그인하지 않은 사용자 = **Anonymous**

**37. 정답: B**

* **해설:** 보안상 UI를 숨길 때는 `If` 위젯을 사용하여 렌더링 자체를 막아야 합니다. 조건에 `CheckRole` 함수를 사용합니다.

**38. 정답: A**

* **해설:** Registered는 로그인한 모든 사용자에게 기본적으로 부여되는 시스템 Role입니다.

**39. 정답: A**

* **해설:** (중요) Server Action을 다른 모듈에서 참조하면 **Strong Reference**가 되어, Producer가 업데이트되면 Consumer도 다시 배포(Republish)해야 합니다. Service Action은 Weak Reference입니다.

**40. 정답: C**

* **해설:** OutSystems는 비밀번호를 안전한 해시 알고리즘(예: BCrypt)으로 단방향 암호화하여 저장합니다.

**41. 정답: B**

* **해설:** Group By를 쓰면 Aggregate의 Output List 구조가 바뀝니다. 그룹화 기준 컬럼 + 집계(Count, Sum 등) 결과만 남습니다.

**42. 정답: A**

* **해설:** Dropdown 설정 필수 4요소: List(소스 데이터), Variable(선택값 저장 변수), Option Text(보여줄 글자), Option Value(저장할 ID).

**43. 정답: B**

* **해설:** 동일한 요청(Request) 내의 Server Action들은 하나의 트랜잭션으로 묶입니다. 하나라도 Abort 되면 전체가 **Rollback** 됩니다.

**44. 정답: B**

* **해설:** Static Entity의 레코드 변경(Identifier 변경 등)은 데이터 모델 변경이므로 **Publish**를 해야 DB에 반영됩니다.

**45. 정답: B**

* **해설:** Pagination은 현재 페이지 시작점(`StartIndex`)과 페이지 당 개수(`MaxRecords`)를 Local Variable로 관리하며 Aggregate에 연결합니다.

**46. 정답: C**

* **해설:** Role 부여/박탈은 다음 로그인 시부터 적용됩니다. 즉시 적용하려면 로그아웃/로그인을 시키거나, 시스템 액션을 통해 세션을 강제로 갱신해야 합니다.

**47. 정답: B**

* **해설:** (O11 Architecture Canvas) Foundation(Library) -> Core -> End User -> Orchestration 순으로 쌓입니다. 하위 레이어는 상위 레이어를 참조할 수 없습니다.

**48. 정답: A**

* **해설:** Text 길이를 늘리는 것은 데이터 손실 없이 가능합니다. (줄이는 것은 경고 발생 및 데이터 잘림 가능성 있음)

**49. 정답: B**

* **해설:** Switch 문은 위에서부터 조건을 검사하여 **가장 먼저 True가 된 첫 번째 분기**로만 이동합니다.

**50. 정답: C**

* **해설:** 화면의 Input Parameter 값이 부모 화면 등에 의해 변경되면 `On Parameters Changed` 이벤트가 발생합니다.