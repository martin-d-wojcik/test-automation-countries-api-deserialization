class Endpoints:
    countries_all = 'https://restcountries.eu/rest/v2/all'
    country_by_name = 'https://restcountries.eu/rest/v2/name/{}'


class JsonSchemas:
    country_by_name = {
        "definitions": {},
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "https://example.com/object1590784564.json",
        "title": "Root",
        "type": "array",
        "default": [],
        "items":{
            "$id": "#root/items",
            "title": "Items",
            "type": "object",
            "required": [
                "name",
                "topLevelDomain",
                "alpha2Code",
                "alpha3Code",
                "callingCodes",
                "capital",
                "altSpellings",
                "region",
                "subregion",
                "population",
                "latlng",
                "demonym",
                "area",
                "gini",
                "timezones",
                "borders",
                "nativeName",
                "numericCode",
                "currencies",
                "languages",
                "translations",
                "flag",
                "regionalBlocs",
                "cioc"
            ],
            "properties": {
                "name": {
                    "$id": "#root/items/name",
                    "title": "Name",
                    "type": "string",
                    "default": "",
                    "examples": [
                        "Denmark"
                    ],
                    "pattern": "^.*$"
                },
                "topLevelDomain": {
                    "$id": "#root/items/topLevelDomain",
                    "title": "Topleveldomain",
                    "type": "array",
                    "default": [],
                    "items":{
                        "$id": "#root/items/topLevelDomain/items",
                        "title": "Items",
                        "type": "string",
                        "default": "",
                        "examples": [
                            ".dk"
                        ],
                        "pattern": "^.*$"
                    }
                },
                "alpha2Code": {
                    "$id": "#root/items/alpha2Code",
                    "title": "Alpha2code",
                    "type": "string",
                    "default": "",
                    "examples": [
                        "DK"
                    ],
                    "pattern": "^.*$"
                },
                "alpha3Code": {
                    "$id": "#root/items/alpha3Code",
                    "title": "Alpha3code",
                    "type": "string",
                    "default": "",
                    "examples": [
                        "DNK"
                    ],
                    "pattern": "^.*$"
                },
                "callingCodes": {
                    "$id": "#root/items/callingCodes",
                    "title": "Callingcodes",
                    "type": "array",
                    "default": [],
                    "items":{
                        "$id": "#root/items/callingCodes/items",
                        "title": "Items",
                        "type": "string",
                        "default": "",
                        "examples": [
                            "45"
                        ],
                        "pattern": "^.*$"
                    }
                },
                "capital": {
                    "$id": "#root/items/capital",
                    "title": "Capital",
                    "type": "string",
                    "default": "",
                    "examples": [
                        "Copenhagen"
                    ],
                    "pattern": "^.*$"
                },
                "altSpellings": {
                    "$id": "#root/items/altSpellings",
                    "title": "Altspellings",
                    "type": "array",
                    "default": [],
                    "items":{
                        "$id": "#root/items/altSpellings/items",
                        "title": "Items",
                        "type": "string",
                        "default": "",
                        "examples": [
                            "DK"
                        ],
                        "pattern": "^.*$"
                    }
                },
                "region": {
                    "$id": "#root/items/region",
                    "title": "Region",
                    "type": "string",
                    "default": "",
                    "examples": [
                        "Europe"
                    ],
                    "pattern": "^.*$"
                },
                "subregion": {
                    "$id": "#root/items/subregion",
                    "title": "Subregion",
                    "type": "string",
                    "default": "",
                    "examples": [
                        "Northern Europe"
                    ],
                    "pattern": "^.*$"
                },
                "population": {
                    "$id": "#root/items/population",
                    "title": "Population",
                    "type": "integer",
                    "examples": [
                        5717014
                    ],
                    "default": 0
                },
                "latlng": {
                    "$id": "#root/items/latlng",
                    "title": "Latlng",
                    "type": "array",
                    "default": [],
                    "items":{
                        "$id": "#root/items/latlng/items",
                        "title": "Items",
                        "type": "integer",
                        "examples": [
                            56
                        ],
                        "default": 0
                    }
                },
                "demonym": {
                    "$id": "#root/items/demonym",
                    "title": "Demonym",
                    "type": "string",
                    "default": "",
                    "examples": [
                        "Danish"
                    ],
                    "pattern": "^.*$"
                },
                "area": {
                    "$id": "#root/items/area",
                    "title": "Area",
                    "type": "integer",
                    "examples": [
                        43094
                    ],
                    "default": 0
                },
                "gini": {
                    "$id": "#root/items/gini",
                    "title": "Gini",
                    "type": "integer",
                    "examples": [
                        24
                    ],
                    "default": 0
                },
                "timezones": {
                    "$id": "#root/items/timezones",
                    "title": "Timezones",
                    "type": "array",
                    "default": [],
                    "items":{
                        "$id": "#root/items/timezones/items",
                        "title": "Items",
                        "type": "string",
                        "default": "",
                        "examples": [
                            "UTC-04:00"
                        ],
                        "pattern": "^.*$"
                    }
                },
                "borders": {
                    "$id": "#root/items/borders",
                    "title": "Borders",
                    "type": "array",
                    "default": [],
                    "items":{
                        "$id": "#root/items/borders/items",
                        "title": "Items",
                        "type": "string",
                        "default": "",
                        "examples": [
                            "DEU"
                        ],
                        "pattern": "^.*$"
                    }
                },
                "nativeName": {
                    "$id": "#root/items/nativeName",
                    "title": "Nativename",
                    "type": "string",
                    "default": "",
                    "examples": [
                        "Danmark"
                    ],
                    "pattern": "^.*$"
                },
                "numericCode": {
                    "$id": "#root/items/numericCode",
                    "title": "Numericcode",
                    "type": "string",
                    "default": "",
                    "examples": [
                        "208"
                    ],
                    "pattern": "^.*$"
                },
                "currencies": {
                    "$id": "#root/items/currencies",
                    "title": "Currencies",
                    "type": "array",
                    "default": [],
                    "items":{
                        "$id": "#root/items/currencies/items",
                        "title": "Items",
                        "type": "object",
                        "required": [
                            "code",
                            "name",
                            "symbol"
                        ],
                        "properties": {
                            "code": {
                                "$id": "#root/items/currencies/items/code",
                                "title": "Code",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "DKK"
                                ],
                                "pattern": "^.*$"
                            },
                            "name": {
                                "$id": "#root/items/currencies/items/name",
                                "title": "Name",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "Danish krone"
                                ],
                                "pattern": "^.*$"
                            },
                            "symbol": {
                                "$id": "#root/items/currencies/items/symbol",
                                "title": "Symbol",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "kr"
                                ],
                                "pattern": "^.*$"
                            }
                        }
                    }

                },
                "languages": {
                    "$id": "#root/items/languages",
                    "title": "Languages",
                    "type": "array",
                    "default": [],
                    "items":{
                        "$id": "#root/items/languages/items",
                        "title": "Items",
                        "type": "object",
                        "required": [
                            "iso639_1",
                            "iso639_2",
                            "name",
                            "nativeName"
                        ],
                        "properties": {
                            "iso639_1": {
                                "$id": "#root/items/languages/items/iso639_1",
                                "title": "Iso639_1",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "da"
                                ],
                                "pattern": "^.*$"
                            },
                            "iso639_2": {
                                "$id": "#root/items/languages/items/iso639_2",
                                "title": "Iso639_2",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "dan"
                                ],
                                "pattern": "^.*$"
                            },
                            "name": {
                                "$id": "#root/items/languages/items/name",
                                "title": "Name",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "Danish"
                                ],
                                "pattern": "^.*$"
                            },
                            "nativeName": {
                                "$id": "#root/items/languages/items/nativeName",
                                "title": "Nativename",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "dansk"
                                ],
                                "pattern": "^.*$"
                            }
                        }
                    }

                },
                "translations": {
                    "$id": "#root/items/translations",
                    "title": "Translations",
                    "type": "object",
                    "required": [
                        "de",
                        "es",
                        "fr",
                        "ja",
                        "it",
                        "br",
                        "pt",
                        "nl",
                        "hr",
                        "fa"
                    ],
                    "properties": {
                        "de": {
                            "$id": "#root/items/translations/de",
                            "title": "De",
                            "type": "string",
                            "default": "",
                            "examples": [
                                "Dänemark"
                            ],
                            "pattern": "^.*$"
                        },
                        "es": {
                            "$id": "#root/items/translations/es",
                            "title": "Es",
                            "type": "string",
                            "default": "",
                            "examples": [
                                "Dinamarca"
                            ],
                            "pattern": "^.*$"
                        },
                        "fr": {
                            "$id": "#root/items/translations/fr",
                            "title": "Fr",
                            "type": "string",
                            "default": "",
                            "examples": [
                                "Danemark"
                            ],
                            "pattern": "^.*$"
                        },
                        "ja": {
                            "$id": "#root/items/translations/ja",
                            "title": "Ja",
                            "type": "string",
                            "default": "",
                            "examples": [
                                "デンマーク"
                            ],
                            "pattern": "^.*$"
                        },
                        "it": {
                            "$id": "#root/items/translations/it",
                            "title": "It",
                            "type": "string",
                            "default": "",
                            "examples": [
                                "Danimarca"
                            ],
                            "pattern": "^.*$"
                        },
                        "br": {
                            "$id": "#root/items/translations/br",
                            "title": "Br",
                            "type": "string",
                            "default": "",
                            "examples": [
                                "Dinamarca"
                            ],
                            "pattern": "^.*$"
                        },
                        "pt": {
                            "$id": "#root/items/translations/pt",
                            "title": "Pt",
                            "type": "string",
                            "default": "",
                            "examples": [
                                "Dinamarca"
                            ],
                            "pattern": "^.*$"
                        },
                        "nl": {
                            "$id": "#root/items/translations/nl",
                            "title": "Nl",
                            "type": "string",
                            "default": "",
                            "examples": [
                                "Denemarken"
                            ],
                            "pattern": "^.*$"
                        },
                        "hr": {
                            "$id": "#root/items/translations/hr",
                            "title": "Hr",
                            "type": "string",
                            "default": "",
                            "examples": [
                                "Danska"
                            ],
                            "pattern": "^.*$"
                        },
                        "fa": {
                            "$id": "#root/items/translations/fa",
                            "title": "Fa",
                            "type": "string",
                            "default": "",
                            "examples": [
                                "دانمارک"
                            ],
                            "pattern": "^.*$"
                        }
                    }
                }
    ,
                "flag": {
                    "$id": "#root/items/flag",
                    "title": "Flag",
                    "type": "string",
                    "default": "",
                    "examples": [
                        "https://restcountries.eu/data/dnk.svg"
                    ],
                    "pattern": "^.*$"
                },
                "regionalBlocs": {
                    "$id": "#root/items/regionalBlocs",
                    "title": "Regionalblocs",
                    "type": "array",
                    "default": [],
                    "items":{
                        "$id": "#root/items/regionalBlocs/items",
                        "title": "Items",
                        "type": "object",
                        "required": [
                            "acronym",
                            "name",
                            "otherAcronyms",
                            "otherNames"
                        ],
                        "properties": {
                            "acronym": {
                                "$id": "#root/items/regionalBlocs/items/acronym",
                                "title": "Acronym",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "EU"
                                ],
                                "pattern": "^.*$"
                            },
                            "name": {
                                "$id": "#root/items/regionalBlocs/items/name",
                                "title": "Name",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "European Union"
                                ],
                                "pattern": "^.*$"
                            },
                            "otherAcronyms": {
                                "$id": "#root/items/regionalBlocs/items/otherAcronyms",
                                "title": "Otheracronyms",
                                "type": "array",
                                "default": []
                            },
                            "otherNames": {
                                "$id": "#root/items/regionalBlocs/items/otherNames",
                                "title": "Othernames",
                                "type": "array",
                                "default": []
                            }
                        }
                    }

                },
                "cioc": {
                    "$id": "#root/items/cioc",
                    "title": "Cioc",
                    "type": "string",
                    "default": "",
                    "examples": [
                        "DEN"
                    ],
                    "pattern": "^.*$"
                }
            }
        }
    }
