from dataclasses import dataclass


@dataclass(frozen=True)
class SchedulerConfig:
    MAX_GLOBAL_CONCURRENCY: int = 3
    MAX_SESSION_CONCURRENCY: int = 2
    MAX_JOB_INPUT_TOKENS: int = 8000
    MAX_JOB_OUTPUT_TOKENS: int = 2000
    MAX_SESSION_TOKENS: int = 50000
    MAX_RETRIES: int = 4
    LOOP_SLEEP_SECONDS: float = 0.10
