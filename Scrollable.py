import tkinter as tk
from tkinter import ttk


class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.master = container

        self.originalMasterWidth = self.master.winfo_width()

        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.verticalScrollbar = tk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview)
        self.verticalScrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.verticalScrollbar.set)

        self.contentFrame = tk.Frame(self.canvas)

        self.canvas.create_window(
            (0, 0), window=self.contentFrame, anchor="nw")

        self.contentFrame.configure(width=self.master.winfo_width(
        ), height=self.master.winfo_height())

        bbox = self.canvas.bbox(tk.ALL)
        self.canvas.configure(scrollregion=bbox,
                              width=self.master.winfo_width(), height=self.master.winfo_height())

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.contentFrame.bind("<Configure>", self.configureHandler)
    # End of __init__

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    # End of _on_mousewheel

    def addWidget(self, uniqueName, widgetType, args, row=0, column=0, sticky="", columnspan=1, rowspan=1):
        self.__setattr__(uniqueName,
                         ttk.__getattribute__(widgetType)(self.contentFrame))
        for arg in args:
            self.__getattribute__(uniqueName).configure(arg)

        self.__getattribute__(uniqueName).grid(
            row=row, column=column, sticky=sticky, columnspan=columnspan, rowspan=rowspan)
    # End of addWidget

    def update(self):
        super().update()
    # End of update

    def configureHandler(self, event):
        if(event.widget is not self.contentFrame and event.widget is not self.canvas):
            self.recalculateScrollBox()
        else:
            width, height = self.calculateWidthAndHeightRequired()
            self.canvas.configure(width=width, height=height)
            self.updateBBoxCanvas(width, height)
    # End of configureHandler

    def calculateWidthAndHeightRequired(self):
        width = self.contentFrame.winfo_width()
        reqWidth = self.contentFrame.winfo_reqwidth()
        reqHeight = self.contentFrame.winfo_reqheight()
        height = self.contentFrame.winfo_height()

        maxHeight = self.master.winfo_height()
        maxWidth = self.master.winfo_width()-self.verticalScrollbar.winfo_width()

        for child in self.master.grid_slaves(column=0):
            if(child is not self):
                paddingY = (
                    int(str(child.cget('pady'))) +
                    int(str(child.cget('borderwidth')))
                )
                # TODO: figure out where this 2*1 is coming from to offset the resizing error
                maxHeight -= (child.winfo_height()+2*(paddingY+1))
        maxHeight -= 2*(
            int(str(self.cget('pady'))) +
            int(str(self.cget('borderwidth'))) +
            int(str(self.master.cget('pady'))) +
            int(str(self.master.cget('borderwidth'))) +
            int(str(self.contentFrame.cget('pady'))) +
            int(str(self.contentFrame.cget('borderwidth')))
        )

        if(reqWidth < self.originalMasterWidth):
            reqWidth = self.originalMasterWidth-2*(
                int(str(self.cget('padx'))) +
                int(str(self.cget('borderwidth'))) +
                int(str(self.master.cget('padx'))) +
                int(str(self.master.cget('borderwidth'))) +
                int(str(self.contentFrame.cget('padx'))) +
                int(str(self.contentFrame.cget('borderwidth'))) +
                int(str(self.verticalScrollbar.cget('borderwidth')))
            )-4  # TODO: figure out where this 2*2 is coming from to offset the resizing error

        reqHeight = maxHeight

        return (reqWidth, reqHeight)
    # End of calculateWidthAndHeightRequired

    def updateBBoxCanvas(self, width, height):
        bbox = self.canvas.bbox("all")

        self.canvas.configure(scrollregion=bbox,
                              width=width,
                              height=height)
    # End of updateBBoxCanvas

    def recalculateScrollBox(self):
        self.canvas.delete("all")
        self.canvas.create_window(
            (0, 0), window=self.contentFrame, anchor="nw")

        width, height = self.calculateWidthAndHeightRequired()

        self.contentFrame.update_idletasks()
        self.contentFrame.configure(width=width, height=height)

        self.originalMasterWidth = self.master.winfo_width()

        self.updateBBoxCanvas(width, height)
    # End of recalculateScrollBox
