package main
import "fmt"



func rc() <- chan int{
	fmt.Println("into rc")
	c:=make(chan int)
	c <- 5
	return c
}
/*
func rcc(in <-chan int) <- chan int{
	out:=make(chan int)
	for n:=range in{
		out <- n+1
	}
	return out
}
*/

func main(){
	w := rc()
	fmt.Println(<-w)
	//s := rcc(c)
	//fmt.Println(<-s)
}
