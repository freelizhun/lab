package main
import (
	"log"
	"time"
	"github.com/coreos/etcd/client"
	"golang.org/x/net/context"
)



func main() {

	cfg := client.Config{
		Endpoints: []string{"http://172.16.235.128:4001"},
		Transport: client.DefaultTransport,
	}

	c, err := client.New(cfg)
	if err != nil {
		// handle error
	}


	kAPI := client.NewKeysAPI(c)

	// create a new key /foo with the value "bar"
	_, err = kAPI.Create(context.Background(), "/foo", "bar")
	if err != nil {
		// handle error
	}

	// delete the newly created key only if the value is still "bar"
	_, err = kAPI.Delete(context.Background(), "/foo", &client.DeleteOptions{PrevValue: "bar"})
	if err != nil {
		// handle error
	}


	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	log.Printf("set uyp withtimeout \n")
	// set a new key, ignoring it's previous state
	//_, err = kAPI.Set(ctx, "/pings", "pong", &client.SetOptions{TTL: "5"})
	opts := client.SetOptions{TTL: time.Second*5}
	_, err = kAPI.Set(ctx, "/pingss", "pong", &opts)
	if err != nil {
		if err == context.DeadlineExceeded {
			log.Printf("Set is done. Metadata is \n")
			// request took longer than 5s
		} else {
			// handle error
			log.Printf("Set is done. Metadata is \n")
		}
	}
}
