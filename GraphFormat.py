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


def dateGraphMajorTicksCalculation(axes):
    lowXlim, highXlim = axes.get_xlim()
    width = highXlim - lowXlim

    # Calculate the major ticks requirement
    if(width < 0.000694*2):
        reformatMajorTicks(
            axes, "%M:%S", "Second", [0, 15, 30, 45])
    elif(width < 0.041*2):
        reformatMajorTicks(
            axes, "%H:%M", "Minute", [0, 15, 30, 45])
    elif(width < 0.041*6):
        reformatMajorTicks(
            axes, "%H:%M", "Hour", range(24))
    elif(width < 0.041*12):
        reformatMajorTicks(
            axes, "%H:%M", "Hour", [0, 3, 6, 9, 12, 15, 18, 21])
    elif(width < 1.5):
        reformatMajorTicks(
            axes, "%d/%m, %H:%M", "Hour", [0, 6, 12, 18])
    else:
        reformatMajorTicks(
            axes, "%d/%m", "Day", range(31))
# End of dateGraphMajorTicksCalculation


def repaintMajorTicks(axes, ls='--', color='black', lw=0.25):
    for xmaj in axes.lines:
        xmaj.remove()
    for xmaj in axes.xaxis.get_majorticklocs():
        axes.axvline(
            x=xmaj, ls=ls, color=color, lw=lw)
# End of repaintMajorTicks


def clearAndResetGraph(axes, figure):
    axes.clear()
    axes.remove()
    figure.clear()
    axes = figure.add_subplot(111)
# End of clearAndResetGraph
