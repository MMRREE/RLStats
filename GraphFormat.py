# Graph formatting for repeated tasks
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def reformatMajorTicks(axes, dateFormat="%H:%M", locatorFrame="Hour", byperiod=[0, 6, 12, 18]):
    formatter = mdates.DateFormatter(dateFormat)
    axes.get_xaxis().set_major_formatter(formatter)
    locator = None
    if(locatorFrame == "Day"):
        locator = mdates.DayLocator(bymonthday=byperiod)
    elif(locatorFrame == "Hour"):
        locator = mdates.HourLocator(byhour=byperiod)
    elif(locatorFrame == "Minute"):
        locator = mdates.MinuteLocator(byminute=byperiod)
    elif(locatorFrame == "Second"):
        locator = mdates.SecondLocator(bysecond=byperiod)
    else:
        locator = mdates.DayLocator(bymonthday=byperiod)
    axes.get_xaxis().set_major_locator(locator)
# End of reformatMajorTicks


def repaintMajorTicks(axes, ls='--', color='black', lw=0.25):
    for xmaj in axes.lines:
        xmaj.remove()
    for xmaj in axes.xaxis.get_majorticklocs():
        axes.axvline(
            x=xmaj, ls=ls, color=color, lw=lw)
# End of repaintMajorTicks
