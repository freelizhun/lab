package main
import ("fmt"
	"time"
	)



func testrun(num int){
	for {
	time.Sleep(time.Second*10)
	fmt.Println("haha", num)
	}
}

func main(){
	go testrun(1)
	go testrun(2)
	var input string
	fmt.Scanln(&input)

}
