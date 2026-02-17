#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Network Speed Monitor

Monitors the amount of data sent and received by the available network interfaces 
to calculate the transmission speed (download and upload) of the Internet.

(c) 2025 Javi Domínguez <fjavids@gmail.com>
Released under GPL 2 license. https://gnu.org/licenses/old-licenses/gpl-2.0.html
It uses Psutil, licensed under 3-Clause BSD License which is compatible with GPL.
"""
from threading import Thread
from datetime import datetime 
from time import sleep
import psutil

class NetworkSpeed(Thread):
	""" Thread that collects network statistics at one-second intervals and calculate download and upload speeds.
	It uses aggregated data from all network interfaces."""

	def __init__(self, sampleRate:int=8, *args, **kwargs):
		""" Initializes the class and sets the sample rate, along with the initial sample.
		@sampleRate: The number of samples to maintain for calculating the network speed. This determines how many samples will be kept in the samples list for calculating speeds.
		@samples: Stores network data samples. The initial sample is stored at position 0 and the rest of the samples are stored in subsequent positions.
		@maxDownload / maxUpload: Stores the maximum recorded download and upload speeds, respectively.
		"""
		super().__init__(self, *args, **kwargs)
		self.setDaemon(True)
		self.sampleRate = sampleRate
		self.samples = [(datetime.now(), psutil.net_io_counters())]
		self.maxDownload = -1
		self.maxUpload = -1

	@property
	def download(self) -> int:
		""" Returns the download speed in bps.
		-1 indicates that the thread has not been started yet."""
		try:
			bytes_recv = psutil.net_io_counters().bytes_recv - self.samples[1][1].bytes_recv
			delta = datetime.now() - self.samples[1][0]
		except IndexError:
			return -1
		seconds = delta.seconds + delta.microseconds/1000000
		if seconds == 0: return -1
		return int(round(bytes_recv/seconds,0))*8

	@property
	def averageDownload(self) -> int:
		""" Returns in bps the average download speed during the current session (since the thread was initialized).
		-1 indicates that the thread has not been started yet."""
		if not self.is_alive(): return -1
		bytes_recv = psutil.net_io_counters().bytes_recv - self.samples[0][1].bytes_recv
		delta = datetime.now() - self.samples[0][0]
		seconds = delta.seconds + delta.microseconds/1000000
		if seconds == 0: return -1
		return int(round(bytes_recv/seconds,0))*8

	@property
	def upload(self) -> int:
		""" Returns the upload speed in bps.
		-1 indicates that the thread has not been started yet."""
		try:
			bytes_sent = psutil.net_io_counters().bytes_sent - self.samples[1][1].bytes_sent
			delta = datetime.now() - self.samples[1][0]
		except IndexError:
			return -1
		seconds = delta.seconds + delta.microseconds/1000000
		if seconds == 0: return -1
		return int(round(bytes_sent/seconds,0))*8

	@property
	def averageUpload(self) -> int:
		""" Returns in bps the average upload speed during the current session (since the thread was initialized).
		-1 indicates that the thread has not been started yet."""
		if not self.is_alive(): return -1
		bytes_sent = psutil.net_io_counters().bytes_sent - self.samples[0][1].bytes_sent
		delta = datetime.now() - self.samples[0][0]
		seconds = delta.seconds + delta.microseconds/1000000
		if seconds == 0: return -1
		return int(round(bytes_sent/seconds,0))*8

	def run(self):
		""" Collects network statistics at one-second intervals and updates maximum download and upload speeds. """
		self.samples.append((datetime.now(), psutil.net_io_counters()))
		while True:
			sleep(1.0)
			self.samples.append((datetime.now(), psutil.net_io_counters()))
			if len(self.samples) > self.sampleRate+1:
				self.samples.pop(1)
				download = self.download
				if download > self.maxDownload:
					self.maxDownload = download
				upload = self.upload
				if upload > self.maxUpload:
					self.maxUpload = upload
