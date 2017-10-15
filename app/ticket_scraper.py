# -*- coding: UTF-8 -*-

from __future__ import print_function
from lxml import html
import requests
import re
from pprint import pprint
import googlemaps
import json

head = 'https://www.foody.vn/'
mid = "/dia-diem?q="

def get_posts(event_name, position, location):
	loc = '-'.join(location.lower().split())
	name = '+'.join(event_name.lower().split())
	pos = '+'.join(position.split())
	page = requests.get("https://www.foody.vn/" + loc + mid + name)
	tree = html.fromstring(page.text)
	pprint(tree)	
	posts_pages = get_pages(tree) 
	post_info = get_post_info(posts_pages, pos)
	return post_info

def get_pages(root):
	pprint("get_pages")
	post_urls = root.xpath("//div[@class='result-name']/div[@class='resname']/h2/a/@href")
	trees = []
	for i in range(len(post_urls)):	 
		page = requests.get(head+post_urls[i])
		tr = html.fromstring(page.text)
		trees.append(tr)
	return trees

def get_post_info(posts_pages, position):
	pprint("get_post_info")
	post_info = []
	gmaps = googlemaps.Client(key='AIzaSyAJPZle4PLnshyPhSBaQOgJdMnNvko6-ZI')
	for post in posts_pages:
		title = post.xpath("//div[@class='main-info-title']/h1//text()")
		if not title :
			pass
		else :
			addr = post.xpath("//div[@class='res-common-add']/span[2]/a/span//text()")
			distr = post.xpath("//div[@class='res-common-add']/span[3]/a/span//text()")
			city = post.xpath("//div[@class='res-common-add']/span[@itemprop='addressRegion']//text()")
			destinations = addr[0] + ',' + distr[0] + ',' + city[0]
			matrix = gmaps.distance_matrix(position, destinations, mode="walking")
			status = matrix['rows'][0]['elements'][0]['status']
			if status == 'OK':
				dis = matrix['rows'][0]['elements'][0]['distance']['text']
			else :
				dis = 'Not found'
			post_info.append((title[0], addr[0], distr[0], city[0], dis))
	return post_info


if __name__ == "__main__":
	event_name = raw_input("Event to search for: ")
	location = raw_input("Location of event: ")
	results = get_posts(event_name, location)
	for r in results:
		print(r)