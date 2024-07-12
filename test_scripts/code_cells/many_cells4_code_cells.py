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
    n := 3
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
    n := 4
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
    n := 5
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
    n := 6
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
    n := 7
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
    n := 8
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
    n := 9
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
    n := 10
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
    n := 11
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
    n := 12
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
    n := 13
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
    n := 14
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
    n := 15
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
    n := 16
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
    n := 17
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
    n := 18
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
    n := 19
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
    n := 20
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
    n := 21
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
    n := 22
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
    n := 23
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
    n := 24
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
    n := 25
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
    n := 26
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
    n := 27
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
    n := 28
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
    n := 29
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
    n := 30
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
    n := 31
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
    n := 32
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
    n := 33
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
    n := 34
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
    n := 35
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
    n := 36
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
    n := 37
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
    n := 38
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
    n := 39
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
    n := 40
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
    n := 41
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
    n := 42
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
    n := 43
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
    n := 44
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
    n := 45
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
    n := 46
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
    n := 47
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
    n := 48
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
    n := 49
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
    n := 50
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
    n := 51
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
    n := 52
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
    n := 53
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
    n := 54
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
    n := 55
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
    n := 56
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
    n := 57
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
    n := 58
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
    n := 59
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
    n := 60
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
    n := 61
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
    n := 62
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
    n := 63
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
    n := 64
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
    n := 65
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
    n := 66
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
    n := 67
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
    n := 68
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
    n := 69
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
    n := 70
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
    n := 71
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
    n := 72
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
    n := 73
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
    n := 74
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
    n := 75
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
    n := 76
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
    n := 77
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
    n := 78
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
    n := 79
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
    n := 80
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
    n := 81
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
    n := 82
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
    n := 83
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
    n := 84
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
    n := 85
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
    n := 86
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
    n := 87
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
    n := 88
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
    n := 89
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
    n := 90
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
    n := 91
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
    n := 92
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
    n := 93
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
    n := 94
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
    n := 95
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
    n := 96
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
    n := 97
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
    n := 98
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
    n := 99
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
    n := 100
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
    n := 101
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
    n := 102
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
    n := 103
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
    n := 104
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
    n := 105
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
    n := 106
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
    n := 107
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
    n := 108
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
    n := 109
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
    n := 110
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
    n := 111
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
    n := 112
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
    n := 113
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
    n := 114
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
    n := 115
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
    n := 116
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
    n := 117
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
    n := 118
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
    n := 119
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
    n := 120
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
    n := 121
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
    n := 122
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
    n := 123
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
    n := 124
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
    n := 125
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
    n := 126
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
    n := 127
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
    n := 128
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
    n := 129
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
    n := 130
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
    n := 131
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
    n := 132
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
    n := 133
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
    n := 134
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
    n := 135
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
    n := 136
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
    n := 137
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
    n := 138
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
    n := 139
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
    n := 140
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
    n := 141
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
    n := 142
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
    n := 143
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
    n := 144
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
    n := 145
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
    n := 146
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
    n := 147
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
    n := 148
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
    n := 149
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
    n := 150
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
    n := 151
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
    n := 152
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
    n := 153
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
    n := 154
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
    n := 155
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
    n := 156
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
    n := 157
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
    n := 158
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
    n := 159
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
    n := 160
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
    n := 161
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
    n := 162
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
    n := 163
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
    n := 164
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
    n := 165
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
    n := 166
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
    n := 167
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
    n := 168
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
    n := 169
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
    n := 170
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
    n := 171
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
    n := 172
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
    n := 173
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
    n := 174
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
    n := 175
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
    n := 176
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
    n := 177
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
    n := 178
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
    n := 179
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
    n := 180
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
    n := 181
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
    n := 182
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
    n := 183
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
    n := 184
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
    n := 185
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
    n := 186
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
    n := 187
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
    n := 188
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
    n := 189
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
    n := 190
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
    n := 191
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
    n := 192
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
    n := 193
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
    n := 194
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
    n := 195
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
    n := 196
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
    n := 197
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
    n := 198
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
    n := 199
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
    n := 200
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
    n := 201
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
    n := 202
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
    n := 203
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
    n := 204
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
    n := 205
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
    n := 206
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
    n := 207
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
    n := 208
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
    n := 209
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
    n := 210
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
    n := 211
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
    n := 212
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
    n := 213
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
    n := 214
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
    n := 215
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
    n := 216
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
    n := 217
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
    n := 218
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
    n := 219
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
    n := 220
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
    n := 221
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
    n := 222
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
    n := 223
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
    n := 224
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
    n := 225
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
    n := 226
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
    n := 227
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
    n := 228
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
    n := 229
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
    n := 230
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
    n := 231
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
    n := 232
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
    n := 233
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
    n := 234
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
    n := 235
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
    n := 236
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
    n := 237
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
    n := 238
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
    n := 239
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
    n := 240
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
    n := 241
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
    n := 242
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
    n := 243
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
    n := 244
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
    n := 245
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
    n := 246
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
    n := 247
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
    n := 248
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
    n := 249
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
    n := 250
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
    n := 251
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
    n := 252
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
    n := 253
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
    n := 254
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
    n := 255
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
    n := 256
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
    n := 257
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
    n := 258
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
    n := 259
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
    n := 260
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
    n := 261
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
    n := 262
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
    n := 263
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
    n := 264
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
    n := 265
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
    n := 266
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
    n := 267
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
    n := 268
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
    n := 269
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
    n := 270
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
    n := 271
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
    n := 272
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
    n := 273
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
    n := 274
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
    n := 275
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
    n := 276
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
    n := 277
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
    n := 278
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
    n := 279
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
    n := 280
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
    n := 281
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
    n := 282
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
    n := 283
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
    n := 284
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
    n := 285
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
    n := 286
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
    n := 287
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
    n := 288
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
    n := 289
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
    n := 290
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
    n := 291
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
    n := 292
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
    n := 293
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
    n := 294
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
    n := 295
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
    n := 296
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
    n := 297
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
    n := 298
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
    n := 299
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
    n := 300
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
    n := 301
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
    n := 302
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
    n := 303
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
    n := 304
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
    n := 305
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
    n := 306
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
    n := 307
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
    n := 308
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
    n := 309
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
    n := 310
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
    n := 311
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
    n := 312
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
    n := 313
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
    n := 314
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
    n := 315
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
    n := 316
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
    n := 317
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
    n := 318
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
    n := 319
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
    n := 320
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
    n := 321
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
    n := 322
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
    n := 323
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
    n := 324
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
    n := 325
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
    n := 326
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
    n := 327
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
    n := 328
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
    n := 329
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
    n := 330
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
    n := 331
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
    n := 332
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
    n := 333
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
    n := 334
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
    n := 335
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
    n := 336
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
    n := 337
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
    n := 338
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
    n := 339
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
    n := 340
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
    n := 341
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
    n := 342
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
    n := 343
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
    n := 344
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
    n := 345
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
    n := 346
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
    n := 347
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
    n := 348
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
    n := 349
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
    n := 350
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
    n := 351
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
    n := 352
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
    n := 353
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
    n := 354
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
    n := 355
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
    n := 356
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
    n := 357
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
    n := 358
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
    n := 359
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
    n := 360
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
    n := 361
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
    n := 362
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
    n := 363
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
    n := 364
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
    n := 365
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
    n := 366
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
    n := 367
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
    n := 368
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
    n := 369
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
    n := 370
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
    n := 371
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
    n := 372
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
    n := 373
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
    n := 374
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
    n := 375
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
    n := 376
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
    n := 377
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
    n := 378
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
    n := 379
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
    n := 380
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
    n := 381
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
    n := 382
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
    n := 383
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
    n := 384
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
    n := 385
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
    n := 386
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
    n := 387
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
    n := 388
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
    n := 389
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
    n := 390
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
    n := 391
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
    n := 392
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
    n := 393
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
    n := 394
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
    n := 395
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
    n := 396
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
    n := 397
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
    n := 398
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
    n := 399
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
    n := 400
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
    n := 401
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
    n := 402
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
    n := 403
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
    n := 404
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
    n := 405
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
    n := 406
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
    n := 407
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
    n := 408
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
    n := 409
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
    n := 410
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
    n := 411
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
    n := 412
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
    n := 413
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
    n := 414
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
    n := 415
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
    n := 416
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
    n := 417
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
    n := 418
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
    n := 419
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
    n := 420
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
    n := 421
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
    n := 422
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
    n := 423
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
    n := 424
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
    n := 425
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
    n := 426
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
    n := 427
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
    n := 428
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
    n := 429
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
    n := 430
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
    n := 431
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
    n := 432
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
    n := 433
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
    n := 434
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
    n := 435
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
    n := 436
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
    n := 437
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
    n := 438
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
    n := 439
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
    n := 440
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
    n := 441
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
    n := 442
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
    n := 443
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
    n := 444
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
    n := 445
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
    n := 446
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
    n := 447
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
    n := 448
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
    n := 449
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
    n := 450
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
    n := 451
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
    n := 452
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
    n := 453
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
    n := 454
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
    n := 455
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
    n := 456
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
    n := 457
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
    n := 458
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
    n := 459
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
    n := 460
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
    n := 461
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
    n := 462
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
    n := 463
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
    n := 464
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
    n := 465
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
    n := 466
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
    n := 467
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
    n := 468
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
    n := 469
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
    n := 470
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
    n := 471
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
    n := 472
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
    n := 473
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
    n := 474
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
    n := 475
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
    n := 476
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
    n := 477
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
    n := 478
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
    n := 479
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
    n := 480
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
    n := 481
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
    n := 482
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
    n := 483
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
    n := 484
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
    n := 485
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
    n := 486
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
    n := 487
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
    n := 488
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
    n := 489
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
    n := 490
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
    n := 491
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
    n := 492
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
    n := 493
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
    n := 494
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
    n := 495
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
    n := 496
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
    n := 497
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
    n := 498
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
    n := 499
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
    n := 500
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
    n := 501
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
    n := 502
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
    n := 503
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
    n := 504
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
    n := 505
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
    n := 506
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
    n := 507
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
    n := 508
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
    n := 509
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
    n := 510
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
    n := 511
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
    n := 512
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
    n := 513
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
    n := 514
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
    n := 515
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
    n := 516
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
    n := 517
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
    n := 518
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
    n := 519
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
    n := 520
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
    n := 521
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
    n := 522
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
    n := 523
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
    n := 524
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
    n := 525
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
    n := 526
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
    n := 527
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
    n := 528
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
    n := 529
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
    n := 530
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
    n := 531
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
    n := 532
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
    n := 533
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
    n := 534
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
    n := 535
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
    n := 536
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
    n := 537
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
    n := 538
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
    n := 539
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
    n := 540
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
    n := 541
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
    n := 542
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
    n := 543
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
    n := 544
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
    n := 545
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
    n := 546
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
    n := 547
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
    n := 548
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
    n := 549
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
    n := 550
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
    n := 551
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
    n := 552
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
    n := 553
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
    n := 554
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
    n := 555
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
    n := 556
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
    n := 557
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
    n := 558
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
    n := 559
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
    n := 560
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
    n := 561
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
    n := 562
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
    n := 563
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
    n := 564
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
    n := 565
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
    n := 566
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
    n := 567
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
    n := 568
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
    n := 569
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
    n := 570
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
    n := 571
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
    n := 572
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
    n := 573
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
    n := 574
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
    n := 575
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
    n := 576
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
    n := 577
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
    n := 578
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
    n := 579
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
    n := 580
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
    n := 581
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
    n := 582
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
    n := 583
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
    n := 584
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
    n := 585
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
    n := 586
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
    n := 587
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
    n := 588
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
    n := 589
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
    n := 590
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
    n := 591
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
    n := 592
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
    n := 593
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
    n := 594
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
    n := 595
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
    n := 596
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
    n := 597
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
    n := 598
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
    n := 599
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
    n := 600
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
    n := 601
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
    n := 602
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
    n := 603
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
    n := 604
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
    n := 605
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
    n := 606
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
    n := 607
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
    n := 608
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
    n := 609
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
    n := 610
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
    n := 611
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
    n := 612
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
    n := 613
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
    n := 614
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
    n := 615
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
    n := 616
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
    n := 617
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
    n := 618
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
    n := 619
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
    n := 620
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
    n := 621
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
    n := 622
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
    n := 623
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
    n := 624
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
    n := 625
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
    n := 626
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
    n := 627
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
    n := 628
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
    n := 629
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
    n := 630
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
    n := 631
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
    n := 632
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
    n := 633
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
    n := 634
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
    n := 635
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
    n := 636
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
    n := 637
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
    n := 638
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
    n := 639
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
    n := 640
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
    n := 641
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
    n := 642
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
    n := 643
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
    n := 644
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
    n := 645
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
    n := 646
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
    n := 647
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
    n := 648
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
    n := 649
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
    n := 650
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
    n := 651
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
    n := 652
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
    n := 653
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
    n := 654
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
    n := 655
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
    n := 656
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
    n := 657
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
    n := 658
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
    n := 659
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
    n := 660
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
    n := 661
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
    n := 662
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
    n := 663
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
    n := 664
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
    n := 665
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
    n := 666
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
    n := 667
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
    n := 668
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
    n := 669
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
    n := 670
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
    n := 671
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
    n := 672
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
    n := 673
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
    n := 674
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
    n := 675
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
    n := 676
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
    n := 677
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
    n := 678
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
    n := 679
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
    n := 680
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
    n := 681
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
    n := 682
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
    n := 683
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
    n := 684
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
    n := 685
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
    n := 686
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
    n := 687
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
    n := 688
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
    n := 689
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
    n := 690
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
    n := 691
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
    n := 692
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
    n := 693
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
    n := 694
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
    n := 695
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
    n := 696
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
    n := 697
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
    n := 698
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
    n := 699
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
    n := 700
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
    n := 701
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
    n := 702
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
    n := 703
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
    n := 704
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
    n := 705
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
    n := 706
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
    n := 707
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
    n := 708
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
    n := 709
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
    n := 710
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
    n := 711
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
    n := 712
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
    n := 713
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
    n := 714
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
    n := 715
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
    n := 716
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
    n := 717
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
    n := 718
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
    n := 719
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
    n := 720
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
    n := 721
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
    n := 722
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
    n := 723
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
    n := 724
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
    n := 725
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
    n := 726
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
    n := 727
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
    n := 728
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
    n := 729
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
    n := 730
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
    n := 731
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
    n := 732
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
    n := 733
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
    n := 734
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
    n := 735
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
    n := 736
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
    n := 737
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
    n := 738
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
    n := 739
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
    n := 740
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
    n := 741
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
    n := 742
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
    n := 743
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
    n := 744
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
    n := 745
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
    n := 746
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
    n := 747
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
    n := 748
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
    n := 749
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
    n := 750
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
    n := 751
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
    n := 752
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
    n := 753
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
    n := 754
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
    n := 755
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
    n := 756
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
    n := 757
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
    n := 758
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
    n := 759
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
    n := 760
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
    n := 761
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
    n := 762
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
    n := 763
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
    n := 764
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
    n := 765
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
    n := 766
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
    n := 767
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
    n := 768
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
    n := 769
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
    n := 770
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
    n := 771
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
    n := 772
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
    n := 773
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
    n := 774
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
    n := 775
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
    n := 776
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
    n := 777
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
    n := 778
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
    n := 779
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
    n := 780
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
    n := 781
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
    n := 782
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
    n := 783
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
    n := 784
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
    n := 785
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
    n := 786
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
    n := 787
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
    n := 788
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
    n := 789
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
    n := 790
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
    n := 791
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
    n := 792
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
    n := 793
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
    n := 794
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
    n := 795
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
    n := 796
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
    n := 797
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
    n := 798
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
    n := 799
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
    n := 800
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
    n := 801
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
    n := 802
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
    n := 803
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
    n := 804
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
    n := 805
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
    n := 806
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
    n := 807
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
    n := 808
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
    n := 809
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
    n := 810
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
    n := 811
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
    n := 812
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
    n := 813
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
    n := 814
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
    n := 815
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
    n := 816
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
    n := 817
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
    n := 818
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
    n := 819
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
    n := 820
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
    n := 821
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
    n := 822
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
    n := 823
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
    n := 824
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
    n := 825
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
    n := 826
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
    n := 827
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
    n := 828
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
    n := 829
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
    n := 830
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
    n := 831
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
    n := 832
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
    n := 833
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
    n := 834
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
    n := 835
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
    n := 836
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
    n := 837
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
    n := 838
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
    n := 839
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
    n := 840
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
    n := 841
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
    n := 842
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
    n := 843
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
    n := 844
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
    n := 845
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
    n := 846
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
    n := 847
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
    n := 848
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
    n := 849
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
    n := 850
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
    n := 851
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
    n := 852
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
    n := 853
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
    n := 854
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
    n := 855
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
    n := 856
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
    n := 857
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
    n := 858
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
    n := 859
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
    n := 860
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
    n := 861
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
    n := 862
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
    n := 863
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
    n := 864
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
    n := 865
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
    n := 866
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
    n := 867
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
    n := 868
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
    n := 869
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
    n := 870
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
    n := 871
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
    n := 872
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
    n := 873
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
    n := 874
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
    n := 875
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
    n := 876
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
    n := 877
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
    n := 878
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
    n := 879
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
    n := 880
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
    n := 881
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
    n := 882
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
    n := 883
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
    n := 884
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
    n := 885
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
    n := 886
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
    n := 887
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
    n := 888
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
    n := 889
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
    n := 890
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
    n := 891
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
    n := 892
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
    n := 893
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
    n := 894
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
    n := 895
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
    n := 896
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
    n := 897
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
    n := 898
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
    n := 899
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
    n := 900
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
    n := 901
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
    n := 902
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
    n := 903
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
    n := 904
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
    n := 905
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
    n := 906
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
    n := 907
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
    n := 908
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
    n := 909
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
    n := 910
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
    n := 911
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
    n := 912
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
    n := 913
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
    n := 914
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
    n := 915
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
    n := 916
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
    n := 917
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
    n := 918
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
    n := 919
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
    n := 920
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
    n := 921
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
    n := 922
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
    n := 923
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
    n := 924
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
    n := 925
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
    n := 926
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
    n := 927
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
    n := 928
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
    n := 929
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
    n := 930
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
    n := 931
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
    n := 932
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
    n := 933
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
    n := 934
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
    n := 935
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
    n := 936
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
    n := 937
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
    n := 938
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
    n := 939
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
    n := 940
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
    n := 941
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
    n := 942
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
    n := 943
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
    n := 944
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
    n := 945
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
    n := 946
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
    n := 947
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
    n := 948
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
    n := 949
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
    n := 950
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
    n := 951
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
    n := 952
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
    n := 953
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
    n := 954
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
    n := 955
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
    n := 956
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
    n := 957
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
    n := 958
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
    n := 959
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
    n := 960
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
    n := 961
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
    n := 962
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
    n := 963
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
    n := 964
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
    n := 965
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
    n := 966
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
    n := 967
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
    n := 968
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
    n := 969
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
    n := 970
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
    n := 971
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
    n := 972
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
    n := 973
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
    n := 974
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
    n := 975
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
    n := 976
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
    n := 977
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
    n := 978
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
    n := 979
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
    n := 980
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
    n := 981
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
    n := 982
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
    n := 983
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
    n := 984
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
    n := 985
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
    n := 986
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
    n := 987
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
    n := 988
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
    n := 989
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
    n := 990
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
    n := 991
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
    n := 992
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
    n := 993
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
    n := 994
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
    n := 995
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
    n := 996
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
    n := 997
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
    n := 998
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
    n := 999
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
    n := 1000
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
    n := 1001
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
    n := 1002
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
    n := 1003
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
    n := 1004
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
    n := 1005
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
    n := 1006
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
    n := 1007
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
    n := 1008
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
    n := 1009
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
    n := 1010
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
    n := 1011
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
    n := 1012
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
    n := 1013
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
    n := 1014
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
    n := 1015
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
    n := 1016
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
    n := 1017
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
    n := 1018
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
    n := 1019
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
    n := 1020
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
    n := 1021
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
    n := 1022
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

