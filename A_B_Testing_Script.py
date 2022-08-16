import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
##Analyzing Ad Sources

#Examining the first few rows of ad_clicks.

print(ad_clicks.head())

#Which ad platform is getting the most views?

print(ad_clicks.groupby("utm_source").user_id.count().reset_index())

#Which ad was clicked on?
ad_clicks["is_click"] =~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head())

#The percent of people who clicked on ads from each utm_source.
#Grouping by utm_source and is_click and counting the number of user_id.
clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"]).user_id.count().reset_index()

#Pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id.

click_pivot = clicks_by_source.pivot(index='utm_source', columns='is_click', values='user_id').reset_index()

click_pivot["percet_clicked"] = click_pivot[True]/(click_pivot[True]+click_pivot[False])

##Analyzing an A/B Test

#Were approximately the same number of people shown both ads?
print(ad_clicks.groupby("experimental_group").user_id.count().reset_index())

#Checking to see if a greater percentage of users clicked on Ad A or Ad B.
A_B = ad_clicks.groupby(["experimental_group", "is_click"]).user_id.count().reset_index()

clicks_by_A_B = A_B.pivot(index='experimental_group', columns='is_click', values='user_id').reset_index()

clicks_by_A_B["percet_clicked"] = clicks_by_A_B[True]/(clicks_by_A_B[True]+clicks_by_A_B[False])

print(clicks_by_A_B.head())

#The Product Manager for the A/B test thinks that the clicks might have changed by day of the week!!

#Calculate the percent of users who clicked on the ad by day For each group (a_clicks and b_clicks)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

A = a_clicks.groupby(["day", "is_click"]).user_id.count().reset_index()

A_pivot = A.pivot(index='day', columns='is_click', values='user_id').reset_index()

A_pivot["percet_clicked"] = A_pivot[True]/(A_pivot[True]+A_pivot[False])

print(A_pivot)

B = b_clicks.groupby(["day", "is_click"]).user_id.count().reset_index()

B_pivot = B.pivot(index='day', columns='is_click', values='user_id').reset_index()

B_pivot["percet_clicked"] = B_pivot[True]/(B_pivot[True]+B_pivot[False])

print(B_pivot)

#It seems that the clicks on the Ad A is more important during the whole week in comparison to the Ad B, Thus I would recommend Using the Ad A version as The ROI for the company would be positive.
#RdEl00
