import (
    "flag"
    "io/ioutil"
    "log"
    "os"
    "path/filepath"
    "strings"
    "time"
    "unicode"
    "fmt"
    "encoding/json"

    "github.com/machinebox/sdk-go/facebox"
)

faceboxClient := facebox.New("http://localhost:8080")

inDir := "/home/dwhitena/go/src/github.com/dwhitena/pach-machine-box/data/train/faces1"

// Walk over images in the training directory.
if err := filepath.Walk(inDir, func(path string, info os.FileInfo, err error) error {

    // Skip any directories.
    if info.IsDir() {
        return nil
    }

    // Open the training image file.
    f, err := os.Open(filepath.Join(inDir, info.Name()))
    if err != nil {
        return err
    }
    defer f.Close()

    // Teach FaceBox the input image.
    if err := faceboxClient.Teach(f, info.Name(), "trump"); err != nil {
        return err
    }

    return nil
}); err != nil {
    log.Println(err)
}

// IdentifiedFaces includes information about the faces
// identified in an image.
type IdentifiedFaces struct {
    Success    bool           `json:"success"`
    FacesCount int            `json:"facesCount"`
    Faces      []facebox.Face `json:"faces"`
}

// Open the input image.
f, err := os.Open("/home/dwhitena/go/src/github.com/dwhitena/pach-machine-box/data/unidentified/image1.jpg")
if err != nil {
    log.Println(err)
}
defer f.Close()

// Teach FaceBox the input image.
faces, err := faceboxClient.Check(f)
if err != nil {
    log.Println(err)
}

// Prepare the output.
output := IdentifiedFaces{
    Success:    true,
    FacesCount: len(faces),
    Faces:      faces,
}

// Marshal the output.
outputData, err := json.MarshalIndent(output, "", "  ")
if err != nil {
    return log.Println(err)
}

fmt.Println(string(outputData))



