import pandas as pd

path = "taxi_peru.csv"
taxi = pd.read_csv(path, sep=';', parse_dates=["start_at", "end_at", "arrived_at"])
print(taxi.shape, '\n', taxi.dtypes, '\n', taxi.head())

# journey_id – уникальный id поездки
# user_id – id пользователя
# driver_id – id водителя
# taxi_id – id машины
# icon – тип поездки (executive, group, easy - исполнительный, группа, легкий)
# start_type – тип заказа (asap, reserved, delayed)
#                         (как можно скорее, зарезервировано, с задержкой)
# start_at – время начала поездки
# start_lat – исходное местоположение пользователя, широта
# start_lon – исходное местоположение пользователя, долгота
# end_at – время окончания поездки
# end_lat – итоговое местоположение, широта
# end_lon – итоговое местоположение, долгота
# end_state – состояние заказа
# driver_start_lat – исходное местоположение водителя, широта
# driver_start_lon – исходное местоположение водителя, долгота
# arrived_at – время прибытия водителя
# source – платформа, с которой сделан заказ
# driver_score – оценка водителя клиентом
# rider_score – оценка клиента водителем

# С какой платформы было сделано больше всего заказов. В ответе значения в %,
# округлённое до целого
taxi_source1 = taxi.source.value_counts()
taxi_source2 = (taxi.source.value_counts() / len(taxi) * 100).round(0)
print("\n", taxi_source1, '\n', taxi_source2)

# количество типов поездок
taxi_icon = taxi.icon.value_counts()
print(taxi_icon)

# итоговое состояние заказов в разбивке по количеству и платформам (source)
taxi['name_end_state'] = taxi.end_state
taxi_end_state = taxi \
    .groupby(["source", "name_end_state"], as_index=False) \
    .agg({"end_state": "count", 'name_end_state': pd.Series.unique}) \
    .sort_values(by=["source", "end_state"], ascending=False)
print("\n", taxi_end_state)

# частота встречаемости каждой из оценок (driver_score)(оценки водителей клиентами)
scores = taxi.driver_score.value_counts(normalize=True).mul(100).round(2)
print("\n",scores)
scores = scores.reset_index()
print("\n", scores)
driver_score_counts = scores.sort_values("proportion")
print("\n", driver_score_counts)

# частота встречаемости каждой из оценок (rider_score)(оценок клиентов водителями)
scores = taxi.rider_score.value_counts(normalize=True).mul(100).round(2)
print("\n",scores)
scores = scores.reset_index()
print("\n", scores)
rider_score_counts = scores.sort_values("proportion")
print("\n", rider_score_counts)
