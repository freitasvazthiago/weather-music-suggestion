# About

This app is makin for search a city and suggest songs by the temperature.

## Installation

**Clone** this repo.  
Make sure that u are at docker-compose file root path  
Run

```bash
docker-compose up -d
```
or

```bash
docker-compose up 
```

**docker-compose up** have a log on terminal if u wish for.

## Usage

availables url's

* http://0.0.0.0:8000/swagger/
* http://0.0.0.0:8000/weather/{city_name}
* http://0.0.0.0:8000/statistic/

As **weather** and **statistic** using as end-point purpose

## Online API

Deployed by **Heroku**

* https://weather-music-suggestion.herokuapp.com/swagger/
* https://weather-music-suggestion.herokuapp.com/weather/{city_name}
* https://weather-music-suggestion.herokuapp.com/statistic/

## Unit Tests

Make sure that u are at docker-compose file root path  
Run

```bash
docker-compose exec web bash
```
To enter at bash of web container

```bash
python3 manage.py test
```
For get asserts results.
