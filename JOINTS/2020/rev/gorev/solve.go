package main

import (
    "fmt"
    "time"
    "math/rand"
    "encoding/hex"
)

func main() {
    rand.Seed(time.Now().Unix())
    key := make([]byte, 64)
    rand.Read(key)
    fmt.Println(hex.EncodeToString(key))
}

