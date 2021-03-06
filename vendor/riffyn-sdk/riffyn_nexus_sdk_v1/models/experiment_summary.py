# coding: utf-8

"""
    Riffyn Nexus REST API V1

    ## Vocabulary Before you begin, please familiarize yourself with our [Glossary of Terms](https://help.riffyn.com/hc/en-us/articles/360045503694). ## Getting Started If you'd like to play around with the API, there are several free GUI tools that will allow you to send requests and receive responses. We suggest using the free app [Postman](https://www.getpostman.com/). ## Authentication Begin with a call the [authenticate](#/authentication/authenticate) endpoint using [HTTP Basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) with your `username` and `password` to retrieve either an API Key or an Access Token. For example:      curl -X POST -u '<username>' https://api.app.riffyn.com/v1/auth -v  You may then use either the API Key or the accessToken for all future requests to the API. For example:      curl -H 'access-token: <ACCESS_TOKEN>' https://api.app.riffyn.com/v1/units -v      curl -H 'api-key: <API_KEY>' https://api.app.riffyn.com/v1/units -v  The tokens' values will be either in the message returned by the `/authenticate` endpoint or in the createApiKey `/auth/api-key` or CreateAccesToken `/auth/access-token` endpoints. The API Key will remain valid until it is deauthorized by revoking it through the Security Settings in the Riffyn Nexus App UI. The API Key is best for running scripts and longer lasting interactions with the API. The Access Token will expire automatically and is best suited to granting applications short term access to the Riffyn Nexus API. Make your requests by sending the HTTP header `api-key: $API_KEY`, or `access-token: $ACCESS_TOKEN`. In Postman, add your preferred token to the headers under the Headers tab for any request other than the original request to `/authenticate`.  If you are enrolled in MultiFactor Authentication (MFA) the `status` returned by the `/authenticate` endpoint will be `MFA_REQUIRED`. A `passCode`, a `stateToken`, and a `factorId` must be passed to the [/verify](#/authentication/verify) endpoint to complete the authentication process and achieve the `SUCCESS` status. MFA must be managed in the Riffyn Nexus App UI.  ## Paging and Sorting The majority of endpoints that return a list of data support paging and sorting through the use of three properties, `limit`,  `offset`, and `sort`. Please see the list of query parameters, displayed below each endpoint's code examples, to see if paging or sorting is supported for that specific endpoint.  Certain endpoints return data that's added frequently, like resources. As a result, you may want filter results on either the maximum or minimum creation timestamp. This will prevent rows from shifting their position from the top of the list, as you scroll though subsequent pages of a multi-page response.  Before querying for the first page, store the current date-time (in memory, a database, a file...). On subsequent pages you *may* include the `before` query parameter, to limit the results to records created before that date-time. E.g. before loading page one, you store the current date time of `2016-10-31T22:00:00Z` (ISO date format). Later, when generating the URL for page two, you *could* limit the results by including the query parameter `before=1477951200000` (epoch timestamp).  ## Postman endpoint examples There is a YAML file with the examples of the request on Riffyn Nexus API [Click here](/v1/collection) to get the file. If you don't know how to import the collection file, [here](https://learning.postman.com/docs/postman/collections/data-formats/#importing-postman-data) are the steps. ## Client SDKs You may write your own API client, or you may use one of ours. [Click here](/v1/clients) to select your programming language and download an API client.   # noqa: E501

    OpenAPI spec version: 4.2.0
    Contact: support@riffyn.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExperimentSummary(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'experiment_id': 'str',
        'purpose': 'str',
        'summary': 'str',
        'created': 'Created',
        'modified': 'Modified',
        'modified_by': 'ModifiedBy'
    }

    attribute_map = {
        'id': '_id',
        'experiment_id': 'experimentId',
        'purpose': 'purpose',
        'summary': 'summary',
        'created': 'created',
        'modified': 'modified',
        'modified_by': 'modifiedBy'
    }

    def __init__(self, id=None, experiment_id=None, purpose=None, summary=None, created=None, modified=None, modified_by=None):  # noqa: E501
        """ExperimentSummary - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._experiment_id = None
        self._purpose = None
        self._summary = None
        self._created = None
        self._modified = None
        self._modified_by = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if experiment_id is not None:
            self.experiment_id = experiment_id
        if purpose is not None:
            self.purpose = purpose
        if summary is not None:
            self.summary = summary
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if modified_by is not None:
            self.modified_by = modified_by

    @property
    def id(self):
        """Gets the id of this ExperimentSummary.  # noqa: E501

        The unique id of the summary.  # noqa: E501

        :return: The id of this ExperimentSummary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExperimentSummary.

        The unique id of the summary.  # noqa: E501

        :param id: The id of this ExperimentSummary.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def experiment_id(self):
        """Gets the experiment_id of this ExperimentSummary.  # noqa: E501

        The unique id of the experiment.  # noqa: E501

        :return: The experiment_id of this ExperimentSummary.  # noqa: E501
        :rtype: str
        """
        return self._experiment_id

    @experiment_id.setter
    def experiment_id(self, experiment_id):
        """Sets the experiment_id of this ExperimentSummary.

        The unique id of the experiment.  # noqa: E501

        :param experiment_id: The experiment_id of this ExperimentSummary.  # noqa: E501
        :type: str
        """

        self._experiment_id = experiment_id

    @property
    def purpose(self):
        """Gets the purpose of this ExperimentSummary.  # noqa: E501

        The purpose of the experiment.  # noqa: E501

        :return: The purpose of this ExperimentSummary.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this ExperimentSummary.

        The purpose of the experiment.  # noqa: E501

        :param purpose: The purpose of this ExperimentSummary.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

    @property
    def summary(self):
        """Gets the summary of this ExperimentSummary.  # noqa: E501

        A summary or report on the experiment.  # noqa: E501

        :return: The summary of this ExperimentSummary.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ExperimentSummary.

        A summary or report on the experiment.  # noqa: E501

        :param summary: The summary of this ExperimentSummary.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def created(self):
        """Gets the created of this ExperimentSummary.  # noqa: E501


        :return: The created of this ExperimentSummary.  # noqa: E501
        :rtype: Created
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ExperimentSummary.


        :param created: The created of this ExperimentSummary.  # noqa: E501
        :type: Created
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this ExperimentSummary.  # noqa: E501


        :return: The modified of this ExperimentSummary.  # noqa: E501
        :rtype: Modified
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ExperimentSummary.


        :param modified: The modified of this ExperimentSummary.  # noqa: E501
        :type: Modified
        """

        self._modified = modified

    @property
    def modified_by(self):
        """Gets the modified_by of this ExperimentSummary.  # noqa: E501


        :return: The modified_by of this ExperimentSummary.  # noqa: E501
        :rtype: ModifiedBy
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this ExperimentSummary.


        :param modified_by: The modified_by of this ExperimentSummary.  # noqa: E501
        :type: ModifiedBy
        """

        self._modified_by = modified_by

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ExperimentSummary, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExperimentSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
