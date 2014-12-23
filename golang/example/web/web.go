package main

import (
	"encoding/json"
	"io"
	"io/ioutil"
	"log"
	"net/http"
	//"io/ioutil"
	"fmt"
	"time"
)

//test method handling
func HandleIndex(w http.ResponseWriter, r *http.Request) {
	if r.Method == "GET" {
		io.WriteString(w, "here is the GET\n")
	}

	if r.Method == "POST" {
		a := make(map[string]string)
		a["test"] = "haha"
		jsonString, err := json.Marshal(a)
		fmt.Println(jsonString)
		fmt.Println(err)
		//io.WriteString(w, jsonString)
	}

	if r.Method == "PUT" {
		io.WriteString(w, "here is the PUT\n")
	}
	if r.Method == "DELETE" {
		io.WriteString(w, "here is the DELETE\n")
	}
}

// from map to json and output json to client
func HandleJson(w http.ResponseWriter, r *http.Request) {
	a := make(map[string]string)
	a["test"] = "haha"
	a["bb"] = "bb"
	jsonString, _ := json.Marshal(a)
	io.WriteString(w, string(jsonString))
}

//recieve client from json to map
func HandleJsonInput(w http.ResponseWriter, r *http.Request) {
	var y map[string]interface{}
	body, _ := ioutil.ReadAll(r.Body)
	json.Unmarshal(body, &y)
	for key, val := range y {
		fmt.Println("the key the val:", key, val)
	}
	io.WriteString(w, "aaa")
}

// to return http Error
func HandleError(w http.ResponseWriter, r *http.Request) {
	if r.Method != "POST" {
		http.Error(w, "post only", http.StatusMethodNotAllowed)
	} else {
		io.WriteString(w, " got you")
	}

}

//test the multiple connection, ok it dosen't need any patch. 
func HandleTime(w http.ResponseWriter, r *http.Request) {
	fmt.Println("into time")
	time.Sleep(time.Second * 10)
}

//curl -X PUT -d "{\"test\": \"that\",\"test1\":\"test111111\"}" -H "haha":"SASA"  http://10.90.1.39:8000/header
//test header
func HandleHeader(w http.ResponseWriter, r *http.Request) {
	s := r.Header.Get("haha")
	if len(s)>0 {
		fmt.Println(s)
	} else {
		fmt.Println("filter it")
		http.Error(w, "header without haha", http.StatusMethodNotAllowed)
	}
}

func main() {
	http.HandleFunc("/", HandleIndex)
	http.HandleFunc("/json", HandleJson)
	http.HandleFunc("/jsoninput", HandleJsonInput)
	http.HandleFunc("/error", HandleError)
	http.HandleFunc("/time", HandleTime)
	http.HandleFunc("/header", HandleHeader)
	//http.ListenAndServe(":8000", nil)
	// for debuging
	log.Fatal(http.ListenAndServe(":8000", nil))

}
