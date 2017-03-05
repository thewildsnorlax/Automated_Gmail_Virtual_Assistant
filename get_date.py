from datetime import date, timedelta

date = date.today()

cd = date.day
cm = date.month
cy = date.year

yesterday = date.today() - timedelta(1)

yd = yesterday.day
ym = yesterday.month
yy = yesterday.year

yester = str(yy) + '/' + str(ym) + '/' + str(yd)
today = str(cy) + '/' + str(cm) + '/' + str(cd)

