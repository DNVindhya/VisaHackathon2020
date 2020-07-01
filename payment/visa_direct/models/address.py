# coding: utf-8

"""
    Funds Transfer API

    The Funds Transfer API can pull funds from the sender&apos;s Visa account (in preparation for pushing funds to a recipient&apos;s account) in an Account Funding Transaction (AFT).  Additionally, the Funds Transfer API also provides functionality to push funds to the recipient&apos;s Visa account in an Original Credit Transaction (OCT).  If a transaction is declined, the Funds Transfer API can also return the funds to the sender&apos;s funding source in an Account Funding Transaction Reversal (AFTR). The API has been enhanced to allow originators to send their PushFundsTransactions(OCTs) and PullFundsTransactions(AFTs) to Visa for routing to multiple U.S. debit networks.

    OpenAPI spec version: v1
    Contact: 
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Address(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, county=None, country=None, state=None, zip_code=None):
        """
        Address - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'county': 'str',
            'country': 'str',
            'state': 'str',
            'zip_code': 'str'
        }

        self.attribute_map = {
            'county': 'county',
            'country': 'country',
            'state': 'state',
            'zip_code': 'zipCode'
        }

        self._county = county
        self._country = country
        self._state = state
        self._zip_code = zip_code

    @property
    def county(self):
        """
        Gets the county of this Address.
        <b>Note:</b>It contains 3-digit numeric FIPS county code of the money transfer operator/Originator.<br><br>Required if cardAcceptor:address:country is \"US\".

        :return: The county of this Address.
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """
        Sets the county of this Address.
        <b>Note:</b>It contains 3-digit numeric FIPS county code of the money transfer operator/Originator.<br><br>Required if cardAcceptor:address:country is \"US\".

        :param county: The county of this Address.
        :type: str
        """

        self._county = county

    @property
    def country(self):
        """
        Gets the country of this Address.
        This field must contain the 3-character alpha country code for the country of the originator or money transfer operator.<br><br>Refer to <a href=\"/request_response_codes#iso_country_and_currency_codes\">ISO Codes</a>

        :return: The country of this Address.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Address.
        This field must contain the 3-character alpha country code for the country of the originator or money transfer operator.<br><br>Refer to <a href=\"/request_response_codes#iso_country_and_currency_codes\">ISO Codes</a>

        :param country: The country of this Address.
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")

        self._country = country

    @property
    def state(self):
        """
        Gets the state of this Address.
        <b>Note:</b>State or province of the money transfer operator/Originator. <br><br> Required if cardAcceptor:address:country is \"US\" or \"CA\".

        :return: The state of this Address.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Address.
        <b>Note:</b>State or province of the money transfer operator/Originator. <br><br> Required if cardAcceptor:address:country is \"US\" or \"CA\".

        :param state: The state of this Address.
        :type: str
        """

        self._state = state

    @property
    def zip_code(self):
        """
        Gets the zip_code of this Address.
        <b>Note:</b>Zip/Postal code of the money transfer operator/Originator.<br><br>Required if cardAcceptor:address:country is \"US\" or \"CA\".

        :return: The zip_code of this Address.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """
        Sets the zip_code of this Address.
        <b>Note:</b>Zip/Postal code of the money transfer operator/Originator.<br><br>Required if cardAcceptor:address:country is \"US\" or \"CA\".

        :param zip_code: The zip_code of this Address.
        :type: str
        """

        self._zip_code = zip_code

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

# ----------------------------------------------------------------------------------------------------------------------
# © Copyright 2018 Visa. All Rights Reserved.
#
# NOTICE: The software and accompanying information and documentation (together, the “Software”) remain the property of
# and are proprietary to Visa and its suppliers and affiliates. The Software remains protected by intellectual property
# rights and may be covered by U.S. and foreign patents or patent applications. The Software is licensed and not sold.
#
# By accessing the Software you are agreeing to Visa's terms of use (developer.visa.com/terms) and privacy policy
# (developer.visa.com/privacy). In addition, all permissible uses of the Software must be in support of Visa products,
# programs and services provided through the Visa Developer Program (VDP) platform only (developer.visa.com).
# THE SOFTWARE AND ANY ASSOCIATED INFORMATION OR DOCUMENTATION IS PROVIDED ON AN “AS IS,” “AS AVAILABLE,” “WITH ALL
# FAULTS” BASIS WITHOUT WARRANTY OR CONDITION OF ANY KIND. YOUR USE IS AT YOUR OWN RISK.
# ----------------------------------------------------------------------------------------------------------------------