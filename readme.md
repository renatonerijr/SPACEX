# SPACEX API Viewer (Backend + Frontend)
SPACEX API Viewer é uma API completa (Django Rest Framework) e Frontend(React) que traz uma melhor visualização da API da SPACEX.

[Português](readme.md) | [English](lang/english/readme.md)


## Instalação
Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os requisitos.

```bash
pip install -r requirements.txt
```
Vá para a pasta react_spacex e use o gerenciador de pacotes [npm](https://www.npmjs.com/) para instalar os requisitos.

```bash
npm install
```

## Rodar os servidores

Vá para a pasta api_spacex e rode o servidor Django

```bash
python3 manage.py runserver
```

Vá para a pasta react_spacex e rode o servidor React

```bash
npm start
```

## Rodar os testes
Vá para a pasta api_spacex e rode o comando:

```bash
python3 manage.py test api_spacex.launches
```

## API
A API possui quatro endpoints:

```
  \launches\latest [GET]
  \launches\next   [GET]
  \launches\past\  [GET]
  \launches\<flight_number:int> [GET]
```
A API retorna um json com as informações mais relevantes, um request para o endpoint \latest retorna algo como isso:
```json
{
    "mission_name": "Amos-17",
    "flight_number": 83,
    "launch_year": "2019",
    "launch_date_utc": "2019-08-06T22:52:00.000Z",
    "rocket": {
        "first_stage": {
            "rocket_name": "Falcon 9",
            "is_reused": true,
            "land_success": null,
            "landing_intent": false
        },
        "second_stage": {
            "costumers": [
                "Spacecom"
            ],
            "nationality": "Israel",
            "manufacturer": "Boeing Satellite Systems"
        }
    },
    "launch_success": true,
    "launch_site": "Cape Canaveral Air Force Station Space Launch Complex 40",
    "imgs": [
        "https://live.staticflickr.com/65535/48478269312_58dd3dc446_o.jpg",
        "https://live.staticflickr.com/65535/48478269747_353dcb2e62_o.jpg",
        "https://live.staticflickr.com/65535/48478119901_2de0441026_o.jpg",
        "https://live.staticflickr.com/65535/48478120646_ab72c2c6c3_o.jpg",
        "https://live.staticflickr.com/65535/48478120031_5aae1f6131_o.jpg",
        "https://live.staticflickr.com/65535/48478269442_08479bed36_o.jpg"
    ],
    "img_mission_patch": "https://images2.imgbox.com/a0/ab/XUoByiuR_o.png",
    "video_link": "https://youtu.be/fZh82-WcCuo",
    "reddit_link": "https://www.reddit.com/r/spacex/comments/cjaawx/amos17_launch_campaign_thread",
    "details": "SpaceX will launch Boeing built Amos-17, a geostationary communications satellite for Israeli company Spacecom. The satellite will be delivered to GTO from KSC LC-39A or possibly CCAFS SLC-40, and will replace the defunct Amos-5 at 17° E. Amos-17 carries multi-band high throughput and regional beams servicing Africa, Europe and the Middle East. The cost of this launch is covered for Spacecom by SpaceX credit following the Amos-6 incident. A recovery of the booster for this mission is not expected."
} 
```

