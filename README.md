# search-weather
1.首先从https://cdn.heweather.com/china-city-list.csv下载城市对应的代码csv文件
2.data.py从csv文件中提取需要的城市名和对应的城市代码，形成city_code.txt
3.query.py文件中的read_code()函数实现城市名城市代码字典的构建，query_code()函数根据城市名查询城市代码，query_weather()根据城市代码查询该城市的天气
（http://wthrcdn.etouch.cn/weather_mini?citykey+'城市代码'）即可返回该城市的天气信息
4.返回字典数据，在前端页面展示
