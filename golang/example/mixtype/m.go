package main
import "fmt"




func main(){
	n:=make(map[string]interface{})
	// or n:=make(map[interface{}]string)
	n["1"]=1
	n["2"]="two"
	fmt.Println(n["1"],n["2"])
	a:=n["1"]
	b:=n["2"]
}
