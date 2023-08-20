
def timeconverter (hour , minutes ,m):
    if m == "am" and hour == 12:
        hour = 0
    elif m == "pm" and hour !=12:
        hour +=12
    
    return f"{hour:02d}{minutes:02d}"
    
  