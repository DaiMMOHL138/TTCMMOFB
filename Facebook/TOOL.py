import requests
import json
import codecs
import os
import time
import tkinter as tk
class APP:
	def __init__(self):

		self.root = tk.Tk()
		self.root.title("Đại TOOL")
		self.root.iconbitmap("icon.ico")
		self.root.geometry("700x500")

class Main:

	def __init__(self):

		self.app_running = APP()

	def run(self):

		self.app_running.root.mainloop()

if __name__ == "__main__":
	
	Main().run()