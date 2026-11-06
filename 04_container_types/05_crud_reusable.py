def find_item(item_id, items):
    for item in items:
        if item["id"] == item_id:
            return item


def update_item(item_id, payload, items):
    item = find_item(item_id, items)
    if item:
        item.update(payload)
        return item


def generate_id(items):
    return max(item["id"] for item in items) + 1


def create_item(payload, items):
    items.append({"id": generate_id(items), **payload})
    return items[-1]


def remove_item(item_id, items):
    item = find_item(item_id, items)
    if item:
        items.remove(item)
        return item
