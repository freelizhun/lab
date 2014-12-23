package main

import (
	"fmt"
)

var sum int

func workerqueue(num int, c chan int) {
	fmt.Println(num)
	for i := 0; i < 10000000; i++ {
		sum = sum + 1
	}
	fmt.Println(sum)

}

func main() {
	c := make(chan int)
	sum = 0
	for i := 0; i < 100; i++ {
		go workerqueue(i, c)
	}
	var input string
	fmt.Scanln(&input)

}
