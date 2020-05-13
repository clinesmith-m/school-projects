from tkinter import *

class FtoC(Canvas):
    def __init__(self, parent, **kwargs):
        if "width" not in kwargs:
            raise KeyError("Argument 'width' not provided.")
        if "height" not in kwargs:
            raise KeyError("Argument 'length' not provided.")

        super_kwargs = kwargs.copy()
        if "frange" in kwargs:
            del super_kwargs["frange"]
        else:
            raise KeyError("Argument 'frange' not provided.")

        super().__init__(parent, super_kwargs)


        # Creating the thermometer lines for the fahrenheit column
        self.f_col_loc = 150
        self.f_left_line = self.create_line(
            self.f_col_loc, 0, self.f_col_loc, kwargs["height"]
        )
        self.f_right_line = self.create_line(
            self.f_col_loc+50, 0, self.f_col_loc+50, kwargs["height"]
        )

        # Creating the thermometer lines for the celcius column
        self.c_col_loc = kwargs["width"]-150
        self.c_left_line = self.create_line(
            self.c_col_loc, 0, self.c_col_loc, kwargs["height"]
        )
        self.c_right_line = self.create_line(
            self.c_col_loc+50, 0, self.c_col_loc+50, kwargs["height"]
        )


        # Drawing the fahrenheit thermometer numbers
        self.low_ftemp = kwargs["frange"][0]
        self.high_ftemp = kwargs["frange"][1]
        self.f_variance = self.high_ftemp - self.low_ftemp
        self.pixels_per_fdegree = kwargs["height"] / self.f_variance
        self.f_thermo_text = []
        for temp in range(self.low_ftemp, self.high_ftemp + 1):
            if temp % 10 == 0:
                temp_y = (temp - self.low_ftemp) * self.pixels_per_fdegree
                self.f_thermo_text.append(
                    self.create_text(
                        self.f_col_loc + 25,
                        temp_y,
                        text = temp
                    )
                )

        # Drawing the celcius thermometer numbers
        self.low_ctemp = ((self.low_ftemp - 32) * (5/9))
        self.high_ctemp = ((self.high_ftemp - 32) * (5/9))
        self.c_variance = self.high_ctemp - self.low_ctemp
        self.pixels_per_cdegree = kwargs["height"] / self.c_variance
        self.c_thermo_text = []
        for temp in range(round(self.low_ctemp), round(self.high_ctemp) + 1):
            if temp % 10 == 0:
                temp_y = (temp - self.low_ctemp) * self.pixels_per_cdegree
                self.c_thermo_text.append(
                    self.create_text(
                        self.c_col_loc + 25,
                        round(temp_y),
                        text = temp
                    )
                )

        # Drawing the degree-F and degree-C symbols
        self.degree_f = self.create_text(
            self.f_col_loc + 60,
            (kwargs["height"] - 10),
            text = "\N{DEGREE SIGN}F"
        )
        self.degree_c = self.create_text(
            self.c_col_loc + 60,
            (kwargs["height"] - 10),
            text = "\N{DEGREE SIGN}C"
        )


        # Creating the triangle to point to the fahrenheit column
        self.f_triline_a = self.create_line(
            self.f_col_loc - 65,
            (kwargs["height"]/2)-25,
            self.f_col_loc - 65,
            (kwargs["height"]/2)+25,
        )
        self.f_triline_b = self.create_line(
            self.f_col_loc - 65,
            (kwargs["height"]/2)-25,
            self.f_col_loc - 15,
            (kwargs["height"]/2),
        )
        self.f_triline_c = self.create_line(
            self.f_col_loc - 65,
            (kwargs["height"]/2)+25,
            self.f_col_loc - 15,
            (kwargs["height"]/2),
        )

        # Creating the triangle to point to the celcius column
        self.c_triline_a = self.create_line(
            self.c_col_loc - 65,
            (kwargs["height"]/2)-25,
            self.c_col_loc - 65,
            (kwargs["height"]/2)+25,
        )
        self.c_triline_b = self.create_line(
            self.c_col_loc - 65,
            (kwargs["height"]/2)-25,
            self.c_col_loc - 15,
            (kwargs["height"]/2),
        )
        self.c_triline_c = self.create_line(
            self.c_col_loc - 65,
            (kwargs["height"]/2)+25,
            self.c_col_loc - 15,
            (kwargs["height"]/2),
        )

        self.f_text = self.create_text(
            self.f_col_loc - 85, 
            (kwargs["height"])/2,
            text = self.get_f_temp((kwargs["height"])/2)
        )

        self.c_text = self.create_text(
            self.c_col_loc - 85, 
            (kwargs["height"])/2,
            text = self.get_c_temp((kwargs["height"])/2)
        )


        # Binding click and drag
        self.bind("<Button-1>", self.change_temp)
        self.bind("<B1-Motion>", self.change_temp)


    def change_temp(self, event):
        # Redrawing the triangle to point to the fahrenheit column
        self.coords(
            self.f_triline_a,
            self.f_col_loc - 65,
            event.y-25,
            self.f_col_loc - 65,
            event.y+25,
        )
        self.coords(
            self.f_triline_b,
            self.f_col_loc - 65,
            event.y-25,
            self.f_col_loc - 15,
            event.y,
        )
        self.coords(
            self.f_triline_c,
            self.f_col_loc - 65,
            event.y+25,
            self.f_col_loc - 15,
            event.y
        )

        # Redrawing the triangle to point to the celcius column
        self.coords(
            self.c_triline_a,
            self.c_col_loc - 65,
            event.y-25,
            self.c_col_loc - 65,
            event.y+25,
        )
        self.coords(
            self.c_triline_b,
            self.c_col_loc - 65,
            event.y-25,
            self.c_col_loc - 15,
            event.y,
        )
        self.coords(
            self.c_triline_c,
            self.c_col_loc - 65,
            event.y+25,
            self.c_col_loc - 15,
            event.y,
        )

        # Changing the text
        self.coords(
            self.f_text,
            self.f_col_loc - 85,
            event.y
        )
        self.coords(
            self.c_text,
            self.c_col_loc - 85,
            event.y
        )
        self.itemconfig(
            self.f_text,
            text = self.get_f_temp(event.y)
        )
        self.itemconfig(
            self.c_text,
            text = self.get_c_temp(event.y)
        )


    def get_f_temp(self, y_val):
        temp = (y_val/self.pixels_per_fdegree) + self.low_ftemp
        return round(temp, 1)

    def get_c_temp(self, y_val):
        temp = (y_val/self.pixels_per_cdegree) + self.low_ctemp
        return round(temp, 1)


window = Tk()

frame = Frame(window)
w = 540
h = 900
lo_f = -50
hi_f = 250

canvas = FtoC(frame, width=w, height=h, frange=[lo_f, hi_f])

frame.pack()
canvas.pack(side='top', fill='both', expand=True)
window.geometry("{}x{}+100+100".format(w, h))

window.mainloop()
