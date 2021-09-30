'''
Module for handling the analysis and manipulation of the data sets.
'''
import pandas as pd


restaurants_df = pd.read_csv('Dashy/data/restaurants_zomato.csv',
                             encoding="ISO-8859-1")

# country iso with counts
country_vals = restaurants_df['country_code'].value_counts()
country_count_df = pd.DataFrame({
    'country_code': country_vals.index,
    'count': country_vals.values
})



# groupby country code/city and count rating:
resturant_votes_df = pd.DataFrame(
    restaurants_df.groupby('Restaurant Name')['Votes'].mean()
)
resturant_votes_df = resturant_votes_df.reset_index()
resturant_votes_df = resturant_votes_df.sort_values(['Votes'],
                                                    ascending=False)
top_ten_df = resturant_votes_df.head(10)



# pie chart - rating:
restaurant_vals = restaurants_df['Rating text'].value_counts()
restaurant_counts_df = pd.DataFrame({
    'Rating text': restaurant_vals.index,
    'Count': restaurant_vals.values
})