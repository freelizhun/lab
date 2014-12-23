package main

import (
	"fmt"
	"errors"
)

//define error 
var shortWrite    = errors.New("short write")
type error interface {
	Error() string
}

// errorString is a trivial implementation of error.
type errorString struct {
	s string
}

func (e *errorString) Error() string {
	return e.s
}

// New returns an error that formats as the given text.
func New(text string) error {
	return &errorString{text}
}

// start define error check, so great really
func check()(int, error){
	s := 1
	fmt.Println("start")
	if s == 1 {
		return 0, errors.New("hahahahah")
	}
		return 0, nil
}
// return by define error
func check2()(int, error){
	s := 1
	fmt.Println("start")
	if s == 1 {
		return 0, shortWrite
	}
		return 0, nil
}


func main() {
     f, err :=check()
     if err!=nil{
	     fmt.Println(err)
	     fmt.Println(f)
     }
// another way to do 
	if f,err :=check2(); err !=nil{
	     fmt.Println(err)
	     fmt.Println(f)
	}else{
		fmt.Println("yes")
	}
}
