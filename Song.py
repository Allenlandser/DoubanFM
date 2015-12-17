from termcolor import colored

class Song(object):
	"""The Song object to hold the baisc information of the current song"""
	def __init__(self, song_data):
		self.name = song_data['title']
		self.artist = song_data['artist']
		self.url = song_data['url']
		self.album_title = song_data['albumtitle']
		self.like = song_data['like']
		self.length = song_data['length']

	def get_basic_information(self):
		return "%s \\ %s" % (colored(self.artist, 'red'), colored(self.name, 'yellow'))
