import datetime as dt

now = dt.datetime.now()  # [module datetime].[class datetime].[method now]

# Get seconds since 01-01-1970 UTC (Coordinated Universal Time)
seconds = now.timestamp()
print(
    f"Seconds since January 1, 1970: {seconds:,.4f} "
    f"or {seconds:.2e} in scientific notation"
)

# %b: abbreviated month, %d: day, %Y: full year
print(now.strftime("%b %d %Y"))
