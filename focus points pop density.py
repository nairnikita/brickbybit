import pandas as pd
from scipy.spatial import cKDTree

df = pd.read_csv("C:/Users/nikit/Downloads/are_general_2020.csv") 
areas = [
    ("Al Quoz Industrial Area (DUBAI)", 25.129592421893612, 55.2149674236469),
    ("Al Musaffah (ABU DHABI)", 24.362453165958904, 54.48312869748285),
    ("Al Karama (DUBAI)", 25.246843275719176, 55.304785932364894),
    ("Al Nuaimia (AJMAN)", 25.38541160535403, 55.45716045319643),
    ("Al Salamah (UMM AL QUWAIN)", 25.47920489022441, 55.587846757747506),
    ("Al Hail (FUJAIRAH)", 25.11569934008603, 56.26940532712436),
    ("Al Nakheel (RAS AL KHAIMAH)", 25.802349918186287, 55.962191868198666),
    ("International City (DUBAI)", 25.168125488770244, 55.40559736485907),
    ("Khalifa City A (ABU DHABI)", 24.424739990639065, 54.52647562221691),
    ("Industrial Area 10 (SHARJAH)", 25.302870077935477, 55.4172061141615)
]

tree = cKDTree(df[['latitude', 'longitude']].values)

results = []
for name, lat, lon in areas:
    distance, index = tree.query([lat, lon], k=1)
    closest_point = df.iloc[index]
    results.append({
        "Area": name,
        "Query_Latitude": lat,
        "Query_Longitude": lon,
        "Closest_Latitude": closest_point['latitude'],
        "Closest_Longitude": closest_point['longitude'],
        "Population_Density": closest_point['are_general_2020']
    })

results_df = pd.DataFrame(results)

results_df.to_csv("nearest_population_density.csv", index=False)

print("Done! Results saved to nearest_population_density.csv")
print(results_df)
