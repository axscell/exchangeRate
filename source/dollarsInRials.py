from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import tkinter as tk


class ExchangeRate() :
	def dollarInRial(self) :
		self.url = 'http://www.tgju.org/currency'
		self.page = urlopen(self.url)
		self.soup = bs(self.page, 'html.parser')
		self.priceOfDollar = self.soup.find('td' , attrs={'class':'nf'})
		self.priceOfDollar = self.priceOfDollar.text
		return self.priceOfDollar
try:
	#calculate the currency
	DIR = '$1 = ' + ExchangeRate().dollarInRial() + " Rial"

	#GUI
	root = tk.Tk()

	root.geometry("400x200")

	root.title('ExchangeRate')

	label = tk.Label(root, text=DIR, bg="red", font=("Courier", 15))

	button = tk.Button(root, text='Click here to show the price', width=25, command=label.pack)
	button.pack()

	button = tk.Button(root, text='Exit', width=25, command=root.destroy)
	button.pack()

	root.mainloop()
except:
	root = tk.Tk()

	root.geometry("350x50")
	root.title("ERROR PAGE")

	label = tk.Label(root, text="you'r not connected to internet", bg="red", font=("Courier", 15),)
	label.pack()

	button = tk.Button(root, text="Exit", width=20, command=root.destroy)
	button.pack()

	root.mainloop()
