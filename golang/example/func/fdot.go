package main
import "fmt"



func add( num ...int){
	for _,val:= range num{
		//fmt.Println(i)
		fmt.Println(val)
	}
}


func main(){
	add(2,3,3)
}

