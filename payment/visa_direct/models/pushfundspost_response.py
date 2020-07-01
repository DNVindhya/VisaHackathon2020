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


class PushfundspostResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, network_id=None, approval_code=None, fee_program_indicator=None, prepaid_balance=None, prepaid_balance_currency=None, merchant_verification_value=None, status_identifier=None, transaction_identifier=None, last4of_pan=None, response_code=None, action_code=None, transmission_date_time=None):
        """
        PushfundspostResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'network_id': 'int',
            'approval_code': 'str',
            'fee_program_indicator': 'str',
            'prepaid_balance': 'str',
            'prepaid_balance_currency': 'str',
            'merchant_verification_value': 'str',
            'status_identifier': 'str',
            'transaction_identifier': 'int',
            'last4of_pan': 'int',
            'response_code': 'str',
            'action_code': 'str',
            'transmission_date_time': 'str'
        }

        self.attribute_map = {
            'network_id': 'networkId',
            'approval_code': 'approvalCode',
            'fee_program_indicator': 'feeProgramIndicator',
            'prepaid_balance': 'prepaidBalance',
            'prepaid_balance_currency': 'prepaidBalanceCurrency',
            'merchant_verification_value': 'merchantVerificationValue',
            'status_identifier': 'statusIdentifier',
            'transaction_identifier': 'transactionIdentifier',
            'last4of_pan': 'last4ofPAN',
            'response_code': 'responseCode',
            'action_code': 'actionCode',
            'transmission_date_time': 'transmissionDateTime'
        }

        self._network_id = network_id
        self._approval_code = approval_code
        self._fee_program_indicator = fee_program_indicator
        self._prepaid_balance = prepaid_balance
        self._prepaid_balance_currency = prepaid_balance_currency
        self._merchant_verification_value = merchant_verification_value
        self._status_identifier = status_identifier
        self._transaction_identifier = transaction_identifier
        self._last4of_pan = last4of_pan
        self._response_code = response_code
        self._action_code = action_code
        self._transmission_date_time = transmission_date_time

    @property
    def network_id(self):
        """
        Gets the network_id of this PushfundspostResponse.
        This contains a code that identifies the network on which the transaction was processed.<br><br>Refer to <a href=\"/request_response_codes#network_id_and_sharing_group_code\">Network ID</a><br><br><b>Note:</b><br>This field is returned only if it is anything other than networkId value 2.<br><br>Supported only in US for domestic transactions.

        :return: The network_id of this PushfundspostResponse.
        :rtype: int
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """
        Sets the network_id of this PushfundspostResponse.
        This contains a code that identifies the network on which the transaction was processed.<br><br>Refer to <a href=\"/request_response_codes#network_id_and_sharing_group_code\">Network ID</a><br><br><b>Note:</b><br>This field is returned only if it is anything other than networkId value 2.<br><br>Supported only in US for domestic transactions.

        :param network_id: The network_id of this PushfundspostResponse.
        :type: int
        """

        self._network_id = network_id

    @property
    def approval_code(self):
        """
        Gets the approval_code of this PushfundspostResponse.
        The authorization code from the issuer.

        :return: The approval_code of this PushfundspostResponse.
        :rtype: str
        """
        return self._approval_code

    @approval_code.setter
    def approval_code(self, approval_code):
        """
        Sets the approval_code of this PushfundspostResponse.
        The authorization code from the issuer.

        :param approval_code: The approval_code of this PushfundspostResponse.
        :type: str
        """

        self._approval_code = approval_code

    @property
    def fee_program_indicator(self):
        """
        Gets the fee_program_indicator of this PushfundspostResponse.
        

        :return: The fee_program_indicator of this PushfundspostResponse.
        :rtype: str
        """
        return self._fee_program_indicator

    @fee_program_indicator.setter
    def fee_program_indicator(self, fee_program_indicator):
        """
        Sets the fee_program_indicator of this PushfundspostResponse.
        

        :param fee_program_indicator: The fee_program_indicator of this PushfundspostResponse.
        :type: str
        """

        self._fee_program_indicator = fee_program_indicator

    @property
    def prepaid_balance(self):
        """
        Gets the prepaid_balance of this PushfundspostResponse.
        Min Inclusive: -999999999.999<br><br>Max Inclusive: 999999999.999<br><br>Note: Applicable only for Top Up Transactions

        :return: The prepaid_balance of this PushfundspostResponse.
        :rtype: str
        """
        return self._prepaid_balance

    @prepaid_balance.setter
    def prepaid_balance(self, prepaid_balance):
        """
        Sets the prepaid_balance of this PushfundspostResponse.
        Min Inclusive: -999999999.999<br><br>Max Inclusive: 999999999.999<br><br>Note: Applicable only for Top Up Transactions

        :param prepaid_balance: The prepaid_balance of this PushfundspostResponse.
        :type: str
        """

        self._prepaid_balance = prepaid_balance

    @property
    def prepaid_balance_currency(self):
        """
        Gets the prepaid_balance_currency of this PushfundspostResponse.
        Refer to <a href=\"/request_response_codes#iso_country_and_currency_codes\">ISO Codes</a>

        :return: The prepaid_balance_currency of this PushfundspostResponse.
        :rtype: str
        """
        return self._prepaid_balance_currency

    @prepaid_balance_currency.setter
    def prepaid_balance_currency(self, prepaid_balance_currency):
        """
        Sets the prepaid_balance_currency of this PushfundspostResponse.
        Refer to <a href=\"/request_response_codes#iso_country_and_currency_codes\">ISO Codes</a>

        :param prepaid_balance_currency: The prepaid_balance_currency of this PushfundspostResponse.
        :type: str
        """

        self._prepaid_balance_currency = prepaid_balance_currency

    @property
    def merchant_verification_value(self):
        """
        Gets the merchant_verification_value of this PushfundspostResponse.
        The concatenated Merchant Verification Value of Visa assigned and Acquirer assigned value is returned.

        :return: The merchant_verification_value of this PushfundspostResponse.
        :rtype: str
        """
        return self._merchant_verification_value

    @merchant_verification_value.setter
    def merchant_verification_value(self, merchant_verification_value):
        """
        Sets the merchant_verification_value of this PushfundspostResponse.
        The concatenated Merchant Verification Value of Visa assigned and Acquirer assigned value is returned.

        :param merchant_verification_value: The merchant_verification_value of this PushfundspostResponse.
        :type: str
        """

        self._merchant_verification_value = merchant_verification_value

    @property
    def status_identifier(self):
        """
        Gets the status_identifier of this PushfundspostResponse.
        

        :return: The status_identifier of this PushfundspostResponse.
        :rtype: str
        """
        return self._status_identifier

    @status_identifier.setter
    def status_identifier(self, status_identifier):
        """
        Sets the status_identifier of this PushfundspostResponse.
        

        :param status_identifier: The status_identifier of this PushfundspostResponse.
        :type: str
        """
        if status_identifier is None:
            raise ValueError("Invalid value for `status_identifier`, must not be `None`")

        self._status_identifier = status_identifier

    @property
    def transaction_identifier(self):
        """
        Gets the transaction_identifier of this PushfundspostResponse.
        The VisaNet reference number for the transaction<br><br><b>Note: </b><br>transactionIdentifier is a Visa generated field that client recieves in the response message.<br><b>Note: </b>As an exception Visa allows clients to use the transactionIdentifier received in the AFT response into the subsequent OCT message - this is to simplify matching the pull and push transaction pair and reconciliation.

        :return: The transaction_identifier of this PushfundspostResponse.
        :rtype: int
        """
        return self._transaction_identifier

    @transaction_identifier.setter
    def transaction_identifier(self, transaction_identifier):
        """
        Sets the transaction_identifier of this PushfundspostResponse.
        The VisaNet reference number for the transaction<br><br><b>Note: </b><br>transactionIdentifier is a Visa generated field that client recieves in the response message.<br><b>Note: </b>As an exception Visa allows clients to use the transactionIdentifier received in the AFT response into the subsequent OCT message - this is to simplify matching the pull and push transaction pair and reconciliation.

        :param transaction_identifier: The transaction_identifier of this PushfundspostResponse.
        :type: int
        """
        if transaction_identifier is None:
            raise ValueError("Invalid value for `transaction_identifier`, must not be `None`")

        self._transaction_identifier = transaction_identifier

    @property
    def last4of_pan(self):
        """
        Gets the last4of_pan of this PushfundspostResponse.
        This field contains the last four digits of the cardholder primary account number (PAN)

        :return: The last4of_pan of this PushfundspostResponse.
        :rtype: int
        """
        return self._last4of_pan

    @last4of_pan.setter
    def last4of_pan(self, last4of_pan):
        """
        Sets the last4of_pan of this PushfundspostResponse.
        This field contains the last four digits of the cardholder primary account number (PAN)

        :param last4of_pan: The last4of_pan of this PushfundspostResponse.
        :type: int
        """

        self._last4of_pan = last4of_pan

    @property
    def response_code(self):
        """
        Gets the response_code of this PushfundspostResponse.
        The source for the response; typically, either the recipient issuer or a Visa system.<br><br>Refer to <a href=\"/request_response_codes#response_code\">response Code</a><br><b>Note: </b>: The VisaNet Response Source for the transaction

        :return: The response_code of this PushfundspostResponse.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this PushfundspostResponse.
        The source for the response; typically, either the recipient issuer or a Visa system.<br><br>Refer to <a href=\"/request_response_codes#response_code\">response Code</a><br><b>Note: </b>: The VisaNet Response Source for the transaction

        :param response_code: The response_code of this PushfundspostResponse.
        :type: str
        """
        if response_code is None:
            raise ValueError("Invalid value for `response_code`, must not be `None`")

        self._response_code = response_code

    @property
    def action_code(self):
        """
        Gets the action_code of this PushfundspostResponse.
        The results of the transaction request <br><br>Refer to <a href=\"/request_response_codes#action_code\">action code</a><br><b>Note: </b>: The VisaNet Response Code for the transaction

        :return: The action_code of this PushfundspostResponse.
        :rtype: str
        """
        return self._action_code

    @action_code.setter
    def action_code(self, action_code):
        """
        Sets the action_code of this PushfundspostResponse.
        The results of the transaction request <br><br>Refer to <a href=\"/request_response_codes#action_code\">action code</a><br><b>Note: </b>: The VisaNet Response Code for the transaction

        :param action_code: The action_code of this PushfundspostResponse.
        :type: str
        """
        if action_code is None:
            raise ValueError("Invalid value for `action_code`, must not be `None`")

        self._action_code = action_code

    @property
    def transmission_date_time(self):
        """
        Gets the transmission_date_time of this PushfundspostResponse.
        Example: 2016-01-15T07:03:52.000Z

        :return: The transmission_date_time of this PushfundspostResponse.
        :rtype: str
        """
        return self._transmission_date_time

    @transmission_date_time.setter
    def transmission_date_time(self, transmission_date_time):
        """
        Sets the transmission_date_time of this PushfundspostResponse.
        Example: 2016-01-15T07:03:52.000Z

        :param transmission_date_time: The transmission_date_time of this PushfundspostResponse.
        :type: str
        """
        if transmission_date_time is None:
            raise ValueError("Invalid value for `transmission_date_time`, must not be `None`")

        self._transmission_date_time = transmission_date_time

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
        if not isinstance(other, PushfundspostResponse):
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