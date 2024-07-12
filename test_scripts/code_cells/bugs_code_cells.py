type Data struct {
    value string
}

func (d Data) Value() string {
    return d.value
}

type WithValue interface {
    Value() string
}

d := Data{"hello"}

// Got a link error because of https://github.com/golang/go/issues/22998
d.Value()

// This works without any problem.
WithValue(d).Value()

import (
    "fmt"
    "time"
)

go func() {
    panic("die!")
}()

time.Sleep(10 * time.Millisecond)
fmt.Println("main done")

import (
    "fmt"
)

type Hello interface {
    SayHello()
}

type person struct {
    name string
}

func (p *person) SayHello() {
    fmt.Printf("Hello, I'm %s.\n", p.name)
}

p := person{"yunabe"}
fmt.Println("---- 1 ----")
p.SayHello()

var h Hello = &p
fmt.Println("---- 2 ----")
h.SayHello()

import (
    "fmt"
    "log"
    "runtime"
    "runtime/debug"
)

type MyData struct {
    b []byte
}

func (m *MyData) Size() int {
    return len(m.b)
}

func NewMyData() *MyData {
    return &MyData{
        b: make([]byte, 10 * (1 << 20)),
    }
}

var l []*MyData
for i := 0; i < 100; i++ {
    d := NewMyData()
    l = append(l, d)
}
l = nil
debug.FreeOSMemory()
runtime.GC()

import (
    "fmt"
)

for i := 0; i < 3; i++ {
    go func(id int) {
        fmt.Println("goroutine:", id)
    }(i)
}



