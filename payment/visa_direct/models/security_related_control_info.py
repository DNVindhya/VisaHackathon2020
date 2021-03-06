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


class SecurityRelatedControlInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, pin_block_format_code=None, zone_key_index=None):
        """
        SecurityRelatedControlInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'pin_block_format_code': 'int',
            'zone_key_index': 'int'
        }

        self.attribute_map = {
            'pin_block_format_code': 'pinBlockFormatCode',
            'zone_key_index': 'zoneKeyIndex'
        }

        self._pin_block_format_code = pin_block_format_code
        self._zone_key_index = zone_key_index

    @property
    def pin_block_format_code(self):
        """
        Gets the pin_block_format_code of this SecurityRelatedControlInfo.
        <b>Note:</b> For a CardPresent with PIN Data scenario, this field is required.

        :return: The pin_block_format_code of this SecurityRelatedControlInfo.
        :rtype: int
        """
        return self._pin_block_format_code

    @pin_block_format_code.setter
    def pin_block_format_code(self, pin_block_format_code):
        """
        Sets the pin_block_format_code of this SecurityRelatedControlInfo.
        <b>Note:</b> For a CardPresent with PIN Data scenario, this field is required.

        :param pin_block_format_code: The pin_block_format_code of this SecurityRelatedControlInfo.
        :type: int
        """

        self._pin_block_format_code = pin_block_format_code

    @property
    def zone_key_index(self):
        """
        Gets the zone_key_index of this SecurityRelatedControlInfo.
        <b>Note:</b> For a CardPresent with PIN Data scenario, this field is required.

        :return: The zone_key_index of this SecurityRelatedControlInfo.
        :rtype: int
        """
        return self._zone_key_index

    @zone_key_index.setter
    def zone_key_index(self, zone_key_index):
        """
        Sets the zone_key_index of this SecurityRelatedControlInfo.
        <b>Note:</b> For a CardPresent with PIN Data scenario, this field is required.

        :param zone_key_index: The zone_key_index of this SecurityRelatedControlInfo.
        :type: int
        """

        self._zone_key_index = zone_key_index

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
        if not isinstance(other, SecurityRelatedControlInfo):
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