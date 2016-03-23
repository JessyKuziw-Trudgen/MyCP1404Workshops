def main():
    print('Area calculator')
    width = float(input('enter width:'))
    height = float(input('enter height:'))
    depth = float(input('enter depth:'))

    area = calc_area(width, height)

    volume = area * depth

    print(width, height, area, volume)


def calc_area(width, height):
    area = width * height
    return area
