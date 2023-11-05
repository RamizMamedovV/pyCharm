
def find_farthest_orbit(data: list) -> list:
    orbit = list(filter(lambda x: x[0] != x[1], data))
    print(f"orbit = {orbit}")
    return max(orbit, key=lambda x: x[0] * x[1] * 3.14)
    # max_o = 0
    # max_list = [0, 0]
    # for i in data:
    #     s = i[0] * i[1] * 3.14
    #     print(s)
    #     if s > max_o:
    #         max_list[0] = i[0]
    #         max_list[1] = i[1]
    #         max_o = s
    # return max_list


orbits = [(1, 3), (2.5, 10), (6, 6), (7, 2), (4, 3)]
print(f"farthest orbit {find_farthest_orbit(orbits)}")
