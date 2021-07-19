from django.shortcuts import render

from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

import instaloader
from instaloader import Instaloader, Post

L = instaloader.Instaloader()
username = "wilson24.74"
password = "puneet@6644"
L.login(username, password) 



class ReactView(APIView):
	def post(self, request, format=None):
		follower_list = []
		Like_list = []
		serializer = InstagramSerializer(data=request.data)
		if serializer.is_valid():
			usernames = serializer.data['username'] #first parameter in api
			print(usernames)
			count = serializer.data['count'] 			
			print(count)
			counts = int(count)
			profile = instaloader.Profile.from_username(L.context, usernames)
			for followee in profile.get_followers():
				follower_list.append(followee.username)
				print(followee.username)
				if len(follower_list) == counts:
					break
			for post in profile.get_posts():
				print('**************************************************')
				for count in post.get_likes():
					print(count.__dict__['_node']['username'])
					Like_list.append(count.__dict__['_node']['username'])
					if len(Like_list) == counts:
						print("Breakkkkkkkkkkkkkkkkkkkkk")
						break
						print(len(Like_list)) 
				if len(Like_list) == counts:
					print("Breakkkkkkkkkkkkkkkkkkkkk")
					break
					print(len(Like_list))
			
			return Response({'follower_list':follower_list ,'Like_list': Like_list,'views_list':Like_list})
