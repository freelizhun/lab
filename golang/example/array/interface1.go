package main

import "fmt"

type Info interface {
	Noofchar() int
	Increment()
}

type Testinfo struct {
	noofchar int     
}

func (x *Testinfo) Noofchar() int {
	return x.noofchar
}
func (x *Testinfo) Increment() {
	x.noofchar++
}

func main(){
	var t Info = &Testinfo{noofchar:1}
	fmt.Println("No of char ",t.Noofchar())
	t.Increment()
	fmt.Println("No of char ",t.Noofchar())
}
