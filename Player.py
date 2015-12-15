import subprocess
import os
from Song import Song

class Player(object):

	def __init__(self):
		self.current_song = None
		self.sub_process = None

	def update_current_song(self, current_song):
		self.current_song = current_song

	def play_current_song(self):
		self.sub_process = subprocess.Popen('mplayer ' + self.current_song.url + ' -slave  >/dev/null 2>&1', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	def stop_playing_current_song(self):
		self.sub_process = subprocess.Popen('killall -9 mplayer', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		