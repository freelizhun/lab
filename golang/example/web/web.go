package main

import (
	"encoding/json"
	"io"
	"io/ioutil"
	"log"
	"net/http"
	//"io/ioutil"
	"fmt"
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

func HandleError(w http.ResponseWriter, r *http.Request) {
	if r.Method != "POST" {
		http.Error(w, "post only", http.StatusMethodNotAllowed)
	}else{
	io.WriteString(w, " got you")
	}

}

func main() {
	http.HandleFunc("/", HandleIndex)
	http.HandleFunc("/json", HandleJson)
	http.HandleFunc("/jsoninput", HandleJsonInput)
	http.HandleFunc("/error", HandleError)
	log.Fatal(http.ListenAndServe(":8000", nil))

}
