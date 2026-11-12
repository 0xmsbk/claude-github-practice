from todo import add_task, complete_task, format_tasks


def test_add_task():
    tasks = add_task([], "buy milk")
    assert tasks == [{"text": "buy milk", "done": False}]


def test_complete_task():
    tasks = add_task([], "buy milk")
    complete_task(tasks, 0)
    assert tasks[0]["done"] is True


def test_format_empty():
    assert format_tasks([]) == "No tasks yet."
