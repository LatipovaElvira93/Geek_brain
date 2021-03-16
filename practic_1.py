s = int(input("enter = "))

if s < 60:
    print(s, "sec")

elif s < 3600:
    m = s // 60
    sec = s % 60
    print(s, " sec = ", m, "min", sec, "sec")

elif s < 86400:
    h = s // 3600
    m = (s % 3600) // 60
    sec = (s % 3600) % 60
    print(s, " sec = ", h, "hours", m, "min", sec, "sec" )

elif s < 2629743:
    d = s // 86400
    h = (s % 86400) // 3600
    m = ((s % 86400) % 3600) // 60
    sec = ((s % 86400) % 3600) % 60
    print(s, " sec = ", d, "day", h, "hours", m, "min", sec, "sec" )

elif s < 31556926:
    month = s // 2629743
    d = (s % 2629743) // 86400
    h = ((s % 2629743) % 86400) // 3600
    m = (((s % 2629743) % 86400) % 3600) // 60
    sec = (((s % 2629743) % 86400) % 3600) % 60
    print(s, " sec = ", month, "month", d, "day", h, "hours", m, "min", sec, "sec" )

elif s >= 31556926:
    y = s // 31556926
    month = (s % 31556926) // 2629743
    d = ((s % 31556926) % 2629743) // 86400
    h = (((s % 31556926) % 2629743) % 86400) // 3600
    m = ((((s % 31556926) % 2629743) % 86400) % 3600) // 60
    sec = ((((s % 31556926) % 2629743) % 86400) % 3600) % 60
    print(s, " sec = ", y, "year", month, "month", d, "day", h, "hours", m, "min", sec, "sec")