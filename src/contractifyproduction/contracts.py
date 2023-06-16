"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from contractifyproduction import utils
from contractifyproduction.models import operations, shared
from typing import Optional

class Contracts:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create_contract(self, request: operations.CreateContractRequest, security: operations.CreateContractSecurity) -> operations.CreateContractResponse:
        r"""Create a contract
        Create a contract
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateContractRequest, base_url, '/api/companies/{company}/contracts', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "contract_write", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json;q=1, application/json;q=0.8, application/json;q=0.5, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateContractResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateContract201ApplicationJSON])
                res.create_contract_201_application_json_object = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateContract401ApplicationJSON])
                res.create_contract_401_application_json_object = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateContract403ApplicationJSON])
                res.create_contract_403_application_json_object = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateContract422ApplicationJSON])
                res.create_contract_422_application_json_object = out

        return res

    
    def delete_contract(self, request: operations.DeleteContractRequest, security: operations.DeleteContractSecurity) -> operations.DeleteContractResponse:
        r"""Delete a contract
        Delete a contract
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteContractRequest, base_url, '/api/companies/{company}/contracts/{contract}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0.8, application/json;q=0.5, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteContractResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteContract400ApplicationJSON])
                res.delete_contract_400_application_json_object = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteContract401ApplicationJSON])
                res.delete_contract_401_application_json_object = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteContract403ApplicationJSON])
                res.delete_contract_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteContract404ApplicationJSON])
                res.delete_contract_404_application_json_object = out

        return res

    
    def get_contract(self, request: operations.GetContractRequest, security: operations.GetContractSecurity) -> operations.GetContractResponse:
        r"""Get a contract
        Get information about a contract
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetContractRequest, base_url, '/api/companies/{company}/contracts/{contract}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0.8, application/json;q=0.5, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetContractResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetContract200ApplicationJSON])
                res.get_contract_200_application_json_object = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetContract401ApplicationJSON])
                res.get_contract_401_application_json_object = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetContract403ApplicationJSON])
                res.get_contract_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetContract404ApplicationJSON])
                res.get_contract_404_application_json_object = out

        return res

    
    def list_contracts(self, request: operations.ListContractsRequest, security: operations.ListContractsSecurity) -> operations.ListContractsResponse:
        r"""List contracts
        List all the contracts within a company
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListContractsRequest, base_url, '/api/companies/{company}/contracts', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListContractsRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0.7, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListContractsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ContractCollection])
                res.contract_collection = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListContracts401ApplicationJSON])
                res.list_contracts_401_application_json_object = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListContracts403ApplicationJSON])
                res.list_contracts_403_application_json_object = out

        return res

    
    def update_contract(self, request: operations.UpdateContractRequest, security: operations.UpdateContractSecurity) -> operations.UpdateContractResponse:
        r"""Update a contract
        Update a contract
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateContractRequest, base_url, '/api/companies/{company}/contracts/{contract}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "contract_write", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json;q=1, application/json;q=0.8, application/json;q=0.6, application/json;q=0.4, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateContractResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateContract200ApplicationJSON])
                res.update_contract_200_application_json_object = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateContract401ApplicationJSON])
                res.update_contract_401_application_json_object = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateContract403ApplicationJSON])
                res.update_contract_403_application_json_object = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateContract404ApplicationJSON])
                res.update_contract_404_application_json_object = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateContract422ApplicationJSON])
                res.update_contract_422_application_json_object = out

        return res

    