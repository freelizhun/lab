package main
import "fmt"



type testInter interface{
	showdata()
	left()
}
type book struct{
	pages int 
	cover string
}
type reader struct{
	pages int
	cover string
}
func (b book)showdata(){
	fmt.Println("show book",b.pages, b.cover)
	//b.left()
}
func (b book)left(){
	fmt.Println("book finished")
}
func (r reader)showdata(){
	fmt.Println("show reader",r.pages, r.cover)
	//r.left()
}
func (r reader)left(){
	fmt.Println("reader finished")
}

func testprint(){
	fmt.Println("haha")
}
func testrun(t testInter){
	t.showdata()
	t.left()
}

func main(){
	bb:=book{pages:100, cover:"green"}
	testrun(bb)
	rr:=book{pages:10, cover:"red"}
	testrun(rr)
	t:=testInter()
	t.showdata()

}
