// Copyright 2012 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// +build !plan9,!solaris

//package fsnotify_test
package main

import (
	"log"

	"golang.org/x/exp/inotify"
)

func ExampleNewWatcher() {
	watcher, err := inotify.NewWatcher()
	if err != nil {
		log.Fatal(err)
	}
	defer watcher.Close()

	done := make(chan bool)
	go func() {
		for {
			select {
			case ev := <-watcher.Event:
				//log.Println("event:", ev.Name)
				log.Println("event:", ev.Name, ev.Mask, ev.Cookie)
				log.Println("event:", ev)

			case err := <-watcher.Error:
				log.Println("error:", err)
			}
		}
	}()

	//err = watcher.Add("./testDir")
	//watcher.Watch("/testDir")
	watcher.AddWatch("./testDir", inotify.IN_CLOSE_WRITE)
	if err != nil {
		log.Fatal(err)
	}
	<-done
}

func main() {
	ExampleNewWatcher()
}
