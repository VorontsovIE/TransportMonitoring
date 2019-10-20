#!/usr/bin/env python3

"""
Gett
"""

# from YandexTransportWebdriverAPI import YandexTransportProxy
from yandex_transport_webdriver_api import *

if __name__ == '__main__':
    # Route  : Tram "A", Moscow
    # Маршрут: Трамвай "А", Москва
    url = 'https://yandex.ru/maps/213/moscow/?ll=37.670196%2C55.730905&' \
          'masstransit[lineId]=213_A_tramway_mosgortrans&' \
          'masstransit[stopId]=stop__9645568&' \
          'masstransit[threadId]=2036927519&' \
          'mode=stop&z=13'
    print('Counting trams on route "A"...')
    proxy = YandexTransportProxy('127.0.0.1', 25555)
    vehicles_data = proxy.get_vehicles_info_with_region(url)
    vehicles_count = proxy.count_vehicles_on_route(vehicles_data)
    print('Number of trams on route "A" right now is ' + str(vehicles_count) + '.')
