import drivers

display = drivers.Lcd()


output = "____"
states = {"lock":0,
          "user":4,
          "lights":6,
          "sounds":6
}

STATICS = {2: "                    ",
           0: "      A~unlock      ",
           1: "       A~lock       ",
           4: "        USER        ",
           5: "        ADMIN       ",
           6: "ON        ",
           7: "OFF       "
}
interfaces = {0:["-------SAFEty-------", "   Enter password:   ", "        " + output + "        ", "*~clear      #~enter"],
           1:[STATICS[2], "       Invalid      ", STATICS[2], "    Only numbers    "],
           2:["  Correct password  ", STATICS[2], STATICS[2], STATICS[2]],
           3:[" Incorrect password ", STATICS[2], STATICS[2], STATICS[2]],
           4:["        MENU        ", STATICS[2], STATICS[1], STATICS[2]],
           5:["        MENU        ", STATICS[states["lock"]], "     B~Settings     ", "       C~Exit       "],
           6:["      SETTINGS      ", "     A~Hardware     ", "      B~Password      ", "       C~Exit       "],
           7:["      HARDWARE      ", "A~Lights: " + STATICS[states["lights"]], "B~Sounds: " + STATICS[states["lights"]], "       C~Exit       "],
           8:["      PASSWORD      ", "       A~User       ", "       C~Admin        ", "       C~Exit       "],
           9:[STATICS[states["user"]], " Enter new password ", "        " + output + "        ", "       C~Exit       "],
           10:[STATICS[2], "       Invalid      ", STATICS[2], "  Minimal 4 digits  "],
           11:["   SECURITY ALERT   ", "       A~User       ", "       C~Admin        ", "       C~Exit       "]
}

DYNAMIC_INTERFACES = [0, 5, 7, 9]

def update():
    new = {0:["-------SAFEty-------", "   Enter password:   ", "        " + output + "        ", "*~clear      #~enter"],
           5:["        MENU         ", STATICS[states["lock"]], "     B~Settings     ", "       C~Exit       "],
           7:["      HARDWARE      ", "A~Lights: " + STATICS[states["lights"]], "B~Sounds: " + STATICS[states["lights"]], "       C~Exit       "],
           9:[STATICS[states["user"]], " Enter new password ", "        " + output + "        ", "       C~Exit       "],
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