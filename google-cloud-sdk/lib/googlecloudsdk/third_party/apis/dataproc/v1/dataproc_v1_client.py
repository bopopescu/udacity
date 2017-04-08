"""Generated client library for dataproc version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.dataproc.v1 import dataproc_v1_messages as messages


class DataprocV1(base_api.BaseApiClient):
  """Generated client library for service dataproc version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://dataproc.googleapis.com/'

  _PACKAGE = u'dataproc'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'DataprocV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new dataproc handle."""
    url = url or self.BASE_URL
    super(DataprocV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.projects_regions_clusters = self.ProjectsRegionsClustersService(self)
    self.projects_regions_jobs = self.ProjectsRegionsJobsService(self)
    self.projects_regions_operations = self.ProjectsRegionsOperationsService(self)
    self.projects_regions = self.ProjectsRegionsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsRegionsClustersService(base_api.BaseApiService):
    """Service class for the projects_regions_clusters resource."""

    _NAME = u'projects_regions_clusters'

    def __init__(self, client):
      super(DataprocV1.ProjectsRegionsClustersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a cluster in a project.

      Args:
        request: (DataprocProjectsRegionsClustersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataproc.projects.regions.clusters.create',
        ordered_params=[u'projectId', u'region'],
        path_params=[u'projectId', u'region'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/regions/{region}/clusters',
        request_field=u'cluster',
        request_type_name=u'DataprocProjectsRegionsClustersCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a cluster in a project.

      Args:
        request: (DataprocProjectsRegionsClustersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'dataproc.projects.regions.clusters.delete',
        ordered_params=[u'projectId', u'region', u'clusterName'],
        path_params=[u'clusterName', u'projectId', u'region'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/regions/{region}/clusters/{clusterName}',
        request_field='',
        request_type_name=u'DataprocProjectsRegionsClustersDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Diagnose(self, request, global_params=None):
      """Gets cluster diagnostic information. After the operation completes, the Operation.response field contains DiagnoseClusterOutputLocation.

      Args:
        request: (DataprocProjectsRegionsClustersDiagnoseRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Diagnose')
      return self._RunMethod(
          config, request, global_params=global_params)

    Diagnose.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataproc.projects.regions.clusters.diagnose',
        ordered_params=[u'projectId', u'region', u'clusterName'],
        path_params=[u'clusterName', u'projectId', u'region'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/regions/{region}/clusters/{clusterName}:diagnose',
        request_field=u'diagnoseClusterRequest',
        request_type_name=u'DataprocProjectsRegionsClustersDiagnoseRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the resource representation for a cluster in a project.

      Args:
        request: (DataprocProjectsRegionsClustersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Cluster) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataproc.projects.regions.clusters.get',
        ordered_params=[u'projectId', u'region', u'clusterName'],
        path_params=[u'clusterName', u'projectId', u'region'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/regions/{region}/clusters/{clusterName}',
        request_field='',
        request_type_name=u'DataprocProjectsRegionsClustersGetRequest',
        response_type_name=u'Cluster',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists all regions/{region}/clusters in a project.

      Args:
        request: (DataprocProjectsRegionsClustersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListClustersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataproc.projects.regions.clusters.list',
        ordered_params=[u'projectId', u'region'],
        path_params=[u'projectId', u'region'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/projects/{projectId}/regions/{region}/clusters',
        request_field='',
        request_type_name=u'DataprocProjectsRegionsClustersListRequest',
        response_type_name=u'ListClustersResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates a cluster in a project.

      Args:
        request: (DataprocProjectsRegionsClustersPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PATCH',
        method_id=u'dataproc.projects.regions.clusters.patch',
        ordered_params=[u'projectId', u'region', u'clusterName'],
        path_params=[u'clusterName', u'projectId', u'region'],
        query_params=[u'updateMask'],
        relative_path=u'v1/projects/{projectId}/regions/{region}/clusters/{clusterName}',
        request_field=u'cluster',
        request_type_name=u'DataprocProjectsRegionsClustersPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ProjectsRegionsJobsService(base_api.BaseApiService):
    """Service class for the projects_regions_jobs resource."""

    _NAME = u'projects_regions_jobs'

    def __init__(self, client):
      super(DataprocV1.ProjectsRegionsJobsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      """Starts a job cancellation request. To access the job resource after cancellation, call regions/{region}/jobs.list or regions/{region}/jobs.get.

      Args:
        request: (DataprocProjectsRegionsJobsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataproc.projects.regions.jobs.cancel',
        ordered_params=[u'projectId', u'region', u'jobId'],
        path_params=[u'jobId', u'projectId', u'region'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/regions/{region}/jobs/{jobId}:cancel',
        request_field=u'cancelJobRequest',
        request_type_name=u'DataprocProjectsRegionsJobsCancelRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes the job from the project. If the job is active, the delete fails, and the response returns FAILED_PRECONDITION.

      Args:
        request: (DataprocProjectsRegionsJobsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'dataproc.projects.regions.jobs.delete',
        ordered_params=[u'projectId', u'region', u'jobId'],
        path_params=[u'jobId', u'projectId', u'region'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/regions/{region}/jobs/{jobId}',
        request_field='',
        request_type_name=u'DataprocProjectsRegionsJobsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the resource representation for a job in a project.

      Args:
        request: (DataprocProjectsRegionsJobsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataproc.projects.regions.jobs.get',
        ordered_params=[u'projectId', u'region', u'jobId'],
        path_params=[u'jobId', u'projectId', u'region'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/regions/{region}/jobs/{jobId}',
        request_field='',
        request_type_name=u'DataprocProjectsRegionsJobsGetRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists regions/{region}/jobs in a project.

      Args:
        request: (DataprocProjectsRegionsJobsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListJobsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataproc.projects.regions.jobs.list',
        ordered_params=[u'projectId', u'region'],
        path_params=[u'projectId', u'region'],
        query_params=[u'clusterName', u'filter', u'jobStateMatcher', u'pageSize', u'pageToken'],
        relative_path=u'v1/projects/{projectId}/regions/{region}/jobs',
        request_field='',
        request_type_name=u'DataprocProjectsRegionsJobsListRequest',
        response_type_name=u'ListJobsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates a job in a project.

      Args:
        request: (DataprocProjectsRegionsJobsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PATCH',
        method_id=u'dataproc.projects.regions.jobs.patch',
        ordered_params=[u'projectId', u'region', u'jobId'],
        path_params=[u'jobId', u'projectId', u'region'],
        query_params=[u'updateMask'],
        relative_path=u'v1/projects/{projectId}/regions/{region}/jobs/{jobId}',
        request_field=u'job',
        request_type_name=u'DataprocProjectsRegionsJobsPatchRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

    def Submit(self, request, global_params=None):
      """Submits a job to a cluster.

      Args:
        request: (DataprocProjectsRegionsJobsSubmitRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Submit')
      return self._RunMethod(
          config, request, global_params=global_params)

    Submit.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataproc.projects.regions.jobs.submit',
        ordered_params=[u'projectId', u'region'],
        path_params=[u'projectId', u'region'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/regions/{region}/jobs:submit',
        request_field=u'submitJobRequest',
        request_type_name=u'DataprocProjectsRegionsJobsSubmitRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

  class ProjectsRegionsOperationsService(base_api.BaseApiService):
    """Service class for the projects_regions_operations resource."""

    _NAME = u'projects_regions_operations'

    def __init__(self, client):
      super(DataprocV1.ProjectsRegionsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      """Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns google.rpc.Code.UNIMPLEMENTED. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to Code.CANCELLED.

      Args:
        request: (DataprocProjectsRegionsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/regions/{regionsId}/operations/{operationsId}:cancel',
        http_method=u'POST',
        method_id=u'dataproc.projects.regions.operations.cancel',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:cancel',
        request_field='',
        request_type_name=u'DataprocProjectsRegionsOperationsCancelRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns google.rpc.Code.UNIMPLEMENTED.

      Args:
        request: (DataprocProjectsRegionsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/regions/{regionsId}/operations/{operationsId}',
        http_method=u'DELETE',
        method_id=u'dataproc.projects.regions.operations.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'DataprocProjectsRegionsOperationsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (DataprocProjectsRegionsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/regions/{regionsId}/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'dataproc.projects.regions.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'DataprocProjectsRegionsOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns UNIMPLEMENTED.NOTE: the name binding below allows API services to override the binding to use different resource name schemes, such as users/*/operations.

      Args:
        request: (DataprocProjectsRegionsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/regions/{regionsId}/operations',
        http_method=u'GET',
        method_id=u'dataproc.projects.regions.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'DataprocProjectsRegionsOperationsListRequest',
        response_type_name=u'ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsRegionsService(base_api.BaseApiService):
    """Service class for the projects_regions resource."""

    _NAME = u'projects_regions'

    def __init__(self, client):
      super(DataprocV1.ProjectsRegionsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(DataprocV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
