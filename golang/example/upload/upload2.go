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
	uuid := uuid.New()
	fmt.Println(uuid)
	out, err := os.Create(uuid+".txt")
	if err != nil {
		fmt.Fprintf(w, "Unable to create the file for writing. Check your write access privilege")
		return
	}
	defer out.Close()

	// write the content from POST to the file
	//_, err = io.Copy(out, file)
	fmt.Println("start to copy")
	io.Copy(out, r.Body)
	fmt.Println("File uploaded successfully : ")

}
func main() {
	http.HandleFunc("/", webUploadHandler)
	http.ListenAndServe(":8080", nil)
}
