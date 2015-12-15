import urllib
import urllib2
import json

class Channel(object):

	def __init__(self):
		self.channel_cul = "http://www.douban.com/j/app/radio/channels"
		self.current_channel = 0
		self.channel_list = []
		page_source = None

		try:
			page_source = urllib.urlopen(self.channel_cul)
		except urllib2.HTTPError:
			print "Get current song information failed"
		page_data = page_source.read()
		json_data =json.loads(page_data)

		for channel_information in json_data['channels']:
			self.channel_list.append(channel_information['name'])

	def pre_channel(self):
		if self.current_channel > 0:
			self.current_channel = self.current_channel - 1
			print self.current_channel


	def next_channel(self):
		if self.current_channel < len(self.channel_list) - 1:
			self.current_channel = self.current_channel + 1
			print self.current_channel
