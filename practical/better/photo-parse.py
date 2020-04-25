from datetime import datetime
from collections import defaultdict

class PhotoInfo:
    def __init__(self, info: str, id: int):
        info_list = info.split(', ')
        [self.name, self.type] = info_list[0].split('.')
        self.location = info_list[1]
        self.datetime = datetime.strptime(info_list[2], '%Y-%m-%d %H:%M:%S')
        self.id = id
        self.group_id = -1

    def __lt__(self, other):
        return self.datetime < other.datetime

def parse_info(input):
    loc_map = defaultdict(list)
    for id, info_str in enumerate(input):
        photo = PhotoInfo(info_str, id+1)
        loc_map[photo.location].append(photo)

    res = [''] * len(input)
    for val in loc_map.values():
        val.sort()
        count = len(val)
        count_len = 0
        while count:
            count //= 10
            count_len += 1
        for idx, item in enumerate(val):
            group_id = str(idx+1).zfill(count_len)
            res[item.id-1] = item.location+group_id+'.'+item.type

    print(res)




input = [
    'photo.jpg, Warsaw, 2013-09-05 14:08:15',
    'john.png, London, 2015-06-20 15:13:22',
    'myFriends.png, Warsaw, 2013-09-05 14:07:13',
    'Eiffel.jpg, Paris, 2015-07-23 08:03:02',
    'pisatower.jpg, Paris, 2015-07-22 23:59:59',
    'BOB.jpg, London, 2015-08-05 00:02:03',
    'notredame.png, Paris, 2015-09-01 12:00:00',
    'me.jpg, Warsaw, 2013-09-06 15:40:22',
    'a.jpg, Warsaw, 2016-02-13 13:33:50',
    'b.jpg, Warsaw, 2016-01-02 15:12:22',
    'c.jpg, Warsaw, 2016-01-02 14:34:30',
    'd.jpg, Warsaw, 2016-01-02 15:15:01',
    'e.jpg, Warsaw, 2016-01-02 09:49:09',
    'f.jpg, Warsaw, 2016-01-02 10:55:32',
    'g.jpg, Warsaw, 2016-02-29 22:13:11',
]

parse_info(input)