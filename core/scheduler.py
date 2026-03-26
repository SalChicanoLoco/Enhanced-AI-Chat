import time
import queue
import threading
from typing import Dict, Any

class Scheduler:
    def __init__(self):
        self.q = queue.Queue()
        self.results: Dict[str, Any] = {}
        self.running = True
        t = threading.Thread(target=self._worker, daemon=True)
        t.start()

    def submit(self, job_id: str, payload: Dict[str, Any]):
        self.q.put((job_id, payload))

    def get(self, job_id: str):
        return self.results.get(job_id)

    def _worker(self):
        while self.running:
            job_id, payload = self.q.get()
            try:
                time.sleep(0.1)
                self.results[job_id] = {"status": "done", "output": payload.get("prompt", "")}
            except Exception as e:
                self.results[job_id] = {"status": "error", "error": str(e)}
