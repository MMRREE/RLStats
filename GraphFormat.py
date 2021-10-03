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


def dateGraphMajorTicksCalculation(axes):
    lowXlim, highXlim = axes.get_xlim()
    width = highXlim - lowXlim

    if(width < 0.000694*2):
        reformatMajorTicks(
            axes, "%H:%M:%S", "Second", range(0, 60, 15))
    elif(width < 0.000694*15):
        reformatMajorTicks(axes, "%H:%M:%S", "Minute", range(0, 60, 1))
    elif(width < 0.000694*60):
        reformatMajorTicks(axes, "%H:%M:%S", "Minute", range(0, 60, 5))
    elif(width < 0.041*2):
        reformatMajorTicks(
            axes, "%H:%M", "Minute", range(0, 60, 15))
    elif(width < 0.041*6):
        reformatMajorTicks(
            axes, "%H:%M", "Hour", range(0, 24, 1))
    elif(width < 0.041*12):
        reformatMajorTicks(
            axes, "%H:%M", "Hour", range(0, 24, 3))
    elif(width < 1.5):
        reformatMajorTicks(
            axes, "%d/%m, %H:%M", "Hour", range(0, 24, 6))
    else:
        reformatMajorTicks(
            axes, "%d/%m/%Y", "Day", range(0, 31, 1))
    repaintMajorTicks(axes)
# End of dateGraphMajorTicksCalculation


def repaintMajorTicks(axes, ls='--', color='black', lw=0.25):
    for xmaj in axes.lines:
        xmaj.remove()
    for xmaj in axes.xaxis.get_majorticklocs():
        axes.axvline(
            x=xmaj, ls=ls, color=color, lw=lw)
    axes.axhline(y=0, ls=ls, color=color, lw=lw)
# End of repaintMajorTicks
