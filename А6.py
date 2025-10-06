N = int(input("Введите количество секунд: "))

hours = N // 3600
minutes = (N % 3600) // 60
seconds = N % 60

print(f"{N} секунд → {hours}:{minutes:02}:{seconds:02}")