import (
    "fmt"
    "os"
    "os/user"
    "runtime"
)

{
    user, _ := user.Current()
    fmt.Printf("Go: %s (%s_%s)\n", runtime.Version(), runtime.GOOS, runtime.GOARCH)
    fmt.Printf("User: %s\n", user.Username)
    wd, _ := os.Getwd()
    fmt.Printf("Working dir: %s\n", wd)
    fmt.Printf("NumCPU: %d\n", runtime.NumCPU())
}

// naiveFib calculates the n-th fibonacci number
func naiveFib(n int) int {
    if n > 1 {
        return naiveFib(n - 1) + naiveFib(n - 2)
    }
    return 1
}

naiveFib(20)

import "fmt"

n := 10

if n > 0 {
    fmt.Println("n is positive:", n)
} else {
    fmt.Println("n is not positive:", n)
}

sum := 0
for i := 1; i <= n; i++ {
    sum += i
}
sum

switch sum {
case 55:
    fmt.Println("OK")
default:
    fmt.Println("Fail")
}

import (
    "fmt"
    "math"
)

fmt.Printf("sin(pi/3) == %f\n", math.Sin(math.Pi/3))
fmt.Printf("cos(pi/3) == %f\n", math.Cos(math.Pi/3))
fmt.Printf("sqrt(3)/2 == %f\n", math.Sqrt(3)/2)
fmt.Printf("log(e^2) == %f\n", math.Log(math.E * math.E))

import (
    "math/rand"
    "time"
)

rand.Seed(time.Now().UnixNano())
r := rand.Int()
r

r % 10000

start := time.Now()
start

end := time.Now()
end

fmt.Printf("end - start = %v", end.Sub(start))

type person struct {
    name string
    age int
}

func (p *person) Hello() string {
    return fmt.Sprintf("Hello! Name: %s, Age: %d", p.name, p.age)
}

p := person{"Alice", 12}
fmt.Printf("p.name = %q\n", p.name)
fmt.Printf("p.Hello() == %q\n", p.Hello())

type hello interface {
    Hello() string
}

func printHello(h hello) {
    if _, ok := h.(*person); ok {
        fmt.Println("h is *person")
    }
    fmt.Printf("h.Hello() == %q\n", h.Hello())
}

p := person{"Alice", 12}
printHello(&p)

// You can pass a type defined in lgo as an interface defined in Go.

import (
    "bytes"
    "fmt"
    "io"
)

type myReader struct {
    content string
    idx int
}

func (r *myReader) Read(p []byte) (n int, err error) {
    if len(p) == 0 {
        return 0, nil
    }
    if r.idx >= len(r.content) {
        return 0, io.EOF
    }
    p[0] = r.content[r.idx]
    fmt.Printf("Read %q\n", r.content[r.idx])
    r.idx++
    return 1, nil
}

{
    r := myReader{content: "Hello!"}
    var buf bytes.Buffer
    io.Copy(&buf, &r)
    fmt.Printf("buf == %q\n", buf.String())
}

// You can pass a struct defined in Go as an interface defined in lgo too.

import (
    "bytes"
    "fmt"
)

type withLen interface {
    Len() int
}

func printLen(l withLen) {
    fmt.Printf("Len(%v) == %d\n", l, l.Len())
}

{
    var buf bytes.Buffer
    buf.WriteString("01234")
    printLen(&buf)
    buf.WriteString("56789")
    printLen(&buf)
}

// return
if true {
    fmt.Println("return!")
    return
}
fmt.Println("continue!")

fmt.Println("start")
defer fmt.Println("defer (1)")
defer fmt.Println("defer (2)")
fmt.Println("end")

import "fmt"

{
    done := make(chan struct{})
    ch := make(chan int)
    // producer
    go func(){
        for i := 0; i < 10; i++ {
            ch <- i * i
        }
        close(ch)
    }()
    // consumer
    go func() {
        for i := range ch {
            fmt.Printf("i == %d\n", i)
        }
        close(done)
    }()
    <-done
}

panic("failed!")

go func() {
    panic("goroutine failed")
}()

import (
    "reflect"
)

type person struct {
    Name string
    Age int
    secret string
}

func (p *person) GetSecret() string {
    return p.secret
}

p := &person{Name:"Alice", Age: 12, secret: "1234"}

{
    t := reflect.TypeOf(p)
    fmt.Println("--- fields ---")
    for i := 0; i < t.Elem().NumField(); i++ {
        fmt.Printf("field[%d] = %s\n", i, t.Elem().Field(i).Name)
    }
    
    fmt.Println("--- methods ---")
    for i := 0; i < t.NumMethod(); i++ {
        fmt.Printf("method[%d] = %s\n", i, t.Method(i).Name)
    }

    // Set "Age" via reflect.
    v := reflect.ValueOf(p)
    v.Elem().Field(1).Set(reflect.ValueOf(34))
    
    fmt.Println("------------")
    fmt.Printf("p == %#v\n", p)
}

// Display HTML
_ctx.Display.HTML(
    `Hello <b>lgo</b>: <a target="_blank" href="https://github.com/yunabe/lgo" >GitHub lgo</a>
<div style="width:50px;height:50px;background-color:red"></div>`,
    nil)

import (
    "fmt"
    "io/ioutil"
    "net/http"    
)

var gopherPNG []byte
{
    res, err := http.Get("https://golang.org/doc/gopher/frontpage.png")
    if err != nil {
        fmt.Printf("Failed to get: %v\n", err)
        return
    }
    defer res.Body.Close()
    gopherPNG, err = ioutil.ReadAll(res.Body)
    if err != nil {
        fmt.Printf("Failed to read: %v\n", err)
        return
    }
    _ctx.Display.Text("PNG Gopher", nil)
    _ctx.Display.PNG(gopherPNG, nil)
}

import (
    "bytes"
    "image"
    jpeg "image/jpeg"
    _ "image/png"
    "os"
    
    "github.com/nfnt/resize"
)

{
    img, _, err := image.Decode(bytes.NewBuffer(gopherPNG))
    if err != nil {
        fmt.Fprintf(os.Stderr, "Failed to decode: %v", err)
        return
    }
    img = resize.Resize(100, 0, img, resize.Lanczos3)
    var buf bytes.Buffer
    jpeg.Encode(&buf, img, &jpeg.Options{Quality: 1})
    _ctx.Display.Text("Resized and highly compressed JPEG", nil)
    _ctx.Display.JPEG(buf.Bytes(), nil)
}

import (
    "bytes"
    "fmt"
    "image"
    png "image/png"
    jpeg "image/jpeg"
    "os"
    "time"
    
    "github.com/nfnt/resize"
)

{
    img, err := png.Decode(bytes.NewBuffer(gopherPNG))
    if err != nil {
        fmt.Fprintf(os.Stderr, "Failed to decode:", err)
        return
    }
    img = resize.Resize(100, 0, img, resize.Lanczos3)
    var labelID, imgID string
    for quality := 25; quality > 0; quality -= 1 {
        var buf bytes.Buffer
        jpeg.Encode(&buf, img, &jpeg.Options{Quality: quality})
        size := float32(len(buf.Bytes()))/1000
        _ctx.Display.Text(fmt.Sprintf("Quality: %d\nSize: %.2fkB", quality, size), &labelID)
        _ctx.Display.JPEG(buf.Bytes(), &imgID)
        time.Sleep(200*time.Millisecond)
    }
}

{
    x := 10 + 3.4 +
}
{
    for i := 0 {}
}

{  // L.1
    a := undefined
    
    x := 10
    y := 3.4  // L.5
    z := x + y

    unused := 10
    
    for i := 0; i; i++ {}  // L.10
    
    _, _ = a, z
}





