# coding=utf-8
from __future__ import unicode_literals
from ..fr_FR import Provider as AddressProvider_FR
from ..nl_BE import Provider as AddressProvider_NL

class Provider(AddressProvider_FR):
    cities = AddressProvider_NL.cities

    provinces = (
		"Anvers", "Hainaut", "Limbourg", "Liège", "Luxembourg", "Namur",
		"Flandre orientale", "Brabant flamand", "Brabant wallon", "Flandre orientale"
    )

    postcode_formats = AddressProvider_NL.postcode_formats
    @classmethod
    def province(cls):
        return cls.random_element(cls.provinces)
    
    @classmethod
    def city(cls):
        return cls.random_element(cls.cities)    

