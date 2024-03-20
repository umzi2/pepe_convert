# Quck start:
Откройте cmd или любой другой терминал:
```
git clone https://github.com/umzi2/pepe_convert.git
cd pepe_convert
pip install -r requirements.txt
```
Теперь об аргументах
```
python pepe_convert.py -h
python pepe_convert.py -i in/48 -o out -f png
```
-h - краткое описание аргументов
-i - директория с вашими изображениями
-o - папка куда сохранятся файлы, если этой папки нет, он её создаст
-f - формат в который конвертируем, если не указать сконвертирует в пнг.


Теперь о скорости: 

Датасет из 38 psd файлов общим весом в гигабайт, каждое изображение примерно 6кХ8к сконвертировался за 2 секунды на ryzen 7 2700

Тот же объём через [image-util](https://github.com/sekiju/image-utils) который написан секиджу на го ленг, занял 45 секунд.

И вот самое обидное для меня, пока что максимальный размер псд который он конвертирует 16к+- по высоте или ширене. Т.е максимум 16кХ16к