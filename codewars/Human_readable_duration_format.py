from math import fabs

from dateutil.relativedelta import relativedelta


def format_duration(seconds):
    res = ""
    if int(seconds) == 0:
        return "now"
    else:
        attrs = ['days', 'hours', 'minutes', 'seconds']
        human_readable = lambda delta: [
            '%d %s' % (getattr(delta, attr), getattr(delta, attr) > 1 and attr or attr[:-1])
            for attr in attrs if getattr(delta, attr)
        ]
        result = (human_readable(relativedelta(seconds=seconds)))

        if len(result) == 2:
            for i in result[:-1]:
                res += i + " "
            res += "and " + result[-1]
            return res
        elif len(result) > 2:
            for i in result[:-1]:
                res += i + ", "
            res += "and " + result[-1]

            if "days" in res:
                last = res.replace(", and ", " and ")
                last2 = last.split(" days,")
                if int(last2[0]) > 365:
                    a = int(int(last2[0]) / 365)
                    b = a * 365
                    c = int(last2[0]) - b
                    if int(a) == 1:
                        return str(a) + " year, " + str(int(fabs(int(c * -1)))) + " days," + str(last2[1])
                    else:
                        return str(a) + " years, " + str(int(fabs(int(c * -1)))) + " days," + str(last2[1])
            return res.replace(", and ", " and ")
        else:
            return result[0]


"""
another solution
"""

# import re
# def format_duration(seconds):
#     if not seconds: return 'now'
#     minutes = seconds / 60
#     seconds %= 60
#     hours = minutes / 60
#     minutes %= 60
#     days = hours / 24
#     hours %= 24
#     years = days / 365
#     days %= 365
#     a = []
#     for n, l in zip([years, days, hours, minutes, seconds], ['year', 'day', 'hour', 'minute', 'second']):
#         if n == 1:
#             a.append('%d %s' % (n, l))
#         elif n > 1:
#             a.append('%d %ss' % (n, l))
#     return re.sub(r', ([^,]*)$', lambda o: ' and ' + o.group(1), ', '.join(a))


# def format_duration(s):
#     dt = []
#     for b, w in [(60, 'second'), (60, 'minute'), (24, 'hour'), (365, 'day'), (s+1, 'year')]:
#         s, m = divmod(s, b)
#         if m: dt.append('%d %s%s' % (m, w, 's' * (m > 1)))
#     return ' and '.join(', '.join(dt[::-1]).rsplit(', ', 1)) or 'now'

# def format_duration(seconds):
#     if not seconds:
#         return 'now'
#     mm, ss = divmod(seconds, 60)
#     hh, mm = divmod(mm, 60)
#     dd, hh = divmod(hh, 24)
#     yy, dd = divmod(dd, 365)
#     units = [(yy, 'year'), (dd, 'day'), (hh, 'hour'), (mm, 'minute'), (ss, 'second')]
#     duration = [
#         f'{unit[0]} {unit[1]}{"s" if unit[0] > 1 else ""}'
#         for unit in units if unit[0]
#     ]
#
#     return ' and'.join(', '.join(duration).rsplit(',', 1))


# def format_duration(seconds):
#     if (seconds == 0): return 'now'
#
#     time = OrderedDict()
#
#     time['years'] = seconds // 31536000
#     time['days'] = seconds // 86400 % 365
#     time['hours'] = seconds // 3600 % 24
#     time['minutes'] = seconds // 60 % 60
#     time['seconds'] = seconds % 60
#
#     output = []
#
#     for key in time:
#         if (time[key] > 1):
#             output.append(str(time[key]) + ' ' + key)
#         elif (time[key] == 1):
#             output.append(str(time[key]) + ' ' + key[:-1])
#
#     print(output)
#
#     return ", ".join(output[:-2] + [" and ".join(output[-2:])])
