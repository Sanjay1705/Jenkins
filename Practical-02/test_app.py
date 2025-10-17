import requests
import time

BASE = "http://localhost:5000"

def wait_for_server(timeout=20):
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(f"{BASE}/health", timeout=2)
            if r.status_code == 200:
                return True
        except Exception:
            pass
        time.sleep(0.5)
    raise RuntimeError("Server did not become ready in time")

def test_health():
    assert wait_for_server()
    r = requests.get(f"{BASE}/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_counter_increment():
    
    wait_for_server()

    r1 = requests.get(f"{BASE}/")
    assert r1.status_code == 200
    v1 = r1.json().get("visits")
    assert isinstance(v1, int)

    r2 = requests.get(f"{BASE}/")
    assert r2.status_code == 200
    v2 = r2.json().get("visits")
    assert v2 == v1 + 1

