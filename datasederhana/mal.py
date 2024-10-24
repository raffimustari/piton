import pandas as pd

anime_df = pd.read_csv(r'C:\Users\Lenovo\Documents\archive\anime.csv')
animelist_df = pd.read_csv(r'C:\Users\Lenovo\Documents\archive\animelist.csv')
anime_with_synopsis_df = pd.read_csv(r'C:\Users\Lenovo\Documents\archive\anime_with_synopsis.csv')
rating_complete_df = pd.read_csv(r'C:\Users\Lenovo\Documents\archive\rating_complete.csv')
watching_status_df = pd.read_csv(r'C:\Users\Lenovo\Documents\archive\watching_status.csv')

print("Animelist DataFrame:")
print(animelist_df.head()) 

print("\nAnime DataFrame:")
print(anime_df.head())

print("\nAnime with Synopsis DataFrame:")
print(anime_with_synopsis_df.head())

print("\nRating Complete DataFrame:")
print(rating_complete_df.head())

print("\nWatching Status DataFrame:")
print(watching_status_df.head())
