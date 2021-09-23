javascript 메모리와 변수

자바스크립트의 동작원리



 

**비트와 바이트**

비트 : 0과 1만 표현할 수 있는 메모리 조각.

바이트 : 8개의 비트. -> 1바이트의 문자 조합은 256가지



**메모리**

데이터를 저장할 수 있는 셀의 집합. 1byte 여러개.

js는 숫자형 변수를 저장하기 위해 8byte(64bit) 을 메모리에 할당. 이 숫자의 메모리 주소값은 첫번째 1byte의 주소값이 된다.



프로그램은 시작하면서 메모리를 할당, 회수하게 되는데 자바스크립트에서는 Resident Set 이라는 곳에 저장하게 되고 각각 segement를 가지게 된다. 

![image-20210923193953008](C:\Users\Moon\AppData\Roaming\Typora\typora-user-images\image-20210923193953008.png)

1) Heap Segement

   ㄴ 참조타입 데이터가 저장되는 곳

   ㄴ 가비지 컬렉션이 발생되는 곳

2) Stack Segement

   ㄴ 원시타입의 데이터가 저장되는 곳



**변수**

1) 값을 저장하기 위해 확보한 메모리 공간 자체
2) 메모리 공간을 식별하기 위해 붙인 이름 (식별자)



**식별자**

1. 어떤 값을 식별할 수 있는 고유한 이름 (변수, 함수 등등)
2. 메모리 주소에 붙인 이름



변수와 식별자가 헷갈릴 수 있는데, 변수는 값을 가지고 있는것이고 식별자는 주소를 가지고 있다 생각하면 된다.



**변수의 선언 단계**

1. 선언 단계 : 렉시컬 환경 -> 환경 레코드에 식별자를 등록
2. 초기화 단계 : 값을 저장히기 위한 메모리 공간을 확보 후 undefined로 초기화

예시)

var 키워드로 선언된 변수는 1,2 단계가 한 번에 진행되어 호이스팅 가능.

```javascript
console.log(score); // 2) undefined 출력

score = 80; // 3) 80 을 위한 메모리 확보후 score 에 할당
var score; // 1) 호이스팅 / 메모리에 undefined 할당 후 score 식별자에 주소 할당

console.log(score); // 4) 출력

score = 90; // 5) 재할당
```

const / let 키워드 는 평가 단계에서 선언 단계가 이뤄지고 런타임에서 초기화 가 진행된다. (선언단계는 score 에 undefined 로 초기화되지 않은 상태.)

```javascript
console.log(score) // cannot access 'score' before initialization

score = 80;
const = score;

console.log(score);

score = 90;
```

```javascript
console.log(score) // score is not defined

score = 80;
const = score; // SysnaxError: Unexpected token

console.log(score);

score = 90; // 재할당이 불가, 즉 선언과 할당이 동시에 이뤄져야 함
```

let, const 키워드는 참조에러가 발생할 수 있으니 유의해서 써야한다.



더 이상 참조되지 않는 변수들은 GC가 메모리 공간 할당 해제함



**호이스팅**

- JS 엔진이 평가단계에서 해당 스코프의 코드를 실행하는데 필요한 변수의 선언부(와 함수 선언문)을 실행컨텍스트에 저장하는 것을 의미





자바스크립트는 **평가단계**와 **실행단계** 두단계로 나누어 실행한다.

```javascript
const result = 10 + 20
```

1) 콜스택에 임의의 주소 세곳에 10과 20 합의 결과인 30을 주소에 할당
2) result 주소값을 30의 주소값