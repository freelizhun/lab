
package main

import (
	"bufio"
//	"compress/gzip"
//	"fmt"
	"io"
//	"io/ioutil"
	"log"
	"net/http"
	"os"
)



//req, err := http.NewRequest("GET", "http://localhost:8080/", pr)
//client := &http.Client{}
//req, err := http.NewRequest("GET", "http://localhost:8080/", nil)
func main(){

in, err := os.Open("./filerandom")
//in, err := os.Open("./filerandom")
if err != nil {
	log.Fatal(err)
}
pr, pw := io.Pipe()
bufin := bufio.NewReader(in)
//gw := gzip.NewWriter(pw)
go func() {
		log.Printf("Start writing")
		//n, err := bufin.WriteTo(gw)
		n, err := bufin.WriteTo(pw)
		if err != nil {
			log.Fatal(err)
		}
//		gw.Close()
		pw.Close()
		log.Printf("Done writing: %d", n)
	}()




url := "http://localhost:8080/upload"
request, err := http.NewRequest("POST", url, pr)

//resp, err := http.DefaultClient.Do(req)
resp, err := http.DefaultClient.Do(request)

//response, err := (&http.Client{}).Do(request)

if err != nil {
	log.Fatal(err)
}
log.Println(resp)
}
