from freezing_utils import device_entry_with_data, get_patcher_dict
from process_patcher import Processor, process_patch


def get_frozen_stats(entries: list[device_entry_with_data]) -> tuple[int, int, int, int]:
    """Returns statistics for the passed list of entries found in a frozen device"""

    device = entries[0]  # the first entry is always the device file

    abstraction_entries = [
        item for item in entries if str(item["file_name"]).endswith(".maxpat")
    ]

    device_patch = get_patcher_dict(device)
    if device_patch == {}:
        return 0, 0, 0, 0

    # get total counts: parse every instance of every abstraction
    count_processor = CountProcessor()
    process_patch(
        device_patch, abstraction_entries, count_processor  # do recurse into abstractions
    )
    object_count_total, line_count_total = count_processor.get_results()

    # get unique counts: parse every entry included in the frozen device once
    object_count_unique = 0
    line_count_unique = 0
    for entry in entries:
        filename = str(entry["file_name"])
        if not (filename.endswith(".amxd") or filename.endswith(".maxpat")):
            continue

        entry_patch = get_patcher_dict(entry)
        if entry_patch == {}:
            continue

        count_processor = CountProcessor()
        process_patch(entry_patch, [], count_processor)  # don't recurse into abstractions
        o, l = count_processor.get_results()

        object_count_unique += o
        line_count_unique += l

    return object_count_total, line_count_total, object_count_unique, line_count_unique


class CountProcessor(Processor):
    def __init__(self):
        self.object_count = 0
        self.line_count = 0

    def process_elements(self, patcher, voice_count: int, abstraction_name=""):
        """Counts objects and lines in the given patcher."""
        self.object_count += len(patcher.get("boxes", [])) * voice_count
        self.line_count += len(patcher.get("lines", [])) * voice_count

    def get_results(self):
        """Returns the current counts."""
        return self.object_count, self.line_count
