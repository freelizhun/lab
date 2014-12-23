package main

import "fmt"

func main(){
a := []int {}
a = append(a, 2)
a = append(a, 3)
for _,v:=range a {
	fmt.Println(v)
}
}
