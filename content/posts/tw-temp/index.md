---
title: "tw-temp"
date: 2021-07-06
draft: False

tags: ["Python"]
categories: ["Projects"]

featuredImage: "tw-temp-cover.jpg"
featuredImagePreview: "tw-temp-cover.jpg"

toc:
  enable: true
---

## Preamble

This is my very first Python project that I published on my GitHub. I use it as a way to practice Python programming because I think is one of the easiest projects to start with programming and, it have the potential of scaling the more you add things to it.

Previously I used Twitter + IFTTT to get the weather info and tweet it every hour with the hashtag of the city I live in. But IFTTT changed it's services and now only allows 24 tweets per day and sometimes less than that so I decided to leave IFTTT and build my own tweeting weather station (which is still in progress) using Python and GitHub Actions, that for now, are not real limits on them.

## Functionality

Tw-temp is a Twitter bot that uses Beautiful Soup for scrapping the temperature data from Yahoo Weather page (not using Yahoo's API) from a specific city. Then, using Twython module for handling Twitter's API calls, it tweets the temperature in Celsius degrees every hour using GitHub Actions.

## Repository

The repository of the source code is hosted on GitHub, from there you can follow the documentation for setting your own Twitter bot:

https://github.com/CesarPazzi/tw-temp

## Improvements And Scalability Of The Project

### Improvements

Certainly, this isn't the end of the development of the project, there's a lot of work to do. 

First, The Code. Although is functional, is very simple and I think it have plenty of room for improvement.

Second, The Sources. Scrapping weather data may is not be the best way. I first think in web scrapping because weather APIs have a quota of how many calls you can do in a certain period of time and web scrapping don't have those limitations. 

Third, Reliability. In case something fail, there is no way to know what fails, there's no other chance to try to execute again, and the script have to wait another hour to try again and hopes to everything works fine.

### Scalability

I have some points on how to scale the functionality. 

* Gather more data: humidity, precipitation (if any), wind and pressure.
* Integration with Hugo (Static Site Generator) for publishing the historic weather data for consulting and reference, making it open in comparison with some weather API services.
* Automatic graphs in a weekly, monthly and yearly basis for better visualization.

## Demo

I set up a Twitter account specifically for demonstration.

https://twitter.com/climaenreynosa

The setup is currently set on the city I live.