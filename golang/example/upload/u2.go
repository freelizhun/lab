package main
import (
	"fmt"
	"io"
	"net/http"
	"os"
)

//curl -v -X POST -N --data-binary @"./haproxy.cfg" http://localhost:8080/webUploadHandler
func webUploadHandler(w http.ResponseWriter, r *http.Request) {
	out, err := os.Create("haha.txt")
	if err != nil {
		fmt.Fprintf(w, "Unable to create the file for writing. Check your write access privilege")
		return
	}
	defer out.Close()

	// write the content from POST to the file
	//_, err = io.Copy(out, file)
	fmt.Println("start to copy")
	io.Copy(out, r.Body)
	//io.CopyN(out, r.Body,1000)
	fmt.Println("File uploaded successfully : ")

}
func main() {
	http.HandleFunc("/", webUploadHandler)
	http.ListenAndServe(":8080", nil)
}
