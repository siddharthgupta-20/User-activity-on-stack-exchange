
User Activity on Stack Exchange

====================================================================================================================================================

VIEWCOUONT DISTRIBUTION
->in the mapper file, we have extracted all the tags with RegEx for each row and then retun the output as (tag,1)
->in the reducer file, we just have to count the number of tags for each and return the output

POPULARITY_OF_TAGS
->We needed to find the top 10 posts in terms of view count so,
   in the mapper we extracted the ViewCount,Id, OwnerUserId for each post and then returned a top 10 list of the given input posts
   Since running the code on shell no parallel processing can be done hence only mapper will give the top 10 viewed posts alog with the OwnerUserId and Id.

POSTS_PER_HOUR
->in the mapper file, we have extracted the  time(only hours) of the post with RegEx for each row and then retun the output as (hour,1)
->in the reducer file, we just have to coount the number of posts for a particular hour and return the output

00      1564
01      1435
02      1364
03      1346
04      1411
05      1751
06      2447
07      2836
08      3145
09      3541
10      3505
11      3281
12      3480
13      3726
14      3909
15      3916
16      3593
17      3456
18      3016
19      2983
20      2761
21      2537
22      2108
23      1738
this was the output of the reducer

COMMENT DISTRIBUTION
->in the mapper we extracted the month and the year of the comment and also the text by RegEx and return the output as (month,length(text))
  in the reducer, for a  particular month we collected all the comment length and the found the median using sorting and applying the formula.
->And then we returned the output of the reducer as (month,number of comments,median for that particular month)
	