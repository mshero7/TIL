**패키지**

Go 프로그램은 패키지로 구성되어 있는데, 프로그램은 main 패키지에서 실행을 시작하게 된다.



**Import**

go는 여러 import 문을 아래와 같이 적을 수 있다. (권장사항)

```go
import (
	"fmt"
	"math"
)
```



**Export되는 이름**

대문자로 시작하는 이름이 export 되는데, 그 말은 package 를 import 할 때 그 패키지의 export 된 이름들만 참조할 수 있다.

```go
package main

import (
	"fmt"
	"math"
)

func main() {
    fmt.Println(math.pi) // (X)
    fmt.Println(math.Pi) // (X)
}
```



**함수**

변수 이름 뒤, 매개변수 선언부 뒤에 타입을 명시해준다. 매개 변수가 같을땐 아래와 같은 표현으로 작성할 수 있다.

```go
package main

import "fmt"

func add(x int, y int) int {
	return x + y
}

func add2(x, y int) int {
	return x + y
}

func main() {
	fmt.Println(add(42, 13))
}
```

복수개의 결과를 얻고자 할때는 아래와 같이 표현한다.

```go
package main

import "fmt"

func swap(x, y string) (string, string) {
	return y, x
}

func main() {
    a, b := swap("hello", "world") // 함수 내에서 := 선언과 초기화를 동시에
	fmt.Println(a, b)
}
```



**변수**

변수 선언은 한 변수 당 하나의 초기값을 포함할 수 있다.

```go
var i, j int = 1, 2
var i, j = 1,2 
```

함수 내에서는 `:=` 라는 짧은 변수 선언은 암시적 type으로 `var` 선언처럼 사용될 수 있습니다.

함수 밖에서는 모든 선언이 키워드(`var`, `func`, 기타 등등)로 시작하므로 `:=` 구문은 사용할 수 없습니다.



**기본 자료형**

```go
1) bool
2) string
3) int  int8  int16  int32  int64
4) uint uint8 uint16 uint32 uint64 uintptr
5) byte // uint8의 별칭
6) rune // int32의 별칭
        // 유니코드에서 code point를 의미합니다.
7) float32 float64
8) complex64 complex128
```



**Zero values**

```go
명시적인 초깃값 없이 선언된 변수는 그것의 zero value 가 주어집니다.

숫자 type에는 0
boolean type에는 false
string에는 "" (빈 문자열)
```



**타입 변환**

uint 타입의 z 에 float64 타입인 f를 넣으면 오류

```go
package main

import (
	"fmt"
	"math"
)

func main() {
	var x, y = 3, 4
	var f float64= math.Sqrt(float64(x*x + y*y))
	var z uint = uint(f) // 
	fmt.Println(x, y, z, f)
}
```



**상수**

상수는 변수처럼 선언되지만 `const` 키워드와 함께 선언됩니다.

상수는 `character` 혹은 `string`, `boolean`, 숫자 값이 될 수 있습니다.

상수는 `:=` 를 통해 선언될 수 없습니다.

```go
const Truth = true
...
const Truth = false // ( X ) 불가능
```

