import json
from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast
from requests import Response

T = TypeVar("T")


# return type is object of class: WelcomeElement
def get_deserialized_object(response: Response) -> 'WelcomeElement':
    result = welcome_from_dict(json.loads(response.text))
    return result[0]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def my_from(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return x[0]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, float) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Currency:
    code: str
    name: str
    symbol: str

    @staticmethod
    def from_dict(obj: Any) -> 'Currency':
        assert isinstance(obj, dict)
        code = from_str(obj.get("code"))
        name = from_str(obj.get("name"))
        symbol = from_str(obj.get("symbol"))
        return Currency(code, name, symbol)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_str(self.code)
        result["name"] = from_str(self.name)
        result["symbol"] = from_str(self.symbol)
        return result


@dataclass
class Language:
    iso639_1: str
    iso639_2: str
    name: str
    native_name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Language':
        assert isinstance(obj, dict)
        iso639_1 = from_str(obj.get("iso639_1"))
        iso639_2 = from_str(obj.get("iso639_2"))
        name = from_str(obj.get("name"))
        native_name = from_str(obj.get("nativeName"))
        return Language(iso639_1, iso639_2, name, native_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["iso639_1"] = from_str(self.iso639_1)
        result["iso639_2"] = from_str(self.iso639_2)
        result["name"] = from_str(self.name)
        result["nativeName"] = from_str(self.native_name)
        return result


@dataclass
class RegionalBloc:
    acronym: str
    name: str
    other_acronyms: List[Any]
    other_names: List[Any]

    @staticmethod
    def from_dict(obj: Any) -> 'RegionalBloc':
        assert isinstance(obj, dict)
        acronym = from_str(obj.get("acronym"))
        name = from_str(obj.get("name"))
        other_acronyms = from_list(lambda x: x, obj.get("otherAcronyms"))
        other_names = from_list(lambda x: x, obj.get("otherNames"))
        return RegionalBloc(acronym, name, other_acronyms, other_names)

    def to_dict(self) -> dict:
        result: dict = {}
        result["acronym"] = from_str(self.acronym)
        result["name"] = from_str(self.name)
        result["otherAcronyms"] = from_list(lambda x: x, self.other_acronyms)
        result["otherNames"] = from_list(lambda x: x, self.other_names)
        return result


@dataclass
class Translations:
    de: str
    es: str
    fr: str
    ja: str
    it: str
    br: str
    pt: str
    nl: str
    hr: str
    fa: str

    @staticmethod
    def from_dict(obj: Any) -> 'Translations':
        assert isinstance(obj, dict)
        de = from_str(obj.get("de"))
        es = from_str(obj.get("es"))
        fr = from_str(obj.get("fr"))
        ja = from_str(obj.get("ja"))
        it = from_str(obj.get("it"))
        br = from_str(obj.get("br"))
        pt = from_str(obj.get("pt"))
        nl = from_str(obj.get("nl"))
        hr = from_str(obj.get("hr"))
        fa = from_str(obj.get("fa"))
        return Translations(de, es, fr, ja, it, br, pt, nl, hr, fa)

    def to_dict(self) -> dict:
        result: dict = {}
        result["de"] = from_str(self.de)
        result["es"] = from_str(self.es)
        result["fr"] = from_str(self.fr)
        result["ja"] = from_str(self.ja)
        result["it"] = from_str(self.it)
        result["br"] = from_str(self.br)
        result["pt"] = from_str(self.pt)
        result["nl"] = from_str(self.nl)
        result["hr"] = from_str(self.hr)
        result["fa"] = from_str(self.fa)
        return result


@dataclass
class WelcomeElement:
    name: str
    top_level_domain: List[str]
    alpha2_code: str
    alpha3_code: str
    calling_codes: List[int]
    capital: str
    alt_spellings: List[str]
    region: str
    subregion: str
    population: int
    latlng: List[int]
    demonym: str
    area: int
    gini: int
    timezones: List[str]
    borders: List[str]
    native_name: str
    numeric_code: int
    currencies: List[Currency]
    languages: List[Language]
    translations: Translations
    flag: str
    regional_blocs: List[RegionalBloc]
    cioc: str

    @staticmethod
    def from_dict(obj: Any) -> 'WelcomeElement':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        top_level_domain = from_list(from_str, obj.get("topLevelDomain"))
        alpha2_code = from_str(obj.get("alpha2Code"))
        alpha3_code = from_str(obj.get("alpha3Code"))
        calling_codes = from_list(lambda x: int(from_str(x)), obj.get("callingCodes"))
        capital = from_str(obj.get("capital"))
        alt_spellings = from_list(from_str, obj.get("altSpellings"))
        region = from_str(obj.get("region"))
        subregion = from_str(obj.get("subregion"))
        population = from_int(obj.get("population"))
        # latlng = from_list(from_int, obj.get("latlng"))
        latlng = from_list(from_float, obj.get("latlng"))
        demonym = from_str(obj.get("demonym"))
        # area = from_int(obj.get("area"))
        area = from_float(obj.get("area"))
        # gini = from_int(obj.get("gini"))
        gini = from_float(obj.get("gini"))
        timezones = from_list(from_str, obj.get("timezones"))
        borders = from_list(from_str, obj.get("borders"))
        native_name = from_str(obj.get("nativeName"))
        numeric_code = int(from_str(obj.get("numericCode")))
        currencies = from_list(Currency.from_dict, obj.get("currencies"))
        languages = from_list(Language.from_dict, obj.get("languages"))
        translations = Translations.from_dict(obj.get("translations"))
        flag = from_str(obj.get("flag"))
        regional_blocs = from_list(RegionalBloc.from_dict, obj.get("regionalBlocs"))
        cioc = from_str(obj.get("cioc"))
        return WelcomeElement(name, top_level_domain, alpha2_code, alpha3_code, calling_codes, capital, alt_spellings, region, subregion, population, latlng, demonym, area, gini, timezones, borders, native_name, numeric_code, currencies, languages, translations, flag, regional_blocs, cioc)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["topLevelDomain"] = from_list(from_str, self.top_level_domain)
        result["alpha2Code"] = from_str(self.alpha2_code)
        result["alpha3Code"] = from_str(self.alpha3_code)
        result["callingCodes"] = from_list(lambda x: from_str((lambda x: str(x))(x)), self.calling_codes)
        result["capital"] = from_str(self.capital)
        result["altSpellings"] = from_list(from_str, self.alt_spellings)
        result["region"] = from_str(self.region)
        result["subregion"] = from_str(self.subregion)
        result["population"] = from_int(self.population)
        result["latlng"] = from_list(from_int, self.latlng)
        result["demonym"] = from_str(self.demonym)
        result["area"] = from_int(self.area)
        result["gini"] = from_int(self.gini)
        result["timezones"] = from_list(from_str, self.timezones)
        result["borders"] = from_list(from_str, self.borders)
        result["nativeName"] = from_str(self.native_name)
        result["numericCode"] = from_str(str(self.numeric_code))
        result["currencies"] = from_list(lambda x: to_class(Currency, x), self.currencies)
        result["languages"] = from_list(lambda x: to_class(Language, x), self.languages)
        result["translations"] = to_class(Translations, self.translations)
        result["flag"] = from_str(self.flag)
        result["regionalBlocs"] = from_list(lambda x: to_class(RegionalBloc, x), self.regional_blocs)
        result["cioc"] = from_str(self.cioc)
        return result


def welcome_from_dict(s: Any) -> List[WelcomeElement]:
    return from_list(WelcomeElement.from_dict, s)
    # return my_from(WelcomeElement.from_dict, s)


def welcome_to_dict(x: List[WelcomeElement]) -> Any:
    return from_list(lambda x: to_class(WelcomeElement, x), x)
