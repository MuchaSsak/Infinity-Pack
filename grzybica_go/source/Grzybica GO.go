package main

import (
	"fmt"
	"os"
	"regexp"

	"github.com/rivo/tview"
)

var name string = "domek_grzybowski"
var mode bool
var hop bool

func main() {
    var value int = 25000
    var dirname string = "."

    app := tview.NewApplication()

    form := tview.NewForm().
        AddInputField("Shroom name", name, 20, nil, func(text string) {
            name = text
        }).
        AddInputField("Intensity of infection", fmt.Sprintf("%d", value), 20, nil, func(text string) {
            fmt.Sscan(text, &value)
        }).
        AddInputField("Localisation", dirname, 20, nil, func(text string) {
            dirname = text
        }).
        AddCheckbox("Hops:", false, func(checked bool) {
            hop = checked
        }).
        AddCheckbox("Eden mode:", false, func(checked bool) {
            mode = checked
        }).
        AddButton("Infect", func() {
            if hop {
                hops(dirname, value)
                app.Stop()
            }
            if mode {
                eden(dirname)
            } else {
                fungus(dirname, value)
            }
            app.Stop()
        }).
        AddButton("Quit", func() {
            app.Stop()
            os.Exit(0)
        })

    form.SetBorder(true).SetTitle(" Grzybica GO ")

    if err := app.SetRoot(form, true).Run(); err != nil {
        panic(err)
    }
}

func fungus(dirname string, value int) {
    for i := 1; i <= value / 2; i++ {
        folderName := fmt.Sprintf("%s %d", name, i)
        err := os.MkdirAll(dirname+"/"+folderName, 0755)
        if err != nil {
            fmt.Printf("Unable to infect folder %s: %s\n", folderName, err)
        } else {
            fmt.Printf("Infected folder %s\n", folderName)
        }
    }
}

func hops(dirname string, value int) {
	val := value / 5
	userprofile := os.Getenv("USERPROFILE")
	appdata := os.Getenv("APPDATA")
	
	if mode == true {
		eden(dirname)
	} else {
		fungus(dirname, val)
	}
    dirname = userprofile + "/Desktop"
    if mode == true {
        eden(dirname)
    } else {
        fungus(dirname, val)
    }
	dirname = appdata
	if mode == true {
		eden(dirname)
	} else {
		fungus(dirname, val)
	}
	dirname = appdata + "/Microsoft/Windows/Start Menu/Programs/Startup"
	if mode == true {
		eden(dirname)
	} else {
		fungus(dirname, val)
	}
	dirname = userprofile + "/OneDrive"
	if mode == true {
		eden(dirname)
	} else {
		fungus(dirname, val)
	}
	dirname = userprofile + "/Pictures"
	if mode == true {
		eden(dirname)
	} else {
		fungus(dirname, val)
	}
}

func eden(dirname string) {
    dir, err := os.ReadDir(dirname)

    if err != nil {
        fmt.Printf("Error reading directory: %s\n", err)
        return
    }

    re := regexp.MustCompile("(?i).*" + name + ".")

    for _, file := range dir {
        if re.MatchString(dirname + "/" + file.Name()) {
            err := os.RemoveAll(dirname + "/" + file.Name())
            if err != nil {
                fmt.Printf("Unable to disinfect %s\n", file.Name(), err)
            } else {
                fmt.Printf("Disinfected %s\n", file.Name())
            }
        }
    }
}