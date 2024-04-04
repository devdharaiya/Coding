import pandas as pd
import plotly.express as px

crypto_df = pd.read_csv('/workspaces/Coding/Plotly/crypto_prices.csv')
fig = px.line()

for i in crypto_df.columns[1:]:
    fig.add_scatter(x = crypto_df['Date'], y = crypto_df[i], name = i)
fig.show()