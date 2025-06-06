from google.protobuf import struct_pb2 as _struct_pb2
from vendor import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResultStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESULT_STATUS_HANDLED_FAILED: _ClassVar[ResultStatus]
    RESULT_STATUS_UNHANDLED_FAILED: _ClassVar[ResultStatus]
    RESULT_STATUS_SUCEEDED: _ClassVar[ResultStatus]
RESULT_STATUS_HANDLED_FAILED: ResultStatus
RESULT_STATUS_UNHANDLED_FAILED: ResultStatus
RESULT_STATUS_SUCEEDED: ResultStatus

class Window(_message.Message):
    __slots__ = ("time_from", "time_to", "window_type_name", "window_type_version", "origin")
    TIME_FROM_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TYPE_VERSION_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    time_from: int
    time_to: int
    window_type_name: str
    window_type_version: str
    origin: str
    def __init__(self, time_from: _Optional[int] = ..., time_to: _Optional[int] = ..., window_type_name: _Optional[str] = ..., window_type_version: _Optional[str] = ..., origin: _Optional[str] = ...) -> None: ...

class WindowType(_message.Message):
    __slots__ = ("name", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class WindowEmitStatus(_message.Message):
    __slots__ = ("status",)
    class StatusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_TRIGGERED_ALGORITHMS: _ClassVar[WindowEmitStatus.StatusEnum]
        PROCESSING_TRIGGERED: _ClassVar[WindowEmitStatus.StatusEnum]
        TRIGGERING_FAILED: _ClassVar[WindowEmitStatus.StatusEnum]
    NO_TRIGGERED_ALGORITHMS: WindowEmitStatus.StatusEnum
    PROCESSING_TRIGGERED: WindowEmitStatus.StatusEnum
    TRIGGERING_FAILED: WindowEmitStatus.StatusEnum
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: WindowEmitStatus.StatusEnum
    def __init__(self, status: _Optional[_Union[WindowEmitStatus.StatusEnum, str]] = ...) -> None: ...

class AlgorithmDependency(_message.Message):
    __slots__ = ("name", "version", "processor_name", "processor_runtime")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_NAME_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    processor_name: str
    processor_runtime: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., processor_name: _Optional[str] = ..., processor_runtime: _Optional[str] = ...) -> None: ...

class Algorithm(_message.Message):
    __slots__ = ("name", "version", "window_type", "dependencies")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    window_type: WindowType
    dependencies: _containers.RepeatedCompositeFieldContainer[AlgorithmDependency]
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., window_type: _Optional[_Union[WindowType, _Mapping]] = ..., dependencies: _Optional[_Iterable[_Union[AlgorithmDependency, _Mapping]]] = ...) -> None: ...

class FloatArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ("status", "single_value", "float_values", "struct_value", "timestamp")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SINGLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUES_FIELD_NUMBER: _ClassVar[int]
    STRUCT_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    status: ResultStatus
    single_value: float
    float_values: FloatArray
    struct_value: _struct_pb2.Struct
    timestamp: int
    def __init__(self, status: _Optional[_Union[ResultStatus, str]] = ..., single_value: _Optional[float] = ..., float_values: _Optional[_Union[FloatArray, _Mapping]] = ..., struct_value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class ProcessorRegistration(_message.Message):
    __slots__ = ("name", "runtime", "connection_str", "supported_algorithms")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STR_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    runtime: str
    connection_str: str
    supported_algorithms: _containers.RepeatedCompositeFieldContainer[Algorithm]
    def __init__(self, name: _Optional[str] = ..., runtime: _Optional[str] = ..., connection_str: _Optional[str] = ..., supported_algorithms: _Optional[_Iterable[_Union[Algorithm, _Mapping]]] = ...) -> None: ...

class ProcessingTask(_message.Message):
    __slots__ = ("task_id", "algorithm", "window", "dependency_results")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    algorithm: Algorithm
    window: Window
    dependency_results: _containers.RepeatedCompositeFieldContainer[Result]
    def __init__(self, task_id: _Optional[str] = ..., algorithm: _Optional[_Union[Algorithm, _Mapping]] = ..., window: _Optional[_Union[Window, _Mapping]] = ..., dependency_results: _Optional[_Iterable[_Union[Result, _Mapping]]] = ...) -> None: ...

class ExecutionRequest(_message.Message):
    __slots__ = ("exec_id", "window", "algorithm_results", "algorithms")
    EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
    exec_id: str
    window: Window
    algorithm_results: _containers.RepeatedCompositeFieldContainer[AlgorithmResult]
    algorithms: _containers.RepeatedCompositeFieldContainer[Algorithm]
    def __init__(self, exec_id: _Optional[str] = ..., window: _Optional[_Union[Window, _Mapping]] = ..., algorithm_results: _Optional[_Iterable[_Union[AlgorithmResult, _Mapping]]] = ..., algorithms: _Optional[_Iterable[_Union[Algorithm, _Mapping]]] = ...) -> None: ...

class ExecutionResult(_message.Message):
    __slots__ = ("exec_id", "algorithm_result")
    EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_RESULT_FIELD_NUMBER: _ClassVar[int]
    exec_id: str
    algorithm_result: AlgorithmResult
    def __init__(self, exec_id: _Optional[str] = ..., algorithm_result: _Optional[_Union[AlgorithmResult, _Mapping]] = ...) -> None: ...

class AlgorithmResult(_message.Message):
    __slots__ = ("algorithm", "result")
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    algorithm: Algorithm
    result: Result
    def __init__(self, algorithm: _Optional[_Union[Algorithm, _Mapping]] = ..., result: _Optional[_Union[Result, _Mapping]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("received", "message")
    RECEIVED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    received: bool
    message: str
    def __init__(self, received: bool = ..., message: _Optional[str] = ...) -> None: ...

class HealthCheckRequest(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    def __init__(self, timestamp: _Optional[int] = ...) -> None: ...

class HealthCheckResponse(_message.Message):
    __slots__ = ("status", "message", "metrics")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNKNOWN: _ClassVar[HealthCheckResponse.Status]
        STATUS_SERVING: _ClassVar[HealthCheckResponse.Status]
        STATUS_TRANSITIONING: _ClassVar[HealthCheckResponse.Status]
        STATUS_NOT_SERVING: _ClassVar[HealthCheckResponse.Status]
    STATUS_UNKNOWN: HealthCheckResponse.Status
    STATUS_SERVING: HealthCheckResponse.Status
    STATUS_TRANSITIONING: HealthCheckResponse.Status
    STATUS_NOT_SERVING: HealthCheckResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    status: HealthCheckResponse.Status
    message: str
    metrics: ProcessorMetrics
    def __init__(self, status: _Optional[_Union[HealthCheckResponse.Status, str]] = ..., message: _Optional[str] = ..., metrics: _Optional[_Union[ProcessorMetrics, _Mapping]] = ...) -> None: ...

class ProcessorMetrics(_message.Message):
    __slots__ = ("active_tasks", "memory_bytes", "cpu_percent", "uptime_seconds")
    ACTIVE_TASKS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    CPU_PERCENT_FIELD_NUMBER: _ClassVar[int]
    UPTIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    active_tasks: int
    memory_bytes: int
    cpu_percent: float
    uptime_seconds: int
    def __init__(self, active_tasks: _Optional[int] = ..., memory_bytes: _Optional[int] = ..., cpu_percent: _Optional[float] = ..., uptime_seconds: _Optional[int] = ...) -> None: ...
