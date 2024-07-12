// Board defines the interface of game-of-life board.
// This interface exists to remove the direct dependency between Board implementation and renderer.
type Board interface {
    Generation() int
    Get(x, y int) bool
    Set(x, y int)
    Size() (int, int)
    Next()
}

type boardImpl struct {
    cur [][]bool
    buf [][]bool
    generation int
}

func NewBoard(w, h int) *boardImpl {
    if w < 3 || h < 3 {
        panic("too small")
    }
    cur := make([][]bool, w)
    buf := make([][]bool, w)
    for i := 0; i < w; i++ {
        cur[i] = make([]bool, h)
        buf[i] = make([]bool, h)
    }
    return &boardImpl{
        cur: cur,
        buf: buf,
    }
}

func (b *boardImpl) Set(x, y int) {
    if x >= 1 && y >= 1 && x < len(b.cur)-1 && y < len(b.cur[0])-1 {
        b.cur[x][y] = true
    }
}

func (b *boardImpl) Get(x, y int) bool {
    return b.cur[x][y]
}

func (b *boardImpl) Size() (int, int) {
    return len(b.cur), len(b.cur[0])
}

func (b *boardImpl) Generation() int {
    return b.generation
}

func (b *boardImpl) nextPixel(x, y int) bool {
    c := 0
    for i := x-1; i < x+2; i++ {
        for j := y-1; j < y+2; j++ {
            if (i != x || j != y) && b.cur[i][j] {
                c += 1
            }
        }
    }
    if !b.cur[x][y] {
        // dead
        return c == 3
    }
    if c == 2 || c == 3 {
        return true
    }
    return false
}

func (b *boardImpl) Next() {
    w := len(b.cur)
    h := len(b.cur[0])
    for i := 0; i < w; i++ {
        for j := 0; j < h; j++ {
            if i == 0 || i == w-1 || j == 0 || j == h-1 {
                // border
                b.buf[i][j] = false
                continue
            }
            b.buf[i][j] = b.nextPixel(i, j)
        }
    }
    tmp := b.cur
    b.cur = b.buf
    b.buf = tmp
    b.generation++
}

import (
    "bytes"
    "encoding/base64"
    "fmt"
    "math/rand"
    "time"
    "os"
)

// Canvas renders the content of GameOfLife to HTML Canvas.
type Canvas struct {
    id string
    jsid string
    width int
    height int
    board Board
    labelID string
    svgID string
}

func NewCanvas(board Board, width, height int) *Canvas {
    return &Canvas{
        id: fmt.Sprintf("canvas%d", rand.Int63()),
        width: width,
        height: height,
        board: board,
    }
}

func (c *Canvas) renderSVG() {
    board := c.board
    w, h := board.Size()
    cw := 100/float64(w)
    ch := 100/float64(h)
    var buf bytes.Buffer
    buf.WriteString(`<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="100" height="100">`)
    for x := 0; x < w; x++ {
        for y := 0; y < h; y++ {
            if !board.Get(x, y) {
                continue
            }
            buf.WriteString(fmt.Sprintf(
                `<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f"></rect>`,
                float64(x)*cw, float64(y)*ch, cw, ch))
        }
    }
    buf.WriteString(`</svg>`)
    _ctx.Display.Text(fmt.Sprintf("Generation: %d", board.Generation()), &c.labelID)
    _ctx.Display.HTML(fmt.Sprintf(
        `<img style="width:%dpx;height:%dpx" src="data:image/svg+xml;base64,%s">`,
        c.width, c.height,
        base64.StdEncoding.EncodeToString(buf.Bytes())), &c.svgID)
}

func (c *Canvas) DisplayAnimation(step int, interval time.Duration) {
    if interval < 10 * time.Millisecond {
        fmt.Fprintf(os.Stderr, "interval is too small: %v", interval)
        return
    }
    c.renderSVG()
    prev := time.Now()
    for i := 0; step < 0 || i < step; i++ {
        c.board.Next()
        time.Sleep(interval-time.Now().Sub(prev))
        prev = time.Now()
        c.renderSVG()
    }
}

{
    g := NewBoard(20, 10)
    c := NewCanvas(g, 400, 200)
    
    var x, y int
    x, y = 1, 1
    g.Set(x, y+1)
    g.Set(x+1, y+1)
    g.Set(x+2, y+1)
    
    x, y = 5, 1
    g.Set(x+1, y+1)
    g.Set(x+2, y+1)
    g.Set(x+3, y+1)
    g.Set(x, y+2)
    g.Set(x+1, y+2)
    g.Set(x+2, y+2)
    
    x, y = 11, 1
    g.Set(x, y)
    g.Set(x+1, y)
    g.Set(x, y+1)
    g.Set(x+1, y+1)
    g.Set(x+2, y+2)
    g.Set(x+3, y+2)
    g.Set(x+2, y+3)
    g.Set(x+3, y+3)
    
    c.DisplayAnimation(20, 250*time.Millisecond)
}

func leftRotate(g *boardImpl) *boardImpl {
    w, h := g.Size()
    n := NewBoard(h, w)
    n.generation = g.generation
    for i := 0; i < w; i++ {
        for j := 0; j < h; j++ {
            n.cur[j][h-1-i] = g.cur[i][j]
        }
    }
    return n
}

func addGlider(g Board, x, y int) {
    g.Set(x, y+2)
    g.Set(x+1, y)
    g.Set(x+1, y+2)
    g.Set(x+2, y+1)
    g.Set(x+2, y+2)
}

{   
    g := NewBoard(160, 160)
    for r := 0; r < 4; r++ {
        max := 7
        for i := 0; i < max; i++ {
            for j := 0; j < max; j++ {
                if i + j >= max {
                    continue
                }
                addGlider(g, i*10+5, j*10+5)
            }   
        }
        g = leftRotate(g)
    }
    c := NewCanvas(g, 480, 480)
    c.DisplayAnimation(300, 100*time.Millisecond)
}

import (
    "math/rand"
)

{   
    w, h := 200, 200
    g := NewBoard(w, h)
    c := NewCanvas(g, 480, 480)
    for i := 1; i < w; i++ {
        for j := 1; j < h; j++ {
            if rand.Int()%2!=0 {
                g.Set(i, j)
            }
        }
    }
    
    for i := 0; i < 10; i++ {
        for j := 0; j < 10; j++ {
            addGlider(g, i*8, j*9)
        }
    }
    c.DisplayAnimation(500, 100*time.Millisecond)
}



