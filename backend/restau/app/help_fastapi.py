import inspect,fastapi

# print(dir(fastapi))

# ['from fastapi import APIRouter',
#  'from fastapi import BackgroundTasks',
#  'from fastapi import Body',
#  'from fastapi import Cookie',
#  'from fastapi import Depends',
#  'from fastapi import FastAPI',
#  'from fastapi import File',
#  'from fastapi import Form',
#  'from fastapi import HTTPException',
#  'from fastapi import Header',
#  'from fastapi import Path',
#  'from fastapi import Query',
#  'from fastapi import Request',
#  'from fastapi import Response',
#  'from fastapi import Security',
#  'from fastapi import UploadFile',
#  'from fastapi import WebSocket',
#  'from fastapi import WebSocketDisconnect',
#  'from fastapi import WebSocketException',
#  'fastapi.__builtins__',
#  'fastapi.__cached__',
#  'fastapi.__doc__',
#  'fastapi.__file__',
#  'fastapi.__loader__',
#  'fastapi.__name__',
#  'fastapi.__package__',
#  'fastapi.__path__',
#  'fastapi.__spec__',
#  'fastapi.__version__',
#  'from fastapi._compat import ',
#  'from fastapi.applications import ',
#  'from fastapi.background import ',
#  'from fastapi.concurrency import ',
#  'from fastapi.datastructures import ',
#  'from fastapi.dependencies import ',
#  'from fastapi.encoders import ',
#  'from fastapi.exception_handlers import ',
#  'from fastapi.exceptions import ',
#  'from fastapi.logger import ',
#  'from fastapi.openapi import ',
#  'from fastapi.param_functions import ',
#  'from fastapi.params import ',
#  'from fastapi.requests import ',
#  'from fastapi.responses import ',
#  'from fastapi.routing import ',
#  'from fastapi.security import ',
#  'from fastapi.status import ',
#  'from fastapi.types import ',
#  'from fastapi.utils import ',
#  'from fastapi.websockets import ']

# print(dir(fastapi._compat))
# ['Annotated', 'Any', 'BaseConfig', 'BaseModel', 'Callable', 'CoreSchema', 'Deque', 'Dict', 'Enum', 'ErrorWrapper', 'FieldInfo', 'FrozenSet', 'GenerateJsonSchema', 'GetJsonSchemaHandler', 'IncEx', 'JsonSchemaValue', 'List', 'Literal', 'Mapping', 'ModelField', 'ModelNameMap', 'PYDANTIC_V2', 'PYDANTIC_VERSION', 'PYDANTIC_VERSION_MINOR_TUPLE', 'PydanticSchemaGenerationError', 'PydanticUndefined', 'PydanticUndefinedType', 'RequestErrorModel', 'RequiredParam', 'Sequence', 'Set', 'Tuple', 'Type', 'TypeAdapter', 'Undefined', 'UndefinedType', 'Union', 'UnionType', 'UploadFile', 'Url', 'ValidationError', 'Validator', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_annotation_is_complex', '_annotation_is_sequence', '_get_model_config', '_model_dump', '_model_rebuild', '_normalize_errors', '_regenerate_error_with_loc', 'copy', 'copy_field_info', 'create_body_model', 'create_model', 'dataclass', 'deque', 'eval_type_lenient', 'evaluate_forwardref', 'field_annotation_is_complex', 'field_annotation_is_scalar', 'field_annotation_is_scalar_sequence', 'field_annotation_is_sequence', 'get_annotation_from_field_info', 'get_args', 'get_cached_model_fields', 'get_compat_model_name_map', 'get_definitions', 'get_missing_field_error', 'get_model_fields', 'get_origin', 'get_schema_from_model_field', 'is_bytes_field', 'is_bytes_or_nonable_bytes_annotation', 'is_bytes_sequence_annotation', 'is_bytes_sequence_field', 'is_dataclass', 'is_scalar_field', 'is_scalar_sequence_field', 'is_sequence_field', 'is_uploadfile_or_nonable_uploadfile_annotation', 'is_uploadfile_sequence_annotation', 'lenient_issubclass', 'lru_cache', 'sequence_annotation_to_type', 'sequence_types', 'serialize_sequence_value', 'value_is_sequence', 'with_info_plain_validator_function']


# print(dir(fastapi.applications))
# print(inspect.getsource(fastapi.applications.FastAPI.build_middleware_stack))

# ['ASGIApp', 'Annotated', 'Any', 'AppType', 'Awaitable', 'BaseHTTPMiddleware', 'BaseRoute', 'Callable', 'Coroutine', 'DecoratedCallable', 'Default', 'DefaultPlaceholder', 'Depends', 'Dict', 'Doc', 'Enum', 'FastAPI', 'HTMLResponse', 'HTTPException', 'IncEx', 'JSONResponse', 'Lifespan', 'List', 'Middleware', 'Optional', 'Receive', 'Request', 'RequestValidationError', 'Response', 'Scope', 'Send', 'Sequence', 'Starlette', 'State', 'Type', 'TypeVar', 'Union', 'WebSocketRequestValidationError', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'deprecated', 'generate_unique_id', 'get_openapi', 'get_redoc_html', 'get_swagger_ui_html', 'get_swagger_ui_oauth2_redirect_html', 'http_exception_handler', 'logger', 'request_validation_exception_handler', 'routing', 'websocket_request_validation_exception_handler']


# print(dir(fastapi.background))
# ['Annotated', 'Any', 'BackgroundTasks', 'Callable', 'Doc', 'P', 'ParamSpec', 'StarletteBackgroundTasks', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


# print(dir(fastapi.concurrency))
# ['AsyncGenerator', 'CapacityLimiter', 'ContextManager', 'TypeVar', '_T', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'anyio', 'asynccontextmanager', 'contextmanager_in_threadpool', 'iterate_in_threadpool', 'run_in_threadpool', 'run_until_first_complete']


# print(dir(fastapi.datastructures))
# ['Address', 'Annotated', 'Any', 'BinaryIO', 'Callable', 'CoreSchema', 'Default', 'DefaultPlaceholder', 'DefaultType', 'Dict', 'Doc', 'FormData', 'GetJsonSchemaHandler', 'Headers', 'Iterable', 'JsonSchemaValue', 'Optional', 'PYDANTIC_V2', 'QueryParams', 'StarletteUploadFile', 'State', 'Type', 'TypeVar', 'URL', 'UploadFile', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'cast', 'with_info_plain_validator_function']


# print(dir(fastapi.dependencies))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'models', 'utils']


# print(dir(fastapi.encoders))
# ['Annotated', 'Any', 'AnyUrl', 'BaseModel', 'Callable', 'Color', 'Decimal', 'Dict', 'Doc', 'ENCODERS_BY_TYPE', 'Enum', 'GeneratorType', 'IPv4Address', 'IPv4Interface', 'IPv4Network', 'IPv6Address', 'IPv6Interface', 'IPv6Network', 'IncEx', 'List', 'NameEmail', 'Optional', 'PYDANTIC_V2', 'Path', 'Pattern', 'PurePath', 'SecretBytes', 'SecretStr', 'Tuple', 'Type', 'UUID', 'UndefinedType', 'Union', 'Url', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_model_dump', 'dataclasses', 'datetime', 'decimal_encoder', 'defaultdict', 'deque', 'encoders_by_class_tuples', 'generate_encoders_by_class_tuples', 'isoformat', 'jsonable_encoder']


# print(dir(fastapi.exception_handlers))
# ['HTTPException', 'HTTP_422_UNPROCESSABLE_ENTITY', 'JSONResponse', 'Request', 'RequestValidationError', 'Response', 'WS_1008_POLICY_VIOLATION', 'WebSocket', 'WebSocketRequestValidationError', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'http_exception_handler', 'is_body_allowed_for_status_code', 'jsonable_encoder', 'request_validation_exception_handler', 'websocket_request_validation_exception_handler']


# print(dir(fastapi.exceptions))
# ['Annotated', 'Any', 'BaseModel', 'Dict', 'Doc', 'FastAPIError', 'HTTPException', 'Optional', 'RequestErrorModel', 'RequestValidationError', 'ResponseValidationError', 'Sequence', 'StarletteHTTPException', 'StarletteWebSocketException', 'Type', 'Union', 'ValidationException', 'WebSocketErrorModel', 'WebSocketException', 'WebSocketRequestValidationError', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'create_model']


# print(dir(fastapi.logger))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'logger', 'logging']


# print(dir(fastapi.openapi))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'constants', 'docs', 'models', 'utils']


# print(dir(fastapi.param_functions))
# ['Annotated', 'Any', 'Body', 'Callable', 'Cookie', 'Depends', 'Dict', 'Doc', 'Example', 'File', 'Form', 'Header', 'List', 'Optional', 'Path', 'Query', 'Security', 'Sequence', 'Undefined', 'Union', '_Unset', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'deprecated', 'params']


# print(dir(fastapi.params))
# ['Annotated', 'Any', 'Body', 'Callable', 'Cookie', 'Depends', 'Dict', 'Enum', 'Example', 'FieldInfo', 'File', 'Form', 'Header', 'List', 'Optional', 'PYDANTIC_V2', 'PYDANTIC_VERSION_MINOR_TUPLE', 'Param', 'ParamTypes', 'Path', 'Query', 'Security', 'Sequence', 'Undefined', 'Union', '_Unset', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'deprecated', 'warnings']


# print(dir(fastapi.requests))
# ['HTTPConnection', 'Request', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


# print(dir(fastapi.responses))
# ['Any', 'FileResponse', 'HTMLResponse', 'JSONResponse', 'ORJSONResponse', 'PlainTextResponse', 'RedirectResponse', 'Response', 'StreamingResponse', 'UJSONResponse', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'orjson', 'ujson']


# print(dir(fastapi.routing))
# ['APIRoute', 'APIRouter', 'APIWebSocketRoute', 'ASGIApp', 'Annotated', 'Any', 'AppType', 'AsyncExitStack', 'AsyncIterator', 'BaseModel', 'BaseRoute', 'Callable', 'Coroutine', 'DecoratedCallable', 'Default', 'DefaultPlaceholder', 'Dependant', 'Dict', 'Doc', 'Enum', 'FastAPIError', 'HTTPException', 'IncEx', 'IntEnum', 'JSONResponse', 'Lifespan', 'List', 'Mapping', 'Match', 'ModelField', 'Mount', 'Optional', 'Request', 'RequestValidationError', 'Response', 'ResponseValidationError', 'Scope', 'Sequence', 'Set', 'Tuple', 'Type', 'Undefined', 'Union', 'WebSocket', 'WebSocketRequestValidationError', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_get_model_config', '_merge_lifespan_context', '_model_dump', '_normalize_errors', '_prepare_response_content', '_should_embed_body_fields', 'asynccontextmanager', 'asyncio', 'compile_path', 'create_cloned_field', 'create_model_field', 'dataclasses', 'deprecated', 'email', 'generate_unique_id', 'get_body_field', 'get_dependant', 'get_flat_dependant', 'get_name', 'get_parameterless_sub_dependant', 'get_request_handler', 'get_typed_return_annotation', 'get_value_or_default', 'get_websocket_app', 'inspect', 'is_body_allowed_for_status_code', 'json', 'jsonable_encoder', 'lenient_issubclass', 'params', 'request_response', 'routing', 'run_endpoint_function', 'run_in_threadpool', 'serialize_response', 'solve_dependencies', 'websocket_session']


# print(dir(fastapi.security))
# ['APIKeyCookie', 'APIKeyHeader', 'APIKeyQuery', 'HTTPAuthorizationCredentials', 'HTTPBasic', 'HTTPBasicCredentials', 'HTTPBearer', 'HTTPDigest', 'OAuth2', 'OAuth2AuthorizationCodeBearer', 'OAuth2PasswordBearer', 'OAuth2PasswordRequestForm', 'OAuth2PasswordRequestFormStrict', 'OpenIdConnect', 'SecurityScopes', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'api_key', 'base', 'http', 'oauth2', 'open_id_connect_url', 'utils']


# print(dir(fastapi.status))
# ['HTTP_100_CONTINUE', 'HTTP_101_SWITCHING_PROTOCOLS', 'HTTP_102_PROCESSING', 'HTTP_103_EARLY_HINTS', 'HTTP_200_OK', 'HTTP_201_CREATED', 'HTTP_202_ACCEPTED', 'HTTP_203_NON_AUTHORITATIVE_INFORMATION', 'HTTP_204_NO_CONTENT', 'HTTP_205_RESET_CONTENT', 'HTTP_206_PARTIAL_CONTENT', 'HTTP_207_MULTI_STATUS', 'HTTP_208_ALREADY_REPORTED', 'HTTP_226_IM_USED', 'HTTP_300_MULTIPLE_CHOICES', 'HTTP_301_MOVED_PERMANENTLY', 'HTTP_302_FOUND', 'HTTP_303_SEE_OTHER', 'HTTP_304_NOT_MODIFIED', 'HTTP_305_USE_PROXY', 'HTTP_306_RESERVED', 'HTTP_307_TEMPORARY_REDIRECT', 'HTTP_308_PERMANENT_REDIRECT', 'HTTP_400_BAD_REQUEST', 'HTTP_401_UNAUTHORIZED', 'HTTP_402_PAYMENT_REQUIRED', 'HTTP_403_FORBIDDEN', 'HTTP_404_NOT_FOUND', 'HTTP_405_METHOD_NOT_ALLOWED', 'HTTP_406_NOT_ACCEPTABLE', 'HTTP_407_PROXY_AUTHENTICATION_REQUIRED', 'HTTP_408_REQUEST_TIMEOUT', 'HTTP_409_CONFLICT', 'HTTP_410_GONE', 'HTTP_411_LENGTH_REQUIRED', 'HTTP_412_PRECONDITION_FAILED', 'HTTP_413_REQUEST_ENTITY_TOO_LARGE', 'HTTP_414_REQUEST_URI_TOO_LONG', 'HTTP_415_UNSUPPORTED_MEDIA_TYPE', 'HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE', 'HTTP_417_EXPECTATION_FAILED', 'HTTP_418_IM_A_TEAPOT', 'HTTP_421_MISDIRECTED_REQUEST', 'HTTP_422_UNPROCESSABLE_ENTITY', 'HTTP_423_LOCKED', 'HTTP_424_FAILED_DEPENDENCY', 'HTTP_425_TOO_EARLY', 'HTTP_426_UPGRADE_REQUIRED', 'HTTP_428_PRECONDITION_REQUIRED', 'HTTP_429_TOO_MANY_REQUESTS', 'HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE', 'HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS', 'HTTP_500_INTERNAL_SERVER_ERROR', 'HTTP_501_NOT_IMPLEMENTED', 'HTTP_502_BAD_GATEWAY', 'HTTP_503_SERVICE_UNAVAILABLE', 'HTTP_504_GATEWAY_TIMEOUT', 'HTTP_505_HTTP_VERSION_NOT_SUPPORTED', 'HTTP_506_VARIANT_ALSO_NEGOTIATES', 'HTTP_507_INSUFFICIENT_STORAGE', 'HTTP_508_LOOP_DETECTED', 'HTTP_510_NOT_EXTENDED', 'HTTP_511_NETWORK_AUTHENTICATION_REQUIRED', 'WS_1000_NORMAL_CLOSURE', 'WS_1001_GOING_AWAY', 'WS_1002_PROTOCOL_ERROR', 'WS_1003_UNSUPPORTED_DATA', 'WS_1005_NO_STATUS_RCVD', 'WS_1006_ABNORMAL_CLOSURE', 'WS_1007_INVALID_FRAME_PAYLOAD_DATA', 'WS_1008_POLICY_VIOLATION', 'WS_1009_MESSAGE_TOO_BIG', 'WS_1010_MANDATORY_EXT', 'WS_1011_INTERNAL_ERROR', 'WS_1012_SERVICE_RESTART', 'WS_1013_TRY_AGAIN_LATER', 'WS_1014_BAD_GATEWAY', 'WS_1015_TLS_HANDSHAKE', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'annotations']


# print(dir(fastapi.types))
# ['Any', 'BaseModel', 'Callable', 'DecoratedCallable', 'Dict', 'Enum', 'IncEx', 'ModelNameMap', 'Set', 'Type', 'TypeVar', 'Union', 'UnionType', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'types']

# print(dir(fastapi.utils))
# ['Any', 'BaseConfig', 'BaseModel', 'DefaultPlaceholder', 'DefaultType', 'Dict', 'FieldInfo', 'Literal', 'ModelField', 'MutableMapping', 'Optional', 'PYDANTIC_V2', 'PydanticSchemaGenerationError', 'Set', 'TYPE_CHECKING', 'Type', 'Undefined', 'UndefinedType', 'Union', 'Validator', 'WeakKeyDictionary', '_CLONED_TYPES_CACHE', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'cast', 'create_cloned_field', 'create_model', 'create_model_field', 'deep_dict_update', 'fastapi', 'generate_operation_id_for_path', 'generate_unique_id', 'get_path_param_names', 'get_value_or_default', 'is_body_allowed_for_status_code', 'is_dataclass', 'lenient_issubclass', 're', 'warnings']


# print(dir(fastapi.websockets))
# print(inspect.getsource(fastapi.websockets.WebSocket))
# ['WebSocket', 'WebSocketDisconnect', 'WebSocketState', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']