---
title: "Hive Block Explorer"
subtitle: "Python Based Local Tool"
date: 2021-11-30
lastmod: 2021-11-30
draft: false
authors: []
description: "This is an Open Source utility tool for the Hive Blockchain which is displays the 'Guts' of a user post, for analytics purposes"

tags: ["Python", "Hive", "Blockchain"]
categories: ["Projects"]

hiddenFromHomePage: false
hiddenFromSearch: false

featuredImage: "hive-block-explorer-cover.jpg"
featuredImagePreview: "hive-block-explorer-cover.jpg"

toc:
  enable: true
math:
  enable: false
lightgallery: false
license: ""
---

<!--more-->

Recently, I've been posting content on the Hive blockchain to earn a little bit of income from my posts in the form of tokens or cryptocurrency.

## Context Please. What Is The Hive Blockchain?

To give more context to this post. Hive is a blockchain based social network where people share content, pretty much like on Facebook but here, the people's votes (or likes) have value, and by voting your post people give your post a value and after 7 days you can collect part of the total value your post gather in that 7 day period time.

But most of the community around this social network are not developers, and adding the fact that there are not too many tools for developers, AND, those tools that are out there, doesn't have the greatest documentation. So, there are not too many developers, and also, it isn't very popular as Ethereum but I still love it because in a year or so, it helped me every now and then to earn some income while I'm still unemployed.

## My Issue With Hive's Tools 

Most of the tools the Hive blockchain has, are web based tools. One in particular is called [Hive Blocks](https://hiveblocks.com/) which let's you visualize, lets say the "guts" of every transaction or people's posts they do on the blockchain. Aside from this app, overall these web apps are not very stable (the domain expire, there's a bad gateway, some functionality broke due to some update, among others), and that intrigues me because, there's no other site that have that functionality that I want and there's also not local tools for doing so.

## Someone Have To Take Action

Knowing that it makes me to dive into the documentation that they have in order to develop local tools (and by local I mean that they run on your PC) and given by my nature, the tools that I may develop, their always be open source to give more room for improvement.

Gratefully, the blockchain API is based on JSON-RPC calls, which is a pretty good thing because the returned outcome is JSON based (text) and in most of the cases it's easier to manipulate.

Around this, I develop a small tool which hopefully, will scale to be a copy (at least in functionality) of the Hive Blocks web page, but for now, it just only displays parts of the "under the hood" contents of a user post.

## How It's Built & Works

It's built using `PyQt5` for the GUI and `jsonrpc_requests` library for handling requests to the API. I've found that using just the `requests` library give Windows some errors because of the `curl` version Windows have preinstalled, some issue with the double quotes when using Python. Using `jsonrpc_requests` you could run the same script on both Windows and Linux and have the same experience. I have not tested in MacOS, I does not have a Mac and I failed to install it in a virtual machine, but it must be identical, it is writen in Python.

The UI is very simplistic, you have your text input box and a button to trigger the function that does everything. The text you've input it's parsed and using `.split` string method to split it into username and permlink of the post, these two are saved into variables which are served as parameters for the API.

Then it uses the API method `bridge.get_post` along with the `username` and `permlink` variables mentioned previously to get the info of the post in JSON format, and then, we can get the required key values we want to display in the UI. Using labels and text boxes we can display the info of the given post. Text boxes are used in case we want to copy the info we are getting like in the case of the post's Tags.

## Repository

I have created a Github Repository where is hosted the sources of the project. Any issues or pull requests are very welcome. https://github.com/CesarPazzi/hive-block-explorer

## Known Issues

There's a lot to improve here but for now this project serves as a proof of concept for a tool that can have a great potential. 

- Some error that the tool have, is that, you need to input the correct string, starting after the @ in the URL, if it's different, the app will crash.
- It only uses one API server (`https://api.hive.blog`) and does not have a drop down menu to select your preferred API server.
- The UI does not stretch properly if it's maximized.
- It does not displays the votes, custom json, community, or replies (not yet implemented).

I will update this post when there's a major functionality or a fixed bug.

