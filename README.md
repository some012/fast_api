Как запустить через Docker

1. Установка [docker-a](https://docs.docker.com/engine/install/)
2. docker build -t small_fast_api_app:v1 . - Собрать контейнер
3. docker run -p 9000:9000 small_fast_api_app:v1 - Запустить контейнер
4. 192.168.99.101:9000 - По этому адресу зайти в браузер 
