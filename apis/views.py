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





class ReactView(APIView):
	def post(self, request, format=None):
		follower_list = []
		Like_list = []
		view_list = []
		serializer = InstagramSerializer(data=request.data)
		if serializer.is_valid():
			usernames = serializer.data['username'] #first parameter in api
			print(usernames)
			followercount = serializer.data['followercount']
			likecount = serializer.data['likecount']
			viewcount = serializer.data['viewcount']
			email = serializer.data['email']
			password = serializer.data['password']
			followercount = int(followercount)
			likecount = int(likecount)
			viewcount = int(viewcount)
			L = instaloader.Instaloader()
			username = email
			password = password
			L.login(username, password) 
			profile = instaloader.Profile.from_username(L.context, usernames)
			if int(followercount)>0: 
			    for followee in profile.get_followers():
				follower_list.append(followee.username)
			#         print(followee.username)
				if len(follower_list) == int(followercount):
				    break

			if int(likecount) > 0: 
			    for post in profile.get_posts():
				print('**************************************************')
				for count in post.get_likes():
			#             print(count.__dict__['_node']['username'])
				    Like_list.append(count.__dict__['_node']['username'])
				    if len(Like_list) == likecount:
					print("Breakkkkkkkkkkkkkkkkkkkkk")
					break
					print(len(Like_list)) 
				if len(Like_list) == likecount:
				    print("Breakkkkkkkkkkkkkkkkkkkkk")
				    break
				    print(len(Like_list))

			if int(viewcount) > 0: 
			    for post in profile.get_posts():
				print('**************************************************')
				for count in post.get_likes():
			#             print(count.__dict__['_node']['username'])
				    view_list.append(count.__dict__['_node']['username'])
				    if len(view_list) == int(viewcount):
					print("Breakkkkkkkkkkkkkkkkkkkkk")
					break
					print(len(view_list))
				if len(view_list) == int(viewcount):
					print("Breakkkkkkkkkkkkkkkkkkkkk")
					break
					print(len(view_list)) 


			print({'follower_list':follower_list ,'Like_list': Like_list,'views_list':view_list})
			
			return Response({'follower_list':follower_list ,'Like_list': Like_list,'views_list':view_list})
