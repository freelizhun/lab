package main
import ("fmt"
	"time"
	"math/rand"
	)


func webserver(num int, c chan int){
	//fmt.Println(num)
	var r int
	for {
	r = rand.Intn(10)
	time.Sleep(time.Second *time.Duration(r))
	c <- r
	c <- r+1
	}


}
func workerqueue(num int, c chan int){
	//fmt.Println(num)
	var a int
	for {
	a= <- c
	fmt.Println("worker",num,a)
	}

}

func main(){
	c := make(chan int)
	go webserver(1, c)
	go workerqueue(2, c)
	go workerqueue(3, c)
	var input string
	fmt.Scanln(&input)

}
