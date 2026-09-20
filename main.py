import pandas as pd

# input
df = pd.read_csv("spotify_artist_streaming_2020_2025.csv",encoding="utf-8")
print(f"INFO:\nColums&Rows: {df.shape}\nStat:\n{df.dtypes}\n-------------------")

# топ 5 жанров
df_genres = df["genre"]
print(f"Топ 5 жанров по количеству треков:\n{df_genres.value_counts().head()}\n-------------------")

# топ 5 стран
df_countries = df["country"]
print(f"Топ 5 стран по количеству треков:\n{df_countries.value_counts().head()}\n-------------------")

# describe() по stream_count
print(f"Статистика stream_count:\n{df["stream_count"].describe()}\n-------------------")

# процент explicit-треков от общего числа
df_explicit = df["explicit"]
explicit = df_explicit.value_counts()
exp = (explicit[True])
print(f"Процент explicit-треков: {exp / (exp + (explicit[False])) * 100}\n-------------------")

# треки: жанр "Pop", stream_count > 300000, explicit == False — сколько их
df_pop = df[["track_name","artist_name","genre","stream_count","explicit"]]
df_pop_cur = df_pop[(df_pop["genre"] == "Pop") & (df_pop["stream_count"] > 300000) & (df_pop["explicit"] == False)]
print(f"Количество треков с параметрами: жанр Pop, stream_count > 300000, explicit == False : {df_pop_cur["genre"].count()}\n-------------------")

# вывести track_name, artist_name, stream_count по этой выборке, отсортировать по stream_count по убыванию
df_pop_sort = df_pop_cur.sort_values(["stream_count"],ascending=False)
print(f"track_name, artist_name, stream_count, stream_count по убыванию по предыдущей выборке:\n{df_pop_sort[["track_name","artist_name","stream_count"]]}\n-------------------")

# треки, где track_name начинается на "S" — сколько их
sr_track_name = df["track_name"]
print(f"Количество треков, начинающихся на S: {sr_track_name.str.startswith("S").sum()}\n-------------------")

# разделить на "короткие" (duration_minutes < 3) и "длинные" (duration_minutes > 5)
short_duration = df[df["duration_minutes"] < 3]
long_duration = df[df["duration_minutes"] > 5]

# describe() по stream_count для каждой группы, сравнить медианы
print(short_duration["stream_count"].describe())
print(f"{long_duration["stream_count"].describe()}\n-------------------")

# посчитать количество треков в каждой группе
print(f"Количество треков, короче 3х минут: {short_duration["stream_count"].count()}")
print(f"Количество треков, длиннее 5и минут: {long_duration["stream_count"].count()}\n-------------------")

# треки, выпущенные в 2020 году, январь-март
df["release_date"] = pd.to_datetime(df["release_date"])
df_2020 = df[(df["release_date"] >= "2020-01-01") & (df["release_date"] <= "2020-03-31")]
print(f"Треки, выпушенные между январем и февралем 2020 года:\n {df_2020[["track_name","release_date"]]}\n-------------------")

# трек с максимальным stream_count в этой подвыборке
max_id = df_2020["stream_count"].idxmax()
print(f"Трек с максимальным количеством прослушиваний в этой выборке: \n{df_2020.loc[max_id,["track_name"]]}\n-------------------")

# разница в днях между самым ранним и самым поздним release_date во всём датасете
df_max_date = df["release_date"].idxmax()
df_min_date = df["release_date"].idxmin()
print(f"Самый поздний выпущенный трек: \n{df.loc[df_max_date,["track_name"]]}\n-------------------")
print(f"Самый ранний выпущенный трек: \n{df.loc[df_min_date,["track_name"]]}\n-------------------")
print(f"Разница в днях: {df["release_date"].max()-df["release_date"].min()}")