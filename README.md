# volviz
A Volatility Index Visualization Tool, very rudimentary

## Results
Since this was a very small research project, the resutls are as found below. These were generated on ``08 May 2020``.

### Front Side View
The frontside view is taking the angle of looking at the VIX Futures Calendar Curve which shows the spike in the March period. From left to right, you are looking further into the speculative future (seperated by contract months) while looking forward and back, you are looking at the observed traded prices (based on daily settlements).

![FrontsideVIX](https://i.imgur.com/hG6k18i.png)

### Back Side View
The backside view is the same as the frontside view except taking a look at the historical side, prior to the large hump from the March 2020 "CoronaCrash", in this picture, you are able to see the steap increase in volatility prior to an eventual bottom resulting in volatility decreasing as seen.

![BacksideVIX](https://i.imgur.com/hG6k18i.png)

### Birdseye View
Similar view, except from the top of the surface plot. This curve can be read using the color coded label for the data and shows a very simple view of the sharp increase with correlation to the speculative time dimension.

![BirdseyeVIX](https://i.imgur.com/NthQMVt.png)

### Single Dimensional View
This is the typical VIX chart that is seen, rather than using any camera angle on this curve at all, a very "straight" approach is taken on the curve which shows the changes in the VIX over time. However, this also shows the deviations between all calendar months as this event occured. For example, although all curves increased during the CoronaCrash where SPX touched the high 2100s, some calendars (propped further in the future) were lower than those closer (such as the May).

![SingleDimVIX](https://i.imgur.com/0k7V71U.png)