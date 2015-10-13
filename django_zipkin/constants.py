DEFAULT_ZIPKIN_SERVICE_NAME = None
DEFAULT_ZIPKIN_LOGGER_NAME = 'zipkin'
DEFAULT_ZIPKIN_DATA_STORE_CLASS = 'data_store.ThreadLocalDataStore'
DEFAULT_ZIPKIN_ID_GENERATOR_CLASS = 'id_generator.SimpleIdGenerator'

TRACE_ID_HDR_NAME = "X-B3-TraceId"
SPAN_ID_HDR_NAME = "X-B3-SpanId"
PARENT_SPAN_ID_HDR_NAME = "X-B3-ParentSpanId"
SAMPLED_HDR_NAME = "X-B3-Sampled"
FLAGS_HDR_NAME = "X-B3-Flags"

ANNOTATION_HTTP_URI = 'http.uri'
ANNOTATION_HTTP_STATUSCODE = 'http.statuscode'
ANNOTATION_DJANGO_VIEW_FUNC_NAME = 'django.view.func_name'
ANNOTATION_DJANGO_VIEW_CLASS = 'django.view.class'
ANNOTATION_DJANGO_VIEW_ARGS = 'django.view.args'
ANNOTATION_DJANGO_VIEW_KWARGS = 'django.view.kwargs'
ANNOTATION_DJANGO_URL_NAME = 'django.url_name'
ANNOTATION_DJANGO_TASTYPIE_RESOURCE_NAME = 'django.tastypie.resource_name'

ANNOTATION_NO_DATA_IN_LOCAL_STORE = 'No ZipkinData in thread local store. This can happen if process_request ' + \
                                    'didn\'t run due to a previous middleware returning a response. Timing ' + \
                                    'information is invalid.'
