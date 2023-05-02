# Lab 3

![instructions](https://github.com/jshepitka/cpe322/blob/main/Labs/Lab%203/Lab3InstructionsScreenshot.JPG)

[Kevin Lu - Internet of Things Repository](https://github.com/kevinwlu/iot)

```
$ pip install jdcal stral geopy
```

- ```$ cd *3``` while in iot directory goes to lesson3.

- ```$python julian.py``` returns the date normally and in 2 "julian" forms in the terminal.

- ```$python date_example.py``` returned more detailed date information in the terminal. 
- ```$python datetime_example.py``` returned the date and time down to decimals of a second. 
- ```$python time_example.py``` output ```Mon May  1 20:33:14 2023``` and continued to return the time every 10 seconds. ctrl + c used to exit.
- ```$python sun.py 'New York'``` did not run without the pytz library. after installing the library, the script returned:
```Timezone: US/Eastern
Latitude: 40.72; Longitude: -74.00

Dawn:    2023-05-01 05:24:54.490627-04:00
Sunrise: 2023-05-01 05:55:08.678720-04:00
Noon:    2023-05-01 12:53:11-04:00
Sunset:  2023-05-01 19:51:44.661736-04:00
Dusk:    2023-05-01 20:22:05.364214-04:00```
