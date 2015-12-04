package main
import (
	"fmt"
	"io"
	"net/http"
	"os"
 	"github.com/pborman/uuid"
        "github.com/justinas/alice"
	"github.com/julienschmidt/httprouter"
	"github.com/gorilla/context"
	"encoding/json"
//	"bufio"
	//"log"


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

func webDownloadHandler(w http.ResponseWriter, r *http.Request) {
	in, err := os.Open("./filerandom")
	if err != nil {
		fmt.Fprintf(w, "Unable to create the file for writing. Check your write access privilege")
		return
	}
	defer in.Close()
	//pr, pw := io.Pipe()
	//bufin := bufio.NewReader(in)

	// write the content from POST to the file
	//_, err = io.Copy(out, file)
	buf := make([]byte, 1024)
	for {
		n, _:=in.Read(buf)
		if n==0{
			break
		} 
		 if _, err := w.Write(buf[:n]); err != nil {
		    panic(err)
		 }
	
	}

	fmt.Println("File uploaded successfully : ")

}
func webDownloadHandler1(w http.ResponseWriter, r *http.Request) {
	uuid := uuid.New()
	fmt.Println(uuid)
	out, err := os.Open("./file")
	if err != nil {
		fmt.Fprintf(w, "Unable to create the file for writing. Check your write access privilege")
		return
	}
	defer out.Close()

	// write the content from POST to the file
	//_, err = io.Copy(out, file)
	fmt.Println("start to copy")
	buffer := make([]byte, 100)
	_, _ = out.Read(buffer)
	//io.Copy(out, buffer)
	w.Write(buffer)
	fmt.Println("File uploaded successfully : ")

}

func loggingHandler(next http.Handler) http.Handler {
  fn := func(w http.ResponseWriter, r *http.Request) {
    fmt.Println("into middle1")

    // put process here

    next.ServeHTTP(w, r)
  }

  return http.HandlerFunc(fn)
}
func recoverHandler(next http.Handler) http.Handler {
  fn := func(w http.ResponseWriter, r *http.Request) {
    fmt.Println("into middle recover")

    // put process here
    a:=1
    if a==1{
    // success operation and to next middleware
    next.ServeHTTP(w, r)
    }else{
     http.Error(w, http.StatusText(500), 500)
     }
  }
  // error oocured
  return http.HandlerFunc(fn)
}

func wrapHandler(h http.Handler) httprouter.Handle {
  return func(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
    context.Set(r, "params", ps)
    h.ServeHTTP(w, r)
  }
}


func getInfoHandler(w http.ResponseWriter, r *http.Request) {
	
	 w.Header().Set("Content-Type", "application/json")
                //a := make(map[string]string)
                a := map[string]interface{}{}
                a["test"] = "haha"
                jsonString, _ := json.Marshal(a)
	 //w.WriteHeader(200)
	 w.Write(jsonString)
}

func main() {
	commonHandlers := alice.New(loggingHandler, recoverHandler)
	//commonHandlers := alice.New(loggingHandler)
	//http.HandleFunc("/", webUploadHandler)
	//http.Handle("/", commonHandlers.ThenFunc(webUploadHandler))
	//http.ListenAndServe(":8080", nil)
	router := httprouter.New()
        router.POST("/upload", wrapHandler(commonHandlers.ThenFunc(webUploadHandler)))
        router.GET("/version", wrapHandler(commonHandlers.ThenFunc(getInfoHandler)))
        router.GET("/download", wrapHandler(commonHandlers.ThenFunc(webDownloadHandler)))
        http.ListenAndServe(":8080", router)


}
