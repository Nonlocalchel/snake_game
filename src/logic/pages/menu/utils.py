from src.logic.app_elements.elements.base.lock import Lock


def get_available_box(*boxs) -> Lock:
    for box in boxs:
        if box.is_lock:
            continue

        return box
