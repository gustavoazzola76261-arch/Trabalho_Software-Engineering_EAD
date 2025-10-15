import pytest
from app.models import InMemoryStore, Task

@pytest.fixture
def store():
    return InMemoryStore()

def test_create_and_get(store):
    t = store.create('Task 1', 'desc')
    assert t.id == 1
    assert store.get(1).title == 'Task 1'

def test_list(store):
    store.create('A')
    store.create('B')
    assert len(store.list()) == 2

def test_update(store):
    t = store.create('Task 1')
    t.title = 'Updated'
    store.update(t)
    assert store.get(t.id).title == 'Updated'

def test_delete(store):
    t = store.create('Task 1')
    assert store.delete(t.id)
    assert store.get(t.id) is None
