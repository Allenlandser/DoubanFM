import urllib
import urllib2
import json
import getch
import sys
import time
import threading
from Song import Song
from Player import Player
from view import View
from channel import Channel

class Client(object):
	"""The client class that responds for the user input and menu print, as well as the main logics"""
	def __init__(self):
		self.url = 'http://douban.fm/j/mine/playlist?type=n&channel=%d&from=mainsite'
		self.current_song = None
		self.player = Player()
		self.channel = Channel()
		self.current_channel = self.channel.current_channel
		self.view = View(self.channel)
		self.update_current_song()
		self.is_playing = False
		self.is_display_help = False
		self.seconds = 0
		self.protect_thread = threading.Thread(target = self.protect)
		self.protect_thread.daemon = True

	def update_current_song(self):
		page_source = None
		url = self.url % self.current_channel
		try:
			page_source = urllib.urlopen(url)
		except urllib2.HTTPError:
			print "Get current song information failed"
		page_data = page_source.read()
		json_data =json.loads(page_data)
		new_json_data = json.dumps(json_data['song'], ensure_ascii=False)
		song_data = json.loads(new_json_data)

		self.current_song = Song(song_data[0]) 
		self.length = self.current_song.length
		self.player.update_current_song(self.current_song)

	def protect(self):
		while True:
			if self.is_playing:
				self.seconds = self.seconds + 1
				if self.seconds == self.length:
					self.next()
			time.sleep(1.0)

	def print_helper(self):
		self.is_display_help = not self.is_display_help

	def play(self):
		self.is_playing = True
		self.seconds = 0
		self.player.play_current_song()

	def stop(self):
		self.is_playing = False
		self.player.stop_playing_current_song()

	def next(self):
		self.is_playing = False
		self.view.print_loading_information()
		self.player.stop_playing_current_song()
		self.update_current_song()
		self.play()
		self.display()

	def pre_channel(self):
		self.channel.pre_channel()
		self.change_channel()

	def next_channel(self):
		self.channel.next_channel()
		self.change_channel()

	def change_channel(self):
		new_channel = self.channel.current_channel
		if new_channel != self.current_channel:
			self.current_channel = new_channel
			self.next()

	def exit(self):
		self.player.stop_playing_current_song()
		self.view.print_exit_informaton()
		sys.exit()

	def display(self):
		if self.is_display_help == False:
			if self.is_playing == True:
				self.view.print_song_information(self.seconds, self.current_song.get_basic_information())
			else:
				self.view.print_pause_information()
		else:
			self.view.print_helper();

	def start(self):
		self.play()
		self.protect_thread.start()
		while True:
			self.display()
			i = getch._Getch()
			choice = i()
			if choice == 'p' and self.is_playing == False:
				self.play()
			elif choice == 's' and self.is_playing == True:
				self.stop()
			elif choice == 'n':
				self.next()
			elif choice == 'i':
				self.pre_channel()
			elif choice == 'k':
				self.next_channel()
			elif choice == 'h':
				self.print_helper()
			elif choice == 'q':
				self.exit()