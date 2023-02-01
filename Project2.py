#%%
import altair as alt
import pandas as pd
import numpy as np

#%%
url = 'https://raw.githubusercontent.com/byuidatascience/data4missing/master/data-raw/flights_missing/flights_missing.json'

data = pd.read_json(url)

#%%
data
# %%
question1 = (data
    .groupby(["airport_code"])
    .agg(
        tot_flights = ('num_of_flights_total', np.sum),
        tot_delays = ('num_of_delays_total', np.sum)
    )
    .assign(
        prop_delays = lambda df: df.tot_delays / df.tot_flights,
        prcnt_delays = lambda df: df.prop_delays * 100
    )
    .reset_index()
)

question1

# %%
alt.Chart(question1).mark_bar().encode(
    x = "airport_code",
    y = "prcnt_delays"
)
# %%
flights = data.query('month != "n/a"').replace("Febuary", "February")
flights.month.unique()
# %%
