from scraper import *

names = get_open_restaurants()
prices = get_open_price_points()
locations = get_open_locations()

data = np.array((names,prices,locations)).T
df = pd.DataFrame(data, columns=["name","price","location"])



