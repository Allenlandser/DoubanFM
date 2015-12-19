# -*- coding: utf-8 -*-
import os
import threading
import time
import sys
from termcolor import colored
from channel import Channel

class View(object):
	def __init__(self, channel):
		self.channel = channel
		self.prefix = 'My DoubanFM \\ '
		self.song_information = None
		self.seconds = 0

	def print_header(self):
		os.system('clear')
		print self.prefix + colored(u"正在播放 >>> ", 'cyan') + self.song_information + "\r"

	def update_header(self):
		self.print_header()
		self.print_channel()

	def stop_print_song_information(self):
		self.stop = True

	def print_song_information(self, seconds, song_information = None):
		self.song_information = song_information
		self.seconds = seconds
		self.print_header()
		self.print_channel()

	def print_pause_information(self):
		os.system('clear')
		print self.prefix + colored(u"点击P键来播放音乐\r", 'green')
		self.print_channel()

	def print_channel(self):
		current_channel = self.channel.current_channel
		channel_list = self.channel.channel_list
		for i in range(len(channel_list)):
			info = ""
			if i != current_channel:
				info = colored(u"   %s\r"  % (channel_list[i]), 'white')
			else:
				info = colored(u" > %s\r" % (channel_list[i]), 'magenta')
			print info

	def print_exit_informaton(self):
		os.system('clear')
		print u"(￣▽￣)Bye~"	

	def print_loading_information(self):
		os.system('clear')
		print self.prefix + colored(u'载入下一曲...\r', 'blue')
		self.print_channel()

	def print_helper(self):
		self.print_header()
		print u'操作手册:'
		print u'P --> 播放'
		print u'S --> 停止'
		print u'N --> 下一曲'
		print u'I --> 上一个频道'
		print u'K --> 下一个频道'
		print u'H --> 显示/关闭操作手册'
		print u'Q --> 退出'

	def convert_seconds_to_minutes(self):
		m, s = divmod(self.seconds, 60)
		return "%02d:%02d" % (m, s)
