package main
import (
	"fmt"
	"io"
	"net/http"
	"os"
 	"github.com/pborman/uuid"

)

//curl -v -X POST -N --data-binary @"./haproxy.cfg" http://localhost:8080/webUploadHandler
func webUploadHandler(w http.ResponseWriter, r *http.Request) {

	// write the content from POST to the file
	//_, err = io.Copy(out, file)
	fmt.Println("start to copy")
	//io.Copy(out, r.Body)
	for i := 0; i < 10; i++ {
	uuid := uuid.New()
	fmt.Println(uuid)
	out, _ := os.Create(uuid+".txt")
	defer out.Close()
	io.CopyN(out, r.Body, 1000)
	}
	fmt.Println("File uploaded successfully : ")

}
func main() {
	http.HandleFunc("/", webUploadHandler)
	http.ListenAndServe(":8080", nil)
}
