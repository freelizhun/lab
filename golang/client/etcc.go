package main

import (
    "log"
    "time"

    "github.com/coreos/etcd/Godeps/_workspace/src/golang.org/x/net/context"
    "github.com/coreos/etcd/client"
)

func main() {
    cfg := client.Config{
        Endpoints:               []string{"http://172.16.235.128:4001"},
        Transport:               client.DefaultTransport,
        // set timeout per request to fail fast when the target endpoint is unavailable
        HeaderTimeoutPerRequest: time.Second,
    }
    c, err := client.New(cfg)
    if err != nil {
        log.Fatal(err)
    }
    kapi := client.NewKeysAPI(c)
    // set "/woo" key with "bar" value
    log.Print("Setting '/woo' key with 'bar' value")
    resp, err := kapi.Set(context.Background(), "/woo", "bar", nil)
    if err != nil {
        log.Fatal(err)
    } else {
        // print common key info
        log.Printf("Set is done. Metadata is %q\n", resp)
    }
    // get "/woo" key's value
    log.Print("Getting '/woo' key value")
    resp, err = kapi.Get(context.Background(), "/woo", nil)
    if err != nil {
        log.Fatal(err)
    } else {
        // print common key info
        log.Printf("Get is done. Metadata is %q\n", resp)
        // print value
        log.Printf("%q key has %q value\n", resp.Node.Key, resp.Node.Value)
    }
}

