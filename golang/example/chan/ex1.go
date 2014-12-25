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
	fmt.Println("into sq1")
		for n := range in {
			out <- n * n
		}
		close(out)
	fmt.Println("into sq2")
	}()
	fmt.Println("into sq3")
	return out
}
func trick(){
	fmt.Println("main1")
	s := gen(2)
	fmt.Println("main2")
	out:= sq(s)
	fmt.Println("main3")
	fmt.Print(<-out)
}
func main() {
	//go sq(s)
	go trick()
	go trick()
        var input string
	        fmt.Scanln(&input)
}
