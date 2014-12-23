package main

import "fmt"

func main(){
//a := map [string]int {}
a := make(map [string]int)
a["user"]=1
a["name"]=2
for key,v:=range a {
	fmt.Println(v)
	fmt.Println(key)
}
}
