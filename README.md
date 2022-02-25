omport json
um tenemos un gran equipo de Houmers que muestran las propiedades y solucionan todos los problemas que podrían ocurrir en ellas. Ellos son parte fundamental de nuestra operación y de la experiencia que tienen nuestros clientes. Es por esta razón que queremos incorporar ciertas métricas para monitorear cómo operan, mejorar la calidad de servicio y para asegurar la seguridad de nuestros Houmers.

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

## Development

Crear tu virtualenv
```sh
python3 -m venv env
```

```sh
pip install -r requeriments.txt
```

```sh
python manage.py migrate
```

```sh
python manage.py runserver
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
Registro de Propiedad
```sh
Request:
/api/propertys/
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

print('Loading function')
def lambda_handler(event, context):
        #print("Received event: " + json.dumps(event, indent=2))
            print("value1 = " + event['key1'])
                print("value2 = " + event['key2'])
                    print("value3 = " + event['key3'])
                        return event['key1'] # Echo back the first key value
                        #raise Exception('Something went wrong')

