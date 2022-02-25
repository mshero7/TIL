/*
  block.go
  블록의 구조 / 해시값 계산 / 새로운 블록 생성 및 새로운 제네시스 블록 생성 구현 과정
  제네시스 블록 : 블록체인에서 생성된 첫 번째 블록, 해당 블록체인 네트워크가 시작되었다는 상징적 의미를 갖고 있다.
*/

package main

import (
	"bytes"
	"crypto/sha256"
	"fmt"
	"strconv"
	"time"
)

type Block struct {
	Timestamp     int64  // 생성시간
	Data          []byte // 가치있는 정보
	PrevBlockHash []byte // 이전 블록의 해시
	Hash          []byte // 현재 블록의 해시
	Nonce         int    // 블록체인에서 목표값 이하의 블록 해시를 찾기 위해 임시로 사용하는 숫자.
}

// Block 해시값을 계산하는 과정을 구현한 것
func (b *Block) SetHash() {
	timestamp := []byte(strconv.FormatInt(b.Timestamp, 10))
	headers := bytes.Join([][]byte{b.PrevBlockHash, b.Data, timestamp}, []byte{})
	hash := sha256.Sum256(headers)

	b.Hash = hash[:]
}

// 새로운 블록을 만들어 내는 과정을 구현한 것
func NewBlock(data string, preBlockHash []byte) *Block {
	block := &Block{time.Now().Unix(), []byte(data), preBlockHash, []byte{}, 0}
	pow := NewProofOfWork(block)
	nonce, hash := pow.Run()

	block.Hash = hash
	block.Nonce = nonce

	return block
}

//blockchain.go
//blockchain 을 구현한 것
type Blockchain struct {
	blocks []*Block
}

// Go Method
func (bc *Blockchain) AddBlock(data string) {
	prevBlock := bc.blocks[len(bc.blocks)-1]
	newBlock := NewBlock(data, prevBlock.Hash)
	bc.blocks = append(bc.blocks, newBlock)
}

func NewGenesisBlock() *Block {
	return NewBlock("Genesis Block", []byte{})
}

func NewBlockchain() *Blockchain {
	return &Blockchain{[]*Block{NewGenesisBlock()}}
}

func main() {
	bc := NewBlockchain()

	bc.AddBlock("Send 1 BTC to Sangsu Moon")
	bc.AddBlock("Send 2 more BTC to Sangsu Moon")

	for _, block := range bc.blocks {
		fmt.Printf("Prev. hash: %x\n", block.PrevBlockHash)
		fmt.Printf("Data: %s\n", block.Data)
		fmt.Printf("Hash: %x\n", block.Hash)
		fmt.Println()
	}
}
