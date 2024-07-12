import (
    "fmt"
)

var sum, i int64
defer func() {
    fmt.Printf("i = %d, sum = %d, i*(i-1)/2 = %d\n", i, sum, i*(i-1)/2)
}()
for i = int64(0);; i++ {
    sum += i
}

import (
    "fmt"
    "time"
)

leaf := 0

func naiveFib(n int64) int64 {
    if n < 2 {
        leaf++
        return 1
    }
    return naiveFib(n-1) + naiveFib(n-2)
}

start := time.Now()
defer func(){
    end := time.Now()
    fmt.Printf("time: %v\n", end.Sub(start))
    fmt.Printf("leaf counter: %d\n", leaf)
    fmt.Printf("avg: %v/cycle\n", end.Sub(start)/time.Duration(leaf))
}()
naiveFib(50)

{
    c := make(chan int)
    // Block forever because no one reads c.
    c <- 10
}

{
    c := make(chan int)
    // Block forever because no one sends an int to c.
    <-c
}

{
    c0, c1 := make(chan int), make(chan int)
    // Block forever because no one read or write c0 and c1.
    select {
    case c0 <- 10:
        fmt.Println("Sent an int to c0")
    case i := <-c1:
        fmt.Println("Received", i)
    }
}

import (
    "fmt"
)

go func() {
    var i int64
    defer func() {
        fmt.Printf("i = %d (in goroutine)\n", i)
    }()
    for i = 0 ;; i++ {}
}()

// This demo demostrates how to use net/http with cancellation in lgo.
import (
    "fmt"
    "io/ioutil"
    "net/http"
)

{
    waitSec := 10
    var err error
    defer func() {
        if err != nil {
            fmt.Printf("Failed: %v", err)
        }
    }()
    url := fmt.Sprintf("https://yunabe-codelab.appspot.com/slow?sec=%d", waitSec)
    req, err := http.NewRequest("GET", url, nil)
    if err != nil {
        return
    }
    res, err := http.DefaultClient.Do(req.WithContext(_ctx))
    if err != nil {
        return
    }
    b, err := ioutil.ReadAll(res.Body)
    if err != nil {
        return
    }
    fmt.Printf("Got: %q", b)
}

