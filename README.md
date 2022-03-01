# Backend Tech Lead Challenge

## Problema
En Houm tenemos un gran equipo de Houmers que muestran las propiedades y solucionan todos los problemas que podrían ocurrir en ellas. Ellos son parte fundamental de nuestra operación y de la experiencia que tienen nuestros clientes. Es por esta razón que queremos incorporar ciertas métricas para monitorear cómo operan, mejorar la calidad de servicio y para asegurar la seguridad de nuestros Houmers.

## Requisitos
Crear un servicio REST que:

- Permita que la aplicación móvil mande las coordenadas del Houmer
- Para un día retorne todas las coordenadas de las propiedades que visitó y cuanto tiempo se quedó en cada una
- Para un día retorne todos los momentos en que el houmer se trasladó con una velocidad superior a cierto parámetro

## Supuestos

- Se basa en que el Houmer se encarga de guiar en el dia al cliente a visitar las diferentes casas para su alquiler y venta.
- Cada visita dura dependiente del cliente para la revisión de la propiedad.
- El Houmer debe registrar mediante el servicio cuando ingresa la propiedad, tambien debe actualizar la salida de la propiedad, en caso no se actualice se realiza el registro de la hora de salida resultado de hora de ingresa + 1h.
- Al realizar actualización de la salida de propiedad se actualiza el tiempo total que estuvo el cliente en la propiedad.
- Cuando ingresa una nueva dirección de la propiedad en el servicio se realiza el calculo de la velocidad de las dos direcciones (coordenadas) en km/h.

## Tech
- https://developers.google.com/maps?hl=es-419
- https://towardsdatascience.com/calculating-distance-between-two-geolocations-in-python-26ad3afe287b


## Development

Tener instalado docker y docker-compose
```sh
docker-compose build
```

```sh
docker-compose up -d
```

## API

Registro de Houm
```sh
Request:
/account/register/
body = {
	"username": "aconga",
	"email": "acongacardenas@gmail.com",
	"password": "A142857.?",
	"password2": "A142857.?"
}

Response:
{
	"response": "Registration Successful!",
	"username": "aconga",
	"email": "acongacardenas@gmail.com",
	"token": "e6f395559188a6fcbeeda7057d7985755d247e00"
}
```

Login de Houm
```sh
Request:
/account/login/
body = {
	"username": "aconga1",
	"password": "A142857.?"
}

Response:
{
	"token": "b1ded22d15d008aa238830385602e2c75d71da36"
}
```

Registro de Propiedad (POST)
```sh
Request:
/api/propertys/
Authorization: Token <token>

body = {
	"address": "av pedro ruiz gallo 935, ate"
}


Response:
{
	"address": "av pedro ruiz gallo 935, ate",
	"latitude": -12.0219671,
	"longitude": -76.9126153,
	"houm": 1
}
```

Listado de propiedad en un dia (GET)

```sh
Request:
/api/propertys/?register=2022-02-24&speed=10
Authorization: Token <token>


Response:
[
	{
		"id": 2,
		"address": "1600 Amphitheatre Parkway, Mountain View, CA",
		"latitude": 37.422388,
		"longitude": -122.0841883,
		"register": "2022-02-25",
		"start_date": "2022-02-25T08:47:04.862649-05:00",
		"finish_date": "2022-02-25T09:47:04.862649-05:00",
		"houm": 1,
		"property_details": {
			"id": 2,
			"description": null,
			"total_time_sec": 3600,
			"speed": "2226698.67",
			"created": "2022-02-25T08:47:04.900147-05:00",
			"updated": "2022-02-25T08:50:47.398390-05:00",
			"property": 2
		}
	},
	{
		"id": 1,
		"address": "av pedro ruiz gallo 935, ate",
		"latitude": -12.0219671,
		"longitude": -76.9126153,
		"register": "2022-02-25",
		"start_date": "2022-02-25T07:46:53.159320-05:00",
		"finish_date": "2022-02-25T08:46:53.159320-05:00",
		"houm": 1,
		"property_details": {
			"id": 1,
			"description": null,
			"total_time_sec": 3600,
			"speed": "",
			"created": "2022-02-25T08:47:04.884733-05:00",
			"updated": "2022-02-25T08:47:04.891684-05:00",
			"property": 1
		}
	}
]
```

Update de Houm
```sh
Request:
api/propertys/2/
body = {
	"finish_date": "2022-02-25T09:47:04.862649-05:00"
}


Response:
{
	"finish_date": "2022-02-25T09:47:04.862649-05:00"
}
```
