from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from kivy.app import App
from kivy.uix.label import Label


class currency() :
	def dollarInRial(self) :
		url = 'http://www.tgju.org/currency'
		page = urlopen(url)
		soup = bs(page, 'html.parser')
		priceOfDollar = soup.find('td' , attrs={'class':'nf'})
		priceOfDollar = priceOfDollar.text
		return priceOfDollar

class CurrencyApp(App):
	def build(self):
		return Label(text='price of dollar is: ' + currency().dollarInRial() + ' Rls')


CurrencyApp().run()
