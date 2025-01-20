from fredapi import Fred
fred = Fred(api_key=api_key)
series_ids = {
    "Treasury Securities": "TREAST", 
    "Loans": "WLCFLL",
    "Reserve Balances with Fed": "WRBWFRBL",
    "Deposits with F.R Bank": "WDTGAL",
    "Reverse Repurchase Agreements": "WLRRAL"
}

dataframes = {}
for label, series_id in series_ids.items():
    dataframes[label] = fred.get_series(series_id)

df = pd.DataFrame(dataframes)
df
