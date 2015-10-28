#!/usr/bin/python

from sys import argv
import re
import sys
import math
import numpy as np
import copy
from igraph import *
from matplotlib import pyplot
from shapely.geometry import *
from descartes.patch import PolygonPatch
from utils import *
from myDictionaries import *
import uuid
import xml.dom.minidom

from floor import *


class rooms(object) :
	'''
	Classe principale: possiede i vari floor di edifici.
	'''
	def __init__(self):
		self.floorplans = []
		self.metrics = dict() 
		pass

	def load(self, labels = None, recursive = None) :
		pass

	def save(self, extension = None, format = None, mask = None) :
		pass

	def plot(self) :
		pass

	def plot_as(self, format  = None, mask = None):
		pass

	def compute(self) :
		pass

	def save_metrics(self, format = None, mask = None):
		pass
