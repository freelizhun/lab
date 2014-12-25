// client.go
package main

import (
	"fmt"
	"log"
	"net/rpc"
)

type Args struct {
	X, Y int
}
type Quotient struct {
			Quo, Rem int
				}

func connect(){
	client, err := rpc.Dial("tcp", "127.0.0.1:1234")
	if err != nil {
		log.Fatal("dialing:", err)
	}
	// Synchronous call
	args := &Args{7, 8}
	//quotient := new(Quotient)
	var reply int
	//divCall := client.Go("Calculator.Add", args, &quotient, nil)
	divCall := client.Go("Calculator.Add", args, &reply, nil)
	fmt.Println("wait for response, it's async")
	replyCall := <-divCall.Done	// will be equal to divCall
	fmt.Println(replyCall)
	fmt.Println(reply)

}


func main() {
	go connect()
	go connect()
	var input string
	fmt.Scanln(&input)
}
