
package main

import (
//	"bufio"
//	"compress/gzip"
//	"io"
//	"io/ioutil"
	"log"
	"net/http"
 //       "encoding/json"
	"io"
	"os"
//	"os"
)



//req, err := http.NewRequest("GET", "http://localhost:8080/", pr)
//client := &http.Client{}
//req, err := http.NewRequest("GET", "http://localhost:8080/", nil)
func main(){




url := "http://localhost:8080/download"
request, err := http.NewRequest("GET", url, nil)

//resp, err := http.DefaultClient.Do(req)
resp, err := http.DefaultClient.Do(request)

//response, err := (&http.Client{}).Do(request)

if err != nil {
	log.Fatal(err)
}

out, err := os.Create("./tmp.txt")
defer out.Close()

io.Copy(out, resp.Body)

log.Println("File uploaded successfully : ")

}
