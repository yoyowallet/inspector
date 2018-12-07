from celery import shared_task

from inspector.checks.engine.processor import CheckProcessor


@shared_task
def execute_check(checkrun_id: int):
    processor = CheckProcessor(checkrun_id)
    prepare = processor.prepare_check()
    if prepare:
        processor.execute_checks()
