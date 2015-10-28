package main
 
import (
    "github.com/coreos/go-etcd/etcd"
    "log"
)
 
func main() {
    log.Printf("Start to Connect to ")
    client := etcd.NewClient([]string{"http://172.16.235.128:4001"})
    resp, err := client.Get("creds", false, false)
    if err != nil {
        log.Fatal(err)
    }
    log.Printf("Current creds: %s: %s\n", resp.Node.Key, resp.Node.Value)
    receiver := make(chan *etcd.Response)
    go client.Watch("/creds", 0, false, receiver, nil)
    r := <-receiver
    log.Printf("Got updated creds: %s: %s\n", r.Node.Key, r.Node.Value)
}

