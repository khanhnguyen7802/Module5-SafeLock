import drivers

display = drivers.Lcd()


output = "____"
states = {"lock":0,
          "lights":1,
          "user":4,
          "sound":1
}

STATICS = {2: "                    ",
           0: "      A~unlock      ",
           1: "       A~lock       ",
           4: "        USER        ",
           5: "        ADMIN       "
}
interfaces = {0:["-------SAFEty-------", "   Enter password:   ", "        " + output + "        ", "*~clear      #~enter"],
           1:[STATICS[2], "       Invalid", STATICS[2], "    Only numbers    "],
           2:["  Correct password  ", STATICS[2], STATICS[2], STATICS[2]],
           3:[" Incorrect password ", STATICS[2], STATICS[2], STATICS[2]],
           4:["        MENU        ", STATICS[2], STATICS[1], STATICS[2]],
           5:["        MENU        ", STATICS[states["lock"]], "     B~Settings     ", "       C~Exit       "],
           6:["      SETTINGS      ", "     A~Hardware     ", "      B~Password      ", "       C~Exit       "]

}

DYNAMIC_INTERFACES = [0, 5]

def update():
    new = {0:["-------SAFEty-------", "   Enter password:   ", "        " + output + "        ", "*~clear      #~enter"],
           5:["        MENU         ", STATICS[states["lock"]], "     B~Settings     ", "       C~Exit       "]

    }
    interfaces.update(new)

def d_print(number):
    interface = interfaces[number]
    i = 1
    if number in DYNAMIC_INTERFACES:
        update()
    for j in interface:
        display.lcd_display_string(j, i)
        i += 1