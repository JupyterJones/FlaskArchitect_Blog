import (
    "fmt"
    "strings"
    "time"
)

interval := 64
start := time.Now()
var sum int64
var msgs []string

{
    n := 1
    sum += int64(n)
    if n % interval == 0 {
        end := time.Now()
        msgs = append(
            msgs,
            fmt.Sprintf("cycle: [%d, %d], took %v on average", n - interval + 1, n, end.Sub(start)/time.Duration(interval)))
        start = end
    }
}

{
    n := 2
    sum += int64(n)
    if n % interval == 0 {
        end := time.Now()
        msgs = append(
            msgs,
            fmt.Sprintf("cycle: [%d, %d], took %v on average", n - interval + 1, n, end.Sub(start)/time.Duration(interval)))
        start = end
    }
}

{
    n := 1023
    sum += int64(n)
    if n % interval == 0 {
        end := time.Now()
        msgs = append(
            msgs,
            fmt.Sprintf("cycle: [%d, %d], took %v on average", n - interval + 1, n, end.Sub(start)/time.Duration(interval)))
        start = end
    }
}

{
    n := 1024
    sum += int64(n)
    if n % interval == 0 {
        end := time.Now()
        msgs = append(
            msgs,
            fmt.Sprintf("cycle: [%d, %d], took %v on average", n - interval + 1, n, end.Sub(start)/time.Duration(interval)))
        start = end
    }
}

sum

fmt.Println(strings.Join(msgs, "\n"))

