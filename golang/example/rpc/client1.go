package main

import (
	"fmt"
	"net/rpc"
	"log"
)

func main(){
serverAddress:="127.0.0.1"
client, err := rpc.DialHTTP("tcp", serverAddress + ":1234")
if err != nil {
		log.Fatal("dialing:", err)
	}

	// Synchronous call
	args := &server.Args{7,8}
	var reply int
	err = client.Call("Arith.Multiply", args, &reply)
	if err != nil {
			log.Fatal("arith error:", err)
		}
		fmt.Printf("Arith: %d*%d=%d", args.A, args.B, reply)
	}
