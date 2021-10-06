from Tooltip import CreateToolTipOnButton

import tkinter as tk
import requests as req

import FileSystem
import re
import webbrowser


class AuthenticationWindow(tk.Frame):
    def __init__(self, master=None, root=None):
        super().__init__(master=master)

        self.master = master
        self.root = root
        self.Authenticated = False
        self._after_tooltip = None

        self.create_widgets()

        self.pack(fill="both", expand=True)
    # End of __init__

    def create_widgets(self):
        self.master.title("Add a authentication key!")
        defaultIco = FileSystem.resource_path('icon.ico')
        self.master.iconbitmap(default=defaultIco)

        self.master.protocol("WM_DELETE_WINDOW", self.onExit)

        self.APIKeyMissingLabel = tk.Label(
            self, text="You don't seem to have a ballchasing API key!")
        self.APIKeyMissingLabel.grid(
            row=0, column=0, columnspan=3, sticky="new", padx=2, pady=2)

        # Rich text formatting starts here
        self.HyperlinkText = tk.Text(
            self, height=1, font=self.APIKeyMissingLabel['font'], borderwidth=0, background="#F0F0F0", cursor="")
        self.HyperlinkText.tag_configure("center", justify="center")
        self.HyperlinkText.grid(
            row=1, column=0, columnspan=3, sticky="new", padx=2, pady=2)
        self.HyperlinkText.tag_configure(
            "hyperlink", underline=1, foreground="#0000EE")
        self.HyperlinkText.tag_bind(
            "hyperlink", "<Button-1>", lambda e: webbrowser.open_new("https://ballchasing.com/upload"))
        self.HyperlinkText.tag_bind(
            'hyperlink', "<Enter>", lambda e: self.HyperlinkText.config(cursor="hand2"))
        self.HyperlinkText.tag_bind(
            'hyperlink', '<Leave>', lambda e: self.HyperlinkText.config(cursor=""))

        self.HyperlinkText.insert("1.0", "Go to ")

        self.HyperlinkText.insert(
            tk.END, "http://ballchasing.com/upload", "hyperlink")

        self.HyperlinkText.insert(
            tk.END, ', login and find the API key there!')

        self.HyperlinkText.tag_add("center", "1.0", tk.END)
        self.HyperlinkText.configure(state="disabled")
        # Rich text formatting ends here

        self.PleaseEnterBelowLabel = tk.Label(
            self, text="Please enter it below:")
        self.PleaseEnterBelowLabel.grid(
            row=2, column=0, columnspan=3, padx=0, pady=2)

        self.AuthenticationInput = tk.Entry(self, width=40, show="*")
        self.AuthenticationInput.grid(
            row=3, column=0, sticky="ne", padx=2, pady=2)

        self.PasteButton = tk.Button(
            self, text="Paste", command=self.onPasteClicked)
        self.PasteButton.grid(row=3, column=1, sticky="new", padx=2, pady=2)

        self.PasteButtonToolTip = CreateToolTipOnButton(
            self.PasteButton, 'You clipboard doesn\'t have the corret input!')

        self.ConfirmAPIKeyButton = tk.Button(
            self, text="Submit!", command=self.APIKeySubmission)
        self.ConfirmAPIKeyButton.grid(
            row=3, column=2, sticky="new", padx=2, pady=2)
    # End of create_widgets

    def APIKeySubmission(self):
        apiKey = self.AuthenticationInput.get()
        print("Submitted " + apiKey)
        API_KEY_RE = re.compile('[A-Za-z0-9]{40}')
        if(API_KEY_RE.search(apiKey) is not None):
            headers = {
                'Authorization': apiKey}
            response = req.get('https://ballchasing.com/api/', headers=headers)
            responseJson = response.json()
            if(responseJson.get('error') is not None):
                print(responseJson.get('error'))
            else:
                currentAuth = FileSystem.loadJson(
                    'rlstats/data/auth.json')
                currentAuth['bc'] = apiKey
                FileSystem.writeJson(
                    'rlstats/data/auth.json', currentAuth)
                mainWindow = self.root.winfo_children()[0]
                mainWindow.authentication = currentAuth
                mainWindow.ballchasingHeaders = {
                    'Authorization': apiKey}
                self.root.deiconify()
                self.master.destroy()
                mainWindow.AuthenticationWindow = None
                mainWindow.create_widgets()
        else:
            self.PasteButtonToolTip.showtip()
    # End of APIKeySubmission

    def onPasteClicked(self):
        API_KEY_RE = re.compile('[A-Za-z0-9]{40}')
        clipboard = self.root.clipboard_get()

        if(API_KEY_RE.search(clipboard) is not None):
            self.AuthenticationInput.delete(0, tk.END)
            self.AuthenticationInput.insert(0, clipboard)
        else:
            self.PasteButtonToolTip.showtip()

    # End of onPasteClicked

    def onExit(self):
        self.master.destroy()
        if(not self.Authenticated):
            self.root.destroy()
    # End of onExit
