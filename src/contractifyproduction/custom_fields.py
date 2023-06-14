"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from contractifyproduction import utils
from contractifyproduction.models import operations, shared
from typing import Optional

class CustomFields:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def list_custom_fields(self, request: operations.ListCustomFieldsRequest, security: operations.ListCustomFieldsSecurity) -> operations.ListCustomFieldsResponse:
        r"""List custom fields
        List all the custom fields within a company
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListCustomFieldsRequest, base_url, '/api/companies/{company}/custom-fields', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0.7, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListCustomFieldsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CustomFieldCollection])
                res.custom_field_collection = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListCustomFields401ApplicationJSON])
                res.list_custom_fields_401_application_json_object = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListCustomFields403ApplicationJSON])
                res.list_custom_fields_403_application_json_object = out

        return res

    