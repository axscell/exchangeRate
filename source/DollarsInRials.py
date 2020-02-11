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

#calculate the currency
DIR = 'the price of dollar in rial is: ' + ExchangeRate().dollarInRial()

#GUI
m = tk.Tk()

m.geometry("400x200")

m.title('ExchangeRate')

label = tk.Label(m, text=DIR, bg="red", font=("Courier", 15))

button = tk.Button(m, text='Dollar in Rial', width=25, command=label.pack)
button.pack()


m.mainloop()


