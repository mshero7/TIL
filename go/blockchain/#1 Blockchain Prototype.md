# #1 Go로 블록체인 만들기

### 블록

블록 체인에서 가장 가치있는 정보, 즉 **거래**를 저장하는 부분.

블록은 header 와 body로 나뉘며, 거래가 담기는 공간은 block body 이다. header 에는 블록의 버전, 현재 시각 그리고 이전 블록의 해시 등 블록의 메타데이터가 저장된다.

실제 비트코인에서는 Timestamp, PrevBlockHash, Hash 는 분리된 공간인 블록헤더에 저장되고, ‘거래’는 또 다른 분리된 공간인 블록 바디에 저장된다. ( 우리는 간단하게 만들거니까 합침 )

```go
// Block 해시값을 계산하는 과정을 구현한 것
func (b *Block) SetHash() {
	timestamp := []byte(strconv.FormatInt(b.Timestamp, 10))
	headers := bytes.Join([][]byte{b.PrevBlockHash, b.Data, timestamp}, []byte{})
	hash := sha256.Sum256(headers)

	b.Hash = hash[:]
}
```

### 해시

해시는 특정 값을 해시함수를 통해 나온 임의의 난수값을 해시라고 한다. 

### 해시의 역할

블록을 안전하게 보호하는 역할을 하며, 다시 내부 내용을 수정하지 못하도록 설계가 되어있다.

이제 블록을 연결할수 있는 해시를 담을수 있는 코드를 만들어보자

```go
// 새로운 블록을 만들어 내는 과정을 구현한 것
func NewBlock(data string, preBlockHash []byte) *Block {
	block := &Block{time.Now().Unix(), []byte(data), preBlockHash, []byte{}}
	block.SetHash()

	return block
}
```

### 블록체인

“블록체인” 에서 “체인”을 만들어보고자 한다. 블록체인을 간단하게 설명하면 링크드 리스트 형태의 데이터베이스이다. 블록은 투입된 순서에 맞게 저장되고, 각각의 블록은 그 앞의 블록과 연결되어져 있다는 뜻이다.

다른 언어에서는 미리 구현되어있는 경우도 있지만, go에서는 배열과 맵으로 구현할 수 있다.

배열은 정렬된 해시를 보관하고 [1]

맵은 해시와 블록의 쌍을 보관한다[2]

우선 해시를 통해 블록에 접근할 필요가 없기 때문에 배열만 사용했다.

```go
// Block 들을 담을 구현체
type Blockchain struct {
    blocks *[]Block
}
```

블록 체인을 추가하는 함수

```go
// 새로운 block이 blockchain에 추가되는 과정을 구현한 것 
func(bc *Blockchain) AddBlock(data string) {
  prevBlock   :=  bc.blocks[len(bc.blocks)-1]
  newBlock    :=  NewBlock(data, prevBlock.Hash)
  bc.blocks   :=  append(bc.blocks, newBlock)
}
```

첫 블록체인을 뜻하는 genesisblock 함수를 생성해보자.

```go
// 새로운 genesisBlock을 만드는 과정을 구현한 것
func NewGenesisBlock() *Block{
  return NewBlock("Genesis Block", []byte{})
}
```

앞서 만들어놓은 함수들로 블록체인을 생성하는 함수를 만들자

```go
//blockchain.go
//새로운 genesisblock으로 새로운 블록체인을 만드는 과정을 구현한 것
func NewBlockchain() *Blockchain {
	return &Blockchain{[]*Block{NewGenesisBlock()}}
}
```

지금까지 구현한 함수들이 잘 작동하는지 main함수를 통해 확인해보자

```go
package main 

import (
  "fmt"
)

func main() {
  // 새로운 블록체인 생성
  bc := NewBlockchain()
  // 새로운 블록들 생성
  bc.AddBlock("Send 1 BTC to Ivan")
  bc.AddBlock("Send 2 more BTC to Ivan")
  // 블록체인 출력
  for _, block := range bc.blocks {
          fmt.Printf("Prev. hash : %x\n", block.PrevBlockHash)
          fmt.Printf("Data : %s\n", block.Data)
          fmt.Printf("Hash : %x\n", block.Hash)
          fmt.Println()
  }
}
```

### 결과

```go
Prev. hash: 
Data: Genesis Block
Hash: ae09bdd5c1b76a8ee6bcfa9ef13638e419c212eb81e14985607ce85fdb3ca522

Prev. hash: ae09bdd5c1b76a8ee6bcfa9ef13638e419c212eb81e14985607ce85fdb3ca522
Data: Send 1 BTC to Sangsu Moon
Hash: 4d536e6c4ba56695d0fc4b206d706c79bdba84b13b70e4b7f66bf1273ae621e5

Prev. hash: 4d536e6c4ba56695d0fc4b206d706c79bdba84b13b70e4b7f66bf1273ae621e5
Data: Send 2 more BTC to Sangsu Moon
Hash: d56abb14b1292382fae27a2dbf24589d2d0ed814021d4b9dfec5e31ee810ccef
```

Genesis Block 을 제외한 첫번째 블록부터 이전 hash값들이 일치하는것을 확인할수있다.

지금까지 매우 간단한 형태의 블록체인을 만들어 보았다. 지금은 단순한 블록들의 나열뿐이고, 실제는 더욱 복잡하게 되어져 있다. 그 과정에는 대표적으로 Pow(작업증명), PoS(지분 증명) 등이 존재한다.