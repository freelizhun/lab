package main

import (
	"fmt"
	"time"
)

func gen(nums ...int) <-chan int {
	fmt.Println("into gen")
	out := make(chan int)
	go func() {
		fmt.Println("into sub go")
		time.Sleep(time.Second * 10)
		for _, n := range nums {
			out <- n
		}
		close(out)
		fmt.Println("into sub go1")
	}()
		fmt.Println("into sub go2")
	return out
}

func sq(in <-chan int) <-chan int {
	fmt.Println("into sq")
	out := make(chan int)
	go func() {
		for n := range in {
			out <- n * n
		}
		close(out)
	}()
	return out
}

func main() {
	s := gen(2)
	out:= sq(s)
	fmt.Print(<-out)
}
