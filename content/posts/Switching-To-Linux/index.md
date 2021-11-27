---
title: "My Transition To Linux... Again"
subtitle: "If it only it was easier"
date: 2021-11-28T18:17:37-06:00
lastmod: 2021-11-28T18:17:37-06:00
draft: false
authors: []
description: "I was having issues with Windows involving running my Python Scripts, Tkinter and PyQt based scripts didn't run at all, adding that and the constant freezes make me consider returning to Linux after 10+ years."

tags: ["Blog", "Linux"]
categories: []

hiddenFromHomePage: false
hiddenFromSearch: false

featuredImage: "linux-transition-cover.jpg"
featuredImagePreview: "linux-transition-cover.jpg"

toc:
  enable: true
math:
  enable: false
lightgallery: false

license: ""
---

<!--more-->

## The Issue

A couple of months ago, I was having some issues dealing with Windows 10. PyQt and Tkinter (Python packages) didn't want to work on my machine and I really want an excuse to switch to Linux because, having Linux as a skill in your resume is a plus and definitely is my main goal if I really want to specialize in development. 

## In Seach For The Right Distro

So I give it a try and look on DistroWatch the most popular Linux distros, and found that MX Linux was at the top, followed by EndeavourOS. MX Linux is Debian based and EndeavourOS is Arch based, in the past (more than 10 years ago) I used Ubuntu and Mint which are both based on Debian and I wanted to "experience" another flavor of Linux, so I ended installing EndeavourOS and I have to say that for my rusty skills, it was not bad at all, compared with the stories you probably read on the Internet of the infamous Arch distro, that you must install and configure everything from the audio drivers to the display server, the distro was basically just click this and that, no command line was needed.

## An Embarrassing Mess

At first I configure it with XFCE but shortly after messing the whole system, after I install Python 3.10, (yeah I install Python 3.10 along with Python 2 and 3.9 that came with the system out of the box, and the aliases where messed, no PIP was installed, some packages were not supported on 3.10 and there was not yet support for 3.10 on the official repos or the AUR, I had to installed it from source and that mess the system to the point I was having startup errors or Gnome Tweaks not running among other issues, and yes, at this time I already installed the OS for the second time) I had to reinstall for the third time the distro.

It's been a challenge to getting back of using the command line after 10 years or so of using Windows, but there's nothing I wouldn't be able to do, except for the installation of VS code right of the box (had to install it via Flatpak) but the instructions on the website were straight forward.

## But Is Not Over

After installing the apps for working and theming the DE it will never stops there because most of the times the apps you want to install are not available for Arch based distros and have to follow the steps on the app's website, when available, that's what it bothers me a lot, there's no a straight forward way to install apps (and update them) on all distros as a standard, `apt-get` on Debian based, `rpm` on Fedora/RHEL based and `pacman` on Arch based are different package managers that in some way or another do the same thing which is installing a package (application), why not coordinate for making a Linux Universal package manager?

I will wrap up this post here and continue another day with my little developer adventures.
