package main

import "fmt"

type Car1 struct{
	name string
	wheels int
}

func (data *Car1)showcar(){
	fmt.Println("in struct def",data.name, data.wheels)
}

func f1(x int) (int, error){
	fmt.Println(x)
	return x+1, nil
}
func f2(car Car1)(int, error){
	fmt.Println("output",car.name, car.wheels)
	return 1, nil

}
func f3(car []Car1)(int, error){
	for index,data := range car{
	fmt.Println("output",data.name, data.wheels, index)
}
	return 1, nil

}
func f4(car []Car1)(int, error){
	for _,data := range car{
	  data.showcar()
  }
	return 1, nil

}
func testf4(){
	s := []Car1{}
	tmp:=Car1{name:"Benz",wheels:4}
	s=append(s,tmp)
	tmp=Car1{name:"Farrari",wheels:4}
	s=append(s,tmp)
	tmp=Car1{name:"BMW",wheels:4}
	s=append(s,tmp)
	f4(s)
	s[0].showcar()
}
func testf3(){
	s := []Car1{}
	tmp:=Car1{name:"Benz",wheels:4}
	s=append(s,tmp)
	tmp=Car1{name:"Farrari",wheels:4}
	s=append(s,tmp)
	tmp=Car1{name:"BMW",wheels:4}
	s=append(s,tmp)
	data,err := f3(s)
	fmt.Println("result f3",data, err)
}

func testf2(){
	carr:="benz"
	s := Car1{name:carr,wheels:4}
	data,err := f2(s)
	fmt.Println("result",data, err)
}
func testf1(){
s:=1
afteradd, err:=f1(s)
fmt.Println("after add",afteradd)
fmt.Println("after add v2",err)
}

func main(){
//a := map [string]int {}
testf1()
testf2()
testf3()
testf4()
}
