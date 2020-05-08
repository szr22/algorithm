from abc import ABC, ABCMeta, abstractmethod
import sys
from typing import List
class IEntry:
    def get_name(self) -> str:
        pass
    def set_name(self, name: str):
        pass
    def get_size(self) -> int:
        pass
    def is_dirctory(self) -> bool:
        pass

class Entry(ABC):
    def __init__(self):
        self.name = ''
    def get_name(self) -> str:
        return self.name
    def set_name(self, name: str):
        self.name = name

class File(Entry):
    def __init__(self):
        self.content = ''
    def get_content(self) -> bytes:
        return self.content
    def set_content(self, content: bytes):
        self.content = content
    def get_size(self) -> int:
        return sys.getsizeof(self.content)
    def is_dirctory(self) -> bool:
        return False
    def __str__(self):
        return 'file{name'+self.name+'}'

class Directory(Entry):
    def __init__(self):
        self.entries = []
    def get_size(self) -> int:
        total = 0
        for e in self.entries:
            total += e.get_size()
        return total
    def is_dirctory(self) -> bool:
        return True
    def add_entry(self, entry: Entry):
        self.entries.append(entry)

class SearchParams:
    def __init__(self):
        self.extension = ''
        self.min_size = 0
        self.max_size = sys.maxsize
        self.name = ''

class IFilter():
    @abstractmethod
    def is_valid(self, params: SearchParams, file: File)->bool:
        pass

class ExtensionFilter(IFilter):
    @classmethod
    def is_valid(cls, params: SearchParams, file: File)->bool:
        if not params.extension:
            return True
        return file.get_extension() == params.extension

class MinSizeFilter(IFilter):
    @classmethod
    def is_valid(cls, params: SearchParams, file: File)->bool:
        # if not params.min_size:
        #     return True
        return file.get_size() >= params.min_size

class MaxSizeFilter(IFilter):
    @classmethod
    def is_valid(cls, params: SearchParams, file: File)->bool:
        # if not params.max_size:
        #     return True
        return file.get_size() <= params.max_size

class NameFilter(IFilter):
    @classmethod
    def is_valid(cls, params: SearchParams, file: File)->bool:
        if not params.name:
            return True
        return file.get_name() == params.name

class FileFilter:
    def __init__(self):
        self.filters = [
            ExtensionFilter(),
            MinSizeFilter(),
            MaxSizeFilter(),
            NameFilter(),
        ]
    def is_valid(self, params: SearchParams, file: File)->bool:
        for filt in self.filters:
            if not filt.is_valid(params, file):
                return False
        return True

class FileSearcher:
    def __init__(self):
        self.file_filter = FileFilter()
    def search(self, dirc: Directory, params: SearchParams) -> List[File]:
        files = []
        queue = []
        queue.append(dirc)

        while queue:
            folder = queue.pop(0)
            for entry in folder.entries:
                if entry.is_dirctory():
                    queue.append(entry)
                else:
                    if self.file_filter.is_valid(params, entry):
                        files.append(entry)
        return files