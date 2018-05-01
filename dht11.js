[
    {
        "id": "97d51a50.1542d8",
        "type": "info",
        "z": "c3aed0d3.3ce58",
        "name": "Clic below and look the result into the display tab",
        "info": "",
        "icon": "commentdown.png",
        "langs": [
            {
                "key": "en-US",
                "title": "Clic below and look the result into the display tab",
                "body": "",
                "isDefault": true
            },
            {
                "key": "fr-FR",
                "title": "Cliquez ci-dessous et regardez le résultat dans le panneau \"Display\"",
                "body": "",
                "isDefault": false
            }
        ],
        "currentLanguage": "es-ES",
        "x": 257,
        "y": 69,
        "wires": []
    },
    {
        "id": "f3c89bbd.7b6208",
        "type": "mqtt in",
        "z": "c3aed0d3.3ce58",
        "name": "Humedad (BenacaPi)",
        "topic": "v1/pi/things/dht11/data/2",
        "qos": "2",
        "broker": "MQTT.Localhost",
        "x": 175,
        "y": 114,
        "wires": [
            [
                "3882bcb1.3f4614",
                "a75a2b4f.111ba8",
                "3cad7a4a.64fa96"
            ]
        ]
    },
    {
        "id": "d5df1823.433978",
        "type": "mqtt in",
        "z": "c3aed0d3.3ce58",
        "name": "Temperatura (BenacaPi)",
        "topic": "v1/pi/things/dht11/data/1",
        "qos": "2",
        "broker": "MQTT.Localhost",
        "x": 170,
        "y": 240,
        "wires": [
            [
                "3882bcb1.3f4614",
                "3b83defa.a83842",
                "cfd3da4a.de2768"
            ]
        ]
    },
    {
        "id": "3882bcb1.3f4614",
        "type": "debug",
        "z": "c3aed0d3.3ce58",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 534,
        "y": 343,
        "wires": []
    },
    {
        "id": "3b83defa.a83842",
        "type": "ui_gauge",
        "z": "c3aed0d3.3ce58",
        "name": "Temperatura",
        "group": "7c5a58a0.955b08",
        "order": 0,
        "width": 0,
        "height": 0,
        "gtype": "gage",
        "title": "Temperatura",
        "label": "ºC",
        "format": "{{value}}",
        "min": 0,
        "max": "50",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "x": 525,
        "y": 240,
        "wires": []
    },
    {
        "id": "a75a2b4f.111ba8",
        "type": "ui_chart",
        "z": "c3aed0d3.3ce58",
        "name": "",
        "group": "7c5a58a0.955b08",
        "order": 0,
        "width": 0,
        "height": 0,
        "label": "Humedad",
        "chartType": "line",
        "legend": "false",
        "xformat": "HH:mm:ss",
        "interpolate": "linear",
        "nodata": "",
        "dot": false,
        "ymin": "0",
        "ymax": "100",
        "removeOlder": 1,
        "removeOlderPoints": "",
        "removeOlderUnit": "604800",
        "cutout": 0,
        "useOneColor": false,
        "colors": [
            "#1f77b4",
            "#aec7e8",
            "#ff7f0e",
            "#2ca02c",
            "#98df8a",
            "#d62728",
            "#ff9896",
            "#9467bd",
            "#c5b0d5"
        ],
        "useOldStyle": false,
        "x": 493,
        "y": 119,
        "wires": [
            [],
            []
        ]
    },
    {
        "id": "3cad7a4a.64fa96",
        "type": "ui_gauge",
        "z": "c3aed0d3.3ce58",
        "name": "Humedad",
        "group": "7c5a58a0.955b08",
        "order": 0,
        "width": 0,
        "height": 0,
        "gtype": "compass",
        "title": "Gauge",
        "label": "%",
        "format": "{{value}}",
        "min": 0,
        "max": "100",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "x": 516,
        "y": 166,
        "wires": []
    },
    {
        "id": "74e4aa17.2fbe84",
        "type": "python3-function",
        "z": "c3aed0d3.3ce58",
        "name": "",
        "func": "\nreturn msg",
        "outputs": 1,
        "x": 251,
        "y": 381,
        "wires": [
            []
        ]
    },
    {
        "id": "cfd3da4a.de2768",
        "type": "file",
        "z": "c3aed0d3.3ce58",
        "name": "Temp",
        "filename": "/home/pi/PROYECTO/temp.txt",
        "appendNewline": true,
        "createDir": true,
        "overwriteFile": "false",
        "x": 392,
        "y": 207,
        "wires": []
    },
    {
        "id": "MQTT.Localhost",
        "type": "mqtt-broker",
        "z": "",
        "broker": "localhost",
        "port": "1883",
        "clientid": "",
        "usetls": false,
        "compatmode": true,
        "keepalive": "15",
        "cleansession": true,
        "willTopic": "",
        "willQos": "0",
        "willPayload": "",
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": ""
    },
    {
        "id": "7c5a58a0.955b08",
        "type": "ui_group",
        "z": "",
        "name": "Red",
        "tab": "2d0d65ba.a25de2",
        "order": 1,
        "disp": true,
        "width": "6",
        "collapse": true
    },
    {
        "id": "2d0d65ba.a25de2",
        "type": "ui_tab",
        "z": "",
        "name": "Colores",
        "icon": "dashboard"
    }
]