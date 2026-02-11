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