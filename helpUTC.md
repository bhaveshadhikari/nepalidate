### Helpful UTC and date library
---
UTC date: [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/UTC]

### JavaScript
`date.UTC(year, monthIndex, day + X)`
- year : number representing year. example: 2020,2021.. 
- monthIndex : 0 - 11 ( Jan - Dec )
- day : defaults to 1. i_th day
- X : offset days
Get WeekDay

`new Date(Date.UTC(1943, 3, 14)).toUTCString()`

### Python
```
from datetime import date, timedelta

d = date(1943, 1, 14) + timedelta(days=15)

print(d.isoformat(), d.strftime("%A"))



d1 = date(1943, 1, 14)
d2 = date(1943, 1, 29)

difference = d2 - d1
print(difference.days)
```