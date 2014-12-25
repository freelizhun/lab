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

func main() {

	client, err := rpc.Dial("tcp", "127.0.0.1:1234")
	if err != nil {
		log.Fatal("dialing:", err)
	}
	// Synchronous call
	args := &Args{7, 8}
	var reply int
	err = client.Call("Calculator.Add", args, &reply)
	fmt.Println("wait for return, it's sync")
	if err != nil {
		log.Fatal("arith error:", err)
	}
	fmt.Printf("Result: %d+%d=%d", args.X, args.Y, reply)
}
